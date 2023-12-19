# type: ignore
import streamlit as st

from utils import get_answer_csv

st.header("Prediktif Analysis dengan Chatbot PredikGPT ")
uploaded_file = st.file_uploader("Upload file data csv anda", type=["csv"])

if uploaded_file is not None:
    query = st.text_area("Tanyakan pertanyaan yang berkenaan dengan dokumen yang diupload")
    button = st.button("Kirim")
    if button:
        st.write(get_answer_csv(uploaded_file, query))
