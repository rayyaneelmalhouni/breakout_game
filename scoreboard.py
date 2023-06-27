
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(200, 220)
        self.display_score()

    def update_score(self, color):
        if color == "yellow":
            self.score += 1
        elif color == "green":
            self.score += 3
        elif color == "orange":
            self.score += 5
        elif color == "red":
            self.score += 7
        else:
            print(color)

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, -100)
        self.write(f"Game Over", align="center", font=("Courier", 36, "normal"))
        self.goto(0, -125)
        self.write(f"Final Score: {self.score}", align="center", font=("Courier", 24, "normal"))

