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

class Car:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed
        print("Current speed :",self.speed)
        
        
    def accelerate(self,speed):
        self.speed+=speed
        print("accelerated by ",self.speed)

    def brake(self,speed):
        print("Current speed  ",self.speed)
        print("Breaked by :",speed)
        self.speed-=speed
        
    def show_speed(self):
        print("Current speed ",self.speed)
        
#your part
Kritika_car =Car("Toyota","1995",0)

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

# Output:
# Insufficient Balance

# class Bank:
#     def __init__(self,name,salary,deposit):
#         self.name=name 
#         self.salary=salary
#         self.deposit=deposit
      
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

#     def deposit(self,deposite):
#         self.amount+=deposite
        
#     def withdraw(self,withdraw):
#         if self.amount <=self.withdraw:
#             print("Insuffeienct amout ")
#         else :
#             self.amount-=self.withdraw
    
    




#world cup



# 🟡 Level 2 (Medium)
# 5. Student Management

# Attributes:

# name
# marks (list)

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

