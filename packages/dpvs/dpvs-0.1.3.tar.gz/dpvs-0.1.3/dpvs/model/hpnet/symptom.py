""" Notation
:symbol B:      batch size
:symbol sL:     sequence length
:symbol tL:     task length
:symbol kL:     fixed value (3), the number of walking tests type
:symbol fL:     feature length
:symbol TtL:    total task (after packing)
:symbol M:      number of symptom prototype
"""

import torch
import torch.nn as nn
from dpvs.utils import pdist

class Symptom(nn.Module):
    def set_global_variable(self):
        self.dist = None    # minimum distance to each symptom prototype among all pixel
    @property
    def out_dim(self): return self._out_dim
    @property
    def eps(self): return 1e-10

class SymptomNet(Symptom):

    def __init__(self, in_dim, n_proto, alpha=0.1, rd=0, re=0, rc=0, rs=0, d_min=2, **kwargs):
        super(SymptomNet, self).__init__()
        self.pv = nn.Parameter(torch.rand(n_proto, in_dim))
        self.M = n_proto
        self.alpha = alpha
        self.Rd, self.Re, self.Rc, self.Rs, self.d_min = rd, re, rc, rs, d_min
        self.loss_d = {}
        self._out_dim = n_proto
        self.set_global_variable()
    
    def forward(self, x):
        """
        x: embedding of underlying inputs 
        step1: calculate global distance to each sym-proto [TtL, ..., M]
        step2: find a patch (a sequence in RNN) which has smallest distance to a prototype
        """
        dist = torch.cdist(x, self.pv)                      # [B E M], there are E pixel
        min_dist, min_pos = dist.flatten(1,-2).min(dim=1)   # [B M], find smallest pixel
        self.dist = min_dist     
        with torch.no_grad():
            _, idx = min_dist.min(dim=1)
            min_pos = min_pos[torch.arange(len(min_pos)), idx]
        max_sim = torch.exp(self.eps-self.alpha*min_dist)
        return max_sim, min_pos

    def compute_loss(self, y):
        div_loss = self.Rd > 0 and self.compute_diversity() or 0
        clu_loss = self.Rc > 0 and self.compute_cluster() or 0
        evi_loss = self.Re > 0 and self.compute_evidence() or 0
        sym_loss = self.Rs > 0 and self.compute_symptom(y) or 0
        loss =  div_loss + clu_loss + evi_loss + sym_loss
        return loss
    
    def compute_cluster(self):
        "we can find at least one prototype close to this instance"
        dist, _ = self.dist.min(dim=1)
        loss = self.Rc * dist.mean()
        self.loss_d['R_c|symptom'] = loss.item()
        return loss

    def compute_symptom(self, y):
        "equation (17) symptom loss: non-depression patients have lower progression score"
        neg_score = self.dist[y==0].view(-1,self.M).mean(0)
        pos_score = self.dist[y==1].view(-1,self.M).mean(0)
        loss = self.Rs * torch.mean(pos_score - neg_score)
        self.loss_d['R_S|symptom'] = loss.item()
        return loss

    def compute_evidence(self):
        "we can find at least one instance close to this prototype"
        dist, _ = self.dist.min(dim=0)
        loss = self.Re * dist.mean()
        self.loss_d['R_e|symptom'] = loss.item()
        return loss

    def compute_diversity(self):
        pairdist = pdist(self.pv)
        totaldist, _ = pairdist.min(dim=1)
        loss = self.Rd * torch.relu(self.d_min-totaldist).mean()
        self.loss_d['R_d|symptom'] = loss.item()
        return loss
