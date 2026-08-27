import pytest
from pydantic import ValidationError

from week1.warmup import (
    Person,
    init_db,
    save_people,
    load_people
)


def test_round_trip(tmp_path):
    db = tmp_path / "test.db"

    init_db(db)

    people = [
        Person(name="Alice", age=25, email="alice@test.com"),
        Person(name="Bob", age=30, email="bob@test.com"),
        Person(name="Charlie", age=35, email="charlie@test.com")
    ]

    save_people(db, people)

    loaded = load_people(db)

    assert loaded == people


def test_invalid_age_rejected():
    with pytest.raises(ValidationError):
        Person(
            name="x",
            age=200,
            email=None
        )


def test_null_email_survives_round_trip(tmp_path):
    db = tmp_path / "test.db"

    init_db(db)

    people = [
        Person(
            name="Alice",
            age=20,
            email=None
        )
    ]

    save_people(db, people)

    loaded = load_people(db)

    assert loaded[0].email is None


def test_load_people_empty_table(tmp_path):
    db = tmp_path / "test.db"

    init_db(db)

    loaded = load_people(db)

    assert loaded == []