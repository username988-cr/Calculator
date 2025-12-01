import pytest
from calculator import add, subtract, multiply, divide, power, validate_operation, get_number


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 7) == 3


def test_multiply():
    assert multiply(3, 5) == 15


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)


def test_power():
    assert power(2, 4) == 16


def test_validate_operation():
    assert validate_operation("1") == "1"
    with pytest.raises(ValueError):
        validate_operation("X")


def test_get_number():
    assert get_number("5.2") == 5.2
    with pytest.raises(ValueError):
        get_number("abc")
