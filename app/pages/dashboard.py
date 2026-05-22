import streamlit as st

from app.components.hero_section import hero_section
from app.components.feature_card import feature_card


def show_dashboard():

    hero_section()

    skills = st.session_state.get(
        "skills",
        []
    )

    total_skills = len(skills)

    ats_score = min(
        total_skills * 10,
        100
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🧠 Skills",
            total_skills
        )

    with col2:

        st.metric(
            "🎯 ATS Score",
            f"{ats_score}%"
        )

    with col3:

        st.metric(
            "🚀 Career",
            "High"
        )

    st.markdown("## 🌟 Features")

    feature_card(
        "Resume Analyzer",
        "Analyze resumes using AI.",
        "📄"
    )

    feature_card(
        "AI Mentor",
        "Get career guidance.",
        "🤖"
    )

    feature_card(
        "Interview Simulator",
        "Practice interviews.",
        "🎤"
    )

    if skills:

        st.subheader(
            "🔥 Detected Skills"
        )

        for skill in skills:

            st.success(skill)

    else:

        st.warning(
            "Upload resume to continue."
        )