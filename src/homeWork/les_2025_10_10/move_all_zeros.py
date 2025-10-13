#DZ 4.1. Move all zeros to the end of the list

original_list = [0, 1, 0, 12, 3]
original_list2 = [0, 1, 0, 12, 3]

for i in range(len(original_list) - 1, -1, -1):
    if original_list[i] == 0:
        original_list.pop(i)
        original_list.append(0)
print(original_list)

# or

original_list2.sort(key=lambda x: x == 0)
print(original_list2)

