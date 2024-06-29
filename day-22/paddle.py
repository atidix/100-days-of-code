from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
        

    def Up(self):
        if self.ycor() < 243:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def Down(self):
        if self.ycor() > -243:
            new_y = self.ycor() - 20 
            self.goto(self.xcor(), new_y)
    
    
    