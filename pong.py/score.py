from turtle import Turtle


class Score(Turtle):
    def __init__(self, direction1, direction2):
        super().__init__()
        self.scoring = 0
        self.color("white")
        self.penup()
        self.goto(direction1, direction2)
        self.ht()

        self.score()

    def score(self):
        self.write(f"{self.scoring}", align="center", font=("Courier", 60, "normal"))

    def upd_score(self):
        self.scoring += 1
        self.clear()
        self.score()
