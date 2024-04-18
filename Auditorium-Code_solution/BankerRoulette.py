names_string = input()
names = names_string.split(", ")
# names_string contains the input values provided. 
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random

length = len(names) - 1

pay = random.randint(0, length)

print(f"{names[pay]} is going to buy the meal today!")