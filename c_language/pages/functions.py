import streamlit as st
from pathlib import Path

def app():
    path = "c_language/md_page/function.md"
    lines = Path(path).read_text()
    st.markdown(lines, unsafe_allow_html=True)