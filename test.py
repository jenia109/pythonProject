class Engine:
    def __init__(self):
        self.sound = "wrrrrrrrrrrrrrrr"

    def start(self):
        print(self.sound)


class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()


c = Car()
c.drive()