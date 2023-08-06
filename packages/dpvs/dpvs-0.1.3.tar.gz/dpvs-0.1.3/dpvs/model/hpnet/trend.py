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
from torch import linalg as LA
from dpvs.utils import seq_len_to_mask, pdist


class Trend(nn.Module):
    def set_global_variable(self):
        self.s_k = None   # similarity observed symptom progression and generative matrix
        self.dist = None  # distance between observation and generative in inv-sigmoid space
    @property
    def out_dim(self): return 2
    @property
    def eps(self): return 1e-10
    @property
    def weight(self):
        return torch.stack([p.weight for p in self.ptrend])
    @staticmethod
    def inv_sigmoid(x):
        res = torch.log(x) - torch.log(1-x)
        return torch.nan_to_num(res, neginf=0)
    @staticmethod
    def cal_bern(x, n):
        res = torch.log(x) + torch.log(1-x)
        res = torch.nan_to_num(res, neginf=0).sum([1,2])
        return res.div(n)
    @staticmethod
    def distance(S, G, n):
        """Reference: torch.dist function
        we are trying to compute distance between observation S and generative data G
        we'd like to get distance of each trend-prototype to each symptom progression
        """
        # S-G (n-patient,n-trend,n-task,n-symptom) ==> (n-patient, n-trend)
        dist = LA.norm(S-G, dim=-1) # (n-patient, n-trend, max-task)
        return dist.sum(-1).div(n)  # (n-patient, n-trend) average across valid task
    

class TrendGenerative(Trend):

    def __init__(self, in_dim, time_dim, n_proto, alpha=0.5, beta=1.0, rd=0, re=0, rc=0, rt=0, d_min=2, t0=None, **kwargs):
        super(TrendGenerative, self).__init__()
        self.encoder = TimeEmbedding(embed_dim=time_dim)
        self.ptrend = nn.ModuleList([
            nn.Linear(2*time_dim, in_dim, bias=False) for _ in range(2*n_proto)
        ])  # first {n_trend} for non-depression, rest {n_trend} for positive
        self.K = n_proto
        self.alpha, self.beta = alpha, beta
        self.Rd, self.Re, self.Rc, self.Rt, self.d_min = rd, re, rc, rt, d_min
        self.loss_d = {}
        if t0 == None:
            self.t0_posterior = ZeroModel(out_dim=2*n_proto)
        self.mlp = nn.Conv1d(
            2*n_proto, 2, kernel_size=1, groups=2, bias=False
        )        
        self.set_global_variable()
    
    def forward(self, sim_itm, test_tl, n_task, demo_bh):
        """
        sim_itm: symptom progression matrix (batch-size, max-ntask, m-symptom)
        test_tl: timestamp at which each task begins (relative to first task)
        n_task:  valid number of task of each subject (batch-size)
        demo_bh: demographic embedding of each subject (batch-size, 88)
        """
        t0 = self.t0_posterior(sim_itm, n_task, demo_bh)
        G_kt = torch.stack([
            self.encoder(
                p, test_tl, n_task, t0
            ) for p,t0 in zip(self.ptrend, t0.unbind(1))
        ], dim=1) # (B, nT, t, nS)
        s_k = self.compute_similarity(sim_itm, G_kt, n_task) 
        with torch.no_grad():
            self.mlp.weight.clamp_(min=0)
        scores = self.mlp(s_k.transpose(0,1))
        return scores[1] - scores[0]
    
    def compute_similarity(self, sim_itm, G_kt, n_task):
        """Follow EQUATION(9)
        :param sim_itm:   (batch-size, max-ntask, n-symptom), all non-negative value
        :param G_kt:      (batch-size, 2n-trend, max-ntask, n-symptom), also non-negative
        """
        batch_size = sim_itm.size(0)         
        dist = self.distance(
            self.inv_sigmoid(sim_itm.unsqueeze(1)), 
            self.inv_sigmoid(G_kt),
            n_task.unsqueeze(-1) 
        )   # dist: (n-patient, 2K-prototype), l2-norm distance between inv(A) and inv(G)
        #ISSUE: this value {bert} is too big at the beginning, no effort to be made to minimize distance therefore
        bern = self.cal_bern(sim_itm, n_task)   
        s_k = torch.exp(-self.alpha * dist - self.beta * bern.unsqueeze(-1))
        self.dist, self.s_k = dist, s_k
        return s_k

    def compute_loss(self, y):
        div_loss = self.Rd > 0 and self.compute_diversity() or 0
        clu_loss = self.Rc > 0 and self.compute_cluster() or 0
        evi_loss = self.Re > 0 and self.compute_evidence() or 0
        trend_loss = self.Rt > 0 and self.compute_trend(y) or 0
        loss =  div_loss + clu_loss + evi_loss + trend_loss   
        return loss
    
    def compute_trend(self, y):
        """equation (18)
        """
        def compute(x, idx):
            pos, neg = x[:, idx], x[:, ~idx]
            return pos.sum(1) - pos.max(1)[0] + neg.max(1)[0]
        k, sk = self.K, self.s_k
        neg_k = torch.arange(k)
        pos_score = compute(sk[y==1], ~neg_k).mean(0)
        neg_score = compute(sk[y==0], neg_k).mean(0)
        loss =  self.Rt * (pos_score + neg_score)
        self.loss_d['R_T|trend'] =loss.item()
        return loss

    def compute_cluster(self):
        "we can find at least one prototype close to this instance"
        dist, _ = self.dist.min(dim=1)
        loss = self.Rc * dist.mean()
        self.loss_d['R_c|trend'] = loss.item()
        return loss

    def compute_evidence(self):
        "we can find at least one instance close to this prototype"
        dist, _ = self.dist.min(dim=0)
        loss = self.Re * dist.mean()
        self.loss_d['R_e|trend'] = loss.item()
        return loss

    def compute_diversity(self):
        K = self.K
        w = self.weight.view(2*K, -1)
        neg, pos = w[:K], w[K:]
        neg_score, _ = pdist(neg).min(dim=1)
        pos_score, _ = pdist(pos).min(dim=1)
        loss = self.Rd * (
            torch.relu(self.d_min-neg_score).mean() + 
            torch.relu(self.d_min-pos_score).mean()
        )
        self.loss_d['R_d|trend'] = loss.item()
        return loss



