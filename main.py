import random
from turtle import Screen
from screen import Line
from platforms import Platform
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.tracer(0)
screen.bgcolor("black")

choice = screen.textinput(title="Добро пожаловать!", prompt="Выберете количество игроков: 1/2 ")

line = Line()

bot_platform = Platform(x_start=-489, y_start=0, color="orange")
right_platform = Platform(x_start=480, y_start=0, color="white")


bot_scoreboard = ScoreBoard(x_coord=-150, y_coord=250, color="orange")
right_scoreboard = ScoreBoard(x_coord=150, y_coord=250, color="white")


game_check = True
ball = Ball()


screen.listen()
screen.onkeypress(bot_platform.up, "w")
screen.onkeypress(bot_platform.down, "s")
screen.onkeypress(right_platform.up, "Up")
screen.onkeypress(right_platform.down, "Down")


bot_scoreboard.update_scoreboard()
right_scoreboard.update_scoreboard()
random_int = random.randint(-80, 80)
if choice == "2":
    while game_check:
        time.sleep(ball.speed)
        line.draw_the_center_line()
        ball.move()

        screen.update()

        if ball.ycor() > 285 or ball.ycor() < -275:
            ball.bounce_y()  # отскок от нижней и верхней стенки
        elif ball.xcor() >= 460 and ball.distance(right_platform) < 65 or ball.xcor() < -464 and \
                ball.distance(bot_platform) < 65:
            ball.bounce_x()  # отскок от платформ
        elif ball.xcor() >= 490:
            bot_scoreboard.score()
            ball.reset_ball()
            screen.update()
            continue
        elif ball.xcor() <= -500:
            right_scoreboard.score()
            ball.reset_ball()
            screen.update()
            continue
        if bot_scoreboard.score_count == 10:
            bot_scoreboard.game_over(winner="Левый")
            game_check = False
        elif right_scoreboard.score_count == 10:
            right_scoreboard.game_over(winner="Правый")
            game_check = False


elif choice == "1":

    while game_check:  # Цикл для игры против ИИ
        time.sleep(ball.speed)
        line.draw_the_center_line()
        ball.move()

        screen.update()

        if ball.xcor() < -100 and ball.ycor() < 0:
            if bot_platform.ycor() - random_int > ball.ycor():
                screen.update()
                bot_platform.move_bot_down()
                screen.update()
            elif bot_platform.ycor() + random_int < ball.ycor():
                screen.update()
                bot_platform.move_bot_up()
                screen.update()
        elif ball.xcor() < -100 and ball.ycor() > 0:
            if bot_platform.ycor() - random_int > ball.ycor():
                screen.update()
                bot_platform.move_bot_down()
                screen.update()
            elif bot_platform.ycor() + random_int < ball.ycor():
                screen.update()
                bot_platform.move_bot_up()
                screen.update()

        if ball.ycor() > 285 or ball.ycor() < -275:
            ball.bounce_y()  # отскок от нижней и верхней стенки
        elif ball.xcor() >= 460 and ball.distance(right_platform) < 65 or ball.xcor() < -464 and \
                ball.distance(bot_platform) < 65:
            ball.bounce_x()  # отскок от платформ
        elif ball.xcor() >= 490:
            bot_scoreboard.score()
            ball.reset_ball()
            screen.update()
            continue
        elif ball.xcor() <= -500:
            right_scoreboard.score()
            ball.reset_ball()
            screen.update()
            continue
        if bot_scoreboard.score_count == 10:
            bot_scoreboard.game_over(winner="Левый")
            game_check = False
        elif right_scoreboard.score_count == 10:
            right_scoreboard.game_over(winner="Правый")
            game_check = False


screen.exitonclick()


