import hydra
from omegaconf import DictConfig, OmegaConf
from dpvs.utils import seed_all
from dpvs.logging import get_logger
from dpvs.configs import Args, Project
from hydra.utils import to_absolute_path

log = get_logger()

def run(args: Args):
    project: Project = args.pop('project', None)
    with hydra.initialize(config_path='configs', version_base=None):
        cfg = hydra.compose(
            config_name = project.engine, 
            overrides= [
                f'hydra.run.dir={project.SAVEPATH}',
                f'datapath={to_absolute_path(project.DATAPATH)}',
                f'checkpoint={to_absolute_path(project.CHECKPOINT)}'
            ]
        )
    OmegaConf.set_struct(cfg, False)
    cfg = OmegaConf.merge(cfg, OmegaConf.create(args.d))
    if project.engine == 'torch':
        torch_run(cfg)
    elif project.engine == 'sklearn':
        scikit_run(cfg)

def scikit_run(cfg):
    # 0. load necessary libraries
    from dpvs.engines.sklearn_run import Engine
    from dpvs.datasets import Datasets

    # 1. load model
    checkpoint = f"{cfg.checkpoint}/best_{cfg.model.name}_model.pt"
    model = hydra.utils.instantiate(cfg.model, checkpoint=checkpoint)
    log.info(f"Model: {model}")

    # 2. load trainer
    trainer: Engine = hydra.utils.instantiate(cfg.trainer, base_estimator=model)

    # 3. load dataset
    data: Datasets = hydra.utils.instantiate(cfg.data)

    # 4. running experiment
    trainer.run(data, checkpoint)



def torch_run(cfg: DictConfig):
    # 0. load necessary libraries
    import torch
    from ignite.engine import Engine, create_supervised_evaluator
    from ignite.metrics import Accuracy, Loss

    # 1. set seed for torch, random and numpy
    if cfg.seed:
        seed_all(cfg.seed)

    # 2. load model module (load best model if exists)
    model = hydra.utils.instantiate(cfg.model).to(cfg.device)
    log.info(f"Model: {model}")

    # 3. resume training if checkpoint exists
    checkpoint = f"{cfg.checkpoint}/best_model.pt"
    try:
        log.info(f'Checkpoint set to {checkpoint}')
        model.load_state_dict(torch.load(checkpoint), strict=False)
    except OSError: pass # start training from scratch

    # 4. create trainer
    trainer: Engine = hydra.utils.instantiate(cfg.trainer.engine, model, cfg)

    # 5. create dataset
    data = hydra.utils.instantiate(cfg.data)
    trainer.state.data = data

    # 6. create evaluator with performance metrics
    metrics = {'acc': Accuracy(), 'nll': Loss(trainer.state.criterion)}
    evaluator: Engine = create_supervised_evaluator(model, metrics=metrics, device=cfg.device)
    trainer.state.evaluator = evaluator

    # 7. add callback
    for name, callback in cfg.callbacks.items():
        hydra.utils.instantiate(callback, trainer)
    
    # 8. start training
    trainer.run(data.train, max_epochs=cfg.epochs, seed=cfg.seed)

    # 9. return best evaluation score
    return 0