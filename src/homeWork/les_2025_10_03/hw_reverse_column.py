#HW 2.2. it is necessary to "flip" a 5-digit number
number_entered_5_digit = int(input("Enter a five-digit number: "))

digit1, remainder_number_entered = divmod(number_entered_5_digit,10000)
digit2, remainder_number_10000 = divmod(remainder_number_entered,1000)
digit3, remainder_number_entered_1000 = divmod(remainder_number_10000,100)
digit4, digit5 = divmod(remainder_number_entered_1000,10)
#😂
print("Flip number : ", digit5,digit4,digit3,digit2,digit1, sep="")

#or so, if we need to work with a number
reversed_number_entered = digit5 * 10000 + digit4 * 1000 + digit3 * 100 + digit2 * 10 +digit1
print("Revers integer number : ", reversed_number_entered )