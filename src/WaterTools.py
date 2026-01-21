# Holds helper functions for other modules.

def ounce2liter(ounces: float) -> float:
    """
    Converts fluid ounces to liters.

    Args:
        ounces (float): amount of ounces.
    Returns:
        float: amount of liters
    """
    return round(ounces/33.814, 2)