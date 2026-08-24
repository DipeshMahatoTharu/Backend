# Day 20 OOP Practice — Step-by-Step Concepts

# =====================================================================
# TASK 1: Class Variable vs Instance Variable
# =====================================================================
# You already know how to define instance variables. Now we will use 
# a class variable to count how many objects of a class are created.
#
# INSTRUCTIONS:
# 1. Add a class variable `instance_count` initialized to 0.
# 2. Inside `__init__`, increment this class variable by 1.
# 3. Confirm that every time you create a new Car, the count increases.

class Car:
    # TODO: Define class variable here
    
    def __init__(self, brand):
        self.brand = brand
        # TODO: Increment the class variable here
        pass

# Test your implementation:
# c1 = Car("Tesla")
# c2 = Car("BMW")
# print(Car.instance_count) # Should print 2


# =====================================================================
# TASK 2: Encapsulation & Property Getter
# =====================================================================
# Today we learn how to protect class properties using @property.
#
# INSTRUCTIONS:
# 1. Initialize a private/protected instance variable `_price` in the constructor.
# 2. Create a getter method `price` using the `@property` decorator to return `_price`.
# 3. Create a setter method `price` using `@price.setter` that verifies the new price is positive. 
#    If the price is less than or equal to 0, raise a ValueError with message "Price must be positive!".

class Product:
    def __init__(self, name, price):
        self.name = name
        # TODO: Initialize protected _price
        pass

    # TODO: Implement getter property 'price'
    
    # TODO: Implement setter property 'price' with validation


# =====================================================================
# TASK 3: Inheritance & super()
# =====================================================================
# You already know basic class structures. Now let's inherit from a 
# base class and override a method while calling the parent behavior.
#
# INSTRUCTIONS:
# 1. Inherit `ElectricCar` from `Vehicle`.
# 2. Inside `ElectricCar.__init__`, call `super().__init__` to initialize `brand` and `price`.
# 3. Add a new instance variable `battery_capacity`.
# 4. Override the `get_info()` method to return the parent info + the battery capacity details.

class Vehicle:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_info(self):
        return f"Vehicle: {self.brand}, Price: {self.price}"

class ElectricCar(Vehicle):
    # TODO: Implement __init__ using super()
    
    # TODO: Override get_info() calling super().get_info()
    pass


# =====================================================================
# TASK 4: Composition (HAS-A Relationship)
# =====================================================================
# A computer "has a" CPU. Instead of inheriting Computer from CPU,
# we pass a CPU instance into the Computer object.
#
# INSTRUCTIONS:
# 1. Create a `CPU` class with `model` and `cores` attributes.
# 2. Create a `Computer` class that accepts a `brand` and a `cpu` object in its constructor.
# 3. Implement a `display_specs` method in `Computer` that accesses and prints details from the CPU.

class CPU:
    def __init__(self, model, cores):
        self.model = model
        self.cores = cores

class Computer:
    def __init__(self, brand, cpu_object):
        # TODO: Initialize brand and CPU object
        pass

    def display_specs(self):
        # TODO: Return specifications string accessing CPU attributes
        return ""
