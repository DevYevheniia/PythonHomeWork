#DZ 6.3. Product of numbers
user_numbers = int(input("Enter a number: "))
save_first_number = user_numbers

while user_numbers >= 10 :
    product = 1
    for digit in str(user_numbers):
        product *= int(digit)
    user_numbers = product
print(f"{save_first_number} -> {user_numbers}")


