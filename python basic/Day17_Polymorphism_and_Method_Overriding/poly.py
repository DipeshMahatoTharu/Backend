# # Your first exercise

# # Write this yourself.

# # class Animal:
# #     def move(self):
# #         print("Animal moves")

# # Create two child classes:

# # Dog
# # Bird

# # Override move().

# # Expected output:

# # Dog runs
# # Bird flies

# # Then:

# # dog = Dog()
# # bird = Bird()

# # dog.move()
# # bird.move()


# Exercise 1 (Easy)

# Create:

# class Animal:
#     def move(self):
#         print("Animal Move")


# class Dog(Animal):
#     def move(self):
#         print("Dog Run")

# class Bird(Animal):
#     def move(self):
#         print("Bird flies")

# dog=Dog()
# dog.move()
# bird=Bird()
# bird.move()
# # Override move().

# # Output:

# Dog runs
# Bird flies





# 🟢 Exercise 2

# Parent:

class Shape:
    def draw(self):
        print("Drawing Shape")
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")
class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle ")

circle=Circle()
circle.draw()

rectangle=Rectangle()
rectangle.draw()

# Output:

# Drawing Circle
# Drawing Rectangle
# 🟢 Exercise 3

# Parent:

class Employee:

# Method:
    def work(self):
        print("Employee is woking")
# work()
class Doctor(Employee):
    def work(self):
        print("Doctor trears patients")
class Teacher(Employee):
    def work(self):
        print("Teacher teaches students")
# Output:
employee=Employee()
employee.work()

# Employee is working

# Children:

# Doctor
# Teacher

# Override work().

# Output:
doctor =Doctor()
doctor.work()
teacher=Teacher()
teacher.work()

# Doctor treats patients
# Teacher teaches students
# 🟢 Exercise 4

# Parent:

class Vehicle:
    def start(self):
        print("")
    
    
class Car(Vehicle):
    def start(self):
        print("Car is boom boom ")

class Bike(Vehicle):
    def start(self):
        print("Bike is suuuu suuu ")

    
class Bus: 
    def start(self):
        print("Buss is buuuuuuuu")
# Method:

# start()
buss = Bus()
buss.start()

car=Car()
car.start()

bike=Bike()
bike.start()
# Children:

# Car
# Bike
# Bus

# Each should print something different.

# 🟢 Exercise 5 (Real Polymorphism)
class Animals:
    def sound(self):
        print("Animal Sounds")
class Dog(Animals):
    def sound(self):
        print("Woof")
class Cat(Animals):
    def sound(self):
        print("Meow")
class Bird(Animals):
    def sound(self):
        print("Tweet")
# Create:
animals=[
    Dog(),
    Cat(),
    Bird(),
]
# animals = [
#     Dog(),
#     Cat(),
#     Bird()
# ]

# Then:
for animal in animals:
    animal.sound()
# for animal in animals:
#     animal.sound()

# Output:

# Woof
# Meow
# Tweet

# This is where you'll really see polymorphism in action.

# 🔥 Mini Challenge
class Charater:
    def attacks(self):
        print("All Attacks")

    
class Warrior(Charater):
    def attacks(self):
        print("Warrior swings sword")

class Mage(Charater):
    def attacks(self):
        print("Mage casts spell")

class Archer(Charater):
    def attacks(self):
        print("Archer shoots arrow")

Attacks=[
    Warrior(),
    Mage(),
    Archer()
]

for attack in Attacks:
    attack.attacks()
# Warrior swings sword
# Mage casts spell
# Archer shoots arrow








# Create:

# class Character

# Children:

# Warrior
# Mage
# Archer

# Each has:

# attack()

# Outputs:

# Warrior swings sword
# Mage casts spell
# Archer shoots arrow

# Then put them in a list:

# characters = [
#     Warrior(),
#     Mage(),
#     Archer()
# ]

# Loop through them:

# for character in characters:
#     character.attack()