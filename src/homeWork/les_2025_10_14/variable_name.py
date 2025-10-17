#DZ 5.1. Variable name
import keyword
import string

user_input = input("Enter the string: ")
if(
    user_input.isidentifier()
    and not keyword.iskeyword(user_input)
    and user_input.islower()
    and not any(ch in string.punctuation.replace("_", "") for ch in user_input)
    and "__" not in user_input
):
    print(True)
else:
    print(False)