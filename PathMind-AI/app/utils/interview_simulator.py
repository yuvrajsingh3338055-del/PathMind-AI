import streamlit as st

from app.utils.interview_questions import get_questions
from app.utils.interview_evaluator import evaluate_answer


def show_interview_simulator():

    st.title("🎤 AI Interview Simulator")

    role = st.selectbox(

        "Choose Interview Role",

        [

            "AI Engineer",

            "Data Scientist",

            "Data Analyst"
        ]
    )

    if st.button("Start Interview"):

        questions = get_questions(role)

        st.subheader(
            "🧠 Interview Questions"
        )

        for question in questions:

            st.info(question)

            answer = st.text_area(

                f"Your Answer - {question}",

                height=120
            )

            if answer:

                feedback = evaluate_answer(
                    answer
                )

                st.success(feedback)

        st.success(
            "🚀 Interview Simulation Completed"
        )