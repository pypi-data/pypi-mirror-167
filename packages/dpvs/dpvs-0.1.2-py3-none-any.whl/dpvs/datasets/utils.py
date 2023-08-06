import numpy as np
from torch.utils.data import Dataset, DataLoader
from dataclasses import dataclass
from typing import Generator

def xpad(arr, *shape, pad_value=0, dtype=float, ):
    if not shape: return 
    _arr = np.full(shape, fill_value=pad_value, dtype=dtype)
    for i, x in enumerate(arr):
        if isinstance(x, np.ndarray):
            size = min(shape[1], len(x))
            _arr[i, :size] = x[:size]
        else:
            _arr[i, :shape[1]] = xpad(x, *shape[1:], pad_value=pad_value)
    return _arr


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