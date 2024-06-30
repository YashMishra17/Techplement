#Class And Objects
# class Student:             #Class name
#     name = "Yash Mishra"    #Blueprint Of Class

# s1 = Student()  #Object Variable(s1)
# print(s1.name)

# s2 = Student()  #Object Variable(s2)
# print(s2.name)

#////////////////////////////////////////////////

# class Car:
#     color = "Blue"
#     brand = "Mercedes"

# car1 = Car()
# print(car1.color)    
# print(car1.brand)

#///////////////////////////////////////////////

#__init__ FUNCTION
# #class Defined
# class Student:           
#     name = "Yash Mishra"
# #Function Defined    
#     def __init__(self):                                     #Both self and s1 will Store At Same Location
#         print(self)
#         print("adding new student in DataBase..")
# #Object Defined
# s1 = Student() 
# print(s1)       


#class Defined
# class Student:   
#     college_name = "Global College"        
    
# #Function Defined   
    
#     #Default  Constructors 
#     def __init__(self):                                     
#         print("adding new student in DataBase..")

#     #Parameterized Constructors
#     def __init__(self, fullname, marks, Age):                                     
#         self.name = fullname
#         self.marks = marks
#         self.Age = Age
#         print("adding new student in DataBase..") #Constructor

# #Object Defined
# s1 = Student("Krishna", 97, 17) 
# print(s1.name, s1.marks, s1.Age)   #Krishna      

# s2 = Student("Arjun", 88, 13) 
# print(s2.name, s2.marks, s2.Age)   #Arjun      

# print(s2.college_name)

# //////////////////////////////////////////////////////////////////////////////////////

# class Student:
#     name = "Yash Mishra"
#     college = "Global Engineering College"
#     Branch = "Computer Science And Engineering"

# s1 = Student()
# print(s1.name)
# print(s1.college)
# print(s1.Branch)

#////////////////////////////////////////////////////////////////////
# class Car:
#     color = "Blue"
#     Brand = "XUV"

# c1 = Car()
# print(c1.color)    
# print(c1.color)

# ////////////////////////////////////////////////////////////////

# class Student:
#     name = "Yash Mishra"

# def __init__(self):
#     print(self)
#     print("Adding New Student Into Database")

# s1 = Student()
# print(s1)        

# //////////////////////////////////////////////////////////////////
#Class Define
class Student:
    college = "Global Engineering College"

#Function Define
    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age
        print("Adding New Student In A Database")

#Object Define
s3 = Student("Yash Mishra", 99, 21)
print(s3.name, s3.marks, s3.age)

s4 = Student("Yash Saraf", 98, 23)
print(s4.name, s4.marks, s4.age)
