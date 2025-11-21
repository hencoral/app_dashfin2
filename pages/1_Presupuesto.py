"""Página de Streamlit para consultar el presupuesto."""

from __future__ import annotations
import datetime
import streamlit as st
from functions.presupuesto_utils import obtener_datos
from utils.styles import load_css

st.set_page_config(page_title="Presupuesto", layout="wide")
# Cargar estilos globales + específicos de la página
load_css("styles/base.css", "styles/presupuesto.css")
st.title("Presupuesto")
st.markdown(
    "Consulta el resumen de presupuesto desde la API proporcionando una fecha de corte."
)

fecha_corte = st.date_input("Fecha de corte", value=datetime.date.today())

with st.spinner("Obteniendo datos de presupuesto..."):
    df_resumen = obtener_datos(fecha_corte.isoformat())
if df_resumen.empty:
    st.info("No se recibieron datos de la API para la fecha seleccionada.")
else:
    st.dataframe(df_resumen, width="stretch")
    st.caption("Datos obtenidos desde el endpoint de presupuesto.")
