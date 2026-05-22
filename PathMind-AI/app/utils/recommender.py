def generate_recommendations(skills):

    recommendations = []

    skill_set = [skill.lower() for skill in skills]

    if "python" not in skill_set:
        recommendations.append(
            "Learn Python for AI/Data Science development."
        )

    if "sql" not in skill_set:
        recommendations.append(
            "SQL is essential for data handling and analytics."
        )

    if "machine learning" not in skill_set:
        recommendations.append(
            "Start learning Machine Learning fundamentals."
        )

    if "power bi" not in skill_set:
        recommendations.append(
            "Power BI can strengthen your analytics profile."
        )

    if "streamlit" not in skill_set:
        recommendations.append(
            "Build more Streamlit projects to improve deployment skills."
        )

    if len(skills) < 5:
        recommendations.append(
            "Increase technical project experience significantly."
        )

    if not recommendations:
        recommendations.append(
            "Excellent profile. Focus on advanced AI projects and research."
        )

    return recommendations