""" This is the increment function"""


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(value_a, value_b):
        """ adds two numbers"""
        return value_a + value_b

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract two numbers """
        return value_a - value_b

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers """
        return value_a * value_b

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide two numbers """
        try:
            return value_a / value_b
        except ZeroDivisionError as myer:
            raise ZeroDivisionError from myer
