from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.Up, "Up")
screen.onkey(r_paddle.Down, "Down")
screen.onkey(l_paddle.Up, "w")
screen.onkey(l_paddle.Down, "s")

game_is_on = True

while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()
        
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.x_bounce()

        elif ball.xcor() > 380:
            ball.reset()
            scoreboard.l_point()       

        elif ball.xcor() < -380:
            ball.reset()
            scoreboard.r_point()

             
             

screen.exitonclick()
