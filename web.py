import streamlit as st
import pandas as pd

st.write("""
# STREAMLIT DEMO
""")

file = st.file_uploader("UPLOAD RAW FILE")
application = st.sidebar.text_input('application')
age = st.slider('How old are you?', 0, 130, 25)
st.write(" I'm ", age, 'years old')
train_df = pd.read_csv("train.csv")
st.dataframe(train_df.head())
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.code("""
@st.cache
def get_data():
    url = "http://data.insideairbnb.com/[...]"
    return pd.read_csv(url)
""", language="python")



