from ignite.engine import Events, Engine
from typing import Callable, List
from dpvs.logging import get_logger

log = get_logger()

def add_lr_scheduler(engine, scheduler):
    def function(engine:Engine, scheduler: Callable):
        optimizer = engine.state.optimizer
        scheduler = scheduler(optimizer=optimizer)
        evaluator = engine.state.evaluator
        evaluator.add_event_handler(Events.EPOCH_COMPLETED, scheduler)
    engine.add_event_handler(Events.STARTED, function, scheduler)

def log_performance(engine):
    from dpvs.utils import xtable
    def function(engine: Engine):
        state = engine.state
        evaluator, train, val, test = state.evaluator, *state.data
        train_dict = evaluator.run(train).metrics.copy()
        val_dict = evaluator.run(val).metrics.copy()
        test_dict = evaluator.run(test).metrics.copy()
        log.info(f'Epoch {state.epoch} \n' + xtable(
            dicts=[train_dict, val_dict, test_dict], 
            index=['train','valid','test'],
            fcodes=['', '.6f', '.6f', '.6f', '.6f'], 
            pads=['<8','>10','>10', '>10', '>10']
        ))
    engine.add_event_handler(Events.EPOCH_COMPLETED, function)


def log_loss(engine, keys=[]):
    from dpvs.datasets.utils import xgroup
    def d2str(d: dict):
        return '  |  '.join(f'{k}: {v:<8.6f}' for k,v in d.items()) 
    def function(engine: Engine, keys: List[str]):
        output = engine.state.output
        output = xgroup(output, 5)
        res = '\n'.join(f'{k:<7s} |     {d2str(output[k])} ' for k in keys)
        log.info(res+'\n')
    engine.add_event_handler(Events.EPOCH_COMPLETED, function, keys)
    
