# class Person:
#     name = "anonymous"

#     # def changeName(self, name): 
#     #     Person.name = name                # 1.method

#     @classmethod                            # 2.method
#     def changeName(cls, name):
#         cls.name = name

# p1= Person()
# p1.changeName("Yash Mishra")
# print(p1.name)
# print(Person.name)        

# //////////////////////////////////////////////////////////////////////////
class Person:
    name = "anonymous"

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = Person()
p1.changename("Yash Mishra")        
print(p1.name)