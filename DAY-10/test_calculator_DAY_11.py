import pytest
from calculator_DAY_9 import add, divide

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (-1, 1, 0)
    ]
)
def test_addition_parametrized(a, b, expected):
    assert add(a, b) == expected
