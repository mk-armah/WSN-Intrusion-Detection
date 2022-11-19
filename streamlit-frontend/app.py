import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv(".env")
ACCESS_KEY_ID = os.environ.get("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.environ.get("SECRET_ACCESS_KEY")


st.set_page_config(page_title="WSN ID", page_icon=":}", layout="centered")

st.title("WSN Intrusion Detection")


st.sidebar.write(
    f"This app shows how a Streamlit app can interact easily with a [Google Sheet] to read or store data."
)

st.sidebar.write(
    f"[Read more](https://docs.streamlit.io/knowledge-base/tutorials/databases/public-gsheet) about connecting your Streamlit app to Google Sheets."
)

form = st.form(key="annotation")

with form:
    cols = st.columns((1, 1))
    author = cols[0].text_input("Report author:")
    bug_type = cols[1].selectbox(
        "Bug type:", ["Front-end", "Back-end", "Data related", "404"], index=2
    )

    comment = st.text_area("Comment:")
    cols = st.columns(2)
    date = cols[0].date_input("Bug date occurrence:")
    bug_severity = cols[1].slider("Bug severity:", 0, 1)
    submitted = st.form_submit_button(label="Submit")


if submitted:

    st.success("Predictions {}") #predictions goes
    st.balloons() 

expander = st.expander("See all records")
with expander:
    st.write(f"Open original [Google Sheet]({GSHEET_URL})")
    st.dataframe(get_data(gsheet_connector))