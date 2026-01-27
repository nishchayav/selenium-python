import pytest


@pytest.fixture
def data():
    return [1,2,3,4,5]


def test_one(data):
    #data=[1,2,3,4,5]
    assert 2 in data
    print(data)

def test_two(data):
    #data=[1,2,3,4,5]
    print(len(data))
    assert len(data)==5
