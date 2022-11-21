from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from imblearn.over_sampling import SMOTE, BorderlineSMOTE
from imblearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE, BorderlineSMOTE
from imblearn.under_sampling import RandomUnderSampler
from functions import Preprocess
from typing import Optional, Union
import pandas as pd
from enum import Enum
import time
import re

class ScalerType(Enum):
    minmaxscaler:str = 'normalize'
    standardscaler:str = 'standardize'


class Model(Enum):
    rf:str = 'rf'
    adboost:str = 'adaboost'
    dt:str = 'dt'
    nn:str = 'nn'


class Train(Preprocess):
    def __init__(self,model:Model,**kwargs):
        super().__init__(**kwargs)
        print(self.sampling_strategy)
        self.model = model

    def make_pipeline():
        pass

    def __call__(self,X):
        split = train_test_split(X)
        print("Split finished")
        steps = self.build_pipeline_steps()

        return steps
    pass



if __name__ == '__main__':
    train = Train(model='rf',test_size = 0.3,sampling_strategy = 'upsample',scaler = 'minmax')
    preprocessing_steps = train(pd.read_csv('WSN-DS.csv'))
    print(preprocessing_steps)