#DZ 3.2. Move an item in a list

list_items = [12, 3, 4, 10]
get_last = list_items.pop(-1)
list_items.insert(0,get_last)
print(list_items)