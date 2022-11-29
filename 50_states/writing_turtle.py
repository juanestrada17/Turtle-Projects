from turtle import Turtle

class Write_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, x_position, y_position, answer_state):
        self.goto(x_position, y_position)
        self.write(f"{answer_state}", align="center", font=("Courier", 7, "normal"))