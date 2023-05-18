import streamlit as st
from home import home
from c_language.c import c_run
from cpp_language.cpp import cpp_run
from python_language.python import python_run

selected = st.sidebar.radio("Page selection : ",
                            ("Home","C","C++","Python"))

if selected == "Home":
    home()
if selected == "C":
    c_run()
if selected == "C++":
    cpp_run()
if selected == "Python":
    python_run()