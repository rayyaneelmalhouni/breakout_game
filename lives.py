
from turtle import Turtle


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.goto(-200, 220)
        self.display_lives()

    def update_lives(self):
        self.lives -= 1

    def display_lives(self):
        self.clear()
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 24, "normal"))


