from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x_coord, y_coord, color):
        super().__init__()
        self.speed(0)
        self.score_count = 0
        self.penup()
        self.hideturtle()
        self.goto(x_coord, y_coord)
        self.color(color)

    def update_scoreboard(self):
        self.write(arg=f'{self.score_count}', align="center", font=("Impact", 30, "normal"))

    def score(self):
        self.score_count += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"{winner} игрок победил", False, align="center", font=("Impact", 40, "normal"))
