import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from dataclasses import dataclass
from typing import Generator
from collections import defaultdict

def xpad(arr, *shape, pad_value=0, dtype=float, rtn_type='numpy'):
    def helper(arr, *shape):
        if not shape: return 
        if len(shape) == 1: return np.array(arr, dtype=dtype)
        _arr = np.full(shape, fill_value=pad_value, dtype=dtype)
        for i, x in enumerate(arr):
            if isinstance(x, np.ndarray):
                size = min(shape[1], len(x))
                _arr[i, :size] = x[:size]
            else:
                _arr[i, :shape[1]] = helper(x, *shape[1:])
        return _arr
    if not shape:
        if hasattr(arr, 'shape'): shape = arr.shape
        else: shape = [len(arr)]
    out = helper(arr, *shape)
    if rtn_type == 'tensor':
        return torch.from_numpy(out)
    return out

def xmove(args, device):
    if not torch.cuda.is_available() or device is None:
        return
    if isinstance(args, list):
        for arg in args: xmove(arg, device)
    elif isinstance(args, dict):
        for key, value in args.items():
            if isinstance(value, torch.Tensor):
                args[key] = value.to(device)
    else:
        raise TypeError("only dictionary inputs are supported, please change your collate function")

def xgroup(iterable, ndigits=None):
    def rd(num, digit=None):
        if digit: num = round(num, digit)
        return num
    out = defaultdict(dict)
    for key in iterable:
        if '|' in key:
            left,right = key.rsplit('|',1)
            out[right][left] = rd(iterable[key], ndigits)
            if '|' in left:
                out[right] = xgroup(out[right])
        else:
            out[key] = rd(iterable[key], ndigits)
    return out

class Data:
    @property
    def keys(self):
        yield from ['train', 'val', 'test']
    def apply(self, func):
        for mode in self.keys:
            data = getattr(self, mode)
            newdata = func(data)
            if isinstance(newdata, Generator):
                setattr(self, mode, list(zip(*newdata)))
            else:
                setattr(self, mode, newdata)
    def __iter__(self):
        for mode in self.keys: 
            yield getattr(self, mode)

@dataclass
class Datasets(Data):
    """Class for keeping track of datasets"""
    train: Dataset = None
    val: Dataset = None
    test: Dataset = None

@dataclass
class Dataloaders(Data):
    """Class for keeping track of dataloaders"""
    train: DataLoader = None
    val: DataLoader = None
    test: DataLoader = None