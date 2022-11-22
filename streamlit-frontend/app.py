import pandas as pd
import streamlit as st
from utils import predict
from ast import literal_eval

hide_menu = """<style>#MainMenu {
    visibility:visible
}
    footer{
        visibility: visible;
    }

    footer:after{
        visibility: visible;
        content = 'copyright chael.ai';
        display:block
        position:relative;
        color:tomato;
    }
}</style>"""


def main():

    st.set_page_config(page_title="WSN ID", page_icon=":}", layout="centered")
    st.title("WSN Intrusion Detection")

    #hide menu bar
    st.markdown(hide_menu,unsafe_allow_html = True)


    model = st.sidebar.selectbox(
            "Select Classifier:", ['Adaboost',"Random Forest", "Decision Tree", "Artificial Neural Network"], index=1
        )

    cols = st.sidebar.columns(2)

    #temporal feature | only adaboost is currently in production
    if model == 'Adaboost':

        cols[0].download_button(
            label="Download Model",
            data="csv",
            file_name='adaboost.chael',
            mime='text/csv',
        )

        cols[1].download_button(
        label="Source Code",
        data="csv",
        file_name='source.code',
        mime='text/csv',
    )

    else:
        st.sidebar.write("Model is currently unavailable")




    #Read me

    # with open("README.text",'r') as file:
    #     readme = file.read()

    # st.sidebar.write(readme)

    # st.sidebar.write(
    #     f"[Github Repository](https://github.com/mk-armah/WSN-Intrusion-Detection)"
    # )
    # st.sidebar.write(
    #     f"Engineered By: Chael.AI"
    # )

    st.image('https://psiborg.in/wp-content/uploads/2021/07/Embedded-banner-2048_11zon-1.jpg')
    form = st.form(key="annotation")


    with form:
        cols = st.columns((1, 1))
        dist_to_ch = cols[0].number_input("dist_to_ch")
        is_channel = cols[1].selectbox(
            "is channel:", [0,1], index=1
        )

        cols = st.columns(3)
        adv_s = cols[0].number_input("adv_s") 
        adv_r = cols[1].number_input("adv_r")
        expaned_energy = cols[2].number_input("expaned_energy")

        cols = st.columns(3)
        sch_s = cols[0].number_input("sch_s") 
        sch_r = cols[1].selectbox(
            "sch_r:", [0,1], index=1
        )
        send_code = cols[2].slider("send_code",0, 15,1)

        cols = st.columns(2)
        data_sent_to_bs = cols[0].number_input("data sent to base station")
        dist_ch_to_bs = cols[1].number_input("distance from cluster head to base station")

        cols = st.columns(2)
        data_s = cols[0].number_input("data_s") 
        data_r = cols[1].number_input("data_r")
        
        cols = st.columns(3)
        join_s = cols[0].number_input("join_s") 
        join_r = cols[1].number_input("join_r")
        rank = cols[2].number_input("rank")

        submitted = st.form_submit_button(label="Predict")

    if submitted:
        
        with st.spinner(text='In progress'):

            prediction = predict(model = model,is_ch = is_channel,dist_to_ch = float(dist_to_ch),
                                adv_s = int(adv_s),adv_r = int(adv_r),join_s = int(join_s),
                                join_r = int(join_r),sch_s = int(sch_s), sch_r = int(sch_r),
                                rank = 1,data_s = int(data_s), data_r = int(data_r),
                                data_sent_to_bs = int(data_sent_to_bs),
                                dist_ch_to_bs = float(dist_ch_to_bs),
                                send_code = send_code, expaned_energy = float(expaned_energy))

            try:
                
                assert prediction.status_code == 200  #upon successful request/prediction
                
                predictions_in_bytes = prediction.content
                prediction = literal_eval(predictions_in_bytes.decode('utf-8'))

                prediction = prediction['status'][0]

                if prediction == 'Normal':

                    st.success("{} Attack  |  All clear ".format(prediction)) #predictions goes
                    st.balloons() 
            
                elif prediction in ['TDMA',"Flooding","Blackhole","Grayhole"]:

                    st.warning("{} Attack Detected".format(prediction)) #predictions goes
            
            except AssertionError:
                if prediction.status_code == 404:

                    error = f"{model} Model Not Found | current version only supports adaboost please consider switching from {model} to adaboost"
                    st.warning(error)
                    
                else:

                    st.warning("An unknown error occured, please consider checking your inputs")

            finally:
                st.info("Don't forget to leave a comment below if you like this work :)")


            expander = st.expander("Leave us a comment")
            with expander:
                comment_form = st.form(key="comments")
                with comment_form:
                    cols = st.columns((2))
                    name = cols[0].text_input("name")
                    email = cols[1].text_input("email address")
                    comment = st.text_area("Comment:")

                    submit_comment = st.form_submit_button(label="Submit")

                    if submit_comment:
                        st.info("Hello {}, your comments on this work has been recieved, out team will contact you via email as soon as possible, Thanks :) ")
                        st.write(name)
    

if __name__ == '__main__':
    main()