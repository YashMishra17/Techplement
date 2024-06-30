#1.WAP to print number from 5 to 1 by using recursion
# def show(n):
#     if(n == 0):#this is called as stoping condition(Base Case)
#         return
#     print(n)
#     show(n-1) 
#     print("END")

# show(5)
#The above function is called is recursive function

#2.WAP to return n! by Using Recursion
# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     return fact(n-1) * n

# print(fact(9))

#3.Write a recursive function to calculate the sum of first n natural numbers.
# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum= calc_sum(6)
# print(sum)    

#4.Write a recursive function to print all elements in a list.
#Hint : use list and index as parameter
# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return 
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["mango", "Litchi", "apple", "banana"]
# print_list(fruits)

#////////////////////////////////////////////////////////////////////////////
#1.WAP to print number from 10 to 1 by using recursion
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(10)    

#////////////////////////////////////////////////////////////////////////////
#2.WAP to return n! by Using Recursion
def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n-1) * n

print(fact(6))    

#///////////////////////////////////////////////////////////////////////////
#3.Write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(4)
print(sum)