import time
from turtle import Turtle
from random import randint


class Ball(Turtle):

    # randint(150, 210)
    def __init__(self):
        super().__init__()
        self.direction = randint(150, 210)
        self.speed("slowest")
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.setheading(self.direction)

    def ball_restart(self):
        self.goto(0, 0)
        self.direction = randint(150, 210)
        time.sleep(0.5)

    def wall_bounce(self):
        if self.ycor() > 480 or self.ycor() < -480:
            new_direction = self.heading()
            self.setheading(-new_direction)

    def paddle1_bounce(self):
        if self.xcor() < -670:
            new_direction = self.heading()
            self.setheading(-new_direction + 180)
            # self.setheading(randint(-10, 50))

    def paddle2_bounce(self):
        if self.xcor() > 680:
            new_direction = self.heading()
            self.setheading(-new_direction - 180)
            # self.setheading(randint(140, 300))
