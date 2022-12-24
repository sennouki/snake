from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen config

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("SNAKE - THE GAME")

# Snake config
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
game_is_on = True
sb = Scoreboard()

food = Food()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.snake1[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        sb.score()
    # Detect collision with wall
    if snake.snake1[0].xcor() > 280 or snake.snake1[0].xcor() < -280:
        game_is_on = False
        sb.game_over()
    if snake.snake1[0].ycor() > 280 or snake.snake1[0].ycor() < -280:
        game_is_on = False
        sb.game_over()
    # Detect collision with tail
    for segments in snake.snake1[1:]:
        if snake.snake1[0].distance(segments) < 10:
            game_is_on = False
            sb.game_over()

screen.exitonclick()
