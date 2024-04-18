# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 != 0:
  print ("Not leap year")
elif year % 100 != 0:
  print ("Leap year")
elif year % 400 == 0:
  print ("leap year")
else:
  print ("Not leap year")
