import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen settings
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake creation and key controls
snakes = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snakes.up, "Up")
screen.onkeypress(snakes.down, "Down")
screen.onkeypress(snakes.left, "Left")
screen.onkeypress(snakes.right, "Right")

# Snake infinite movement

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakes.snake_move()
    # Detect collision with food
    if snakes.head.distance(food) < 15:
        scoreboard.scores()
        snakes.extend()
        food.refresh()

    # Detect collision with wall.
    if snakes.head.xcor() > 290 or snakes.head.xcor() < - 290 or snakes.head.ycor() < -290 or snakes.head.ycor() > 290:
        scoreboard.reset()
        snakes.reset()

    # Detect collision with tail.
    for segment in snakes.segments[1:]:
        if snakes.head.distance(segment) < 10:
            scoreboard.reset()
            snakes.reset()



screen.exitonclick()
