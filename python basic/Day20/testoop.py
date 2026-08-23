# For every question, before coding, write comments like:

# # I use a class because...
# # I use an instance variable because...
# # I use a class variable because...
# # I use @property because...

# Don't worry if the choice is wrong — that's what I'll correct.

# 🧠 Real-Life OOP Adaptation Set
# 🟢 Q1 — Student Management

# A college needs a system to store student information.

# Each student has:

# Name
# Age
# Student ID
# Marks

# The college name is the same for every student.

# The system should be able to:

# Display student information
# Calculate average marks
# Update marks

# Create 3 students and test the system.

# Goal: Decide what should belong to the object and what should be shared.

#in my view college name should be shared and other should be in object so it can change for all other student but schoool name never change 

# class Student:
#     collegename="Herald College Kathmandu"
#     def __init__(self,name,age,student_ID,marks):
#         self.name=name
#         self.age=age
#         self.student_ID=student_ID
#         self.marks=marks

#     def display(self):
#         print(Student.collegename)
#         print(self.name)
#         print(self.age)
#         print(self.student_ID)
#         print(self.marks)
    
#     def update(self,new_marks):
#         self.marks=new_marks

# stu1=Student("Dipesh",23,2508059,98)
# stu2=Student("sty",24,208059,88)
# stu3=Student("ssad",54,278059,85)

# stu3.display()
# stu3.update(90)        
# stu3.display()

        






# 🟢 Q2 — Food Delivery App

# Build a simple food-order system.

# Each customer has:

# Name
# Address
# Phone number

# Each order has:

# Food name
# Quantity
# Price

# The order should be able to:

# Calculate total price
# Add another item
# Display order information

# Think about:

# Which things belong to each object?

# class Food:
#     def __init__(self,name,address,phone_number):
#         self.name=name
#         self.address=address
#         self.phone_number=phone_number
#     def order(self,foodname,quantity,price):
#        self.foodname=foodname
#        self.quantity=quantity
#        self.price=price
       
#     def total_price(self):
#         print(self.quantity * self.price) 
        
# order1=Food("Dipesh","Sifal",9860793587)
# order1.order("Achha wala Pizza " ,2,120)
# order1.total_price()


# 🟢 Q3 — Bank Account

# Build a banking system.

# Each account has:

# Account holder
# Account number
# Balance

# The bank has:

# Bank name

# The account should support:

# Deposit
# Withdraw
# Check balance

# The balance should not be directly modified from outside.

# Example:

# account.deposit(5000)
# account.withdraw(1000)

# Think carefully about how the balance should be protected.


# class BankingSystem:
#     def __init__(self,Account_holder,Account_number,balance) :
#         self.Account_holder=Account_holder
#         self.Account_number=Account_number
#         self.__balance=balance


#     def deposit(self,amount):
#         self.__balance +=amount
            
#     def withdraw(self,amount):
#         #if balance is greater then amount then accepted else 
#         if amount <= self.__balance:
#             self.__balance-=amount
#         else:
#             print("Insuffient Balance")
#     def check(self):
#         return self.__balance
# account1=BankingSystem("Dipesh Mahato",989423432432,500000)               
# account1.deposit(50000)
# account1.withdraw(10000)
# print(account1.check())        
    


# 🟢 Q4 — Netflix Account

# Build a Netflix account system.

# Each user has:

# Username
# Subscription plan
# Watch time

# The account should support:

# Watching a movie
# Changing subscription
# Showing account information

# Netflix has a company name shared by all users.

# Also create something that calculates the user's total watch time.

# 🟡 Q5 — University Employee System

# A university has employees.

# Each employee has:

# Name
# Salary
# Department

# All employees belong to the same university.

# The university wants to:

# Change the university name for everyone
# Display employee information
# Increase salary
# Validate whether a salary amount is valid

# Before coding, decide which functionality should belong to:

# object
# class
# static utility
# 🟡 Q6 — E-Commerce Product

# Build a product system for an online store.

# Each product has:

# Name
# Price
# Stock

# The store has:

# Store name
# Currency

# The system should:

# Show product information
# Calculate discounted price
# Increase stock
# Decrease stock

# The price should not be allowed to become negative.

# Think:

# Should price be directly accessible?

# 🟡 Q7 — Online Account Security

# Build a user account system.

# Each user has:

# Username
# Email
# Password

# Requirements:

# Password must be hidden.
# User should be able to change password.
# User should be able to verify password.
# Password should never simply be displayed.

# Think about why certain information should be hidden.

# 🟡 Q8 — Car Rental System

# A car rental company has:

# Vehicle
# Car
# Motorcycle

# Every vehicle has:

# Brand
# Model
# Rental price

# A car additionally has:

# Number of doors

# A motorcycle additionally has:

# Engine capacity

# Create the relationship between these objects.

# Don't use polymorphism yet.

# Think:

# Is a Car a type of Vehicle?

# 🟡 Q9 — College People

