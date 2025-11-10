# DZ 11.3. Parity check
def is_even(number: int) -> bool:
    return (number & 1) == 0

print(is_even(2494563894038 ** 2))
print(is_even(1056897 ** 2))
print(is_even(24945638940387 ** 3))