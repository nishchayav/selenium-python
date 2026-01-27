import pytest
from calculator_DAY_9 import add, subtract, multiply, divide

def test_addition():
    assert add(2, 3) == 5
    print(add(2, 3))

def test_subtraction():
    assert subtract(5, 3) == 2
    print(subtract(5, 3))

def test_multiplication():
    assert multiply(4, 3) == 12
    print(multiply(4, 3))

def test_division():
    assert divide(10, 2) == 5
    print(divide(10, 2))


def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

