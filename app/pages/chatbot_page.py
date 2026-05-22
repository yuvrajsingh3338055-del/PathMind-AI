import streamlit as st

from app.utils.chatbot import chatbot_response


def show_chatbot():

    st.title("🤖 AI Career Chatbot")

    user_message = st.text_input(
        "Ask Your Question"
    )

    if st.button("Send"):

        response = chatbot_response(
            user_message
        )

        st.markdown(
            f"""
            <div class="glass-card">

            <h3>
                🤖 AI Response
            </h3>

            <p>
                {response}
            </p>

            </div>
            """,

            unsafe_allow_html=True
        )