##DZ 11.1. Prime number generator

def prime_generator(end: int) -> int:
    """
    Generates prime numbers from 2 up to and including the specified number.
    Return:
    int: The next prime number in tdefhe sequence each time the generator is called.
    """

    def _is_prime(number: int) -> bool:
        """Checks if a number is prime."""
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if _is_prime(num):
            yield num


from inspect import isgenerator

gen = prime_generator(1)
print(isgenerator(gen))
print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))
