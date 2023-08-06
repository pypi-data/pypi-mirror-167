""" Notation
:symbol B:      batch size
:symbol sL:     sequence length
:symbol tL:     task length
:symbol kL:     fixed value (3), the number of walking tests type
:symbol fL:     feature length
"""
import torch
import torch.nn as nn
from .feature import FeatureNet
from .symptom import SymptomNet
from .trend import TrendGenerative

EPS = 1e-8
def normalize(x, epsilon=EPS):
    x = x / (x.norm(p=2, dim=-1, keepdim=True) + epsilon)
    return x

class HierarchicalProtoNetCLS(nn.Module):

    classes = ['nodep', 'dep'] 
    num_class = 2

    def __init__(self, flayer, slayer, tlayer, normalize=False, pos_weight=1.0):
        """initialize two-layer protopnet
        
        :param flayer:      nn.Module, feature layer to embed signals
        :param slayer:      nn.Module, symptom layer to enable local prototyping analysis
        :param tlayer:      nn.Module, trend layer to enable global prototyping analysis
        """
        super(HierarchicalProtoNetCLS, self).__init__()
        self.flayer: FeatureNet = flayer
        self.slayer: SymptomNet = slayer(in_dim=self.flayer.out_dim)
        self.tlayer: TrendGenerative = tlayer(in_dim=self.slayer.out_dim)
        self.normalize = normalize
        self.criterion = nn.BCEWithLogitsLoss(pos_weight=torch.tensor([pos_weight]))
        self.sigmoid = nn.Sigmoid()

    def forward(self, seq_data_bh, seq_len_bh, test_t_l, task_len_bh, demo_bh, ps_id, **kwargs):
        """process one batch of data 
           ~~all variable name must be the same to batch_d definition
        
        :param seq_data_bh:     [B, tL, 3, sL, fL] signal data of each task of each subject
        :param seq_len_bh:      [B, tL, 3]
        :param task_len_bh:     [B]
        :param test_t_l  :      [B, tL]  
        """
        embedding, seq_len = self.flayer(seq_data_bh, demo_bh, seq_len_bh, task_len_bh)
        if self.normalize: 
            embedding = normalize(embedding)
        s_itm, pos = self.slayer(embedding)
        s_itm, pos = seq_len.pad(s_itm), seq_len.pad(pos)  # pack-all-task -> patient-task
        logits = self.tlayer(s_itm, test_t_l, task_len_bh, demo_bh)
        self.xpack = seq_len        #ISSUE: this is saved to compute loss for symptom
        return logits

    def compute_loss(self, y_pred, y_true, **kwargs):
        loss_ce = self.criterion(y_pred, y_true)
        loss_symptom = self.slayer.compute_loss(self.xpack.repeat(y_true))
        loss_trend = self.tlayer.compute_loss(y_true)
        loss_total = loss_ce + loss_symptom + loss_trend
        self.loss_d = {**self.slayer.loss_d, **self.tlayer.loss_d, 'CE': loss_ce.item(), 'loss': loss_total.item()}
        return loss_total

    def pred(self, seq_data_bh, seq_len_bh, test_t_l, task_len_bh, demo_bh, ps_id, **kwargs):
        with torch.no_grad():
            logits = self.forward(seq_data_bh, seq_len_bh, test_t_l, task_len_bh, demo_bh, ps_id, **kwargs)
            return self.sigmoid(logits)

    def restore_from_checkpoint(self, checkpoint):
        try:
            self.load_state_dict(torch.load(checkpoint), strict=False)
        except OSError: pass # start training from scratch
    
    def save_to_checkpoint(self, checkpoint):
        torch.save(self.state_dict(), checkpoint)