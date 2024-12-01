import streamlit as st

def configure_interface():
    st.title("Upload de Arquivos DIO - Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolher um arquivo", type=["png", "jpg", "pdf"]) 