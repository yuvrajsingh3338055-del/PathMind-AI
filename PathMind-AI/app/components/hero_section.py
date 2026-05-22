import streamlit as st


def hero_section():

    st.markdown(
        """
        <div style="
            padding:40px;
            border-radius:25px;
            background:linear-gradient(
                135deg,
                rgba(0,245,255,0.12),
                rgba(59,130,246,0.12)
            );
            margin-bottom:30px;
        ">

        <h1 style="
            color:white;
            font-size:48px;
            margin-bottom:10px;
        ">
            🚀 PathMind AI
        </h1>

        <p style="
            color:#cbd5e1;
            font-size:20px;
        ">
            AI-Powered Career Intelligence Platform
        </p>

        </div>
        """,

        unsafe_allow_html=True
    )