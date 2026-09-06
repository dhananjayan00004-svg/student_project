import streamlit as st
from db_helper import init_db

def main():
    init_db()
    st.title("login page")
    
if __name__ == "__main__":
    main()