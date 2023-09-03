from turtle import Turtle
import random
Y_MAX = 287
Y_MIN = -281
SPEED = 0.06
SPEED_MULTIPLIER = 0.65
MOVE = 5
'''''
Y_MAX = 287
Y_MIN = -281
SPEED = 0.06
SPEED_MULTIPLIER = 0.65
MOVE = 5
'''''

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.x_move = MOVE
        self.y_move = MOVE
        self.speed = SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.boost()

    def reset_ball(self):
        self.goto(0, random.randint(-250, 250))
        self.bounce_x()
        self.speed = SPEED

    def boost(self):
        self.speed *= SPEED_MULTIPLIER
        return self.speed
