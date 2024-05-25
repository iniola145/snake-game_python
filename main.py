from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left1, "Left")
screen.onkey(snake.right1, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Scoreboard
    scoreboard.score_card()

    # Detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.count()

    # Game over
    if snake.head.xcor() > 900 or snake.head.xcor() < -900 or snake.head.ycor() > 900 or snake.head.ycor() < -900:
        # game_is_on = False
        scoreboard.reset()
        snake.fail()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.fail()

screen.exitonclick()
