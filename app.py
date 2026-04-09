import streamlit as st

st.set_page_config(layout="wide")

# El orden ahora es: Esquema (izq), Centro (editor), Sugerencias (der)
col_esquema, col_centro, col_sugerencias = st.columns([1, 2, 1])

with col_esquema:
    st.header("Esquema")
    st.write("1. Título")
    st.write("2. Introducción")

with col_centro:
    st.header("Editor de Texto")
    st.text_area("Sección del proyecto", height=400)

with col_sugerencias:
    st.header("Sugerencias de IA")
    st.write("Aquí aparecerán las sugerencias.")