from calculator.Operation import Operation
from calculator.Calculator import Calculator


calculator1 = Calculator()

print(calculator1.perform_calculation(10, 5, Operation.add))
print(calculator1.perform_calculation(10, 5, Operation.subtract))
print(calculator1.perform_calculation(10, 5, Operation.divide))
print(calculator1.get_calculation_history()) 