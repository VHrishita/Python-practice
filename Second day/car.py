class Car:

    def __init__(self, name, speed, model):
        self.name = name
        self.speed = speed
        self.model = model

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def getSpeed(self):
        print("Current Speed:", self.speed)



c1 = Car("BMW", 10, "X5")


c1.getSpeed()

c1.accelerate()
c1.accelerate()
c1.getSpeed()

c1.brake()
c1.brake()
c1.brake()   
c1.getSpeed()
