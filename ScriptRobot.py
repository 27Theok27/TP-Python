class Robot:
    def __init__(self, name, color, weight, x, y, direction, message):
        self.name = name
        self.color = color
        self.weight = weight
        self.x = x
        self.y = y
        self.direction = direction
        self.message = message

    def introduce_self(self):
        print("My name is " + self.name)

    def avancer(self):
        if self.direction == "Z":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "D":
            self.x += 1
        elif self.direction == "Q":
            self.x -= 1

    def communiquer(self, message):
        print(self.name + " dit : " + message)