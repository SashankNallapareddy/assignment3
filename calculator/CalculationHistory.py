class CalculationsHistory:
    history = []
    
    @classmethod
    def add_history(cls, calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        return cls.history