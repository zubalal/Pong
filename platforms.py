from turtle import Turtle
import random

MOVE_STEP = 10
BOT_MOVE_STEP = 20


class Platform(Turtle):
    def __init__(self, x_start, y_start, color):  # x_start и y_start нужны для ввода данных в классе, в main (Platform(350, 0))
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.goto(x_start, y_start)
        self.bot_move = 5
        self.random_int = random.randint(30, 80)

    def up(self):
        y_coord = self.ycor()
        self.goto(self.xcor(), y_coord + MOVE_STEP)

    def down(self):
        y_coord = self.ycor()
        self.goto(self.xcor(), y_coord - MOVE_STEP)

    def move_bot_up(self):
        y_coord = self.ycor()
        self.goto(self.xcor(), y_coord + self.bot_move)

    def move_bot_down(self):
        y_coord = self.ycor()
        self.goto(self.xcor(), y_coord - self.bot_move)

    def increase_bot_speed(self):
        self.bot_move += 3











