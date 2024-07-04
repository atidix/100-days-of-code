from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")
SCORE_POSITION = (0,270)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("./day-20 & 21/data.txt") as read:
            self.high_score = int(read.read())
        self.penup()
        self.goto(SCORE_POSITION)
        self.hideturtle()
        self.write_score()
    
    def write_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open ("./day-20 & 21/data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()