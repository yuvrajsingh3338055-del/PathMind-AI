import streamlit as st

from app.utils.recommender import generate_recommendations


def show_recommendations():

    st.title("⭐ AI Career Recommendations")

    st.markdown(
        """
        Personalized AI-powered recommendations
        based on your resume and detected skills.
        """
    )

    skills = st.session_state.get("skills", [])

    if skills:

        recommendations = generate_recommendations(
            skills
        )

        st.subheader("🧠 Recommended Improvements")

        for rec in recommendations:

            st.info(rec)

        st.markdown("---")

        st.subheader("🚀 Suggested Career Path")

        lower_skills = [

            skill.lower()

            for skill in skills
        ]

        if "machine learning" in lower_skills:

            st.success(
                "Recommended Career: AI Engineer / Data Scientist"
            )

        elif "power bi" in lower_skills:

            st.success(
                "Recommended Career: Data Analyst / BI Developer"
            )

        elif "python" in lower_skills:

            st.success(
                "Recommended Career: Software Developer"
            )

        else:

            st.warning(
                "Build more technical projects to unlock stronger career recommendations."
            )

    else:

        st.warning(
            "Upload a resume first."
        )