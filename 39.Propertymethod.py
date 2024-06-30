# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = str((self.phy + self.chem + self.math )/ 3) + "%"  

#     # def calcPercentage(self):   
#     #     self.percentage = str((self.phy + self.chem + self.math )/ 3) + "%"       #1.Method
        
#     @property
#     def percentage(self):    
#         return str((self.phy + self.chem + self.math )/ 3) + "%"  

# stu1 = Student(98, 99, 98)        
# print(stu1.percentage)

# stu1.phy = 88
# print(stu1.percentage)
# stu1.calcPercentage()
# print(stu1.percentage)

# /////////////////////////////////////////////////////////////////////////////////////
class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths


    @property
    def percentage(self):
        return str((self.phy+ self.chem+ self.maths)/ 3) + "%"
    
stu1 = Student(78,88,95)
print(stu1.percentage)
