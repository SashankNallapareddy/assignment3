"""
Module docstring: A brief description of the calculator script.
"""

from calculator.operation import Operation
from calculator.calculator import Calculator

calculator1 = Calculator()

print(calculator1.perform_calculation(10, 5, Operation.add))
print(calculator1.perform_calculation(10, 5, Operation.subtract))
print(calculator1.perform_calculation(10, 5, Operation.divide))
print(calculator1.get_calculation_history())
