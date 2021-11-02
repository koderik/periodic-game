import file_reader as fr  # The code to test


def test_create():
    fr.read_file("avikt.txt")


def test_verify():
    dict = fr.read_file("avikt.txt")
    assert dict["Ac"] == "227.0"
