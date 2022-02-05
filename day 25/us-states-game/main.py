import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# print(answer_state)


data = pandas.read_csv("50_states.csv")
# print(data)
all_states = data["state"].to_list()
guessed_states = []
correct_answers = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)
        correct_answers += 1


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
