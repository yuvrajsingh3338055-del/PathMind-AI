import streamlit as st


def profile_sidebar():

    st.sidebar.markdown(
        "<br>",
        unsafe_allow_html=True
    )

    st.sidebar.image(

        "assets/yuvraj.png",

        width=120
    )

    st.sidebar.markdown(
        """
        <div style="
            text-align:center;
        ">

        <h2 style="
            color:white;
            margin-bottom:5px;
        ">
            Yuvraj Singh
        </h2>

        <p style="
            color:#00f5ff;
            font-size:16px;
            font-weight:bold;
        ">
            Founder • PathMind AI 🚀
        </p>

        <p style="
            color:#94a3b8;
            font-size:13px;
        ">
            Building AI-powered career intelligence systems
        </p>

        </div>
        """,

        unsafe_allow_html=True
    )