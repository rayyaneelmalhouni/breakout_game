
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0, -240)
        self.color("white")
        self.x_move = 40

    def move_right(self):
        if self.xcor() <= 220:
            self.goto(self.xcor() + self.x_move, -240)

    def move_left(self):
        if -220 <= self.xcor():
            self.goto(self.xcor() - self.x_move, -240)

    def reset(self):
        self.goto(0, -240)


