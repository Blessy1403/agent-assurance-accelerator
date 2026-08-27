import sqlite3

user_input = "'; DROP TABLE people; --"

with sqlite3.connect("people.db") as conn:
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM people WHERE name = ?",
        (user_input,)
    )

    result = cursor.fetchall()

    print(result)