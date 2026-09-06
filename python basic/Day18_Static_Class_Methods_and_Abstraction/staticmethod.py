# Exercise 1 (Very Easy)

# Write this yourself.

class School:

# Class variable:

    name = "Oxford"

# Create a class method:
    @classmethod
    def show_school(cls,newname):
        cls.name=newname
        print(cls.name  )

        
School.show_school("Harveal")
# show_school()

# Print:

# Oxford

# Call:

# School.show_school()

# Expected output:

# Oxford
# 🟢 Exercise 2

# Create:
class Company:
    
    company_name = "OpenAI"

    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
        print(cls.company_name)

Company.change_company("Google")

        
# change_company(new_name)

# Inside it:

# cls.company_name = new_name

# Test:

# Company.change_company("Google")
# print(Company.company_name)

# Expected output:

# Google
# 🟢 Exercise 3

# Create:

class Student:

# Class variable:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)
Student.show_school()

Student.school="XYZ School"

Student.show_school()






# Class method:

# show_school()

# Print the school.

# Then:

# Student.school = "XYZ School"

# Call show_school() again.

# Expected output:

# ABC School
# XYZ School


# 🟢 Exercise 4 (Most Important)

# Create:

class Bank:

# Class variable:

    bank_name = "Nabil Bank"

    @classmethod
    def change_bank(cls,name):
        cls.name=name
        print(cls.name)
    
# Bank.bank_name
    
bank1=Bank
bank1.change_bank("NIC Asia")


# Class method:

# change_bank(name)

# Update:

# cls.bank_name = name

# Then:

# bank1 = Bank()
# bank2 = Bank()

# Bank.change_bank("Global IME")

# print(bank1.bank_name)
# print(bank2.bank_name)

# Expected output:

# Global IME
# Global IME

# This proves that changing the class variable changes it for every object.

# 🏆 Mini Challenge

# Create:

class Game:

# Class variable:

    version = "1.0"

# Class method:
    @classmethod
    def update_version(cls,new_version):
        cls.version=new_version
        # cls.version
        print(Game.version)

        
Game.update_version("2.0")


# Then:

# Game.update_version("2.0")
# print(Game.version)

# Expected output:

# 2.0   