from src.calculator import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(40, 2) == 42


def test_add_negative():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 5) == 5


def test_subtract():
    assert subtract(10, 3) == 7


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)