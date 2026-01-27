import pytest
from calculator_DAY_10 import add, subtract, multiply, divide


def setup_module(module):
    print("\n[setup_module] Module setup")

def teardown_module(module):
    print("\n[teardown_module] Module teardown")

def setup_function(function):
    print("\n[setup_function] Before test")

def teardown_function(function):
    print("\n[teardown_function] After test")




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

