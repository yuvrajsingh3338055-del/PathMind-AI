SKILLS = [

    "python",
    "machine learning",
    "deep learning",
    "sql",
    "java",
    "c++",
    "html",
    "css",
    "javascript",
    "react",
    "pandas",
    "numpy",
    "tensorflow",
    "streamlit",
    "ai",
    "data science",
    "flask",
    "django",
    "git",
    "github"
]


def extract_skills(text):

    text = text.lower()

    detected_skills = []

    for skill in SKILLS:

        if skill in text:

            detected_skills.append(skill)

    return detected_skills