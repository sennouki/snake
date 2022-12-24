from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scoring = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setx(0)
        self.sety(270)
        self.write(f"Score: {self.scoring}", align="center", font=("Arial", 15, "normal"))

    def score(self):
        self.clear()
        self.scoring += 1
        self.write(f"Score: {self.scoring}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=("Arial", 15, "normal"))



