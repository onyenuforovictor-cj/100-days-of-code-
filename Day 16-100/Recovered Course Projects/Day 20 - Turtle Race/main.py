from turtle import Turtle , Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="which turtle "
                                              "will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
all_turtle = []
y_position = [-80,-60,-40,-20,0,20]

for turtle_index in range(0 , 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x= -230 , y= y_position[turtle_index] )
        all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You win!{winning_colour} turtle is the winner")
            else:
                print(f"You lose!{winning_colour} turtle is the winner")
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)

screen.exitonclick()