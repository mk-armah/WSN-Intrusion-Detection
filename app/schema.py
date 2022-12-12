from pydantic import BaseModel
from enum import Enum

class Features(BaseModel):
    is_ch:str
    dist_to_ch:str
    adv_s:str
    adv_r:str
    join_s:str
    join_r:str
    sch_s:str
    sch_r:str
    rank:str
    data_s:str
    data_r:str
    data_sent_to_bs:str
    dist_ch_to_bs:str
    send_code:str
    expaned_energy:str

class ModelName(str, Enum):
    rf:str  = 'rf'
    adaboost:str = 'adaboost'
    nn:str = 'nn'
    dt:str = 'dt' 