from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forwards():
    tim.fd(50)
def turnr():
    tim.right(10)
def turnl():
    tim.left(10)
def back():
    tim.fd(-50)
def clearscreen():
    screen.reset()


screen.onkey(forwards, "w")
screen.onkey(turnr, "a")
screen.onkey(turnl, "d")
screen.onkey(back, "s")
screen.onkey(clearscreen, "c")
screen.listen()

screen.exitonclick()
