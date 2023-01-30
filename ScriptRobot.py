class Robot:
    name = ""
    x = 0
    y = 0
    direction = ""
    message = ""

    def __init__(self, name, x, y, direction, message):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.message = message

    def introduce_self(self):
        print("Mon nom est " + self.name)

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


robot = Robot("Leo",0, 0, "Z", "Bonjour")
robot.introduce_self()
robot.avancer()
robot.communiquer(robot.message)
print("La position de " + robot.name + " est " + str(robot.x))

