import streamlit as st

from app.utils.auth import (

    register_user,

    login_user
)


def show_login():

    st.title("🔐 PathMind AI Login")

    menu = st.selectbox(

        "Select Option",

        [

            "Login",

            "Register"
        ]
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(

        "Password",

        type="password"
    )

    if menu == "Register":

        if st.button("Create Account"):

            register_user(

                username,
                password
            )

            st.success(
                "Account Created Successfully 🚀"
            )

    else:

        if st.button("Login"):

            result = login_user(

                username,
                password
            )

            if result:

                st.session_state[
                    "logged_in"
                ] = True

                st.success(
                    "Login Successful 🚀"
                )

            else:

                st.error(
                    "Invalid Username or Password"
                )