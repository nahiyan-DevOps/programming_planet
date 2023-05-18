import streamlit as st
from multi_page import MultiPage
from c_language.pages import basic, array, conditional, functions, loops, pointer, strings

def c_run():
    app = MultiPage()
    logo_col1, logo_col2, logo_col3 = st.columns(3)
    with logo_col1:
        pass
    with logo_col2:
        st.image("images/c.png",
                 width=200)
    with logo_col3:
        pass
    st.title("C - Programming Language")

    app.add_page("Basic", basic.app)
    app.add_page("Array", array.app)
    app.add_page("Conditional Statement", conditional.app)
    app.add_page("Function", functions.app)
    app.add_page("Loop", loops.app)
    app.add_page("Pointer", pointer.app)
    app.add_page("String", strings.app)

    app.run()