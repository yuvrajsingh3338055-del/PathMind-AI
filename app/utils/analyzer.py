def calculate_scores(skills):

    total_skills = len(skills)

    skill_score = min(total_skills * 10, 100)

    career_readiness = min(
        total_skills * 8,
        100
    )

    if total_skills >= 10:

        market_demand = "High"

    elif total_skills >= 5:

        market_demand = "Medium"

    else:

        market_demand = "Low"

    return {

        "skill_score": skill_score,

        "career_readiness": career_readiness,

        "market_demand": market_demand
    }