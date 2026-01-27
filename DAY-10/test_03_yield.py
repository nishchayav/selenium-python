import pytest

@pytest.fixture()
def setup_teardown():
    print("SETUP")
    yield
    print("TEARDOWN")


def test_ex(setup_teardown):
    print("test1 running")


def test_two(setup_teardown):
    print("test2 running")