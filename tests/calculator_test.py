"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_division():
    """ Testing division of two numbers"""
    calc = Calculator()
    result = calc.divide_numbers(10, 2)
    assert result == 5

def test_calculator_division():
    """ Testing division of two numbers"""
    calc = Calculator()
    result = calc.divide_numbers(0, 5)
    assert result == 5
