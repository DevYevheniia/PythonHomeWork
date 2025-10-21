#DZ 6.1. Range of letters
import string

input_user = input("enter two letters with a hyphen: ")
first, last = input_user.split("-")
letter_box = string.ascii_letters
first_letter_index = letter_box.index(first)
last_letter_index = letter_box.index(last)
if first_letter_index <= last_letter_index:
    result = letter_box[first_letter_index:last_letter_index + 1]
    print(result)
else:
    result = letter_box[first_letter_index:] + letter_box[:last_letter_index + 1]
    print(result)