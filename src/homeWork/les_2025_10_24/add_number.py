#DZ 8.1. Add 1 to a number

def add_one(some_list):
    gluing_numbers = ""
    for i in some_list:
        gluing_numbers += str(i)
    str_to_num = str(int(gluing_numbers) + 1)
    result = []
    for ch in str_to_num:
        result.append(int(ch))
    return result

print(add_one([9, 9, 9]))

