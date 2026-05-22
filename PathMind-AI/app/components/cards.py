import streamlit as st


def metric_card(title, value, description):

    st.container(border=True)

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:18px;
            background:rgba(255,255,255,0.03);
            border:1px solid rgba(255,255,255,0.06);
            margin-bottom:15px;
        ">

        <h3 style="
            color:#00F5FF;
            margin-bottom:10px;
        ">
            {title}
        </h3>

        <h1 style="
            color:white;
            margin-bottom:10px;
        ">
            {value}
        </h1>

        <p style="
            color:#94a3b8;
        ">
            {description}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )