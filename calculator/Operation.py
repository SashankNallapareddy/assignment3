class Operation:  
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError as e:
            print(f"Error: Division by zer0 : {e}")
            raise 