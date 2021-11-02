"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_division():
    """ Testing division of two numbers"""
    calc = Calculator()
    result = calc.divide_numbers(5, 0)
    assert result == 5
