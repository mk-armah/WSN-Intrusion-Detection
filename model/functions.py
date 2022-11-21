from typing import Optional, Union
import pandas as pd
from enum import Enum
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from imblearn.over_sampling import SMOTE, BorderlineSMOTE
from imblearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE, BorderlineSMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import (precision_recall_curve,
                             precision_recall_fscore_support,
                             roc_auc_score,
                             plot_confusion_matrix,
                             roc_curve,
                             precision_score,
                             recall_score,
                             accuracy_score,
                             plot_precision_recall_curve)

class Preprocess:

    def __init__(self,sampling_strategy:str,
                test_size:Optional[Union[float, int]] = 0.30,
                train_size:Optional[Union[float, int]] = None,
                scaler:str =  None, **kwargs):

        self.train_size = train_size
        self.test_size = test_size
        self.sampling_strategy = sampling_strategy
        self.apply_scale = False
        self.scaler = scaler

        try:
            assert self.scaler == 'minmax' or 'scaler' or None 
        except AssertionError:
            raise("scaler should be one of | minmax,scaler or None")


    def train_test_split(self,data):
        X = self.data.drop(columns = ['attack_type','id','who_ch','time'],axis = 1)
        
        y = self.data['attack_type']
        
        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=self.test,train_size = self.train_size, random_state=42,stratify = y)
        
        split = {"training":[X_train,y_train],
                "testing":[X_test, y_train, y_test]}
        
        return split

    def remove_anomalies(data):
        drop_duplicates =  lambda x:x.drop_duplicates()
        data = drop_duplicates(data)


    def build_pipeline_steps(self):
        """"builds pipeline steps"""
        
        steps  = []
        print(self.sampling_strategy)
        if self.sampling_strategy == 'undersample':
            sampling = RandomUnderSampler(sampling_strategy= {'Normal':10217},random_state=42)

        elif self.sampling_strategy == 'upsample':
            sampling  = BorderlineSMOTE(random_state=111)
        
        steps:list[tuple] = [("sampling_strategy",sampling)]
        
        if self.scaler is not None:
            steps.append(("scaler",self.scaler))

        return steps


class Metrics: 

    def __init__(self,estimator,y_test,y_pred,verbose:int = 0):
        self.estimator = estimator
        self.verbose = verbose
        self.y_test = y_test

    def prfs_metrics(y_true,y_pred,labels:list = None)->pd.DataFrame:
        """calculates precision recall f1score and support (prfs) metrics
            and presents them in a nicely formatted pandas dataframe
            
            Args:
                y_true:pd.Series/np.array | true values of the target variable
                y_pred:pd.Series/np.array | predictions obtained from a model
                
            Returns:
                metrics:pd.DataFrame | dataframe of prfs metrics"""


        labels = np.unique(y_true) if labels is None else labels
        metrics = pd.DataFrame(

            precision_recall_fscore_support(
                    y_true,y_pred,
                    labels = labels
            ),

            columns = y_true.unique() if labels is None else labels,
            index = ['precision',
                    'recall',
                    'F-measure',
                    'support']
        )
        return metrics

    def plot_confusion_matrix():
        pass

    def cross_validate(self):
        """cross validation"""

        cv_scores = cross_val_score(estimator = self.estimator,cv = 10,X = X_train,y = y_train,error_score = 'raise')
        
        if self.verbose >= 1:

            print("Cross Validation Score : {}".format(cv_scores.mean()))
        
        return cv_scores


    def get_roc_auc_score(self):
        """roc auc score"""

        roc_auc = roc_auc_score(y_test,y_probas, multi_class='ovr')
        
        if self.verbose >= 0:
            print("Adaboost Classifier RoC/AuC Score : {}".format(nb_roc_auc))
        
        return roc_auc
    
    
def Calc_Detection_Speed(func):
    def wrap():
        times = []
        for i in range(100):
            start_time = time.time()
            func().predict(X_test.values.astype(np.float32)) #score the testing data
            times.append(time.time() - start_time)
        avg_inf_time = np.mean(times)
        
        pattern= "ds_(.*)"
        match = re.search(pattern,func.__name__)

        if match:
            content = match.group(1)
            algorithm = re.sub('_'," ",content)
            formatted_results = algorithm+" Classifier has an average speed of : {}s".format(round(avg_inf_time,3))
        else:
            print("Unrecognized Algorithm naming convention")
            
        return formatted_results
    
    return wrap



def infologger(func,task:str = 'train'):

    """log model metrics to use desired location | This is a decorator function
    Args:
        func: function | evaluation function """

    def wrapper():
        
        print("Model is evaluating\n")
        
        print("-"*15,"\n")

        return wrapper



