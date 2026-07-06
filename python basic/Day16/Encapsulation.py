# What is Encapsulation?

# Big word.

# Simple idea.

# Encapsulation means protecting data so it can't be changed directly.

# Imagine a bank account.

# Bank Account

# Balance = Rs. 50,000

# Should anyone be able to do this?

# account.balance = 1000000000

# ❌ No.

# That would be unsafe.

# Instead, the class should control how the balance changes.

# Example without Encapsulation
# class Bank:
#     def __init__(self):
#         self.balance = 1000

# Now someone can do:

# bank.balance = -999999

# 😱 That's bad.

# Private Variables

# Python lets us mark variables as private by adding two underscores.
class Bank:
    def __init__(self):
        self.__balance = 1000

# Notice:

# __balance

# The two underscores tell other programmers:

# "This is private. Don't access it directly."

# Example
# class Bank:
#     def __init__(self):
#         self.__balance = 1000

#     def show_balance(self):
#         print(self.__balance)


# account = Bank()

# account.show_balance()

# Output:

# 1000

# Now try:

# print(account.__balance)

# Python says:

# AttributeError

# because the variable is private.

# Why?

# Instead of changing the balance directly:

# account.__balance = 5000

# we make methods like:

# deposit()
# withdraw()

# Those methods decide whether the change is allowed.

# That's encapsulation.







# class Bankbalance:
#     def __init__(self):
#         self._balance=1000
    
#     def show_balance(self):
#         print(self._balance)



# account=Bankbalance()
# account.show_balance()


# print(account.__balance)


# Now let's complete encapsulation properly.

# Add a deposit() method.
class BankBalance:
    def __init__(self):
        self.__balance=1000
    def deposit(self,amount):
        self.__balance += amount
    def show_balance(self):
        print(self.__balance)


# Expected output:
account=BankBalance()
account.deposit(500)

account.show_balance()
# 1500
# Then try:
# account.deposit(2000) account.show_balance()

# Expected:

# 3500

# Once you make deposit() work, we'll add withdraw() with a safety check:

# ```python id="knm3rj" if amount



# Exercise 1 (Easy)

# Write this yourself.

class Student:
    def __init__(self,name):
        self.__name=name
    
    def show_name(self):
        print(self.__name)

student1=Student("Dipesn")
student1.show_name()


# Constructor:

# __name

# Method:

# show_name()

# Create:

# student1 = Student("Dipesh")

# Output:

# Dipesh

# Then try:

# print(student1.__name)

# What happens?

# 🟢 Exercise 2 (Deposit)

# Write:

class Wallet:
    def __init__(self):
        self.__money=500

    def add_money(self,amount):
        self.__money+=amount

    def show_money(self):
        print(self.__money)

    def withdraw(self,amount):
        if self.__money>= amount:
            self.__money -= amount
        else:
            print("no enough moeny ")
            
# Private variable:

# __money = 500

# Methods:

# add_money(amount)
# show_money()

# Test:

wallet = Wallet()

wallet.add_money(300)

wallet.show_money()
wallet.withdraw(900)
# Expected output:

# 800
# 🟢 Exercise 3 (Withdraw)

# Extend the Wallet class.

# Add:

# withdraw(amount)

# Rules:

# If there is enough money:

# Subtract it.

# Otherwise print:

# Not enough money

# Test:

# wallet = Wallet()

# wallet.withdraw(200)

# wallet.show_money()

# Output:

# 300

# Then:

# wallet.withdraw(1000)

# Output:

# Not enough money
# 🟢 Exercise 4 (Mini Challenge)

# Create:

class Game:

# Private variable:

# __health = 100

# Methods:

# damage(amount) → decrease health
# heal(amount) → increase health
# show_health()

# Test:

# player = Game()

# player.damage(40)

# player.heal(10)

# player.show_health()

# Expected:

# 70