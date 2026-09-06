# # class student:
# #     pass


# # student1=student()
# # student1.name="Dipesh"
# # student1.age=23

# # print(student1.name)


# # class student:
# #     pass

# # student1 = student()

# # student1.name = "Dipesh"
# # student1.age = 23

# # print(student1.name)
# # print(student1.age) 


# # class Dog:

# #     pass

# # dog1 = Dog()
# # dog2 = Dog()

# # print(dog1)
# # print(dog2)



# # Exercise 1

# # Create a class Car, create 2 objects, and print them.
# class Car:
#     pass


# car1=Car()
# car2 =Car()

# print(car1)
# print(car2)



# # # Exercise 2

# # # Create a class Phone, create 3 objects, and print them.
# # class Phone:
# #     pass

# # phone1=Phone()
# # phone2=Phone()
# # phone3=Phone()



# # print(phone1)
# # print(phone2)
# # print(phone3)
# # # Exercise 3

# # # Create your own class Laptop with 2 objects and print them.

# # # Exercise 4

# # # Create a class Book with 3 objects and print them.



# # 🟢 Exercise 1 (Easy)

# # Create a class:

# class Car:
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
# # Constructor should take:

# # brand
# # year

# # Create:
# car1=Car("BMW",2022)

# car2=Car("Toyota",2020)

# print(car1.brand)
# print(car1.year)


# # Create a class:

# class Car:
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
# # Constructor should take:

# # brand
# # year

# # Create:
# car1=Car("BMW",2022)

# car2=Car("Toyota",2020)

# print(car1.brand)
# print(car1.year)


# print(car2.brand)

# print(car2.year)



# BMW, 2022
# Toyota, 2020

# Print:

# BMW
# 2022
# Toyota
# 2020
# 🟢 Exercise 2

# Create a class:

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age =age

# Constructor:

# name
# age

# Create:


# Dipesh, 23
# Ram, 20

# detail1=Student("Dipesh",22)
# detail2=Student("Ram",20)

# print(detail1.name)
# print(detail1.age)
# print(detail2.name)
# print(detail2.age)


# Print both.

# 🟢 Exercise 3

# Create a class:

# class Laptop:
#     def __init__(self,brand,name,price):
#         self.brand=brand 
#         self.name=name
#         self.price=price


# # Constructor:

# # brand
# # ram
# # price

# laptop1=Laptop("Lenovo","Diepsh",90000)
# laptop2=Laptop("Asus Tuf","Ram",10500)


# print(laptop1.brand)
# print(laptop1.name)
# print(laptop1.price)

# print(laptop2.brand)
# print(laptop2.name)
# print(laptop2.price)



# Create two laptops and print all information.

# 🟢 Exercise 4

# Create a class:

# class Book:

# Constructor:

# title
# author

# Create 3 books and print them.

# 🟢 Exercise 5

# Create a class:

# class Animal:

# Constructor:

# name
# color

# Create two animals and print them.

# 🔥 Exercise 6 (Memory Test)

# Without looking at previous code, write from memory:

# class Phone:
#     def __init__(self, brand, price):
#         ...

# Create two phones and print their information.





# 🟢 Exercise 1

# Create a class:

# class Student:
#     def __init__(self,name):
#         self.name=name
        
#     def studing(self):
#         print(self.name ,"is studing ")


# student1 =Student("dipesh")

# student1.studing()
# # Constructor:

# name

# Method:

# study()

# When called, it should print:

# Dipesh is studying.
# 🟢 Exercise 2

# Create a class:

# class Dog:
#     def __init__(self, name):
#         self.name=name

#     def bark(self):
#         print(self.name ,"says Woof")


# Dog1=Dog("Tommy")
# Dog1.bark()


# Constructor:

# name

# Method:

# bark()    

# Output:

# Tommy says Woof!
# 🟢 Exercise 3

# Create a class:

class Car:
    
# Constructor:

# brand
    def __init__(self,brand):
        self.brand=brand
    def drive(self):
        print(self.brand,"is Driving")

    
car1=Car("BMW")

car1.drive()

# Method:

# drive()

# Output:

# BMW is driving.
# 🟢 Exercise 4

# Create a class:
class Laptop:
    def __init__(self,brand):
        self.brand=brand
    
    def start(self):
        print(self.brand,"is starting")
laptop1=Laptop("DELL")
laptop1.start()
    
# Laptop

# Constructor:

# brand

# Method:

# start()

# Output:

# Dell is starting.
# 🟢 Exercise 5

# Create a class:

class Book:
    def __init__(self,title):
        self.title=title

    def read(self):
        print("Reading",self.title)

book1=Book("Python Basic")
book1.read()
# Constructor:

# title

# Method:

# read()

# Output:

# Reading Python Basics

# (if the title is "Python Basics")