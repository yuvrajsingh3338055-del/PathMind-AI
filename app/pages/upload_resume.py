import streamlit as st

from app.utils.parser import extract_text_from_pdf
from app.utils.skill_extractor import extract_skills


def show_upload_resume():

    st.title("📄 Resume Intelligence System")

    st.markdown(
        """
        Upload your resume and let PathMind AI
        analyze your technical skills,
        career readiness,
        and ATS compatibility.
        """
    )

    uploaded_file = st.file_uploader(

        "Upload Resume (PDF)",

        type=["pdf"]
    )

    if uploaded_file is not None:

        with st.spinner(
            "🤖 Analyzing Resume with AI..."
        ):

            extracted_text = extract_text_from_pdf(
                uploaded_file
            )

            skills = extract_skills(
                extracted_text
            )

            st.session_state["skills"] = skills

            st.session_state["resume_text"] = extracted_text

        st.success(
            "✅ Resume uploaded successfully!"
        )

        st.markdown("---")

        st.subheader(
            "🧠 Detected Skills"
        )

        if skills:

            cols = st.columns(3)

            for index, skill in enumerate(skills):

                with cols[index % 3]:

                    st.success(
                        skill.upper()
                    )

        else:

            st.warning(
                "No skills detected."
            )

        st.markdown("---")

        st.subheader(
            "📑 Extracted Resume Text"
        )

        st.text_area(

            "Resume Content",

            extracted_text,

            height=300
        )