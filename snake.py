from turtle import Turtle

# Snake config
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake1 = []
        self.create_snake()

    def create_snake(self):
        for position in COORDINATES:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake1.append(new_snake)

    def extend(self):
        self.add_snake(self.snake1[-1].position())

    def move(self):

        for snake_numb in range(len(self.snake1) - 1, 0, -1):
            new_x = self.snake1[snake_numb - 1].xcor()
            new_y = self.snake1[snake_numb - 1].ycor()
            self.snake1[snake_numb].goto(new_x, new_y)
        self.snake1[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake1[0].heading() != 270:
            self.snake1[0].setheading(0)
            new_heading = self.snake1[0].heading() + 90
            self.snake1[0].setheading(new_heading)

    def left(self):
        if self.snake1[0].heading() != 0:
            self.snake1[0].setheading(0)
            new_heading = self.snake1[0].heading() + 180
            self.snake1[0].setheading(new_heading)

    def down(self):
        if self.snake1[0].heading() != 90:
            self.snake1[0].setheading(0)
            new_heading = self.snake1[0].heading() + 270
            self.snake1[0].setheading(new_heading)

    def right(self):
        if self.snake1[0].heading() != 180:
            self.snake1[0].setheading(0)
            new_heading = self.snake1[0].heading() + 0
            self.snake1[0].setheading(new_heading)


