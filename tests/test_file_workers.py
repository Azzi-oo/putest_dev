from my_funcs.file_workers import read_from_file
import pytest
import os


@pytest.fixture(autouse=True)
def clear_file():
    if os.path.exists("tests/testfile.txt"):
        os.remove("tests/testfile.txt")
    yield


def create_test_data(test_data):
    with open("tests/testfile.txt", "w") as f_o:
        f_o.writelines(test_data)


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data)
    assert test_data == read_from_file("tests/testfile.txt")
    
    
def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n']
    create_test_data(test_data)
    assert test_data == read_from_file("tests/testfile.txt")
