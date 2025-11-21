from __future__ import annotations
import pandas as pd
import requests
import streamlit as st
from functions.common_utils import API_TOKEN, API_URL

@st.cache_data(show_spinner=False)
def obtener_datos(fecha_corte: str) -> pd.DataFrame:
    
    if not API_URL or not API_TOKEN:
        st.error("Las variables de entorno API_URL o API_TOKEN no están configuradas.")
        return pd.DataFrame()

    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    params = {"endpoint": "presupuesto", "fecha_corte": fecha_corte}

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame([data.get("resumen", {})])
    except requests.exceptions.RequestException as e:
        st.error(f"Error al obtener datos de la API: {e}")
        return pd.DataFrame()