from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("deeppink3")
i = 3
for i in range (0,4):
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(50)

my_screen = Screen()
print(my_screen)
my_screen.exitonclick()