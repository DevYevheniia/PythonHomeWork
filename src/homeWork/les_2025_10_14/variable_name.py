#DZ 5.1. Variable name
import keyword

user_input = input("Enter the string: ")
if(
    user_input.isidentifier()
    and not keyword.iskeyword(user_input)
    and user_input.islower()
    and user_input.count('_') <= 1
):
    print(True)
else:
    print(False)