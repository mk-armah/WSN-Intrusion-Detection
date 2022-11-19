from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from imblearn.over_sampling import SMOTE,BorderlineSMOTE
from imblearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler


from enum import Enum


# class ScalerType(Enum):
#     minmaxscaler = MinMaxScaler()
#     standardscaler = StandardScaler()


 
class Preprocess():
    def __init__(self,train_sample_size,
                sampling_strategy:str,data,scaler = None)

        self.train_sample_size = train_sample_size
        self.strategy = sampling_strategy
        self.apply_scale = False
        try:
            assert self.scaler == 'minmax' or 'scaler' or None 
        except AssertionError:
            raise("scaler should be one of | minmax,scaler or None")


    def train_test_split(self):
        X = df.drop(columns = ['attack_type','id','who_ch','time'],axis = 1)
        
        y = df['attack_type']
        
        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42,stratify = y)
        
        return X_train, X_test, y_train, y_test

    def make_pipeline(self):
        if self.sampling_strategy == 'undersample':
            sampling = RandomUnderSampler(sampling_strategy= {'Normal':10217},random_state=42)

        elif self.sampling_strategy == 'upsampling':
            sampling  = BorderlineSMOTE(random_state=111)

        steps = [("sampling_strategy",sampling)]
        
        if self.scaler is not None:
            steps.append(("scaler",scaler))

        
        