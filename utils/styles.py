# utils/styles.py

from pathlib import Path
import streamlit as st


def load_css(*css_files: str) -> None:
    """
    Carga uno o varios archivos CSS y los inyecta en Streamlit.
    Rutas relativas a la raíz del proyecto.
    """
    # Detectar la raíz del proyecto (carpeta donde está app.py)
    root_dir = Path(__file__).resolve().parent.parent

    css_content = ""
    for css_file in css_files:
        css_path = root_dir / css_file
        if css_path.is_file():
            css_content += css_path.read_text(encoding="utf-8") + "\n"

    if css_content:
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
