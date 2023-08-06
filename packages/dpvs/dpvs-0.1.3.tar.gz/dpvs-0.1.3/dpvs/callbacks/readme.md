### template

```yaml
lr_scheduler:                                   # name of callback
    _target_: dpvs.callbacks.add_lr_scheduler   # function to call
    scheduler:                                  # function parameter (recursive call)
        _target_: ignite.handlers.ReduceLROnPlateauScheduler
        _partial_: true                         # functools.partial is applied
        metric_name: ${optim_metrics}
        mode: min
        factor: 0.1
        patience: 10
```

with the aforementioned configurations, we can instantiate a callback with little efforts 

```python
"""
:param:
    engine (ignite.engine.Engine)   to which the callback is applied
    scheduler                       used to help instantiate scheduler

:logic:
    1. at `STARTED`, we call function(engine, scheduler)
        - grab optimizer instance from engine.state
        - instantiate scheduler with optimizer
        - grab evaluator instance from engine.state

    2. at each `EPOCH_COMPLETED`, a predefined scheduler is called
"""
def add_lr_scheduler(engine, scheduler):
    def function(engine:Engine, scheduler: Callable):
        optimizer = engine.state.optimizer
        scheduler = scheduler(optimizer=optimizer)
        evaluator = engine.state.evaluator
        evaluator.add_event_handler(Events.EPOCH_COMPLETED, scheduler)
    engine.add_event_handler(Events.STARTED, function, scheduler)
```

### Engine.State

This is a list of engine.state inherit and defined by me, you can access them by calling `engine.state.xxx` in your callback function

```yaml
# =========== defined by Torch.Ignite =============================
iteration:  18
epoch:      1
max_epochs: 100
output:     {R_c|symptom: 1.1255736351013184, ...}
batch:      (X_dict, y)
metrics:    {f1: F1, auc: AUC, ...}
dataloader: the training dataloader
seed:       random seed used in this experiment run
times:      {'EPOCH_COMPLETED': 2.1060516834259033, 'COMPLETED': 0.0}
# ============ defined by engine.state.xx = yy ======================
optimizer:  torch.optim.xxx
lr:         learning rate
evaluator:  define test_step
data:       train/val/test dataloader
```