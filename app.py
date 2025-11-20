import streamlit as st
# codigo inicial de la app
st.set_page_config(
    page_title="Dashboard Financiero Cronhis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Dashboard Financiero - Cronhis")

st.markdown("""
Bienvenido al sistema de análisis presupuestal.

Seleccione una página desde el menú lateral.
""")