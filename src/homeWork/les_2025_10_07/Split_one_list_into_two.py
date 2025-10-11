#DZ 3.3. Split one list into two lists

original_list = [1, 2, 3, 4, 5]

if not original_list:
    result = [[], []]
elif len(original_list) % 2 == 0:
    finding_middle_list = len(original_list) // 2
    result = [original_list[:finding_middle_list], original_list[finding_middle_list:]]
else:
    finding_middle_list = len(original_list) // 2 + 1
    result = [original_list[:finding_middle_list], original_list[finding_middle_list:]]

print(f"{result}")
