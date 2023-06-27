
from turtle import Screen
import time
from ball import Ball
from lives import Lives
from paddle import Paddle
from scoreboard import ScoreBoard
from turn import Turn
from wall import Wall

screen = Screen()
screen.setup(width=610, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()
paddle = Paddle()
wall = Wall()
scoreboard = ScoreBoard()
lives = Lives()
turn = Turn()

screen.listen()
screen.onkey(fun=paddle.move_right, key="Right")
screen.onkey(fun=paddle.move_left, key="Left")


game_is_on = True
while lives.lives > 0:
    if not wall.bricks:
        paddle.reset()
        ball.reset()
        wall.create_bricks()
        turn.update_turn()
        turn.display_turn()
    time.sleep(ball.speed)
    ball.move()
    screen.update()
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bound_x()
    if ball.ycor() > 280:
        ball.bound_y()
    for brick in wall.bricks:

        if ball.distance(brick) < 50:
            ball.hit(brick)
            scoreboard.update_score(brick.color()[1])
            scoreboard.display_score()
            if brick.ycor() - 20 <= ball.ycor() <= brick.ycor() + 20:
                ball.bound_x()
            else:
                ball.bound_y()
            wall.destroy(brick)
    if paddle.distance(ball) < 55 and -235 < ball.ycor() < -220:
        ball.bound_y()
    elif ball.ycor() < -280:
        lives.update_lives()
        lives.display_lives()
        if lives.lives > 0:
            ball.reset()
        else:
            scoreboard.game_over()

screen.exitonclick()

