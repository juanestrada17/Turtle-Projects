from turtle import Turtle, Screen
from paddle import Paddle
from score import Score
from ball import Ball

import time

turtle = Turtle()
screen = Screen()

turtle.speed("fastest")
turtle.color("white")

turtle.penup()
turtle.goto(0, -480)
turtle.setheading(90)

screen.setup(1500, 1000)
screen.bgcolor("Black")
screen.tracer(0)
turtle.pensize(4)

# Division creation

for x in range(25):
    turtle.forward(20)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()

# Score creation in the map
score = Score(-50, 400)
score2 = Score(50, 400)

# Create the two paddles
paddle1 = Paddle(-710, 0)
paddle2 = Paddle(710, 0)

# moving the paddles
screen.listen()
screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")

# ball


game_is_on = True
ball = Ball()

while game_is_on:
    ball.forward(20)
    screen.update()
    time.sleep(0.04)
    if ball.distance(paddle1) < 60:
        ball.paddle1_bounce()
    elif ball.distance(paddle2) < 60:
        ball.paddle2_bounce()
    else:
        ball.wall_bounce()

    if ball.xcor() < -755:
        ball.ball_restart()
        score2.upd_score()
    elif ball.xcor() > 755:
        ball.ball_restart()
        score.upd_score()

screen.exitonclick()
