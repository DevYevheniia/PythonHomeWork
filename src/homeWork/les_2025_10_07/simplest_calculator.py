from decimal import Decimal, getcontext, ROUND_HALF_UP

#MoneyGrow 🌱 #DZ 3.1. The simplest calculator
#The project showcases best practices for financial accuracy in Python applications.
#A Python-based financial calculator for deposits and compound interest using exact decimal precision.

getcontext().prec = 10

initial_amount = Decimal(input("Еnter the deposit amount (your initial amount) : "))
annual_rate = Decimal(input("Еnter annual rate % (e.g. 5) : ")) / Decimal('100')
number_of_accruals_per_year = Decimal(input("Еnter number of accruals per year : "))
years = Decimal(input("Еnter number of years : "))
income_tax = Decimal(input("Enter income tax % (e.g. 19.5): ")) / Decimal('100')

final_amount = initial_amount * (Decimal('1') + annual_rate / number_of_accruals_per_year) ** (number_of_accruals_per_year * years)

profit_before_tax = final_amount - initial_amount
profit_after_tax = profit_before_tax * (Decimal('1') - income_tax)

final_amount = final_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
profit_before_tax = profit_before_tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
profit_after_tax = profit_after_tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print()
print(" Deposit Calculation Result: ")
print(f" Final amount: {final_amount}")
print(f" Profit before tax: {profit_before_tax}")
print(f" Profit after tax: {profit_after_tax}")
