import sqlite3


def connect_db():

    conn = sqlite3.connect(
        "users.db"
    )

    return conn


def create_users_table():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS accounts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            password TEXT
        )
        """
    )

    conn.commit()

    conn.close()


def register_user(

    username,
    password
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(

        """
        INSERT INTO accounts (
            username,
            password
        )

        VALUES (?, ?)
        """,

        (
            username,
            password
        )
    )

    conn.commit()

    conn.close()


def login_user(

    username,
    password
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT * FROM accounts

        WHERE username = ?
        AND password = ?
        """,

        (
            username,
            password
        )
    )

    data = cursor.fetchone()

    conn.close()

    return data