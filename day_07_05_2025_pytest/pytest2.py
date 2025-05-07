import pytest
import time


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


def test_add():

    # Arrange
    calc = Calculator()
    a = 5
    b = 3

    # Act
    result = calc.add(a, b)

    # Assert
    assert result == 8


def test_divide():
    # Arrange
    calc = Calculator()
    a = 6
    b = 3

    # Act
    result = calc.divide(a, b)

    # Assert
    assert result == 2


def test_divide_by_zero():
    # Arrange
    calc = Calculator()
    a = 6
    b = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        calc.divide(a, b)

@pytest.mark.slow   # Mark this test as slow
def test_very_slow():
    time.sleep(5)
    calc = Calculator()
    result = calc.add(5, 10)
    assert result == 15


@pytest.mark.skip(reason="Skipping this test for demonstration purposes")
def test_skipped():
    calc = Calculator()
    result = calc.add(5, 10)
    assert result == 15

@pytest.mark.xfail(reason="This test is expected to fail")
def test_expected_failure():
    calc = Calculator()
    result = calc.divide(5, 0)
    # assert result == 20