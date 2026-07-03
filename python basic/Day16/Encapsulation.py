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




