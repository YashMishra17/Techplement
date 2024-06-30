#Methods

class Student:                      #Class Define
    college_name = "Global College"

    def __init__(self, name, marks, Age):  #Function Define  (Constructor)
        self.name = name
        self.marks = marks
        self.Age = Age

    def welcome(self):              #1.Method Define
        print("welcome student",self.name)  

    def get_marks(self):            #2.Method Define
        print(self.marks)

    def get_Age(self):              #3.Method Define
        return self.Age    

s1 = Student("karan", 99, 21)            #Object Define
s1.welcome()
s1.get_marks()
print(s1.get_Age())


#Practice Question

#1.Creste student class that takes name and marks of three subjects as arguments in constructor.Then create a method to print average
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod #Decorator
    def hello():
        print("Hello")
       

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("Tony Stark", [99,98,97])      
s1.avg_marks()
s1.hello()     

#////////////////////////////////////////////////////////////////////////



