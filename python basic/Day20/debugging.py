# Day 20 OOP Debugging Exercises

# =====================================================================
# BUGGY SCENARIO 1: Mutable Class Variable Trap
# =====================================================================
# Goal: Each student should have their own list of courses.
# Explain why the code below fails to do this, and how you would fix it.

# class Student:


#     def __init__(self, name,course):
#         self.name = name
#         self.courses =course

#     def enroll(self, course_name):
#         self.courses.append(course_name)

# # Running code:
# s1 = Student("Dipesh",["Math","computer"])
# s2 = Student("Anjali",["Science ", "Data Science"])

# s1.enroll("Front-end")

# print("Dipesh's Courses:", s1.courses)
# print("Anjali's Courses:", s2.courses) # Why does Anjali have s1's course?

# ---------------------------------------------------------------------
# QUESTION: What is wrong and why does it fail?
#
# MY ANSWER: The given code is already correct because self.courses is an instance variable created for each object. 
# Therefore, s1 and s2 have separate course lists. 
# The comment saying Anjali gets s1's course is incorrect. The problem would occur if courses = [] were defined as a class variable.
# _____________________________________________________________________
#




# =====================================================================
# BUGGY SCENARIO 2: Infinite Recursion in Property Setter
# =====================================================================
# Goal: Protect account balance from negative values.
# The code below causes a "RecursionError: maximum recursion depth exceeded".
# Explain why this happens and fix it.

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     @property
#     def balance(self):
#         return self.balance # Calls getter again?

#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative")
#         self.balance = value # Calls setter again?

# # ---------------------------------------------------------------------
# # QUESTION: Why does this loop infinitely, and how do you resolve it?
# #
# # MY ANSWER:used extra method woth getter and setter 
# # _____________________________________________________________________
# #
# # CORRECTED CODE:
# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
    
#     @property
#     def balance(self):
#         return self._balance
#     @balance.setter
#     def balance(self,value):
#         if value < 0:
#             print("value cant be negative ")
#             return
#         self._balance=value

# acc1=BankAccount(500)
# print(acc1.balance)

# acc1.balance=-1
# print(acc1.balance)


        
    
# ---------------------------------------------------------------------


# =====================================================================
# BUGGY SCENARIO 3: Broken super() parameters
# =====================================================================
# Goal: Developer should inherit from Employee, initialize name, and add programming language.
# The code below fails to compile/run. Explain and fix it.

# class Employee:
#     def __init__(self, name):
#         self.name = name

# class Developer(Employee):
#     def __init__(self, name, lang):
#         # Why is this super call incorrect?
#         super(name)
#         self.lang = lang

# ---------------------------------------------------------------------
# QUESTION: What is wrong with the super() usage?
#
# MY ANSWER:
# To properly initialize the parent class so it sets up self.name, you must call its __init__ 
# method and pass the name argument to it like this: super().__init__(name)
#
# CORRECTED CODE:

class Employee:
    def __init__(self,name):
        self.name = name

class Developer(Employee):
    def __init__(self,name,lang):
        super().__init__(name)
        self.lang=lang

name1=Developer("Dipesh","Python")
print(name1.name)
print(name1.lang)
