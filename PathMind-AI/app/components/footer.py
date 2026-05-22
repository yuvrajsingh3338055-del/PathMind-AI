import streamlit as st


def footer():

    st.markdown(
        """
        <hr style="
            margin-top:40px;
            border:1px solid rgba(255,255,255,0.08);
        ">

        <div style="
            text-align:center;
            padding:20px;
            color:#94a3b8;
            font-size:14px;
        ">

        🚀 Built with Streamlit & AI <br>

        Founder • Yuvraj Singh <br>

        PathMind AI © 2026

        </div>
        """,

        unsafe_allow_html=True
    )