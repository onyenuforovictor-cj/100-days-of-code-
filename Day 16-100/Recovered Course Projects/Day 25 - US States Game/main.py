import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    response = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What is another State's name?",
    )

    if response is None:
        continue

    answer_state = response.strip().title()

    if answer_state == "Exit":
        missing_state = [state for state in all_state if state not in guessed_states]
        pandas.DataFrame(missing_state).to_csv("States_to_learn.csv", index=False)
        break

    if answer_state in all_state and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
