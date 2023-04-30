import streamlit as st
from web_functions import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "visualisation" : visualise
}

# membuat sidebar
st.sidebar.title("Navigasi")

#membuat radio option
page = st.sidebar.radio("pages", list (Tabs.keys()))

#load dataset
df, x, y = load_data()

#kondisi call app fuction
if page in ["Prediction", "visualisation"]:
    Tabs[page].app(df, x,y)
else:
    Tabs[page].app() 
 