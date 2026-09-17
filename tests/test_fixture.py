import pytest

@pytest.fixture
def person_name():
    return "Blessy"

def test_person(person_name):
    assert person_name == "Blessy"