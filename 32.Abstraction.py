class Car:
    def __init__(self):
        self.clutch = False
        self.acc = False
        self.brk = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()            