def chatbot_response(message):

    message = message.lower()

    if "python" in message:

        return (
            "Python is one of the best "
            "languages for AI, Data Science, "
            "and backend development."
        )

    elif "ai" in message:

        return (
            "Focus on Machine Learning, "
            "Deep Learning, and AI projects."
        )

    elif "resume" in message:

        return (
            "Keep your resume ATS-friendly "
            "with strong projects and skills."
        )

    elif "job" in message:

        return (
            "Build projects, optimize LinkedIn, "
            "and apply consistently."
        )

    elif "skills" in message:

        return (
            "Focus on high-income technical "
            "skills and real-world projects."
        )

    else:

        return (
            "Continue learning and building 🚀"
        )