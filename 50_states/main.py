from turtle import Turtle, Screen
import pandas
from writing_turtle import Write_turtle

data = pandas.read_csv("50_states.csv")
state_list = (data["state"].to_list())

# Creates the map and the input for the map

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)

turtle.shape(image)

# state count
total_states = 0

# write
write = Write_turtle()

game_is_on = True

while game_is_on:
    screen.update()
    answer_state = screen.textinput(title=f"Guess the state {total_states}/50 ",
                                    prompt="What's another states name?")
    if answer_state is None:
        game_is_on = False
    elif answer_state.title() in state_list:
        state_list.remove(answer_state.title())
        total_states += 1
        x_position = int(data.x[data.state == answer_state.title()])
        y_position = int(data.y[data.state == answer_state.title()])
        write.write_state(x_position, y_position, answer_state.title())
        if len(state_list) == 0:
            print("You've done it")
            game_is_on = False


screen.exitonclick()


# THIS is how to find the position of the turtle with the x and y coordinate using turtle
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# WITH .item() you can retrieve the first item