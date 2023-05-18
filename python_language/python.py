import streamlit as st
from multi_page import MultiPage
from python_language.pages import data_type, date_time, decision, function, intro, keyword, list, numbers, string, tuple

def python_run():
    app = MultiPage()
    logo_col1, logo_col2, logo_col3 = st.columns(3)
    with logo_col1:
        pass
    with logo_col2:
        st.image("images/python.png",
                 width=200)
    with logo_col3:
        pass
    st.title("Python - Programming Language")

    app.add_page("Introduction", intro.app)
    app.add_page("Data Type", data_type.app)
    app.add_page("Keywords", keyword.app)
    app.add_page("Number", numbers.app)
    app.add_page("Decision", decision.app)
    app.add_page("Function", function.app)
    app.add_page("Date-Time Module", date_time.app)
    app.add_page("List", list.app)
    app.add_page("Tuple", tuple.app)
    app.add_page("String", string.app)

    app.run()