# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..") 

# class ToyotaCar(Car) :  #we inherit all properties from class Car
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("prius")

# print(car1.name)
# print(car2.name)

# print(car1.start())
# print(car2.stop())

#///////////////////////////////////////////////////////////////////////////////
class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")    

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")         

print(car1.name)
print(car2.name)

print(car1.start())
print(car2.stop())




