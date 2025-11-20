# functions/common_utils.py

import os
import datetime
import requests
import pandas as pd
from dotenv import load_dotenv
import streamlit as st

# CONFIGURACIÓN GLOBAL

load_dotenv()  # Carga el archivo .env solo aquí

API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")


# FUNCIONES COMPARTIDAS

