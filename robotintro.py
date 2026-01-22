class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print(f"Hello, I am {self.name}. I am a {self.model} model.")

my_robot = Robot("RoboOne", "v2.5")
my_robot.introduce()