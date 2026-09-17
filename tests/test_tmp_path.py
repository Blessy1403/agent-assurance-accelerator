def test_temp_file(tmp_path):

    file = tmp_path / "hello.txt"

    file.write_text("Hello AAA")

    assert file.read_text() == "Hello AAA"
