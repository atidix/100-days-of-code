# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / height ** 2

if BMI < 18.5:
  print (f"Your BMI is {BMI} and you are underweight")
elif BMI <25:
  print (f"Your BMI is {BMI} and you have a normal weight")
elif BMI <30:
  print (f"Your BMI is {BMI} and you are slighlty overweight")
elif BMI <35:
  print (f"Your BMI is {BMI} and you are obese")
else:
  print (f"Your BMI is {BMI} and you are clinically obese")