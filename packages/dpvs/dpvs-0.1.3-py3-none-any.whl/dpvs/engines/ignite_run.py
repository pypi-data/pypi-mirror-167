import torch
import torch.nn as nn
from ignite.engine import Engine
from ignite.contrib.handlers import ProgressBar
from dpvs.logging import get_logger
from dpvs.datasets.utils import xmove
from typing import Dict

def create_engine(
    model: nn.Module, 
    optimizer: torch.optim.Optimizer,
    device: str,
    metrics: dict
    ):
    """
    Combines the .... into an engine
    """
    device = torch.device(device)
    optimizer= optimizer(params=model.parameters())
    
    
    # Training ============================================================
    def train_step(engine, batch):
        model.train()
        x, y = batch
        xmove(x, device)
        y_pred = model(**x)
        loss = model.compute_loss(y_pred, y.to(device))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        return model.loss_d

    # Define trainer engine and keep track of criterion/optimizer
    engine = Engine(train_step)
    # anything you'd be using in callback by adding engine.state.xx = xx
    engine.state.optimizer = optimizer
    engine.state.lr = optimizer.param_groups[0]['lr']

    ProgressBar(
        bar_format='{desc}[{n_fmt}/{total_fmt}]{percentage:3.0f}%{postfix}',
        persist=True
    ).attach(
        engine, 
        output_transform=lambda x: dict([(k, x[k]) for k in ('CE', 'loss')]),
        state_attributes=['lr']
    )
    
    # Evaluation ========================================================
    def test_step(engine, batch):
        model.eval()
        x, y = batch
        xmove(x, device)
        y_prob = model.pred(**x)
        return y_prob.cpu().numpy(), y.cpu().numpy()
    
    evaluator = Engine(test_step)
    for name, metric in metrics.items():
        metric.attach(evaluator, name)
    engine.state.evaluator = evaluator
        
    # change ignite logging level (disable INFO level logging)
    get_logger('ignite.engine.engine.Engine', level='WARNING')

    return engine






     

