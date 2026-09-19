import streamlit as st
from db_helper import init_db, add_user,verify_user, get_all_users
def main():
    init_db()
    st.title("login page")
    choice = st.selectbox("Choose an option", ["Login", "Create Account"])
    if choice == "Create Account":
        st.subheader("Create New Account")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        if st.button("Create Account"):
            if new_username and new_password:
                add_user(new_username, new_password)
                st.success(f"Account created for {new_username}!")
            elif not new_username or not new_password:
                st.error("Please enter both username and password.")
            else:
                st.error("Account creation failed. Please try again.")
    elif choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if verify_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid username or password.")
           

if __name__ == "__main__":
    main()