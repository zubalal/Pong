from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.right(90)
        self.pensize(width=3)
        self.resizemode("auto")
        self.pendown()
        self.speed(0)

    def draw_the_center_line(self):

        for i in range(0, 600, 11):
            if i % 2 == 0:
                self.pendown()
                self.forward(12)
            elif i % 2 != 0:
                self.penup()
                self.forward(12)
