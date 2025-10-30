# DZ 9.2. Difference between numbers
def difference(*args: float) -> float:
    """
    The function calculates the difference between the maximum and minimum values
    among the arguments.
    return: The difference between the maximum and minimum. If there are no arguments, 0.
    """
    if not args:
        return 0
    return round(max(args) - min(args), 2)


print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())
