import streamlit as st
from pathlib import Path

def app():
    path = "cpp_language/md_page/encapsulation.md"
    lines = Path(path).read_text()
    st.markdown(lines,unsafe_allow_html=True)