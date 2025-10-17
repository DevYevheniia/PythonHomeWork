#DZ 5.2. Modify the calculator
from decimal import Decimal, getcontext
getcontext().prec = 10

while True:
    try:
        num1_str = input("Enter the first number: ")
        num1 = Decimal(num1_str)

        operator = input("Enter action (+, -, *, /): ")

        num2_str = input("Enter second number: ")
        num2 = Decimal(num2_str)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: division by zero")
                continue
            result = num1 / num2
        else:
            print("Invalid action")
            continue
        print(f"Result : {result}")

    except Exception as e:
        print("An error occurred : ", e)
        continue

    cont = input("Do you want to continue? (y/yes to continue): ").lower()
    if cont not in ('y','у','yes'):
        print("Thanks for using the calculator! 👋")
        break