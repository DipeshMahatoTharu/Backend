# Day 20 OOP Debugging Exercises

# =====================================================================
# BUGGY SCENARIO 1: Class Variable Mutability
# =====================================================================
# Goal: Each employee should have their own unique list of projects.
# Explain why the code below fails to do this, and how you would fix it.

class Employee:
    projects = []  # Shared?

    def __init__(self, name):
        self.name = name

    def add_project(self, project_name):
        self.projects.append(project_name)

# Demonstration:
emp1 = Employee("Alice")
emp2 = Employee("Bob")
emp1.add_project("Database Migration")

print("Alice's Projects:", emp1.projects)
print("Bob's Projects:", emp2.projects) # Why does Bob have Alice's project?

# ---------------------------------------------------------------------
# QUESTION: What is wrong and why does it fail?
#
# MY ANSWER:
# _____________________________________________________________________
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the Employee class below to fix the bug.
# ---------------------------------------------------------------------


# =====================================================================
# BUGGY SCENARIO 2: Broken super() call in Inheritance
# =====================================================================
# Goal: Manager should inherit from Employee, initialize name and salary,
# and add a department attribute.

class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Worker):
    def __init__(self, name, salary, department):
        # Why does this fail to initialize name and salary correctly?
        super(name, salary)
        self.department = department

# ---------------------------------------------------------------------
# QUESTION: What is wrong and why does it fail?
#
# MY ANSWER:
# _____________________________________________________________________
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the Manager class below to fix the bug.
# ---------------------------------------------------------------------


# =====================================================================
# BUGGY SCENARIO 3: Infinite Recursion in Property Setter
# =====================================================================
# Goal: Protect price from negative values using a property setter.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.price = value

# Running:
# p = Product("Phone", 500) # This causes a RecursionError (Maximum recursion depth exceeded)!

# ---------------------------------------------------------------------
# QUESTION: What is wrong and why does it fail?
#
# MY ANSWER:
# _____________________________________________________________________
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the Product class below to fix the bug.
# ---------------------------------------------------------------------
