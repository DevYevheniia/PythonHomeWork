#DZ 4.3. List of 3 elements
import random

n = random.randint(3,10)
random_list = []
for i in range(n):
    number = random.randint(0,100)
    random_list.append(number)
print(random_list)
#or use syntactic sugar to make it look better