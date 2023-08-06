Here we define all metrics used in evaluation

```yaml
# from configs/torch.yaml
metrics:
    _target_: builtins.dict
    auc: 
        _target_: dpvs.metrics.AUC
    f1:
        _target_: dpvs.metrics.F1
    rec:
        _target_: dpvs.metrics.Recall
    prec:
        _target_: dpvs.metrics.Precision

with the above setting
metrics = {
    'auc': AUC object,
    'f1':  F1 object,
    'rec': Recall object,
    'prec': Precision Object
}
```

To be noted: each `EpochMetric` will by default take a tuple of two numpy array. If you want to change the default behavior, you should pass a functin `output_transform` that maps output from evaluation step (see example below)
```python
# suppose we define evaluation step this way, it output predicted probabiltiy and true class
def test_step(engine, batch):
    model.eval()
    x, y = batch
    xmove(x, device)
    y_prob = model.pred(**x)
    return y_prob.cpu().numpy(), y.cpu().numpy()

def default_preprocessing(output):
    "default: turn predicted probability into 0/1 predicted class"
    y_pred, y  = output
    return np.round(y_pred) , y

class EpochMetric(Metric):
    """
    EpochMetric takes two arguments
    :compute_fn:        compute measurements from output of evaluation `test_step`
    :output_transform:  preprocess output of evaluation `test_step` 
    """
    def __init__(
        self, compute_fn: Callable, 
        output_transform: Callable = lambda x: default_preprocessing
    ):
        super().__init__(output_transform)
        self.compute_fn = compute_fn
```
