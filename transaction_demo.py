import sqlite3

try:
    with sqlite3.connect("people.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO people(name, age) VALUES (?, ?)",
            ("Alice", 25)
        )

        # Intentional error
        cursor.execute(
            "INSERT INTO wrong_table VALUES (1)"
        )

        conn.commit()

except Exception as e:
    print("Transaction rolled back")
    print(e)