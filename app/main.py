"""This script serves as a server to a streamlit frontend

Author : Ing. Michael Kofi Armah
Last Update Date : 21-11-22"""
from fastapi import FastAPI
from schema import Features,ModelName
import joblib 
from aws import AWS
import os
import numpy as np
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fastapi import Request


app  = FastAPI()

templates = Jinja2Templates(directory="./templates")



app.mount(
    "/templates/js",
    StaticFiles(
        directory="templates/js"),
    name="js")

app.mount(
    "/templates/css",
    StaticFiles(
        directory="templates/css"),
    name="css")

app.mount(
    "/templates/scss",
    StaticFiles(
        directory="templates/scss"),
    name="scss")


@app.get("/")
async def home(request:Request):
    return templates.TemplateResponse(
        "index.html",context= {"request":request})



@app.get("/{model_name}/predict")
def predictions( is_ch: int, dist_to_ch: int|float,
                adv_s: int, adv_r: int,
                join_s: int, join_r: int,
                sch_s: int, sch_r: int,
                rank: int, data_s: int,
                data_r: int, data_sent_to_bs:int,
                dist_ch_to_bs:int|float,send_code: int,
                expaned_energy:int|float, model_name:ModelName):
                
        
            features = [
                        is_ch,dist_to_ch,adv_s,                 
                        adv_r,join_s,join_r,sch_s,sch_r,                
                        rank,data_s,data_r,data_sent_to_bs,     
                        dist_ch_to_bs,send_code,expaned_energy 
                    ]
            
            #load model

            try:
                modelpath = "./models/"+model_name.value+".chael"
                model = joblib.load(modelpath)

            except Exception as exc:
                return {'status':"model unavailable"}

            prediction = model.predict(np.array(features).reshape(1,-1))  
            prediction = list(prediction)

            return {"status":prediction}



# --- ---- ---- more functionalities --- --- --- -- 
@app.get("/{}/download")
def getmodel():
    """download/send model to user"""
    return {}