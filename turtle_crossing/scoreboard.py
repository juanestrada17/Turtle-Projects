from turtle import Turtle

FONT = ("Courier", 22, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.ht()
        self.goto(-220, 250)
        self.pendown()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
