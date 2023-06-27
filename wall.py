
from brick import Brick


class Wall:
    def __init__(self):
        self.bricks = []
        self.colors = ["yellow", "green", "orange", "red"]
        self.create_bricks()

    def create_bricks(self):
        for section in range(4):
            color = self.colors[section]
            for row in range(2):
                for brick in range(15):
                    new_brick = Brick(brick*40 - 285, 50 + section * 40 + row * 20)
                    new_brick.color("black", color)
                    self.bricks.append(new_brick)


    def destroy(self, brick: Brick):
        self.bricks.remove(brick)
        brick.destroy()

