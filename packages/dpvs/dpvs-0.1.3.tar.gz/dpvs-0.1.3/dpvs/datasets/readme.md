we tell hydra how to create data module here: I will illustrate its usage with two examples: one defined in `configs/sklearn.yaml` and one defined in `configs/torch.yaml`

### Sklearn

```yaml
# part of sklearn.yaml
data:
    _target_: dpvs.datasets.make_numpy
    data_dir: ${datapath}
    label_mode: label_last    
    # nested dictionary 'train_split': {'trian': 0.6, ...}
    train_split:      
        train: 0.6
        valid: 0.2
        test: 0.2
    ...
```
```python
from dpvs.datasets.utils import Datasets
"""
Datasets is a dataclass that store trian/val/test torch.utils.data.Dataset
train_data/val_data/test_data are all torch.utils.data.Dataset
"""
def make_numpy(
    label_mode, data_dir, part_seed, train_split, sample_rate, nw, add_world_frame, use_cache, **kwargs
):  # all arguments without default-value should be set in yaml config file
    ...
    return Datasets(train=train_data, val=val_data, test=test_data)

data: Datasets = hydra.utils.instantiate(cfg.data)
X, y = data.train[0]        #all training features and labels
assert X[0].shape == (129, )#hand crafted features (np.ndarray)
assert len(y) == 420        #length of training samples
```

### Torch

```yaml
# part of torch.yaml
data:
    _target_: dpvs.datasets.make_tensor
    data_dir: ${datapath}
    label_mode: 'label_seq'
    # nested dictionary 'train_split': {'trian': 0.6, ...}
    train_split:      
        train: 0.6
        valid: 0.2
        test: 0.2
    train_sz: 32
    test_sz: 32
    ...
```
```python
"""
Dataloaders is a dataclass that store trian/val/test torch.utils.data.Dataloader
train_data/val_data/test_data are all torch.utils.data.Dataset
"""
from dpvs.datasets.utils import Dataloaders
def make_tensor(
    label_mode, data_dir, part_seed, train_split, sample_rate, nw, add_world_frame, use_cache, train_sz=32, test_sz=128, demo_dim=88, **kwargs
):
    collate_fn = BatchCollator(...)
    return Dataloaders(
        train=DataLoader(train_data, batch_size=train_sz, shuffle=True, collate_fn=collate_fn),
        val=DataLoader(val_data, batch_size=test_sz, shuffle=False, collate_fn=collate_fn),
        test=DataLoader(data.test, batch_size=test_sz, shuffle=False, collate_fn=collate_fn),
    )
data: Dataloaders = hydra.utils.instantiate(cfg.data)
for (X,y) in data.train:    #train dataloader
    len(y): 32
    X: {
        'ps_id': array(...),
        'test_id_bh': array(...),
        'demo_bh':      torch.Size([32, 88]),   # subject-wise demographic embedding
        'task_len_bh':  torch.Size([32]),       # subject-wise number of valid task
        'test_t_l':     torch.Size([32, 15]),   # subject-wise task time (normalized)
        'seq_len_bh':   torch.Size([32,15,3]),  # subject-wise sequence length of each task
        'seq_data_bh':  torch.Size([32,15,3,300,10]) # subject-wise sequence data
    }
```