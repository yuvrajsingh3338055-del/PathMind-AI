import streamlit as st

from app.utils.database import get_all_users


def show_admin_dashboard():

    st.title("🛡️ Admin Dashboard")

    users = get_all_users()

    total_users = len(users)

    st.metric(

        "👥 Total Users",

        total_users
    )

    st.subheader(
        "📊 User Records"
    )

    if users:

        for user in users:

            st.markdown(
                f"""
                <div class="glass-card">

                <h3>
                    👤 {user[1]}
                </h3>

                <p>
                    <b>Skills:</b> {user[2]}
                </p>

                <p>
                    <b>ATS Score:</b> {user[3]}%
                </p>

                </div>
                """,

                unsafe_allow_html=True
            )

    else:

        st.warning(
            "No users found."
        )