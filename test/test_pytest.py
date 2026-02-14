import pytest
from src import calculator


def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(-1, -1) == -2


def test_fun2():
    assert calculator.fun2(5, 3) == 2
    assert calculator.fun2(-1, -1) == 0


def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(-1, -1) == 1


def test_fun4():
    assert calculator.fun4(1, 2, 3) == 6
    assert calculator.fun4(-1, -1, -1) == -3


def test_invalid_input():
    with pytest.raises(ValueError):
        calculator.fun1("a", 2)

    with pytest.raises(ValueError):
        calculator.fun4(1, "b", 3)
