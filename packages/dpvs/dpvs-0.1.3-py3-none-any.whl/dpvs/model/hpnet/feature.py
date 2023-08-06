from dpvs.utils import tween, seq_len_to_mask, xpack
from dpvs.model.sparsemax import Sparsemax
from dpvs.model.vision_models import CNN1D
import torch
import torch.nn as nn
from torch.nn.utils import rnn


class Feature(nn.Module):
    @property
    def out_dim(self): return self._out_dim
    @property
    def eps(self): return 1e-10


class RNN(Feature):
    """
    This link helps me a lot in understanding bi-directional LSTM
        https://towardsdatascience.com/understanding-the-outputs-of-multi-layer-bi-directional-lstms-13ad99a80dd3
    
    I also implement sparsemax introduced here to avoid uniform-like attention score
        https://github.com/deep-spin/entmax
    """
    def __init__(self, in_dim, hid_size=64, num_layers=2, bidirectional=True, dropout=0.0, demo_dim=0):
        super(RNN, self).__init__()
        self.rnn = GRU(
            input_size=in_dim, batch_first=True, hidden_size=hid_size, num_layers=num_layers, dropout=dropout, bidirectional=bidirectional
        )
        self.num_layers = num_layers
        self._demo_dim = demo_dim
        self._out_dim = 128
        self.agg = DENSE((1+bidirectional)*hid_size + demo_dim)
        # self.softmax = Sparsemax(dim=1)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, seq_bh, seq_len_bh, demo_bh, **kwargs):
        batch_size = seq_bh.size(0)
        # clamp seq_len_bh to be 1 to meet minimum requirement, but kick them out later on
        seq_out, hn = self.rnn(seq_bh, seq_len=seq_len_bh.clamp(min=1))
        batch_siz, seq_maxlen, _ = seq_out.shape
        seq_out[seq_len_bh==0] = 0; hn[:, seq_len_bh==0] = 0
        if self._demo_dim == 0:
            return hn[-self.num_layers:].transpose(0,1).reshape(batch_size, -1)
        attn_input = torch.cat([seq_out, demo_bh[:,None,:].repeat(1,seq_maxlen,1)],dim=-1)
        attn = self.agg(attn_input)
        mask = (~seq_len_to_mask(seq_len_bh)).unsqueeze(-1).to(attn).bool()
        attn = self.softmax(attn.masked_fill(mask, self.eps))
        return torch.bmm(attn.transpose(1,2), seq_out).squeeze()
        
         
class GRU(nn.Module):
    def __init__(self, input_size, hidden_size=100, num_layers=1, dropout=0.0, batch_first=True, bidirectional=False, bias=True):
        super(GRU, self).__init__()
        self.batch_first = batch_first
        self.gru = nn.GRU(input_size, hidden_size, num_layers, bias=bias, batch_first=batch_first, dropout=dropout, bidirectional=bidirectional)
        self.init_param()
    def init_param(self):
        for name, param in self.named_parameters():
            if 'bias' in name:
                param.data.fill_(0)
                n = param.size(0)
                start, end = n // 4, n // 2
                param.data[start:end].fill_(1)
            else:
                nn.init.xavier_uniform_(param)
    def forward(self, x, seq_len=None, h0=None):
        batch_size, max_len, _ = x.size()
        if seq_len is not None and not isinstance(x, rnn.PackedSequence):
            sort_lens, sort_idx = torch.sort(seq_len, dim=0, descending=True)
            x = x[sort_idx] if self.batch_first else x[:, sort_idx]
            x = rnn.pack_padded_sequence(
                x, sort_lens.tolist(), batch_first=self.batch_first
            )
            output, h0 = self.gru(x, h0)  # -> [N,L,C]
            output, _ = rnn.pad_packed_sequence(output, batch_first=self.batch_first, total_length=max_len)
            _, unsort_idx = torch.sort(sort_idx, dim=0, descending=False)
            output = output[unsort_idx] if self.batch_first else output[:, unsort_idx]
            h0 = h0[:, unsort_idx]
        else:
            output, h0 = self.gru(x, h0)
        return output, h0
    
