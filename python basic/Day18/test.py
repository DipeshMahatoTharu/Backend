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
        
        print("Braked by  ",self.speed)

    def show_speed(self):
        return self.speed
        
        
        



car1 =Car("Toyota","1995",0)

car1.accelerate(20)

# 2. Employee Class

# Attributes:

# name
# salary

# Methods:

# increase_salary(amount)
# decrease_salary(amount)
# show_salary()
# 3. Mobile Phone

# Attributes:

# brand
# battery (100%)

# Methods:

# use_phone(minutes)
# charge(percent)
# show_battery()
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

# Rules:

# Can't watch if not subscribed.
# Total watch time should increase.