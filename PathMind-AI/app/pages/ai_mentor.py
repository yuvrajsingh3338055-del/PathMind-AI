import streamlit as st

from app.utils.mentor import mentor_response


def show_ai_mentor():

    st.title("🤖 AI Career Mentor")

    st.markdown(
        """
        Ask PathMind AI anything about:
        
        • AI careers  
        • Data Science  
        • Resume improvement  
        • Skill growth  
        • Jobs & internships
        """
    )

    skills = st.session_state.get("skills", [])

    user_question = st.text_input(
        "Ask your career question"
    )

    if st.button("Generate AI Advice"):

        if user_question:

            with st.spinner("AI Mentor Thinking..."):

                response = mentor_response(
                    user_question,
                    skills
                )

            st.success(response)

        else:

            st.warning(
                "Please enter a question."
            )

    st.markdown("---")

    st.subheader("💡 Suggested Questions")

    st.info(
        "How can I become an AI Engineer?"
    )

    st.info(
        "What skills should I learn for Data Science?"
    )

    st.info(
        "How can I improve my resume?"
    )

    st.info(
        "What projects should I build?"
    )