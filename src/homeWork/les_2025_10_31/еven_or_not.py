#DZ 10.3. Check if it is even or not
def is_even(digit: int) -> bool:
    """
    The function checks if a number is even.
    Return:
    bool : True if the number is even, False if odd
    """
    return digit % 2 == 0

print(is_even(2))
print(is_even(5))
print(is_even(0))