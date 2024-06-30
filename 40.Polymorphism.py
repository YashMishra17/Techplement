# print(1 + 3) #4
# print(type(1))

# print("yash" + "mishra") #Conctenation
# print(type("yash"))

# print([1,2,3] + [4,5,6]) #Merging Two List
# print(type([1,2,3]))

#So Above ExampleS Are Operator Overloading

#Complex Numbers

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img,"j")    

#     def add(self, num2):                              # Without Using Dunder Function
#         newReal = self.real + num2.real   
#         newImg = self.img + num2.real
#         return Complex(newReal, newImg)

    # def __add__(self, num2):                        #By Using Dunder Fuction
    #     newReal = self.real + num2.real   
    #     newImg = self.img + num2.real
    #     return Complex(newReal, newImg)  

    # def __sub__(self, num2):                        #By Using Dunder Fuction
    #     newReal = self.real - num2.real   
    #     newImg = self.img - num2.img
    #     return Complex(newReal, newImg)  

# num1 = Complex(1, 3)
# num1.showNumber()  

# num2 = Complex(2, 4)
# num2.showNumber()  

# num3 = num1.add(num2)                                 #Without Using DundeR Function
# num3.showNumber()

# num3 = num1 + num2                          #By Using Dunder Function
# num3.showNumber()

# num3 = num1 - num2                          #By Using Dunder Function
# num3.showNumber()

# ///////////////////////////////////////////////////////////////////////////////////////
class Complex:
    def __init__(self, img, real):
        self.img = img
        self.real = real

    def shownumber(self):
        print(self.real,"i +",self.img,"j") 

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.real
        return complex(newReal, newImg)      
    
num1 = Complex(2,4)    
num1.shownumber()