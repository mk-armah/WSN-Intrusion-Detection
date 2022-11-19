import pandas as pd
import streamlit as st


st.set_page_config(page_title="WSN ID", page_icon=":}", layout="centered")

st.title("WSN Intrusion Detection")

import time

model = st.sidebar.selectbox(
        "Select Classifier:", ['Adaboost',"Random Forest", "Decision Tree", "Artificial Neural Network"], index=1
    )

cols = st.sidebar.columns(2)
cols[0].download_button(
    label="Download Model",
    data="csv",
    file_name='large_df.csv',
    mime='text/csv',
)

cols[1].download_button(
    label="Download Data",
    data="csv",
    file_name='dataset.csv',
    mime='text/csv',
)

#Read me

# with open("README.text",'r') as file:
#     readme = file.read()

# st.sidebar.write(readme)

st.sidebar.write(
    f"[Github Repository](https://github.com/mk-armah/WSN-Intrusion-Detection)"
)
st.sidebar.write(
    f"Engineered By: Chael.AI"
)

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
    data_sent_to_bs = cols[0].number_input("data_sent_to_bs") 
    dist_ch_to_bs = cols[1].number_input("dist_ch_to_bs")

    cols = st.columns(2)
    data_s = cols[0].number_input("data_s") 
    data_r = cols[1].number_input("data_r")

    
    submitted = st.form_submit_button(label="Predict")

if submitted:
    with st.spinner(text='In progress'):
        import time
        time.sleep(5)
        st.success("{} Attack Detected".format("predictions")) #predictions goes
        st.balloons() 
        st.info("Don't forget to leave a comment below if you like this work :)")

        # st.snow()
        st.warning('Warning message')

expander = st.expander("Give your comments")

with expander:
     comment = st.text_area("Comment:")