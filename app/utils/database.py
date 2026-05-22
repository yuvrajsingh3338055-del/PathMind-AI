import sqlite3


def connect_db():

    conn = sqlite3.connect(
        "pathmind.db"
    )

    return conn


def create_table():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            skills TEXT,

            ats_score INTEGER
        )
        """
    )

    conn.commit()

    conn.close()


def save_user_data(

    name,
    skills,
    ats_score
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(

        """
        INSERT INTO users (
            name,
            skills,
            ats_score
        )

        VALUES (?, ?, ?)
        """,

        (
            name,
            skills,
            ats_score
        )
    )

    conn.commit()

    conn.close()


def get_all_users():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users"
    )

    data = cursor.fetchall()

    conn.close()

    return data