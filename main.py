import turtle
import pandas

screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        data_missing_states = pandas.DataFrame(missing_states)
        data_missing_states.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row_data = data[data.state == answer_state]
        t.goto(state_row_data.x.item(), state_row_data.y.item())
        t.write(answer_state)



screen.exitonclick()




