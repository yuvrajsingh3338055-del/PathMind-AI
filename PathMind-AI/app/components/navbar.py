from streamlit_option_menu import option_menu
import streamlit as st


def navigation():

    with st.sidebar:

        selected = option_menu(
            menu_title="PathMind AI",

            options=[
                "Dashboard",
                "Upload Resume",
                "Analytics",
                "Recommendations",
                "AI Mentor",
                "ATS Analyzer",
                "Roadmap Generator",
                "Interview Simulator",
                "Resume Builder",
                "Admin Dashboard",
                "AI Chatbot"
            ],

            icons=[
                "speedometer2",
                "file-earmark-arrow-up",
                "graph-up",
                "stars",
                "robot",
                "clipboard-data",
                "map",
                "chat-dots",
                "file-earmark-text",
                "shield-lock",
                "chat-square-dots"
            ],

            menu_icon="denger",

            default_index=0,
        )

    return selected