target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

i = 0
for total in range(0, target + 1, 2):
  i = total + i

print(i)
