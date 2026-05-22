import streamlit as st

from app.utils.resume_builder import generate_resume


def show_resume_builder():

    st.title("🧾 AI Resume Builder")

    name = st.text_input(
        "Full Name"
    )

    role = st.text_input(
        "Target Role"
    )

    skills = st.text_area(
        "Skills"
    )

    education = st.text_area(
        "Education"
    )

    projects = st.text_area(
        "Projects"
    )

    if st.button("Generate Resume"):

        resume = generate_resume(

            name,
            role,
            skills,
            education,
            projects
        )

        st.subheader(
            "📄 Generated Resume"
        )

        st.code(
            resume,
            language="markdown"
        )

        st.download_button(

            label="📥 Download Resume",

            data=resume,

            file_name="resume.md",

            mime="text/markdown"
        )