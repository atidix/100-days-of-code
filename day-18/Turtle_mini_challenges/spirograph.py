from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(100)


def draw_spirograph(heading):
    for i in range(0, int(360/heading)):
        tim.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        tim.circle(100)
        tim.setheading(heading + tim.heading())

draw_spirograph(15)

screen.exitonclick()