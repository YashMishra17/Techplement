#1.)Question
#Define a cricle class to create a circle with radius r using the costructor.
#Define an Area() method of the class which calculates the area of circle
#Define a Perimeter() method of the class which allows you to claculate the perimeter of the circle

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimeter(self):
#         return 2 * (22/7) * self.radius    

# cl = Circle(21)
# print(cl.area())
# print(cl.perimeter())

#2.)Question
#Define a Employee Class With Attribuute role,department & salary. This class also has showDetails() method.
#Create an Engineer Class that inherits properties from employee & has Additional attributes : name and age

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self): 
#         print("role =", self.role)   
#         print("dept =", self.dept)
#         print("salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):    
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "80000")     

# # emp1 = Employee("Accountant","Finance","80000")    
# # emp1.showDetails()  
        
# engg1 = Engineer("Elon Musk", 40)
# engg1.showDetails()  

#3.) Question 
#Create a class caleed Order which stores item and its price.
#use Dunder Function__gt__() to convey that:
#order1>order2 if price of order1 > price of order2

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, odr2):
#         return self.price > odr2.price    

# odr1 = Order("chips",20)        
# odr2 = Order("tea",15)

# print(odr1 > odr2)

#////////////////////////////////////////////////////////////////////////////////
#Define a cricle class to create a circle with radius r using the costructor.
#Define an Area() method of the class which calculates the area of circle
#Define a Perimeter() method of the class which allows you to claculate the perimeter of the circle

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return(22/7) * self.radius ** 2

    def perimeter(self):
        return(2) * (22/7) * self.radius      

c1 = Circle(21)            
print(c1.area())
print(c1.perimeter())


