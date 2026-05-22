def calculate_ats_score(
    resume_skills,
    job_description
):

    job_description = job_description.lower()

    matched_skills = []

    missing_skills = []

    important_skills = [

        "python",
        "sql",
        "machine learning",
        "data science",
        "power bi",
        "excel",
        "streamlit",
        "deep learning",
        "pandas",
        "numpy"
    ]

    for skill in resume_skills:

        if skill.lower() in job_description:

            matched_skills.append(skill)

    for skill in important_skills:

        if (
            skill in job_description
            and skill not in [
                s.lower() for s in resume_skills
            ]
        ):

            missing_skills.append(skill)

    score = int(

        (
            len(matched_skills)
            / len(important_skills)
        ) * 100
    )

    return {

        "score": score,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills
    }