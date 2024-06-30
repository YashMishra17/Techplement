#1.WAP to print elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)

#2.WAP to search for a number x in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]
    
nums = [1,4,9,16,25,36,49,64,81,100]

x = 64

# idx = 0
# for el in nums:
#     if(el == x):
#         print("Number Found At idx", idx)
#     idx += 1    

 #This Type of Method is also called as linear search       


#/////////////////////////////////////////////////////////////////
# 1.WAP to print elements of the following list using a for loop:
#[1,4,9,16,25,36,49,64,81,100]   

list = [1,4,9,16,25,36,49,64,81,100] 
for nums in list:
    print(nums)   

# ////////////////////////////////////////////////////////////    
#2.WAP to search for a number x in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]    
x = 64  

idx = 0
for el in nums:
    if(el == x):
        print("Element is found at idx",idx)
        idx += 1


        
     
    
