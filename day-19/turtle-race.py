from turtle import Turtle, Screen
import random

colors = ["red", "orange", "gold", "green", "royalblue", "orchid1", "purple3"]
screen = Screen()
screen.setup(500, 400)

turtles = []

for i in range(0, 7):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-230, -150+(50*i))
    turtles.append(tim)

user_bet = screen.textinput("Make a bet!", "Which turtle will win the race? Pick a color: red, orange, gold, green, royalblue, orchid1, purple3")

race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"The {win_color} turtle won! You guessed right!")
            else:
                print(f"The {win_color} turtle won! You guessed wrong! Better luck next time")
        else:
            turtle.forward(random.randint(0,10))














screen.exitonclick()