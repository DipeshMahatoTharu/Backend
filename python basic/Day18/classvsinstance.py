# Day 18 — Class Variables vs Instance Variables

# This is much easier than polymorphism.

# What is an Instance Variable?

# An instance variable belongs to one object.

# Example:

# class Student:
#     def __init__(self, name):
#         self.name = name

# Create:

# student1 = Student("Dipesh")
# student2 = Student("Ram")

# Memory:

# student1
# └── name = Dipesh

# student2
# └── name = Ram

# Each object has its own name.

# That's why it's called an instance variable.

# What is a Class Variable?

# Now imagine:

# Every student studies in the same school.

# Instead of storing:

# student1.school

# student2.school

# student3.school

# We store it once.

# Example:

# class Student:
#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name

# Now:

# student1 = Student("Dipesh")
# student2 = Student("Ram")

# Memory:

# Student Class
# │
# ├── school = ABC School

# student1
# └── name = Dipesh

# student2
# └── name = Ram

# Notice:

# There is only one copy of school.

# Both students share it.

# Rule
# Instance Variable

# Uses:

# self.name

# Every object gets its own value.

# Class Variable

# Uses:

# school = "ABC School"

# Shared by every object.

# Example
# class Student:

#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(self.name)
#         print(Student.school)

# Create:

# student1 = Student("Dipesh")
# student2 = Student("Ram")

# Output:

# Dipesh
# ABC School

# Ram
# ABC School



# 🟢 Exercise 1

# Write this yourself.

# Create:

# class Student:

# Class variable:

# school = "ABC School"

# Constructor:

# name

# Method:

# show()

# Output:

# Name: Dipesh
# School: ABC School

# Create:

# student1 = Student("Dipesh")
# student1.show()


# class Student():
#     school="ABC school"
    
#     def __init__(self,name):
#         self.name=name
    
#     def show(self):
#         print(Student.school)
#         print(self.name)


# student1=Student("Dipesh")
# student1.show()


# Exercise 2

# Now you'll see why class variables are shared.

# Write this yourself:

# class Employee:

# Class variable:

# company = "Google"

# Constructor:

# name

# Method:

# show()

# Create:

# employee1 = Employee("Dipesh")
# employee2 = Employee("Ram")

# Print both.

# Then change:

# Employee.company = "OpenAI"

# Now print both again.

# Question to answer after running it:

# Why did both employees change from "Google" to "OpenAI"?

# class Employee():
#     company="Google"

#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(self.company)
#         print(self.name)

        
# employee1=Employee("OpenAI")
# employee1.show()


# Exercise 3 (Important)

# Now let's see the difference between a class variable and an instance variable.

# Write this yourself.

# Create:

class Car:
    wheels = 6

# Constructor:
    def __init__(self,brand):
        self.brand=brand
# brand
    def show(self):
        print(self.brand)
        print(self.wheels)

        
car=Car("Toyota")
car.show()
# Method:

# show()

# Output example:

# Brand: Toyota
# Wheels: 4

# Create:


car2 = Car("BMW")
car2.show()
# Show both.

# Then change:

# Car.wheels = 6

# Show both again.

# Think about it before running:

# What do you expect the output to be after changing Car.wheels to 6?