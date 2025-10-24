#DZ 7.4. Finding common elements
def common_elements():
    numbers_of_3 = [x for x in range(100) if x % 3 == 0]
    numbers_of_5 = [x for x in range(100) if x % 5 == 0]

    set_3 = set(numbers_of_3)
    set_5 = set(numbers_of_5)
    print(set_3)
    print(set_5)
    return sorted(set_3.intersection(set_5))

print(common_elements())