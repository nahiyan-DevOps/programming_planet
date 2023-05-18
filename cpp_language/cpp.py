import streamlit as st
from multi_page import MultiPage
from cpp_language.pages import array, constructor, dataAabstruction, datatype, decission_making, encapsulation, friend_function, function, input_output, intro, loop, object_class, overloading, structure, token, variables

def cpp_run():
    app = MultiPage()
    logo_col1, logo_col2, logo_col3 = st.columns(3)
    with logo_col1:
        pass
    with logo_col2:
        st.image("images/cpp.png",
                 width=200)
    with logo_col3:
        pass
    st.title("C++ - Programming Language")

    app.add_page("Introduction", intro.app)
    app.add_page("Data Type", datatype.app)
    app.add_page("Variables", variables.app)
    app.add_page("I/O", input_output.app)
    app.add_page("Array", array.app)
    app.add_page("Decission Statements", decission_making.app)
    app.add_page("Loops", loop.app)
    app.add_page("Function", function.app)
    app.add_page("Structure", structure.app)
    app.add_page("Token", token.app)
    app.add_page("OOP", object_class.app)
    app.add_page("Constructor", constructor.app)
    app.add_page("Data Abstruction", dataAabstruction.app)
    app.add_page("Encapsulation", encapsulation.app)
    app.add_page("Overloading", overloading.app)
    app.add_page("Friend Function", friend_function.app)

    app.run()