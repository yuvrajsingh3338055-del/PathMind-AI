import os

import google.generativeai as genai

from dotenv import load_dotenv


load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


def fallback_response(question):

    question = question.lower()

    if "ai" in question:

        return (
            "Focus on Python, Machine Learning, "
            "Deep Learning, and real AI projects."
        )

    elif "data" in question:

        return (
            "Learn Pandas, NumPy, SQL, "
            "Power BI, and visualization."
        )

    elif "resume" in question:

        return (
            "Build strong projects and optimize "
            "your technical skills section."
        )

    elif "job" in question:

        return (
            "Focus on internships, GitHub, "
            "LinkedIn, and project building."
        )

    else:

        return (
            "Continue improving technical skills "
            "and building real-world projects."
        )


def mentor_response(question, skills):

    try:

        skill_text = ", ".join(skills)

        prompt = f"""
        You are PathMind AI,
        an advanced AI career mentor.

        User Skills:
        {skill_text}

        User Question:
        {question}

        Give:
        - roadmap
        - learning advice
        - project guidance
        - career direction
        """

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception:

        return fallback_response(question)