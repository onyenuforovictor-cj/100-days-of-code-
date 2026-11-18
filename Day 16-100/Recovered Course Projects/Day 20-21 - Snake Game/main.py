from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

WALL_LIMIT = 280


def game_loop():
    snake.move()

    head_x = snake.head.xcor()
    head_y = snake.head.ycor()
    hit_wall = abs(head_x) >= WALL_LIMIT or abs(head_y) >= WALL_LIMIT

    if hit_wall:
        scoreboard.reset()
        scoreboard.goto(0, 0)
        scoreboard.write(
            "GAME OVER",
            align="center",
            font=("Arial", 24, "normal"),
        )
        screen.update()
        return

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            break

    screen.update()
    screen.ontimer(game_loop, 100)


game_loop()
screen.exitonclick()
