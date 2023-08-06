import hydra
from omegaconf import DictConfig, OmegaConf
from dpvs.utils import seed_all
from dpvs.logging import get_logger
from dpvs.configs import Args, Project
from hydra.utils import to_absolute_path


log = get_logger(formatter="%(message)s")

def run(args: Args):
    project: Project = args.pop('project', None)
    overrides = [
        f'hydra.run.dir={project.SAVEPATH}',
        f'datapath={to_absolute_path(project.DATAPATH)}',
        f'checkpoint={to_absolute_path(project.CHECKPOINT)}'
    ] + project.override
    with hydra.initialize(config_path='configs', version_base=None):
        cfg = hydra.compose(
            config_name = project.engine, overrides=overrides
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
    from dpvs.datasets import Dataloaders
    from ignite.engine import Engine

    # 1. set seed for torch, random and numpy
    if cfg.seed: seed_all(cfg.seed)
    device = cfg.device

    # 2. load model module (load best model if exists)
    checkpoint = f"{cfg.checkpoint}/best_{cfg.model._target_.split('.')[-1]}_model.pt"
    model = hydra.utils.instantiate(cfg.model).to(device)
    model.restore_from_checkpoint(checkpoint)
    log.info(f"Model: {model}")

    # 3. create trainer
    trainer: Engine = hydra.utils.instantiate(cfg.trainer, model=model,)

    # 4. create dataset
    data: Dataloaders = hydra.utils.instantiate(cfg.data)
    trainer.state.data = data

    # 5. add callback
    for name, callback in cfg.callbacks.items():
        hydra.utils.instantiate(callback, engine=trainer)
    
    # 6. start training
    trainer.run(data.train, max_epochs=cfg.epochs)

    # 7. return best evaluation score
    return 0