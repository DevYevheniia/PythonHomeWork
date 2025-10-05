#HW 2.1. Displaying a number in a column
number_entered_4_digit = int(input("Enter a four-digit number: "))

digit1, remainder_number_entered = divmod(number_entered_4_digit,1000)
digit2, remainder_after_1000 = divmod(remainder_number_entered,100)
digit3, digit4 = divmod(remainder_after_1000,10)
print(digit1)
print(digit2)
print(digit3)
print(digit4)