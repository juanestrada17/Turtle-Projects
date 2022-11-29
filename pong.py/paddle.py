from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, direction, direction2):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.segments = []
        self.setheading(90)
        self.goto(direction, direction2)
        self.shapesize(1, 6)

    def up(self):
        if self.ycor() != 420:
            self.forward(20)

    def down(self):
        if self.ycor() != -420:
            self.back(20)
