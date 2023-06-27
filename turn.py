
from turtle import Turtle


class Turn(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.turn = 1
        self.goto(0, 220)
        self.display_turn()

    def update_turn(self):
        self.turn += 1

    def display_turn(self):
        self.clear()
        self.write(f"Turn: {self.turn}", align="center", font=("Courier", 24, "normal"))


