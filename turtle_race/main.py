import turtle
from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

ydir = -120

for t_index in range(6):
    turtles = Turtle(shape="turtle")
    turtles.color(colors[t_index])
    turtles.penup()
    turtles.goto(-230, ydir)
    all_turtles.append(turtles)
    ydir += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        turtle.forward(randint(0, 10))








screen.exitonclick()


