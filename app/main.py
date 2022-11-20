from fastapi import FastAPI
from model import Features,Model
import joblib 
from utils import load_model
from aws import AWS
import os

#load environment variables
from dotenv import load_dotenv
load_dotenv(".env")

#assign environment variables to variables
ACCESS_KEY_ID = os.environ.get("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.environ.get("SECRET_ACCESS_KEY")

app  = FastAPI()
s3 = AWS(ACCESS_KEY_ID,SECRET_ACCESS_KEY,"wsn-intrusion-detection")

@app.post("/{}/predict")
def predictions( is_ch: int, dist_to_ch: int|float,
                adv_s: int, adv_r: int,
                join_s: int, join_r: int,
                sch_s: int, sch_r: int,
                rank: int, data_s: int,
                data_r: int, data_sent_to_bs:int,
                dist_ch_to_bs:int|float,send_code: int,
                expaned_energy:int|float, model:Model):
                
            
            features = [is_ch,dist_to_ch,adv_s,adv_r,join_s,
            join_r,sch_s,sch_r,rank,data_s,data_r,data_sent_to_bs,
            dist_ch_to_bs,send_code,expaned_energy]
            
            #load model
            model = load_model(model)
            output = model.predict(features)
            
            return {"Features":features,"Model Prediction":output}


@app.get("/{}/download")
def getmodel():
    """download/send model to user"""
    return {}

