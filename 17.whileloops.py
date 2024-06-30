#While Loops #1. WAP to print "Hello" five times
# count = 1 #Count is variable used to 
# while count <= 5:
#     print("Hello")
#     count += 1
# print(count)    

# i = 1
# while i<=1000:
#     print("Yash Mishra", i)
#     i = i+1
# print(i)    


# 2. WAP to print number from 1 to 5
i = 1
# while i <= 5:
#     print(i)
#     i += 1

# print("Loop Ended") 

#3. WAP to print reverse number from 1 to 5
i = 5
# while i >= 1:
#     print(i)
#     i -= 1

#4.WAP to print numbers from 1 to 100
i = 1
# while i <= 100:
#     print(i)
#     i += 1

#5.WAP to print numbers from 100 to 1
i = 100
# while i >= 1: #Stopping Condition23
#     print(i)
#     i -= 1

#6. WAP to print a multiplication table for a number n 
# n = int(input("Enter a Number:"))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

#7. WAP to print elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

# print(nums[0])
# print(nums[2])

# idx = 0
# while idx < len(nums):
#     print(nums[idx]) #num[0], num[1], num[2]...
#     idx += 1


#Traversing
heroes = ["ironman", "Black Panther", "Moon Knight", "DareDevil", "Spiderman"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1

#8.WAP to search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)
# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 81
# i = 0 #Initialization
# while i < len(nums):
#     if(nums[i] == x ):
#         print("found at idx", i)
#         #break
#     else:
#         print("Finding.....")    
#     i += 1


#Break And continue Statement
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# print("end of loop")   

# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1 

#9.WAP to print odd number from 1 to 10
# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

#10.WAP to print even number from 1 to 10
# i = 1
# while i <= 10:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# ////////////////////////////////////////////////////////////////////////////////

#WAP to print you name five times using while loop

# count = 1
# while count <= 5:
#     print("Yash Mishra")
#     count += 1

#///////////////////////////////////////////////  

# WAP to print number from 1 to 5 using while loop

# count = 1
# while count <= 5:
#     print(count)
#     count += 1
#////////////////////////////////////////////////  

#3. WAP to print reverse number from 1 to 5       

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# ////////////////////////////////////////////////////////////    
# 4. WAP to print number from 1 to 100 using while loop    
    
# count = 1
# while i <= 100:
#     print(i)
#     i += 1    

#////////////////////////////////////////////////////////////
#5.WAP to print numbers from 100 to 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# //////////////////////////////////////////////////////////////
#6. WAP to print a multiplication table for a number n 
# n = int(input("Enter a number :"))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

# ///////////////////////////////////////////////////////////////
#7. WAP to print elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]

# list = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(list):
#     print(list[idx])
#     idx += 1

#//////////////////////////////////////////////////////////////////
#8.WAP to search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 64
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("number is found ", i)
#         break
#     else:
#         print("finding...")    
#         i += 1

#/////////////////////////////////////////////////////////////////
#9.WAP to print odd number from 1 to 10

# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

#////////////////////////////////////////////////////////////////
#10.WAP to print even number from 1 to 10

i = 1
while i <= 100:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1   
        













