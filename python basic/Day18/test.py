# Level 1 (Easy)
# 1. Car Class

# Create a Car class.

# Attributes:

# brand
# model
# speed (starts at 0)

# Methods:

# accelerate(speed)
# brake(speed)
# show_speed()

# Example:

# Current Speed: 0

# Accelerated by 20

# Current Speed: 20

# Braked by 5

# Current Speed: 15

# class Car:
#     def __init__(self,brand,model,speed):
#         self.brand=brand
#         self.model=model
#         self.speed=speed
#         print("Current speed :",self.speed)
        
        
#     def accelerate(self,speed):
#         self.speed+=speed
#         print("accelerated by ",self.speed)

#     def brake(self,speed):
#         print("Current speed  ",self.speed)
#         print("Breaked by :",speed)
#         self.speed-=speed
        
#     def show_speed(self):
#         print("Current speed ",self.speed)
        
# #your part
# Kritika_car =Car("Toyota","1995",0)

# Kritika_car.accelerate(20)
# Kritika_car.brake(5)
# Kritika_car.show_speed()

# 2. Employee Class

# Attributes:

# name
# salary

# Methods:

# increase_salary(amount)
# decrease_salary(amount)
# show_salary()


# class Employee:
#     def __init__(self,name,salary):
#         self.name=name 
#         self.salary=salary
      
#     def increase_salary(self,amount):
        
#         print("Starting Salary :",self.salary)
#         self.salary +=amount
        
#         print("Increase of salary :" , amount)
#         print("Salary after increasing   :",self.show_salary(), "\n")

#     def decrease_salary(self,amount):
#         self.salary-=amount
        
#         print("Decreased salary : ",amount)
#         print("salary after decreasing ",self.show_salary())
        
#     def show_salary(self):
        
#         return self.salary

        
# emplyee=Employee("Dipesh Mahato ",50000)
# emplyee.increase_salary(30000)
# emplyee.decrease_salary(4000)



        

# 3. Mobile Phone

# Attributes:

# brand
# battery (100%)

# Methods:

# use_phone(minutes)
# charge(percent)
# show_battery()

# Battery: 100%

# Use phone for 30 minutes

# Battery: 70%

# Charge 20%

# Battery: 90%

# Charge 30%
# Battery: 100%

# class Phone:
#     def __init__(self,brand,battery):
#         self.brand=brand
#         self.battery=100

#     def use_phone(self,minutes):
#         self.battery-=minutes
        
#         if self.battery<=0:
#             self.battery=0
#             print("Phone Switch off ")
#         else:
#             print("Battery percentage is :",self.battery)


#     def charge_phone(self,percent):
#         self.battery+=percent
        
#         if self.battery >= 100:
#             self.battery=100
#             print("battery full")
#         else:
#             print("Batter charging : " ,self.battery)
        
# phone1=Phone("Chinese phone ",40)
# phone1.use_phone(30)

# phone1.charge_phone(10)
        



        


# 4. Bank Account (Upgrade)

# Improve your current program.

# Add:
# deposit()
# withdraw()
# check_balance()
# Prevent withdrawing more than the balance.
# Example:
# Balance = 500

# Withdraw 700



# class Account:
#     def __init__(self,balance,account):
#         self.balance=balance
#         self.account=account

#     def withdraw(self,amount):
#         if self.balance < amount:
#             print("Insufficent amount ")
#         else:
#             self.balance -= amount
#             print("Rs",amount ,"was withdraw")
#             print("Your balance is Rs:",self.get_balance())
      
#     def deposit(self,amount):
#         self.balance += amount
#         print("Rs",amount)
#         print("Your balance is Rs:",self.get_balance())
    
   
#     def get_balance(self):
#         return self.balance

#     def check_balance(self):
#         print(self.get_balance())
        
# account1=Account(500,31313131)

# account1.withdraw(500)
    

# account1.check_balance()






# 🟡 Level 2 (Medium)
# 5. Student Management

# Attributes:

# name
# marks (list)
# class Student_Management:
#     def __init__(self,name,marks):
#         self.marks=marks
#         self.name=name

#     def average(self):
#         return sum(self.marks)/len(self.marks)
   
    
#     def hightest(self):
#         hightest =self.marks[0]

#         for marks in self.marks:
#            if marks > hightest:
#             hightest=marks
            
#         return hightest
#     def lowest(self):
#         lowest=self.marks[0]
        
#         for marks in self.marks:
#             if marks<lowest:
#                 lowest=marks
                
#         return lowest
#     def passmarks(self):
#         if self.average()>=40:
#             print("pass")
#         else:
#             print("Fail")
            


# student1=Student_Management("Dipesh",[90,32,67])
# print(student1.average())
# print(student1.lowest())
# print(student1.hightest())
# student1.passmarks()

            
        
    
# Methods:

# average()
# highest_mark()
# lowest_mark()
# result()

# Output:

# Average : 88.3
# Highest : 95
# Lowest : 78
# Result : PASS



# 6. Shopping Cart

# Attributes:

# owner
# total_price

# Methods:

# add_item(price)
# remove_item(price)
# show_total()

# class Shopping:
#     def __init__(self,owner,total_price):
#          self.owner=owner
#          self.total_price=total_price

#     def add_item(self,price):
#         self.total_price += price 
#         print("Your total price is :",self.total_price)
#     def remove_item(self,price):
#         self.total_price -= price
#         print("Your total after removing is :",self.total_price)

#     def show_total(self):
#         print("Total price is :",self.total_price)
# shopping1=Shopping("Dipesh",7000)
# shopping1.add_item(4000)
# shopping1.remove_item(3111)
# shopping1.show_total()

        
        

# 7. Movie Ticket

# Attributes:

# movie_name
# available_seats

# Methods:

# book_ticket(number)
# cancel_ticket(number)
# show_available()

# Don't allow booking more seats than available.

# 8. ATM Machine

# Menu

# 1. Deposit
# 2. Withdraw
# 3. Balance
# 4. Exit

# Keep asking until Exit.

# 🔵 Level 3 (Hard)
# 9. Library System

# Book:

# title
# author
# available

# Methods:

# borrow()
# return_book()
# 10. Cricket Player

# Attributes:

# name
# runs
# balls

# Methods:

# score_run()
# strike_rate()
# show_stats()
# 11. Restaurant Bill

# Attributes:

# customer
# bill

# Methods:

# add_food(price)
# add_drink(price)
# discount(percent)
# final_bill()
# 12. Inventory System

# Attributes:

# product_name
# quantity

# Methods:

# add_stock()
# sell_stock()
# show_stock()

# Prevent negative stock.

#  Challenge (No Help)

# Build a Netflix Account.

# Attributes:

# username
# subscription (True/False)
# watch_time

# Methods:

# subscribe()
# watch(hours)
# cancel_subscription()
# show_details()