# A college has:

# Person
# Student
# Teacher

# Every person has:

# Name
# Age

# Students additionally have:

# Student ID
# Course

# Teachers additionally have:

# Employee ID
# Subject

# Don't repeat the name and age initialization unnecessarily.

# 🟡 Q10 — Smartphone

# A smartphone combines different functionality.

# Create:

# Phone
# Camera
# Smartphone

# Phone can:

# Make calls

# Camera can:

# Take pictures

# Smartphone should have both capabilities.

# Think:

# Does Smartphone need to inherit from one class or multiple classes?

# 🟡 Q11 — Hospital Patient

# Build a patient record system.

# Each patient has:

# Name
# Age
# Medical record number
# Weight

# The medical record number should be protected from accidental modification.

# The system should allow:

# Updating weight
# Viewing patient information
# Calculating BMI

# The BMI should be accessible like:

# patient.bmi

# not:

# patient.bmi()

# Think about why.

# 🟡 Q12 — Ride Sharing App

# Build a simple ride-sharing system.

# A driver has:

# Name
# Vehicle
# Rating

# A ride has:

# Pickup location
# Destination
# Distance
# Price

# The system should:

# Calculate ride price
# Display ride information
# Validate whether the distance is valid

# Think about which functionality needs the object and which doesn't.

# 🔴 Q13 — Payment System

# Build a payment system.

# The application should allow:

# eSewa
# Khalti
# Bank

# For now, don't implement polymorphism.

# Instead, focus on designing the base payment functionality and hiding complicated payment-processing details from the user.

# The user should only need something simple such as:

# payment.pay()

# Think:

# What should the user see?

# What should remain internal?

# 🔴 Q14 — Game Character

# Build a game character system.

# Each character has:

# Name
# Health
# Level
# Position

# The game has:

# Game name
# Game version

# The character should be able to:

# Move
# Take damage
# Heal
# Level up

# The game version should be changeable for all game-related objects.

# 🔴 Q15 — University Course System

# Build:

# Course
# Student
# Teacher

# A course has:

# Course name
# Course code
# Maximum students

# A student has:

# Name
# Student ID

# A teacher has:

# Name
# Employee ID

# The course should allow:

# Adding students
# Removing students
# Checking available seats

# Don't let the number of students exceed the maximum.

# 🔥 Q16 — Banking System

# Build a more realistic banking system.

# Requirements:

# Account
# Owner
# Account number
# Private balance
# Bank
# Bank name shared across accounts
# Operations
# Deposit
# Withdraw
# Balance checking
# Transfer money between accounts
# Additional requirements
# Validate transaction amounts.
# Balance should not be directly changed.
# Bank name should be changeable for all accounts.
# Balance should be accessible through a property.

# You decide which OOP features are appropriate.

# 🔥 Q17 — E-Commerce System

# Build a small Amazon-style system.

# Create:

# Customer
# Product
# Cart
# Order

# Customer:

# Name
# Email
# Address

# Product:

# Name
# Price
# Stock

# Cart:

# Add product
# Remove product
# Calculate total

# Order:

# Customer
# Products
# Total
# Order status

# Requirements:

# Protect important internal data.
# Use properties where appropriate.
# Use class-level data where appropriate.
# Use static functionality where appropriate.

# You decide the design.

# 🔥 Q18 — Social Media Account

# Build a simplified social media system.

# A user has:

# Username
# Email
# Password
# Followers
# Following

# The system should allow:

# Follow another user
# Unfollow
# Change password
# Show profile
# Count followers

# The password should be protected.

# Think carefully about which data should be instance data.

# 🏆 Q19 — Final Real-Life Project
# Hotel Booking System

# Build a simplified hotel booking backend.

# You need:

# Hotel
# Room
# Customer
# Booking
# Hotel

# Has:

# Name
# Location
# Number of rooms
# Room

# Has:

# Room number
# Room type
# Price
# Availability
# Customer

# Has:

# Name
# Phone
# Email
# Booking

# Has:

# Customer
# Room
# Number of nights
# Total price

# The system should support:

# Registering customers
# Adding rooms
# Checking room availability
# Booking a room
# Cancelling a booking
# Calculating total price
# Showing booking information
# Restrictions

# Don't use polymorphism yet.

# You must decide where to use:

# Classes
# Objects
# Instance variables
# Instance methods
# Class variables
# Class methods
# Static methods
# Encapsulation
# Abstraction
# Inheritance
# super()
# @property
# Multiple inheritance only if genuinely useful
# 🧠 Your special rule

# For every question, start with comments like:

# # Class:
# # Why?


# # Instance variable:
# # Why?


# # Class variable:
# # Why?


# # Instance method:
# # Why?


# # Class method:
# # Why?


# # Static method:
# # Why?


# # Encapsulation:
# # Why?


# # Abstraction:
# # Why?


# # Inheritance:
# # Why?


# # Property:
# # Why?