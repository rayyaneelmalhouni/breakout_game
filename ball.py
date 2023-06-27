
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, -220)
        self.x_move = 10
        self.y_move = 10
        self.continuous_hits = 0
        self.speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bound_x(self):
        self.x_move *= -1

    def bound_y(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0, -220)
        self.continuous_hits = 0
        self.speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def hit(self, brick):
        self.continuous_hits += 1
        new_speed = 0.1
        if brick.color()[1] == "red":
            new_speed = 0.03
        elif brick.color()[1] == "orange":
            new_speed = 0.05
        elif self.continuous_hits >= 12:
            new_speed = 0.07
        elif self.continuous_hits >= 4:
            new_speed = 0.09

        if new_speed < self.speed:
            self.speed = new_speed
