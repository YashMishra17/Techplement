#del Keyword
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Yash")

# print(s1.name)
# del s1.name
# print(s1.name)

#////////////////////////////////////////////////////////////

#Private Attributes And Methods
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass     
        
#     def reset_pass(self):
#         print(self.__acc_pass)         #(Private)

# acc1 = Account("12345678", "abcdefg")      
# print(acc1.acc_no)  
# # print(acc1.__acc_pass)    #Public

# print(acc1.reset_pass())
#/////////////////////////////////////////////////////////////////////////////

#Conceptual Private
# class Person:
#     __name = "Yash Mishra" #This Is Conceptual Private

# p1 = Person()

# print(p1.__name) #It Gives Error

#///////////////////////////////////////////////////////////////

# class Person:
#     __name = "Yash Mishra"

#     def __hello(self):        #Private Keyword
#         print("Hello Everyone!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# # print(p1.__hello) #We can't access it directly because it is a private function

# print(p1.welcome())

#/////////////////////////////////////////////////////////////////////////////////////////////
#del Keyword
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Yash")

# print(s1.name)
# del s1.name
# print(s1.name)

# ////////////////////////////////////////////////////////////////////////////
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass) #Private

# acc1 = Account("123456", "abcdefghigklmnopqrstuvwxyz")        
# print(acc1.acc_no)
# print(acc1.acc_pass)

# /////////////////////////////////////////////////////////////////////////////

# class Person:

#     def __hello(self):
#         print("Hello Everyone!")

#     def welcome(self):
#         self.__hello()   

# p1 = Person()
# print(p1.welcome())         