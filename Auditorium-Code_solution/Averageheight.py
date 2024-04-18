# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum = 0
for i in student_heights:
  sum = sum + i

print(f"total height = {sum}")
print(f"number of students = {n+1}")
print(f"average height = {round(sum/(n+1))}")
