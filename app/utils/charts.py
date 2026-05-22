import plotly.express as px

import pandas as pd


def generate_skill_chart(skills):

    df = pd.DataFrame({

        "Skill": skills,

        "Value": [1] * len(skills)
    })

    chart = px.bar(

        df,

        x="Skill",

        y="Value",

        color="Skill",

        title="📊 Detected Skills Analysis"
    )

    chart.update_layout(

        xaxis_title="Skills",

        yaxis_title="Strength",

        template="plotly_dark"
    )

    return chart