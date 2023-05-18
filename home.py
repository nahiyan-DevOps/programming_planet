import streamlit as st

def home():
    logo_col1, logo_col2, logo_col3 = st.columns(3)
    with logo_col1:
        pass
    with logo_col2:
        st.image("images/Logo.png",
                 width=200)
    with logo_col3:
        pass
    st.title("Welcome to Programming Planet")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/c.png", width=150)
    with col2:
        st.image("images/cpp.png", width=150)
    with col3:
        st.image("images/python.png", width=150)

    st.subheader("Programming Planet is a place where every newbie can get a head start to the magical world of coding")