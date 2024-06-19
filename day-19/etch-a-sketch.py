from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def fd():
    tim.forward(10)

def bk():
    tim.backward(10)

def ac():
    tim.setheading(tim.heading() + 10)

def cc():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(fun=fd, key="w")
screen.onkey(fun=bk, key="s")
screen.onkey(fun=ac, key="a")
screen.onkey(fun=cc, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
