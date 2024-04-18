print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = name1 + name2
final_name = name.lower()

t = final_name.count("t")
r = final_name.count("r")
u = final_name.count("u")
e = final_name.count("e")

true = t + r+ u + e

l = final_name.count("l")
o = final_name.count("o")
v = final_name.count("v")
e = final_name.count("e")

love = l+o+v+e

str_love_score = str(true) + str(love)

love_score = int(str_love_score)
if love_score <= 10 or love_score >= 90:
  print(f"Your score is {love_score}, you go together like coke and mint.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")
