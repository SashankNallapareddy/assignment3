
from calculator.Operation import Operation

def test_addition():
    assert Operation.add(2,2) == 4

def test_subtraction():
    assert Operation.subtract(2,2) == 0

def test_division():
    try:
        Operation.divide(2, 0)
    except ZeroDivisionError as e:
        assert str(e) == "division by zero"

def test_multiply():
    assert Operation.multiply(2,2) == 4
    