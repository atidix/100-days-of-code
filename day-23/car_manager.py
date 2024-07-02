from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self): 
        random_car = random.randint(0,6)
        if random_car == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250,250))
            new_car.setheading(180)
            self.car_list.append(new_car)
    
    def move(self):
        for car in self.car_list:
            car.fd(self.car_speed)
    
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

