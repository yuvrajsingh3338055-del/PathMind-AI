import streamlit as st

from app.utils.charts import generate_skill_chart


def show_analytics():

    st.title("📊 Career Analytics Dashboard")

    skills = st.session_state.get("skills", [])

    if skills:

        st.subheader("🧠 Skills Intelligence")

        chart = generate_skill_chart(
            skills
        )

        st.plotly_chart(
            chart,
            width="stretch"
        )

        st.subheader("📈 Analytics Insights")

        st.success(
            f"{len(skills)} technical skills detected."
        )

        if len(skills) >= 10:

            st.info(
                "Excellent technical profile."
            )

        elif len(skills) >= 5:

            st.warning(
                "Strong foundation with growth potential."
            )

        else:

            st.error(
                "Need more technical skill development."
            )

    else:

        st.warning(
            "Upload a resume first."
        )