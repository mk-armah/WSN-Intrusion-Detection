import joblib
from model import Model

def load_model(model):
    if model == Model.rf:
        model = joblib.load("../models/rf.chael")
        return Model
    if model == Model.adaboost:
        model = joblib.load("../models/adaboost.chael")
        return Model
    if model == Model.dt:
        model = joblib.load("../models/dt.chael")
        return Model
    if model == Model.nn:
        model = joblib.load("../models/nn.chael")
        return Model
    else:
        return None

    #Alternative code
    # try:
    #     modelpath = "../models"+model+."chael"
    #     model.load(modelpath)
    # except Exception as exc:
    #     return None