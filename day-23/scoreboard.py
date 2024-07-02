from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
LEVEL_POSITION = (-220,260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(LEVEL_POSITION)
        self.level = 1
        self.write_level()
    
    def write_level(self):
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=(FONT))

    def update_score(self):
        self.clear()
        self.level += 1
        self.write_level()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
        
        