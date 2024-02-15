from calculator.Operation import Operation

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def compute(self):
        if self.operation == Operation.add:
            return Operation.add(self.a, self.b)
        elif self.operation == Operation.subtract:
            return Operation.subtract(self.a, self.b)
        elif self.operation == Operation.multiply:
            return Operation.multiply(self.a, self.b)
        elif self.operation == Operation.divide:
            return Operation.divide(self.a, self.b)
        else:
            raise ValueError("Invalid operation")