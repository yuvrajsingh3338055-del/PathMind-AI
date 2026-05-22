def evaluate_answer(answer):

    answer = answer.lower()

    if len(answer) >= 150:

        return (
            "Excellent detailed answer 🚀"
        )

    elif len(answer) >= 80:

        return (
            "Good answer 👍 "
            "Add more technical depth."
        )

    elif len(answer) >= 30:

        return (
            "Average answer ⚠️ "
            "Explain concepts better."
        )

    else:

        return (
            "Weak answer ❌ "
            "Provide more detailed explanation."
        )