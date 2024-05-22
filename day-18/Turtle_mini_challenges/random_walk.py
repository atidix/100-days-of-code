from turtle import Turtle, Screen
import random

direction = [0, 90, 180, 270]
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.width(10)
tim.speed(10)

for i in range(random.randint(100, 200)):
    tim.setheading(random.choice(direction))
    tim.forward(20)
    tim.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

screen.exitonclick()