import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python",
    "sql",
    "machine learning",
    "data science",
    "deep learning",
    "power bi",
    "excel",
    "tableau",
    "statistics",
    "pandas",
    "numpy",
    "streamlit",
    "ai",
    "nlp",
    "tensorflow",
    "scikit-learn",
    "java",
    "c++",
    "communication",
    "leadership"
]

def extract_skills(text):

    text = text.lower()

    detected_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            detected_skills.append(skill)

    return list(set(detected_skills))