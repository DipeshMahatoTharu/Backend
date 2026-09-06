# class Student:
#     def __init__(self,name,marks):
#          self.name=name
#          self.marks=marks

#     def get_marks(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
        
#         return sum/3
#     def show(self):
#         print(f"HI,{self.name} Your average marks is {self.get_marks()}")
# s1=Student("Dipesh",[90, 90 ,95])

# print(s1.show())


class Account:
    def __init__(self,balance,account):
        self.balance=balance
        self.account=account

    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount ,"was debited")
        print("Your balance is Rs:",self.get_balance())
      
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount)
        print("Your balance is Rs:",self.get_balance)
        
    def get_balance(self):
        return self.balance

account1=Account(1000,31313131)

account1.debit(30)
