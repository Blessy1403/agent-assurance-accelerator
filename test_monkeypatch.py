def get_name():
    return "Original"

def test_name(monkeypatch):

    monkeypatch.setattr(
        __import__(__name__),
        "get_name",
        lambda: "Mocked"
    )

    assert get_name() == "Mocked"