class DENSE(nn.Sequential):
    def __init__(self, in_dim, out_dim=1, hid_dim=[24,12], dropout=0.0):
        in_dims = [in_dim] + hid_dim
        out_dims = hid_dim + [out_dim]
        seq = [nn.Linear(a,b) for a,b in zip(in_dims, out_dims)]
        act = [nn.LeakyReLU(), nn.Dropout(dropout)]
        super().__init__(*tween(seq, act))

class CNN(Feature, CNN1D):

    def __init__(self, **kwargs):
        super(Feature, self).__init__(**kwargs)
        self._out_dim = 128
    
    def forward(self, seq_bh, **kwargs):
        seq_bh = seq_bh.transpose(1,2)      # (3xtotal-task, in-dim, max-seqlen)
        embedding = super(Feature, self).forward(seq_bh)
        return embedding.transpose(1,2)     # (3xtotal-task, out-dim, channel-size)

        
class FeatureNet(nn.Module):
    """
    B: batch-size   |   tL: max task-len     |   sL: max seq-len      |   fL: input-dim
    eL:embed-len    |   TtL: total task-len  |   cL: channel size
    Input:
        seq_bh [B,tL,3,sL,fL]    raw feature concated with segment embedding
        seq_len_bh [B,tL,3]      number of valid sequence of each subject each task each segment
        task_len_bh [B]          number of valid task of each subject
        demo_bh [B,88]           demogrpahic embedding of each subject
    Return:
        rtn_embed [TtL,3,...]    signal embedding of each task 
        seq_len [TtL,3]          signal valid length of each task
    """
    def __init__(self, backbone, **kwargs):
        super(FeatureNet, self).__init__()
        cls, param = BACKBONE.get(backbone)
        self.feature = cls(**{**kwargs, **param})
        self.out_dim = self.feature.out_dim

    def forward(self, seq_data_bh, demo_bh, seq_len_bh, task_len_bh, **kwargs):
        # step1: pack data to avoid padded task sequence
        # step2: pack back to be ready for symptom local analysis
        _, _, _, sL, fL = seq_data_bh.size()
        seq_len = xpack(seq_len_bh, task_len_bh)
        input = seq_len.pack(seq_data_bh)
        TtL, _, sL, fL = input.shape
        demo = seq_len.repeat(demo_bh).unsqueeze(1).repeat(1,3,1)
        embedding = self.feature(
            seq_bh=input.view(-1, sL, fL), 
            seq_len_bh=seq_len.data.view(-1), 
            demo_bh=demo.view(-1, demo.size(-1))
        )
        output = embedding.reshape(TtL,-1,self.out_dim)
        return output, seq_len

    # def find_rf(self, pos, ps_id, input_shape, output_shape):
    #     analysis = defaultdict(list)
    #     inp = torch.zeros(input_shape, requires_grad=True).to(pos.device)
    #     inp = inp.view(-1, *input_shape[-2:])
    #     embedding = self.feature(seq_bh=inp)
    #     output = embedding.reshape(output_shape)
    #     grad = torch.zeros_like(output)
    #     grad[:,pos,:]=1.0
    #     output.backward(gradient=grad)
    #     grad_data = inp.grad.mean([0, 1]).abs().data

    @property
    def name(self): return self.feature.__class__.__name__
        
def get_bounds(gradient):
    coords = gradient.nonzero(as_tuple=True)[0] # get non-zero coords
    mini, maxi = coords.min().item(), coords.max().item()
    return {'bounds': (mini, maxi), 'range': maxi - mini}

BACKBONE = {
    'null': (nn.Identity, {}),
    'rnn': (RNN, {
        'demo_dim': 0, 'in_dim': 10, 'hid_size': 64
    }),
    'rnn_demo': (RNN, {
        'demo_dim': 88, 'in_dim': 10, 'hid_size': 64
    }),
    'cnn_vgg': (CNN, {
        'n_channels': [10,8,16,32,64,128], 
        'channel_sizes': [5,5,5,5,5],
        'deep': 1
    }), # (300) -> (5) 
    'cnn_deep': (CNN, {
        'n_channels': [10,8,16,32,64,128],
        'channel_sizes': [4,3,3,3,3],
        'last_pool': True, 
    }), # (300) -> (5)
    'cnn_wide': (CNN, {
        'n_channels': [10,8,16,32,64,128], 
        'channel_sizes': [8,8,8,8,8],
        'last_pool': False, 'deep': -1
    }), # (300) -> (5) this isn't alex since alex has stride of four
}