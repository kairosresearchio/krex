import math


def get_decimal_places(value):
    """Returns the number of decimal places for a given value."""
    if value > 0:
        return int(-math.log10(value))
    return 0  # Avoid errors when value is 0


def reverse_decimal_places(decimal_places):
    """Converts a decimal place count back to its corresponding value."""
    return 10**-decimal_places


# Testing the functions
# print(get_decimal_places(0.01))  # 2
# print(get_decimal_places(0.001))  # 3
# print(get_decimal_places(1))  # -1
# print(get_decimal_places(10))  # -2

# print(reverse_decimal_places(2))  # 0.01
# print(reverse_decimal_places(3))  # 0.001
# print(reverse_decimal_places(-1))  # 1
# print(reverse_decimal_places(-2))  # 10
