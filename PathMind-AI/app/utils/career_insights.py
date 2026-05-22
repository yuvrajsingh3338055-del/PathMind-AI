def get_career_insights(role):

    insights = {

        "AI Engineer": {

            "salary": "$120K+",

            "demand": "Very High",

            "difficulty": "Advanced",

            "project": "Build an AI Chatbot"
        },

        "Data Scientist": {

            "salary": "$110K+",

            "demand": "High",

            "difficulty": "Medium",

            "project": "Netflix Recommendation System"
        },

        "Web Developer": {

            "salary": "$90K+",

            "demand": "High",

            "difficulty": "Medium",

            "project": "Full Stack Portfolio Website"
        },

        "Cybersecurity": {

            "salary": "$115K+",

            "demand": "Very High",

            "difficulty": "Advanced",

            "project": "Security Scanner Tool"
        }
    }

    return insights.get(
        role,
        {}
    )