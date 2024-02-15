from calculator.Operation import Operation
from calculator.CalculationHistory import CalculationsHistory
from calculator.Calculation import Calculation

class Calculator:
    def __init__(self):
        self.operation = Operation()

    def perform_calculation(self, a, b, operation):
        calculation = Calculation(a, b, operation)
        result = calculation.compute()
        CalculationsHistory.add_history(calculation)
        return result

    def get_calculation_history(self):
        return CalculationsHistory.get_history()
