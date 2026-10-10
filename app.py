import pandas as pd
import streamlit as st
from datetime import datetime
from db_helper import (
    init_db,
    add_user,
    verify_user,
    fetch_users,
    change_password
)
import openpyxl
from PIL import Image
import base64
from io import BytesIO
from deep_translator import MyMemoryTranslator


# =========================================================
# MAIN APP
# =========================================================

def main():

    # Initialize database
    init_db()

    # =====================================================
    # CUSTOM CSS
    # =====================================================

    st.markdown(
        """
        <style>

        .main-app-title {
            background: linear-gradient(135deg, #124d0b, #1dfa02);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            font-size: 2.2rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 35px;
            box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2);
            letter-spacing: 1px;
        }

        div[data-testid="stVerticalBlockBorderDiv"] {
            border: 3px dotted #FF4B4B !important;
            padding: 30px !important;
            border-radius: 12px !important;
            background-color: #ffffff !important;
            box-shadow: none !important;
        }

        .heading-bar {
            background-color: #124d0b;
            color: white;
            padding: 12px 15px;
            border-radius: 6px;
            font-size: 1.4rem;
            font-weight: bold;
            margin-bottom: 25px;
            text-align: center;
        }

        section[data-testid="stSidebar"] .stButton button {
            margin-bottom: 8px;
            text-align: left !important;
            justify-content: flex-start !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # MAIN TITLE
    # =====================================================

    st.markdown(
        '<div class="main-app-title">🎓 STUDENT App</div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # SESSION STATES
    # =====================================================

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""

    if "login_time" not in st.session_state:
        st.session_state.login_time = ""

    if "auth_action" not in st.session_state:
        st.session_state.auth_action = "Login"

    if "current_page" not in st.session_state:
        st.session_state.current_page = "Dashboard"

    # =====================================================
    # AFTER LOGIN
    # =====================================================

    if st.session_state.logged_in:

        # =================================================
        # SIDEBAR
        # =================================================

        with st.sidebar:

            st.title(f"👋 Hello, {st.session_state.username}!")

            # -----------------------------
            # Dashboard
            # -----------------------------

            db_type = (
                "primary"
                if st.session_state.current_page == "Dashboard"
                else "secondary"
            )

            if st.button(
                "📊 Dashboard",
                type=db_type,
                use_container_width=True
            ):
                st.session_state.current_page = "Dashboard"
                st.rerun()

            # -----------------------------
            # Change Password
            # -----------------------------

            cp_type = (
                "primary"
                if st.session_state.current_page == "Change Password"
                else "secondary"
            )

            if st.button(
                "🔑 Change Password",
                type=cp_type,
                use_container_width=True
            ):
                st.session_state.current_page = "Change Password"
                st.rerun()

            # -----------------------------
            # Analytics
            # -----------------------------

            an_type = (
                "primary"
                if st.session_state.current_page == "Analytics"
                else "secondary"
            )

            if st.button(
                "📈 Analytics",
                type=an_type,
                use_container_width=True
            ):
                st.session_state.current_page = "Analytics"
                st.rerun()

            # -----------------------------
            # Contact Us
            # -----------------------------

            ce_type = (
                "primary"
                if st.session_state.current_page == "Contact US"
                else "secondary"
            )

            if st.button(
                "📞 Contact Us",
                type=ce_type,
                use_container_width=True
            ):
                st.session_state.current_page = "Contact US"
                st.rerun()

            # -----------------------------
            # Data Entry
            # -----------------------------

            de_type = (
                "primary"
                if st.session_state.current_page == "Data Entry"
                else "secondary"
            )

            if st.button(
                "📝 Data Entry",
                type=de_type,
                use_container_width=True
            ):
                st.session_state.current_page = "Data Entry"
                st.rerun()

            # -----------------------------
            # Image Upload
            # -----------------------------

            im_type = (
                "primary"
                if st.session_state.current_page == "Image Upload"
                else "secondary"
            )

            if st.button(
                "🖼️ Image Upload",
                type=im_type,
                use_container_width=True
            ):
                st.session_state.current_page = "Image Upload"
                st.rerun()

            # -----------------------------
            # Instagram
            # -----------------------------

            in_type = (
                "primary"
                if st.session_state.current_page == "Instagram"
                else "secondary"
            )

            if st.button(
                "📸 Instagram",
                type=in_type,
                use_container_width=True
            ):
                st.session_state.current_page = "Instagram"
                st.rerun()

            # -----------------------------
            # Video Upload
            # -----------------------------

            vu_type = (
                "primary"
                if st.session_state.current_page == "Video Upload"
                else "secondary"
            )

            if st.button(
                "📹 Video Upload",
                type=vu_type,
                use_container_width=True
            ):
                st.session_state.current_page = "Video Upload"
                st.rerun()

            # -----------------------------
            # Admission Form
            # -----------------------------

            af_type = (
                "primary"
                if st.session_state.current_page == "Admission Form"
                else "secondary"
            )

            if st.button(
                "📝 Admission Form",
                type=af_type,
                use_container_width=True
            ):
                st.session_state.current_page = "Admission Form"
                st.rerun()

            # -----------------------------
            # Logout
            # -----------------------------

            st.markdown("---")

            if st.button(
                "🚪 Log Out",
                use_container_width=True
            ):

                st.session_state.logged_in = False
                st.session_state.username = ""
                st.session_state.login_time = ""
                st.session_state.current_page = "Dashboard"

                st.rerun()

        # =================================================
        # WELCOME MESSAGE
        # =================================================

        st.success(
            f"Welcome back, {st.session_state.username}!"
        )

        st.caption(
            f"🕒 **Logged in since:** "
            f"{st.session_state.login_time}"
        )

        # =================================================
        # DASHBOARD
        # =================================================

        if st.session_state.current_page == "Dashboard":

            st.subheader("👥 Dashboard")

            try:

                raw_users = fetch_users()

                if raw_users:

                    df = pd.DataFrame(
                        raw_users,
                        columns=["Username", "Password Hash"]
                    )

                    # Hide password hash
                    df_display = df[["Username"]]

                    st.dataframe(
                        df_display,
                        use_container_width=True,
                        hide_index=True
                    )

                    st.metric(
                        label="Total Registered Users",
                        value=len(df_display)
                    )

                else:

                    st.info(
                        "No registered users found in the database."
                    )

            except Exception as e:

                st.error(
                    f"Error loading dashboard directory: {e}"
                )

        # =================================================
        # CHANGE PASSWORD
        # =================================================

        elif st.session_state.current_page == "Change Password":

            col1, col2, col3 = st.columns([1, 1.8, 1])

            with col2:

                with st.container(border=True):

                    st.markdown(
                        '<div class="heading-bar">'
                        'Change Password'
                        '</div>',
                        unsafe_allow_html=True
                    )

                    current_password = st.text_input(
                        "🔑 Current Password",
                        type="password"
                    )

                    new_password = st.text_input(
                        "🆕 New Password",
                        type="password"
                    )

                    confirm_password = st.text_input(
                        "🔁 Confirm New Password",
                        type="password"
                    )

                    if st.button(
                        "Update Password",
                        use_container_width=True
                    ):

                        if (
                            current_password.strip() == ""
                            or new_password.strip() == ""
                            or confirm_password.strip() == ""
                        ):

                            st.warning(
                                "Please fill in all fields."
                            )

                        elif new_password != confirm_password:

                            st.error(
                                "New passwords do not match!"
                            )

                        elif new_password == current_password:

                            st.warning(
                                "New password cannot be "
                                "the same as your old password."
                            )

                        else:

                            if verify_user(
                                st.session_state.username,
                                current_password
                            ):

                                try:

                                    change_password(
                                        st.session_state.username,
                                        new_password
                                    )

                                    st.success(
                                        "Password updated successfully!"
                                    )

                                except Exception as e:

                                    st.error(
                                        f"Database error: {e}"
                                    )

                            else:

                                st.error(
                                    "Incorrect current password."
                                )

        # =================================================
        # ANALYTICS
        # =================================================

        elif st.session_state.current_page == "Analytics":

            st.subheader("📊 Analytics")

            st.write(
                f"This is your personalized "
                f"{st.session_state.current_page.lower()} view."
            )

        # =================================================
        # CONTACT US
        # =================================================

        elif st.session_state.current_page == "Contact US":

            st.subheader("📞 Contact Us")

            st.write(
                "Click the button below if you need "
                "to get in touch with our team."
            )

            @st.dialog(
                "Contact Information",
                width="small"
            )
            def show_contact_form():

                st.write(
                    "Feel free to reach out using "
                    "the form below!"
                )

                name = st.text_input(
                    "Your Name"
                )

                email = st.text_input(
                    "Your Email Address"
                )

                message = st.text_area(
                    "Your Message"
                )

                if st.button(
                    "Submit Inquiry"
                ):

                    if (
                        name.strip() == ""
                        or email.strip() == ""
                        or message.strip() == ""
                    ):

                        st.error(
                            "Please fill out all fields "
                            "before submitting."
                        )

                    else:

                        st.success(
                            f"Thank you, {name}! "
                            "Your message has been sent."
                        )

            if st.button(
                "Contact Us",
                use_container_width=True
            ):

                show_contact_form()

        # =================================================
        # DATA ENTRY
        # =================================================

        elif st.session_state.current_page == "Data Entry":

            st.subheader("📝 Data Entry")

            st.title("📂 Excel File Upload")

            uploaded_file = st.file_uploader(
                "Upload Excel File",
                type=["xlsx", "xls"]
            )

            if uploaded_file is not None:

                try:

                    df = pd.read_excel(
                        uploaded_file
                    )

                    st.success(
                        "File uploaded successfully!"
                    )

                    st.dataframe(
                        df,
                        use_container_width=True
                    )

                except Exception as e:

                    st.error(
                        f"Error reading the Excel file: {e}"
                    )

        # =================================================
        # IMAGE UPLOAD
        # =================================================

        elif st.session_state.current_page == "Image Upload":

            st.subheader("🖼️ Image Upload")

            st.write(
                "Upload an image file below:"
            )

            uploaded_image = st.file_uploader(
                "Choose an image file",
                type=["png", "jpg", "jpeg"]
            )

            if uploaded_image is not None:

                try:

                    image = Image.open(
                        uploaded_image
                    )

                    buffer = BytesIO()

                    image.save(
                        buffer,
                        format="PNG"
                    )

                    img_base64 = base64.b64encode(
                        buffer.getvalue()
                    ).decode()

                    st.markdown(
                        f"""
                        <div style="
                            display:flex;
                            justify-content:center;
                        ">
                            <img
                                src="data:image/png;base64,{img_base64}"
                                style="
                                    width:250px;
                                    height:250px;
                                    border-radius:50%;
                                    object-fit:cover;
                                "
                            >
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.success(
                        "Image uploaded successfully!"
                    )

                except Exception as e:

                    st.error(
                        f"Error displaying the image: {e}"
                    )

        # =================================================
        # INSTAGRAM
        # =================================================

        elif st.session_state.current_page == "Instagram":

            st.subheader("📸 Instagram")

            st.write(
                "Welcome to the Instagram view!"
            )

            st.write(
                "Click the button below to visit Instagram."
            )

            st.link_button(
                "Visit Instagram",
                "https://www.instagram.com/"
            )

        # =================================================
        # VIDEO UPLOAD
        # =================================================

        elif st.session_state.current_page == "Video Upload":

            st.subheader("📹 YouTube Video")

            st.write(
                "Paste a YouTube video link below:"
            )

            youtube_url = st.text_input(
                "YouTube URL",
                placeholder="https://www.youtube.com/watch?v=..."
            )

            if youtube_url:

                try:

                    st.video(
                        youtube_url
                    )

                except Exception as e:

                    st.error(
                        f"Error playing YouTube video: {e}"
                    )

        # =================================================
        # Admission Form
        # =================================================
        
        elif st.session_state.current_page == "Admission Form":

            st.subheader("📝 Admission Form")

            st.write(
                "Please fill out the admission form below:"
            )
            st.set_page_config(page_title="Admission Form", page_icon="📝",layout="centered")
            st.markdown("""
            <style>
            .stApp {
                background-color: #000000;
            }
            h1 {
                text-align: center;
                color: #adff2f;
                font-size: 36px;
                font-weight: 400;
            }
            label {
                color: #00ff00  !important;
                }
                div.stbutton>button {
                background-color::#ffffff;
                color: white;
                border-radius: 8px;
                border: none;
                width: 100%;
                }
                div.stbutton>button:hover {
                background-color:#ffffff;
                color: white;
                }
            </style>
            """, unsafe_allow_html=True)
            st.title("school Admission Form")
            st.write("Please fill out the form below to apply for admission.")
            with st.form("admission_form"):
                st.markdown("**student`s Name:**")
                col1, col2 = st.columns(2)
                with col1:
                    first_name = st.text_input("First", key="student_first")
                with col2:
                    last_name = st.text_input("Last Name", key="student_last")
                class_name = st.text_input(
                "Class you want to apply for  *",
                 placeholder="for example: 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th, 11th, 12th",)
                dob = st.date_input(
                    "student`s DOB  *",
                    min_value=datetime(2000, 1, 1),
                    max_value=datetime(2026, 12, 31),
                   help="Please select the student's date of birth."
                )
                st.markdown("**Parent`s/ Guardian`s Name:**")
                col1, col2 = st.columns(2)
                with col1:
                    parent_first = st.text_input(
                        "First Name", key="parent_first"
                    )   
                with col2:
                    parent_last = st.text_input(
                        "Last Name", key="parent_last"
                    )
                st.markdown("**Current Address**")
                street = st.text_input("Street Address")
                street2 = st.text_input("Street Address Line 2")

                col1, col2 = st.columns(2)
                with col1:
                    city = st.text_input("City")
                with col2:
                    region = st.text_input("Region")

                col1, col2 = st.columns(2)
                with col1:
                    postal = st.text_input("Postal / Zip Code")
                with col2:
                    country = st.selectbox(
                        "Country",
                        ["Select Country", "India", "USA",
                        "UK", "Canada", "Australia"]
                    )
                phone = st.text_input("Phone", placeholder="Phone Number")
                email = st.text_input("Email *", placeholder="Email")

                submitted = st.form_submit_button("Submit")

                if submitted:
                    if not all([
                        first_name, last_name, class_name,
                        parent_first, parent_last, email
                    ]):
                        st.error("Please fill in all required fields.")
                    elif "@" not in email or "." not in email.split("@")[-1]:
                        st.error("Please enter a valid email address.")
                    elif dob is None:
                        st.error("Please select the student's date of birth.")
                    else:
                        st.success("Admission form submitted successfully!")

                        st.subheader("Admission Details")
                        st.write("Student Name:", first_name, last_name)
                        st.write("Class:", class_name)
                        st.write("Date of Birth:", dob)
                        st.write("Parent Name:", parent_first, parent_last)
                        st.write("Address:", street, street2, city, region, postal, country)
                        st.write("Phone:", phone)
                        st.write("Email:", email)
        # ================================================
        # UNKNOWN PAGE
        # =================================================

        else:

            st.warning(
                "Page not found. Returning to Dashboard."
            )

            st.session_state.current_page = "Dashboard"
            st.rerun()

    # =====================================================
    # LOGIN / SIGN UP PAGE
    # IMPORTANT: THIS ELSE FIXES YOUR LOGIN ISSUE
    # =====================================================

    else:

        # Reset current page when logged out
        st.session_state.current_page = "Dashboard"

        # ---------------------------------------------
        # CENTER LOGIN BOX
        # ---------------------------------------------

        col1, col2, col3 = st.columns([1, 1.8, 1])

        with col2:

            with st.container(border=True):

                # -----------------------------------------
                # LOGIN / SIGN UP BUTTONS
                # -----------------------------------------

                btn_col1, btn_col2 = st.columns(2)

                with btn_col1:

                    login_type = (
                        "primary"
                        if st.session_state.auth_action == "Login"
                        else "secondary"
                    )

                    if st.button(
                        "🔑 Go to Login",
                        type=login_type,
                        use_container_width=True
                    ):

                        st.session_state.auth_action = "Login"
                        st.rerun()

                with btn_col2:

                    signup_type = (
                        "primary"
                        if st.session_state.auth_action == "Sign Up"
                        else "secondary"
                    )

                    if st.button(
                        "📝 Go to Sign Up",
                        type=signup_type,
                        use_container_width=True
                    ):

                        st.session_state.auth_action = "Sign Up"
                        st.rerun()

                st.markdown(
                    "<hr style='margin:15px 0; "
                    "border:0; "
                    "border-top:1px solid #eee;'>",
                    unsafe_allow_html=True
                )

                # =========================================
                # LOGIN SECTION
                # =========================================

                if st.session_state.auth_action == "Login":

                    st.markdown(
                        '<div class="heading-bar">'
                        'Login Section'
                        '</div>',
                        unsafe_allow_html=True
                    )

                    username = st.text_input(
                        "👤 Username"
                    )

                    password = st.text_input(
                        "👁️ Password",
                        type="password"
                    )

                    if st.button(
                        "Login",
                        use_container_width=True
                    ):

                        if (
                            username.strip() == ""
                            or password.strip() == ""
                        ):

                            st.warning(
                                "Please enter username "
                                "and password."
                            )

                        else:

                            if verify_user(
                                username,
                                password
                            ):

                                # -------------------------
                                # SUCCESSFUL LOGIN
                                # -------------------------

                                st.session_state.logged_in = True

                                st.session_state.username = (
                                    username
                                )

                                st.session_state.login_time = (
                                    datetime.now().strftime(
                                        "%d-%b-%Y %I:%M %p"
                                    )
                                )

                                # Go to dashboard
                                st.session_state.current_page = (
                                    "Dashboard"
                                )

                                # Refresh app
                                st.rerun()

                            else:

                                st.error(
                                    "Invalid username or password"
                                )

                # =========================================
                # SIGN UP SECTION
                # =========================================

                elif st.session_state.auth_action == "Sign Up":

                    st.markdown(
                        '<div class="heading-bar">'
                        'Create New Account'
                        '</div>',
                        unsafe_allow_html=True
                    )

                    new_user = st.text_input(
                        "👤 Choose Username"
                    )

                    new_password = st.text_input(
                        "🔒 Choose Password",
                        type="password"
                    )

                    if st.button(
                        "Sign Up",
                        use_container_width=True
                    ):

                        if (
                            new_user.strip() == ""
                            or new_password.strip() == ""
                        ):

                            st.warning(
                                "Please fill in all fields"
                            )

                        elif add_user(
                            new_user,
                            new_password
                        ):

                            st.success(
                                "Account created successfully! "
                                "Please log in."
                            )

                            st.session_state.auth_action = (
                                "Login"
                            )

                            st.rerun()

                        else:

                            st.error(
                                "Username already exists. "
                                "Choose another."
                            )


# =========================================================
# RUN APP
# =========================================================

if __name__ == "__main__":
    main()
