# What is Inheritance?

# Inheritance means:

# A child class can use the code of a parent class.

# Instead of writing the same code again and again, we inherit it.

# Real-life example 

# Imagine:

# Animal
# │
# ├── Dog
# ├── Cat
# └── Bird

# Every animal can:

# Eat 
# Sleep 

# So instead of writing eat() and sleep() inside every class, we write them once in Animal.

# Then:

# Dog inherits them.
# Cat inherits them.
# Bird inherits them.




# our First Exercise

# Without looking at my code, write this yourself.

# Parent Class
# Vehicle

class Vehicle:
    def drive(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

car1=Car()
car1.drive()

    
# Method:

# start()

# Output:

# Vehicle Started
# Child Class
# Car

# Car should inherit from Vehicle.

# Create:

# car1 = Car()

# Call:

# car1.start()

# Expected Output:

# Vehicle Started