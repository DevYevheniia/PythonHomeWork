#DZ 4.2. Find the sum of elements with even indices

original_list = [0, 1, 7, 2, 4, 8]
if not original_list:
    print("Empty list")
else:
    even_index_elements = original_list[::2]
    final_sum = sum(even_index_elements) * original_list[-1]
    print(final_sum)