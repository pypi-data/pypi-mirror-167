from pathlib import Path
from dataclasses import dataclass
import os

class Args:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            assert key != 'd', "property d is reserved for other purpose"
            self.set(key, value)
    @property
    def d(self):
        return self.__dict__
    def update(self, **kwargs):
        for k,v in kwargs.items():
            self.set(k, v)
    def set(self,__name, __value):
        setattr(self, __name, __value)
    def pop(self,__name, __default):
        return self.__dict__.pop(__name, __default)


@dataclass
class Project:
    root: str = Path(__file__).parent
    name: str = 'project_name'
    data: str = 'data'
    log: str = 'logs'
    model: str = 'checkpoint'
    engine: str = 'torch'

    def __post_init__(self):
        self.ROOT = Path(os.getenv('PROJECT_ROOT', self.root))
        self.SAVEPATH = self.ROOT/self.log/self.name
        
        if os.path.isabs(self.data):
            self.DATAPATH = Path(self.data)
        else:
            self.DATAPATH = self.ROOT/self.data
        if os.path.isabs(self.model):
            self.CHECKPOINT = Path(self.model)
        else:
            self.CHECKPOINT = self.SAVEPATH/self.model
        self.CHECKPOINT.mkdir(exist_ok=True, parents=True)
        self.DATAPATH.mkdir(exist_ok=True, parents=True)
    
    def parse(self):
        pass