class ZeroModel(nn.Module):
    def __init__(self, out_dim):
        super().__init__()
        self.out_dim = out_dim

    def forward(self, sim_matrix, *args):
        return sim_matrix.new_zeros((sim_matrix.size(0), self.out_dim))

class TimeEmbedding(nn.Module):
    """
    Reference to Xu, D., Ruan, C., Korpeoglu, E., Kumar, S., & Achan, K. (2020). Inductive representation learning on temporal graphs. arXiv preprint arXiv:2002.07962.
    >> ts   (batch_size, max-ntask, 1)
    >> out  (batch_size, max-ntaks, embed-dim * 2)
    """
    def __init__(self, embed_dim=12):
        super(TimeEmbedding, self).__init__()
        self.basis = nn.Parameter(10.0 ** -torch.linspace(0, 9, embed_dim))
        self.phase = nn.Parameter(torch.zeros(embed_dim).float())
        self.scale = 1/torch.sqrt(torch.tensor(embed_dim))
        self.act = nn.Sigmoid()
    
    def forward(self, pt, ts, nt, t0):
        """
        :argument:
        @pt   (callable: 2d -> num-symptom) : specific trend function
        @ts   (batch_size, max-ntask)       : task time to each user
        @nt   (batch_size,)                 : effective number of task to each user
        @t0   (batch_size)                  : specific trend offset
        :variable:
        @embed_cos (batch_size, max-ntask, embed-dim), here embed-dim is n-symptom
        @embed_sin (...), the same to @embed_cos
        :rtn:
        @G_k_t(batch_size, max-ntask, 2xtime-dim)
        """
        ts = ts - t0[:,None]               # (batch-size, max-ntask, 1)
        ts = ts[...,None]                  # add one more dimension at the end
        embed_cos = self.apply(torch.cos, self.basis, self.phase, ts)
        embed_sin = self.apply(torch.sin, self.basis, self.phase, ts)
        embed = torch.cat([embed_cos, embed_sin], dim=-1)
        mask = seq_len_to_mask(nt, embed.size(1))
        Phi_t =  self.scale * embed * mask[...,None] # (batch-size, max-ntask, 2embed-dim)
        return self.act(pt(Phi_t))

    @staticmethod
    def apply(func, basis, phase, ts):
        embed = ts * basis.view(1,1,-1)
        embed += phase.view(1,1,-1)
        return func(embed)