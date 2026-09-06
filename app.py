import streamlit as st
from db_helper import init_db

def main():
    init_db()
    st.title("login page")
    choice = st.selectbox("Choose an option", ["Login", "Create Account"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    st.button("login")

if __name__ == "__main__":
    main()