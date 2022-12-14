from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")
with open("data.txt") as file:
    h_score = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(h_score)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def scores(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
