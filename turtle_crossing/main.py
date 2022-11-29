import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from random import randint
from scoreboard import Scoreboard

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player
player = Player()

# Create cars
all_cars = []
for _ in range(25):
    all_cars.append(CarManager())

# Movement command
screen.listen()
screen.onkeypress(player.up, "Up")
# Scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        scoreboard.next_level()
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        for reset_cars in all_cars:
            reset_cars.clears()
    for each_car in all_cars:
        each_car.car_move(STARTING_MOVE_DISTANCE)
        player.reset_position()
        if each_car.xcor() < -300:
            each_car.goto(randint(300, 1000), randint(-240, 280))

        if player.distance(each_car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()



