#1. (a)Create Account class  with 2 attributes - balance and account number.
#   (b)Create methods for debit,credit and printing the balance.

# class Account:

#     def __init__(self, balance, accountnumber):
#         self.balance = balance
#         self.accountnumber = accountnumber

#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount,"was deleted")
#         print("total balance =", self.get_balance())

#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.",amount,"was added")
#         print("total balance =", self.get_balance())    

#     def get_balance(self):
#         return self.balance    

# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)

#//////////////////////////////////////////////////////////////////////////////////
#1. (a)Create Account class  with 2 attributes - balance and account number.
#   (b)Create methods for debit,credit and printing the balance.

class Account:                                       #class define

    def __init__(self, balance, accountnumber):       #function define           
        self.balance = balance
        self.accountnumber = accountnumber

    def debit(self,amount):                      #Method Define
        self.balance -=amount
        print("RS.",amount,"was deleted")
        print("Total Balance =" ,self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("RS",amount,"was added")    
        print("Total Balance =", self.get_balance())

    def get_balance(self):
        return self.balance    
    
#Object Define
acc1= Account(1000, 12345)    
acc1.credit(100)    
acc1.debit(100)

            
