
from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color("white")
        self.goto(x, y)

    def destroy(self):
        self.goto(1000, 1000)


