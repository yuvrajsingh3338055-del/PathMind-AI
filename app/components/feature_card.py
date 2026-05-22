import streamlit as st


def feature_card(
    title,
    description,
    emoji
):

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:20px;
            background:rgba(255,255,255,0.05);
            margin-bottom:20px;
        ">

        <h3 style="color:white;">
            {emoji} {title}
        </h3>

        <p style="color:#cbd5e1;">
            {description}
        </p>

        </div>
        """,

        unsafe_allow_html=True
    )