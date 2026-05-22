import streamlit as st

from app.utils.career_insights import get_career_insights


def show_roadmap():

    st.title(
        "🧠 AI Career Roadmap"
    )

    role = st.selectbox(

        "Choose Career Path",

        [

            "AI Engineer",

            "Data Scientist",

            "Web Developer",

            "Cybersecurity"
        ]
    )

    # ROADMAPS
    if role == "AI Engineer":

        roadmap = [

            "Python",

            "Machine Learning",

            "Deep Learning",

            "LLMs",

            "AI Projects"
        ]

    elif role == "Data Scientist":

        roadmap = [

            "Python",

            "Pandas",

            "Statistics",

            "Visualization",

            "Machine Learning"
        ]

    elif role == "Web Developer":

        roadmap = [

            "HTML",

            "CSS",

            "JavaScript",

            "React",

            "Backend"
        ]

    else:

        roadmap = [

            "Networking",

            "Linux",

            "Ethical Hacking",

            "Penetration Testing",

            "Cloud Security"
        ]

    # BUTTON
    if st.button(
        "Generate Roadmap"
    ):

        insights = get_career_insights(
            role
        )

        st.success(
            f"{role} Roadmap Generated 🚀"
        )

        # METRICS
        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "💰 Salary",

                insights["salary"]
            )

        with col2:

            st.metric(

                "📈 Demand",

                insights["demand"]
            )

        with col3:

            st.metric(

                "⚡ Difficulty",

                insights["difficulty"]
            )

        st.markdown("---")

        # PROJECT CARD
        st.markdown(

            f"""
            <div class="glass-card">

            <h3>
                🚀 Recommended Project
            </h3>

            <p>
                {insights["project"]}
            </p>

            </div>
            """,

            unsafe_allow_html=True
        )

        st.markdown("## 🛣️ Learning Roadmap")

        # ROADMAP LOOP
        for index, skill in enumerate(

            roadmap,

            start=1
        ):

            st.markdown(

                f"""
                <div class="glass-card">

                <h3>
                    Step {index}
                </h3>

                <p>
                    {skill}
                </p>

                </div>
                """,

                unsafe_allow_html=True
            )