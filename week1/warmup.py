from pydantic import BaseModel, Field
import sqlite3


class Person(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    email: str | None = None


def init_db(db_path: str) -> None:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS people (
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT
        )
        """)

        conn.commit()


def save_people(db_path: str, people: list[Person]) -> int:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        for person in people:
            cursor.execute(
                """
                INSERT INTO people (name, age, email)
                VALUES (?, ?, ?)
                """,
                (person.name, person.age, person.email)
            )

        conn.commit()

    return len(people)


def load_people(db_path: str) -> list[Person]:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT name, age, email
        FROM people
        """)

        rows = cursor.fetchall()

    return [
        Person(
            name=row[0],
            age=row[1],
            email=row[2]
        )
        for row in rows
    ]