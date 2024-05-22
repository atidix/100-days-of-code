from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

for i in range(3, 11):
    tim.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    for x in range(i):
        tim.forward(100)
        tim.right(360/i)
   



screen.exitonclick()