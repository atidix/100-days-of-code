# import colorgram

# a = colorgram.extract('/home/atidix/100-days-of-code/day-18/Turtle_mini_challenges/hirst_painting/hirst.jpg', 30)

# rgb_colors = []
# for color in a:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

# print(rgb_colors)

color_list = [(250, 228, 16), (236, 251, 244), (212, 13, 9), (199, 12, 36), (230, 228, 6), (196, 70, 20), (32, 90, 188), (235, 148, 38), (43, 212, 70), (33, 30, 152), (16, 22, 54), (67, 9, 48), (244, 39, 150), (14, 206, 223), (238, 244, 249), (66, 202, 229), (62, 21, 10), (225, 19, 111), (15, 155, 21), (228, 166, 9), (248, 11, 9), (245, 58, 16), (98, 75, 9), (223, 140, 203), (68, 240, 160), (10, 97, 62), (6, 39, 33), (68, 219, 157)]

from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(100)

tim.penup()
tim.goto(-250, -250)

def line():
    for i in range(1,11):
        tim.color(random.choice(color_list))
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.penup()
        tim.forward(50)
for i in range(1, 11):
    tim.pendown()
    line()
    tim.goto(-250,-250)
    tim.setheading(90)
    tim.penup()
    tim.forward(50 * i)
    tim.pendown()
    tim.setheading(0)

screen.exitonclick()