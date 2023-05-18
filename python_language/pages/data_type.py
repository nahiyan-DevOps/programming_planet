import streamlit as st
from pathlib import Path

def app():
    path = "python_language/md_page/datatype.md"
    lines = Path(path).read_text()
    st.markdown(lines,unsafe_allow_html=True)