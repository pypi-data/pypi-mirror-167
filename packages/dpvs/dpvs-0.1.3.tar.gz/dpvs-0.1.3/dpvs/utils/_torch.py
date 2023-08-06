import torch
import torch.nn as nn
from torch.nn.utils import rnn
import numpy as np

__all__ = ['seq_len_to_mask', 'xpack', 'pdist']

def seq_len_to_mask(seq_len, max_len=None):
    """
    >>> size = torch.randint(3, 10, (3,)) # e.g., [3,6,6]
    >>> seq_len_to_mask(size).shape == torch.Size([3,size.max()])
    True
    >>> seq_len_to_mask(size, 10).shape   # True/False matrix
    torch.Size([3, 10])
    """
    if isinstance(seq_len, np.ndarray):
        assert len(np.shape(seq_len)) == 1, f"seq_len can only have one dimension, got {len(np.shape(seq_len))}."
        max_len = int(max_len) if max_len else int(seq_len.max())
        broad_cast_seq_len = np.tile(np.arange(max_len), (len(seq_len), 1))
        mask = broad_cast_seq_len < seq_len.reshape(-1, 1)

    elif isinstance(seq_len, torch.Tensor):
        assert seq_len.dim() == 1, f"seq_len can only have one dimension, got {seq_len.dim() == 1}."
        batch_size = seq_len.size(0)
        max_len = int(max_len) if max_len else seq_len.max().long()
        broad_cast_seq_len = torch.arange(max_len).expand(batch_size, -1).to(seq_len)
        mask = broad_cast_seq_len.lt(seq_len.unsqueeze(1))
    else:
        raise TypeError("Only support 1-d numpy.ndarray or 1-d torch.Tensor.")

    return mask

class xpack:

    def __init__(self, data, length, batch_first=True, enforce_sorted=False):
        if length.is_cuda: length = length.cpu()
        self.length = length
        self.data, self.batch_sizes, self.sorted_indices, self.unsorted_indices = rnn.pack_padded_sequence(data, length, batch_first=batch_first, enforce_sorted=enforce_sorted)
    
    @property
    def sequence(self):
        return rnn.PackedSequence(
            data=self.data, batch_sizes=self.batch_sizes,
            sorted_indices=self.sorted_indices, unsorted_indices=self.unsorted_indices
        )
    
    def pad(self, data=None, batch_first=True, padding_value=0, total_length=None, **kwargs):
        if data is None: data = self.data
        batch_sizes = kwargs.get('batch_sizes', self.batch_sizes)
        sorted_indices = kwargs.get('sorted_indices', self.sorted_indices)
        unsorted_indices = kwargs.get('unsorted_indices', self.unsorted_indices)
        rtn, _ = rnn.pad_packed_sequence(
            rnn.PackedSequence(
                data, batch_sizes, sorted_indices, unsorted_indices
            ), 
            batch_first=batch_first, padding_value=padding_value, total_length=total_length
        )
        return rtn

    def pack(self, data, batch_first=True, enforce_sorted=False, return_sequence=False):
        seq =  rnn.pack_padded_sequence(data, self.length, batch_first=batch_first, enforce_sorted=enforce_sorted)
        return seq if return_sequence else seq.data

    def repeat(self, data):
        idx = torch.cat([self.sorted_indices[:i] for i in self.batch_sizes])
        if not isinstance(data, torch.Tensor):
            idx = idx.cpu().numpy()
        return data[idx]

    
def pdist(x, p=2):
    "calculate self-(p-norm)distance where diagonal is ignored"
    pairdist = torch.cdist(x,x,p=p)
    diagonal = torch.eye(len(x)).to(x) * pairdist.max()
    return pairdist + diagonal