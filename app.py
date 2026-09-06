import streamlit as st
from db_helper import init_db

def main():
    init_db()
    st.title("login page")
    choice = st.selectbox("Choose an option", ["Login", "Create Account"])
    if choice == "Create Account":
        st.subheader("Create New Account")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        if st.button("Create Account"):
            # Here you would add logic to create the account in the database
            st.success(f"Account created for {new_username}!")
    elif choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Here you would add logic to authenticate the user
            st.success(f"Logged in as {username}!")

if __name__ == "__main__":
    main()