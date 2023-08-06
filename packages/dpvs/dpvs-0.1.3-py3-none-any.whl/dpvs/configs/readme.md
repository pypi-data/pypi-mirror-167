### Hydra 

Here I defined two configurations for model based on `sklearn` and one based on `torch`. You can learn how to setup a config object in this [tutorial](https://hydra.cc/docs/tutorials/basic/your_first_app/using_config/)

```yaml
# part of sklearn.yaml
model:
  _target_: dpvs.model.sklearn_models.make_model    # here I create model from sklearn_models.py
  load_best: false
  name: ???  #dt/knn/svm/rf/adaboost/xgboost ??? indicates missing value, must be set

trainer:
  _target_: dpvs.engines.sklearn_run.Engine  # here I create trainer from sklearn_run.py
  params: {}
  optim_metrics: f1
  n_jobs: 1
  hypopt: false
  save_best: ${model.load_best}              # variable referencing
```

```yaml
# part of torch.yaml
defaults:
  - model: hpnet # see https://hydra.cc/docs/tutorials/basic/your_first_app/config_groups/, this will direct hydra to look at hpnet.yaml in model folder

# engine configuration
trainer:
  _target_: dpvs.engines.ignite_run.create_engine
  device: ${device}
  metrics:                      # create a dictionary with four metric keys
    _target_: builtins.dict     # python built-in functions
    auc:                        # essentially, metrics[auc] = AUC()
      _target_: dpvs.metrics.AUC
    f1:
      _target_: dpvs.metrics.F1
    rec:
      _target_: dpvs.metrics.Recall
    prec:
      _target_: dpvs.metrics.Precision
```

### Project

I have also defined two helper class here: `Args` and `Project`

```python
# Args help me to set up argument specific to each experiment
class Args:
    """
    >>> args = Args(a=1, b=2)
    >>> assert args.a == 1
    >>> assert args.d == {'a': 1, 'b': 2}
    """
    def update(self, **kwargs)
    def set(self, __name, __value)
    def pop(self, __name, __default_popvalue)
```

we can update hydra configurations with argument by merging them:

```python
"""
cfg: (omegaconf.DictConfig)  a composed config created from yaml file
"""
OmegaConf.set_struct(cfg, False)    # turn it True will raise non-existing error
cfg = OmegaConf.merge(cfg, OmegaConf.create(args.d))    # update cfg with args.d
```

by default hydra will mess up your working directory, to preserve current working directory, I use `Project` to manage them and indicate hydra where to save objects. If we add `PROJECT_ROOT=the-path-you-prefer` in `.env` file in the same directory with your `main.py`, it will automatically choose this path over its default value
```python
@dataclass
class Project:
    root: str = os.getcwd()     # by default, use current working directory 
    name: str = 'project_name'  # experiment name
    data: str = 'data'          # data folder, if not absolute path, relative to root
    log: str = 'logs'           # save path, relative to root
    checkpoint: str = 'checkpoint' # checkpoint, if not absolute path, relative to ro
    engine: str = 'torch'       # which yaml configuration file to look at
    override: List[str] = field(default_factory=list)    # a list of override string
    # override can be learnt here: https://hydra.cc/docs/advanced/override_grammar/basic/

overrides = [
    f'hydra.run.dir={project.SAVEPATH}',                #change hydra runtime path
    f'datapath={to_absolute_path(project.DATAPATH)}',   #override {datapath} in yaml
    f'checkpoint={to_absolute_path(project.CHECKPOINT)}'#override {checkpoint} in yam
] + project.override    # pass additional overriding arguments to hydra

with hydra.initialize(config_path='configs', version_base=None):
    cfg = hydra.compose(
        config_name = project.engine, overrides=overrides
    )   # construct configuration by taking at look at configs/{project.engine}.yaml
        # with a list of {overrides} commands
```
