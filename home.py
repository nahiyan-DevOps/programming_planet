import streamlit as st
import mysql.connector
import pandas as pd

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
    st.empty()
    st.subheader("About Me")
    # MySQL database connection details
    host = '192.168.20.112'
    port = 3306
    user = 'app_db'
    password = '1234'
    db_name = 'app_db'
    table_name = 'about'

    # Connect to the MySQL database
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name
        )
        cursor = connection.cursor()

        # Fetch all rows from the table
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Create a pandas DataFrame from the fetched data
        df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
        df = df.reset_index(drop=True)
        df = df.drop('id', axis=1)
        df = df.set_index('author_name')
        # Display the DataFrame in Streamlit
        st.dataframe(df)

    except mysql.connector.Error as error:
        st.error(f"Error connecting to MySQL: {error}")

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()