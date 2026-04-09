import streamlit as st

st.set_page_config(layout="wide")

col_izq, col_centro, col_der = st.columns([1, 2, 1])

with col_izq:
    st.header("Sugerencias de IA")
    st.write("Aquí aparecerán las sugerencias.")

with col_centro:
    st.header("Editor de Texto")
    st.text_area("Sección del proyecto", height=400)

with col_der:
    st.header("Esquema")
    st.write("1. Título")
    st.write("2. Introducción")