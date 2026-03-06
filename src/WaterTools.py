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

def liter2ounce(liters: float) -> float:
    """
    Converts liters to fluid ounces.

    Args:
        liters (float): amount of liters.
    Returns:
        float: amount of ounces
    """
    return round(liters*33.814, 2)

def kg2lbs(kg: float) -> float:
    """
    Converts kilograms to pounds.

    Args:
        kg (float): amount of ounces.
    Returns:
        float: amount of pounds
    """
    return round(kg*2.20462, 2)