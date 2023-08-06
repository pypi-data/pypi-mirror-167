The `trainer` instance is defined from here. Let's take a look at two examples: scikit-learn based `sklearn_run.py` and torch-based `ignite_run.py`

### Sklearn

```yaml
# part of configs/sklearn.yaml
trainer:
  _target_: dpvs.engines.sklearn_run.Engine
  params: {}
  optim_metrics: f1 # by which standard do we select best model on validation data
  n_jobs: 1
  hypopt: false
  save_best: ${model.load_best}
```
```python
from dpvs.train import run
from dpvs.configs import Project, Args
args = Args(
    project = Project(name='test', engine='sklearn'),   #use sklearn.yaml template
    model = { 'name': 'adb', },                         #override model parameter
    trainer = {     # hypopt to search best model
        'params': {
            'n_estimators': list(range(6,10)) + [20],
            'algorithm': ['SAMME', 'SAMME.R'],
            "learning_rate":  [0.0001, 0.001, 0.01, 0.1]
        },
        'hypopt': True, #enable hyperparameter search   
        'n_jobs': 3     #number of parallel processing
    }
)
run(args)
```

### Ignite-Torch

```yaml
# part of configs/torch.yaml
trainer:
  _target_: dpvs.engines.ignite_run.create_engine
  device: ${device}
  optimizer:
    _target_: torch.optim.Adam
    _partial_: true
    lr: 1e-3
    weight_decay: 0.0
  metrics:
    _target_: builtins.dict
    auc: 
      _target_: dpvs.metrics.AUC
    ...
defaults:
  - model: none
```
```python
from dpvs.train import run
from dpvs.configs import Project, Args
args = Args(
    project = Project(
        name='test', engine='torch',    # use torch.yaml 
        override=['model=hpnet']        # override model in defaults list
    ), 
    model = {
        'slayer': {'n_proto': 12},      # nested overriding
        'tlayer': {'n_proto': 10},      # nested overriding
    }
)
run(args)
```

### Ignite

Let's dive into what happened inside `ignite_run.py`

```python
def create_engine(
    model: nn.Module,                       # model
    optimizer: torch.optim.Optimizer,       # partial optimizer (wait for model)
    device: str,                            # device, cuda/cpu
    metrics: dict                           # evaluation methods
):
    device = torch.device(device)
    optimizer= optimizer(params=model.parameters()) # pass model to instantiate optim
    
    # Training Function =============================================================
    def train_step(engine, batch):
        model.train()           # train mode
        x, y = batch            # grab a batch (feature/target)
        xmove(x, device)        # move data to device
        y_pred = model(**x)     # forward passing
        loss = model.compute_loss(y_pred, y.to(device))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        return model.loss_d     # return all loss
    # Define trainer engine and keep track of criterion/optimizer
    engine = Engine(train_step)
    # anything you'd be using in callback by adding engine.state.xx = xx
    engine.state.optimizer = optimizer                  #keep track of optimizer
    engine.state.lr = optimizer.param_groups[0]['lr']   #keep track of learn rate

    # Evaluation Function ===========================================================
    def test_step(engine, batch):
        model.eval()
        x, y = batch
        xmove(x, device)
        y_prob = model.pred(**x)
        return y_prob.cpu().numpy(), y.cpu().numpy()    #return pred prob and true
    # Define evaluator engine and save its access in engine.state
    evaluator = Engine(test_step)
    engine.state.evaluator = evaluator
    for name, metric in metrics.items():                #add evaluation
        metric.attach(evaluator, name)                  #add metrics to evaluator

    return engine
```