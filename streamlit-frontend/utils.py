import requests



def predict(model,**kwargs):

    #fifteen features :)

    try:
        # assert len(kwargs.values()) == 15
        features = features_ = ['is_ch', 'dist_to_ch','adv_s','adv_r','join_s','join_r',
                                'sch_s','sch_r','rank','data_s','data_r','data_sent_to_bs',
                                'dist_ch_to_bs','send_code','expaned_energy']
        
        #get all values in features that are also in kwargs
        check = [i for i in features if i in list(kwargs.keys())]

        #check whether their total are equal
        assert len(check) == len(kwargs)
        
    except AssertionError as ass:
        print(check)
        print("an input is feature was excluded {}".format(ass))
                 

    url = "http://api:8000/adaboost/predict"
    output = requests.get(url= url,params = kwargs)
    
    return output


if __name__ == "__main__":

    predictions = predict(model = 'adaboost',is_ch = 1,dist_to_ch = 1,adv_s = 1,adv_r = 1,
                join_s = 1,join_r = 1,sch_s =1,sch_r = 1,rank = 1,
                data_s = 1,data_r = 1,data_sent_to_bs = 1,
                dist_ch_to_bs = 1,send_code = 1,expaned_energy = 1)

    
    print(predictions.content)