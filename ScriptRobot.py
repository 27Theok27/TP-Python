class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def avancer(self):
        if self.direction == "Z":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "D":
            self.x += 1
        elif self.direction == "Q":
            self.x -= 1

    