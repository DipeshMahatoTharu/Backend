"""
============================================================
DAY 23 CHALLENGE & FINAL PROJECT
============================================================

Today we have two mini-projects to build. Both focus on defensive 
programming, fail-fast checking, and custom exception handling.

------------------------------------------------------------
PROJECT 1: BANK TRANSACTION VALIDATOR
------------------------------------------------------------
Build a transaction validator for a single bank account represented 
as a dictionary: `account = {"holder": "Dipesh", "balance": 1000.0}`.

Requirements:
1. Define custom exceptions:
   - `InvalidAmountError` (if amount <= 0 or not a number)
   - `InsufficientFundsError` (if withdraw amount > balance)
   - `InvalidAccountError` (if account dict is missing required keys)
2. Implement functions:
   - `validate_account(acc)`: Raises InvalidAccountError if keys "holder" or "balance" are missing.
   - `deposit(acc, amount)`: Increases balance. Raises InvalidAmountError if input is invalid.
   - `withdraw(acc, amount)`: Decreases balance. Raises InsufficientFundsError or InvalidAmountError on validation failure.

------------------------------------------------------------
PROJECT 2: USER REGISTRATION SYSTEM
------------------------------------------------------------
Build a console user registration service that maintains an in-memory 
database of users in a dictionary: `database = {"admin": "admin@test.com"}`.

Input:
- username, email, age, password

Validation Rules (must raise custom exceptions):
1. Username must not be empty or blank. (Raise `EmptyUsernameError`)
2. Username must not already exist in the database keys. (Raise `DuplicateUserError`)
3. Age must be a valid integer between 13 and 120. (Raise `InvalidAgeError`)
4. Email must contain '@' and '.' characters. (Raise `InvalidEmailError`)
5. Password must be at least 6 characters long. (Raise `WeakPasswordError`)

Requirements:
- Implement a function `register_new_user(database, username, email, age, password)`.
- Use a try-except block to catch these exceptions, print the specific error, and return False.
- If all validations pass, add `username: email` to the database and return True.


"""

# 1. Define custom exceptions:
#    - `InvalidAmountError` (if amount <= 0 or not a number)
#    - `InsufficientFundsError` (if withdraw amount > balance)
#    - `InvalidAccountError` (if account dict is missing required keys)

account = {"holder": "Dipesh", "balance": 1000.0}
class InvalidAmountError(Exception):
   pass
class InsufficientFundsError(Exception):
   pass
class InvalidAccountError(Exception):
   pass
def deposit(acc, amount):
   try:
      amount=float(amount)
   except:
      raise InsufficientFundsError("please enter number only :")

   if amount <0:
      raise InsufficientFundsError("withdraw must be greater then 0 ")
   
   acc["balance"]=acc["balance"]+amount
   return acc["balance"]

def validate_account(acc):
   if  "holder" not in acc or  "balance" not in acc:
      raise InvalidAccountError("Account doesnt exist")
   
def withdraw(acc,amount):
   if acc["amount"]< amount :
      raise InsufficientFundsError ("Insufficient funds")
   acc["amount"] -= amount
   return acc["amount"]

      
      
   
   
# 2. Implement functions:
#    - `validate_account(acc)`: Raises InvalidAccountError if keys "holder" or "balance" are missing.
#    - `deposit(acc, amount)`: Increases balance. Raises InvalidAmountError if input is invalid.
#    - `withdraw(acc, amount)`: Decreases balance. Raises InsufficientFundsError or InvalidAmountError on validation failure.




# Input:
# - username, email, age, password

# Validation Rules (must raise custom exceptions):
# 1. Username must not be empty or blank. (Raise `EmptyUsernameError`)
# 2. Username must not already exist in the database keys. (Raise `DuplicateUserError`)
# 3. Age must be a valid integer between 13 and 120. (Raise `InvalidAgeError`)
# 4. Email must contain '@' and '.' characters. (Raise `InvalidEmailError`)
# 5. Password must be at least 6 characters long. (Raise `WeakPasswordError`)

# Requirements:
# - Implement a function `register_new_user(database, username, email, age, password)`.
# - Use a try-except block to catch these exceptions, print the specific error, and return False.
# - If all validations pass, add `username: email` to the database and return True.

class EmptyUsernameError(Exception):
   pass
class DuplicateUserError(Exception):
   pass
class InvalidAgeError(Exception):
   pass
class InvalidEmailError(Exception):
   pass
class WeakPasswordError(Exception):
   pass
def register_new_user(database,username,email,age,password):
   try:
      if not username or username.strip() == "":
         raise EmptyUsernameError("User name must be filled ")
      
      if username in database:
         raise DuplicateUserError("Username already exit in database")
      
      if age < 13 or age > 120:
         raise InvalidAccountError("Age must be between 13 to 120 ")
      
      if   "@" not in email or "." not in email:
         raise InvalidEmailError("Email must contain @ or .")
      
      if len(password) < 6 :
         raise WeakPasswordError("Password must be greater then 6")
      database[username] = email
      return True
   except Exception as e:
      print(f"Registration Failed {e} ")
      return False