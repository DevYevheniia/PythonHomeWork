#DZ 10.1. Generating function

def pow(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func) -> int:
    """
    begin: first element
    end: number of elements
    func: function that generates values
    """
    current = begin
    i = 0
    while i < end:
        yield current
        current = func(current)
        i += 1


gen = some_gen(2, 4, pow)

for num in gen:
    print(num)
