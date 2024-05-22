from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.color("black")
tim.shape("turtle")

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen.exitonclick()
















