import pandas as pd

import numpy as np

from enum import Enum

import warnings
warnings.filterwarnings("ignore")


class Eval(Metrics):
        
    def __init__(self,log_to:logTo = 'wandb',metrics:list[str,None] = None,**kwargs):
        """
        evaluates trained model against classification metrics

        Init Args:
            log_to:str | where to log the results of the evaluation to One of [wandb,logging,console]
            metrics:str | evaluation metric to choose, if metrics is None, accuracy score will be used for evaluation
        """
        super().__init__(**kwargs)
        self.log_to = log_to
        self.metrics = metrics



    # @infologger
    def __call__(self):
        pass

    pass