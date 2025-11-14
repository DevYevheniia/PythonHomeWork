#DZ 11.2. Filling a list with cubes of numbers
def generate_cube_numbers(end: int):
    """
    Generates cubes of numbers, starting from 2,
    until the cube exceeds the specified value.
    Return:
    int: The cube of the number each time the generator is called.
    """
    n = 2
    while True:
        cube = n ** 3
        if cube > end:
            return
        yield cube
        n += 1

from inspect import isgenerator
gen = generate_cube_numbers(1)
print(isgenerator(gen))
print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(1000)))