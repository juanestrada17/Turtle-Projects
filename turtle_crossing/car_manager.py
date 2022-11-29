from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.shapesize(1, 2)
        self.setheading(180)
        self.penup()
        self.goto(randint(0, 1000), randint(-240, 280))

    def car_move(self, move):
        self.forward(move)

    def clears(self):
        self.clear()
        self.shape("square")
        self.color(choice(COLORS))
        self.shapesize(1, 2)
        self.setheading(180)
        self.penup()
        self.goto(randint(0, 1000), randint(-240, 280))
