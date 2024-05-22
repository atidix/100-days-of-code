from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.color("black")
tim.shape("turtle")

for i in range(4):
    tim.forward(100)
    tim.right(90)
    
screen.exitonclick()