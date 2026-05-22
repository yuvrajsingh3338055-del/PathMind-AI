def get_questions(role):

    role = role.lower()

    if role == "ai engineer":

        return [

            "What is Machine Learning?",

            "Explain supervised learning.",

            "What is overfitting?",

            "Difference between AI and ML?",

            "Explain neural networks."
        ]

    elif role == "data scientist":

        return [

            "What is data cleaning?",

            "Explain Pandas.",

            "Difference between mean and median?",

            "What is feature engineering?",

            "Explain data visualization."
        ]

    elif role == "data analyst":

        return [

            "What is SQL?",

            "Explain joins.",

            "What is Power BI?",

            "What is dashboarding?",

            "Explain data reporting."
        ]

    else:

        return [

            "Tell me about yourself.",

            "Why should we hire you?"
        ]