import turtle
import pandas

screen = turtle.Screen()
screen.title("us states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer_turtle = turtle.Turtle()
writer_turtle.hideturtle()

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
all_data = pandas.read_csv("50_states.csv")
print(all_data)

states_list = all_data["state"].to_list()
correct_guesses = []
states_to_learn = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 correct", prompt="Guess a State name: ").title()
    if answer_state == "Exit":
        break
    if answer_state in correct_guesses:
        pass
    elif answer_state in states_list:
        x_cor = all_data[all_data["state"] == answer_state]["x"]
        y_cor = all_data[all_data["state"] == answer_state]["y"]
        writer_turtle.penup()
        writer_turtle.goto(int(x_cor), int(y_cor))
        writer_turtle.write(answer_state, font=("arial", 10, "bold"))
        correct_guesses.append(answer_state)

# generating states to learn
for state in states_list:
    if state in correct_guesses:
        pass
    else:
        states_to_learn.append(state)
data = pandas.DataFrame(states_to_learn)
data.to_csv("states_to_learn.csv")
turtle.mainloop()