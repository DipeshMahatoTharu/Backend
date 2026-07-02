# Exercise 1 (Method Overriding)

# Don't look at any example while coding.

# Create:

class Animal:
    def sound(self):
        print("Animal make a sounf ")
class Dog(Animal):
    def sound(self):
        print("Dog Bark")
dog1 = Dog()
dog1.sound()


# Method:

# sound()

# Output:

# Animal makes a sound

# Now create:

# class Dog(Animal):

# Override the same method:

# sound()

# Output:

# Dog barks

# Then:

# dog1 = Dog()
# dog1.sound()
# Expected Output
# Dog barks



# Exercise 1

# Write this yourself.

# Create:

class Person:
    def __init__(self,name):
        self.name = name
        print("Person Constructor")

    
# Constructor:

# name

# Print:

# Person Constructor

# Now create:

class Student(Person):
    def __init__(self,name):
        super().__init__(name)
        print("Student Construtor")

    
# Use:

# super().__init__(name)

# Then print:

# Student Constructor

# Create:

student1 = Student("Dipesh")

# Finally:

print(student1.name)

# Expected output:

# Person Constructor
# Student Constructor
# Dipesh



# Write this yourself.

# Create:

class LivingThing:
    def live(self):
        
        print("Living ... ")


class Animal(LivingThing):
    def eat(self):
        
        print("Eating") 
        
class Dog(Animal):
    def bark(self):
        
        print("Woof")

# Method:

# live()

# Output:

# Living...

# Now:

# class Animal(LivingThing):

# Method:

# eat()

# Output:

# Eating...

# Now:

# class Dog(Animal):

# Method:

# bark()

# Output:

# Woof!

# Create:

dog1 = Dog()

# Call:

dog1.live()
dog1.eat()
dog1.bark()
# Expected Output
# Living...
# Eating...
# Woof!