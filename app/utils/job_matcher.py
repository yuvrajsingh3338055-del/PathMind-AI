def calculate_job_match(resume_skills, job_description):

    job_description = job_description.lower()

    matched_skills = []

    for skill in resume_skills:

        if skill.lower() in job_description:

            matched_skills.append(skill)

    if len(resume_skills) == 0:

        score = 0

    else:

        score = int(
            (len(matched_skills) / len(resume_skills)) * 100
        )

    return score, matched_skills