#DZ 8.3. Unique number

def find_unique_value(some_list):
    for i in some_list:
        if some_list.count(i) == 1:
            return i

print(find_unique_value([2, 3, 3, 3, 5, 5]))