"""
Module used to get calculation history.
"""

class CalculationsHistory:
    """
    Get Calculation history.
    """
    history = []

    @classmethod
    def add_history(cls, calculation):
        """
        Add a calculation to the history.

        Args:
            calculation: The calculation to be added.
        """
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        """
        Get the history of calculations.

        Returns:
            list: List of calculations in the history.
        """
        return cls.history
