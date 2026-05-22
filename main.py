import streamlit as st

from app.components.navbar import navigation

from app.components.footer import footer
from app.components.profile_sidebar import profile_sidebar
from app.utils.database import create_table
from app.pages.dashboard import show_dashboard
from app.pages.upload_resume import show_upload_resume
from app.pages.analytics import show_analytics
from app.pages.recommendations import show_recommendations
from app.pages.ai_mentor import show_ai_mentor
from app.pages.ats_analyzer import show_ats_analyzer
from app.pages.roadmap import show_roadmap
from app.pages.interview_simulator import show_interview_simulator
from app.pages.resume_builder import show_resume_builder
from app.pages.admin_dashboard import show_admin_dashboard
from app.pages.chatbot_page import show_chatbot

from app.pages.login import show_login

from app.utils.auth import create_users_table

#----------------- create_table-----------------#

create_table()
create_users_table()


# ----------------footer-----------------------#

footer()


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(

    page_title="PathMind AI",

    page_icon="🚀",

    layout="wide"
)


# ---------------- LOAD CSS ---------------- #
def load_css():

    with open(
        "app/styles/main.css"
    ) as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True
        )


load_css()

# --------------profile_sidebar-----------------#

profile_sidebar()


# ---------------- NAVIGATION ---------------- #

selected = navigation()

# --------------ADD LOGIN GATE-----------------#


if "logged_in" not in st.session_state:

    st.session_state[
        "logged_in"
    ] = False


if not st.session_state["logged_in"]:

    show_login()

    st.stop()
# ---------------- ROUTING ---------------- #

if selected == "Dashboard":

    show_dashboard()

elif selected == "Upload Resume":

    show_upload_resume()

elif selected == "Analytics":

    show_analytics()

elif selected == "Recommendations":

    show_recommendations()

elif selected == "AI Mentor":

    show_ai_mentor()

elif selected == "ATS Analyzer":

    show_ats_analyzer()

elif selected == "Roadmap Generator":

    show_roadmap()

elif selected == "Interview Simulator":

    show_interview_simulator()

elif selected == "Resume Builder":

    show_resume_builder()

elif selected == "Admin Dashboard":

    show_admin_dashboard()

elif selected == "AI Chatbot":

    show_chatbot()