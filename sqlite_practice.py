import sqlite3

with sqlite3.connect("people.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
    """)

    cursor.execute(
        "INSERT INTO people (name, age) VALUES (?, ?)",
        ("Blessy", 22)
    )

    cursor.execute("SELECT * FROM people")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_people_name
    ON people(name)
    """)

    print("Index created successfully")


    name = "Blessy"

    cursor.execute(
        "SELECT * FROM people WHERE name = ?",
        (name,)
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)