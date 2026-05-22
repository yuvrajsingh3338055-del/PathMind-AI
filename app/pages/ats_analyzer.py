import streamlit as st

from app.utils.job_matcher import calculate_job_match
from app.utils.report_generator import generate_report
from app.utils.database import save_user_data

def show_ats_analyzer():

    st.title("📄 ATS Resume Analyzer")

    skills = st.session_state.get("skills", [])

    name = st.text_input(
    "Enter Your Name"
)

    job_description = st.text_area(
        "Paste Job Description"
    )

    if st.button("Analyze Resume Match"):

        score, matched_skills = calculate_job_match(
            skills,
            job_description
        )

        st.subheader("🎯 ATS Match Score")

        st.progress(score / 100)

        st.success(
            f"Match Score: {score}%"
        )
      
        
        save_user_data(

    name,

    ", ".join(skills),

    score
)

        # PDF REPORT GENERATION
        pdf_file = generate_report(
            skills,
            score
        )

        with open(pdf_file, "rb") as file:

            st.download_button(

                label="📥 Download AI Report",

                data=file,

                file_name="PathMind_Report.pdf",

                mime="application/pdf"
            )

        st.subheader("✅ Matched Skills")

        if matched_skills:

            for skill in matched_skills:

                st.info(skill)

        else:

            st.warning(
                "No matching skills found."
            )

    else:

        st.info(
            "Upload resume and paste a job description."
        )