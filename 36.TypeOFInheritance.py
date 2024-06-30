#MultiLevel Inheritance

# class Car:                                              # First Class
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..") 

# class ToyotaCar(Car) :  #we inherit all properties from class Car    #Second Class
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):                             #Third Class
#     def __init__(self,type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()  

#///////////////////////////////////////////////////////////////////////////////////////////////////

#Multiple Inheritance       
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"  

# class C(A, B):
#     varC = "welcome to class C"    

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#///////////////////////////////////////////////////////////////////
# #MultiLevel Inheritance
# class Car:                              #Class 1
#     @staticmethod
#     def start():
#         print("Car Started...")

#     @staticmethod
#     def stop():
#         print("Car Stopped...")

# class ToyotaCar(Car):                   #Class 2
#     def __init__(self,brand):
#         self.brand = brand    

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type

# car1 = Fortuner("diesel")        
# car1.start()

# ////////////////////////////////////////////////////////////////////////
#Multiple Inheritance

# class A:
#     var1 = "Welcome to the class A"

# class B:
#     var2 = "Welcome to the class B"

# class C(A,B):
#     var3 = "Welcome to the class C"

# c1 = C()    
# print(c1.var3)
# print(c1.var2)
# print(c1.var1)

        

