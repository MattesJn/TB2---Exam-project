import streamlit as st
from male_page import function_male
from female_page import function_female

st.title("⚽ Football Scout ⚽")

options = ["male football", "female football"]
page_selection = st.sidebar.selectbox("Menu", options)

if "male_football" not in st.session_state:
    st.session_state.male_football = 0

if "female_football" not in st.session_state:
    st.session_state.female_football = 0

if page_selection == "male football":
    st.session_state.male_football = 1
    st.session_state.female_football = 0

if page_selection == "female football":
    st.session_state.female_football = 1
    st.session_state.male_football = 0

if st.session_state.male_football == 1:
    function_male()

if st.session_state.female_football == 1:
    function_female()
