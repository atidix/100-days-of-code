import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
scoreboard = Scoreboard()
all_cars = CarManager()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:  
    time.sleep(0.1)
    screen.update()

    all_cars.create_car()
    all_cars.move()

    for car in all_cars.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.ycor() > 280:
        player.reset()
        scoreboard.update_score()
        all_cars.increase_speed()

    


    


screen.exitonclick()

