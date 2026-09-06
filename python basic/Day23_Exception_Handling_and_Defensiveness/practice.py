# Day 23 Practice — Exceptions & Input Validation

# =====================================================================
# TASK 1: Multiple Except Blocks
# =====================================================================
# A robust function must catch different exception types separately 
# and return user-friendly messages for each.
#
# INSTRUCTIONS:
# 1. Complete `parse_and_divide` which accepts two strings.
# 2. Convert both to floats. Catch `ValueError` (if strings are not numbers).
# 3. Divide first by second. Catch `ZeroDivisionError` (if division by 0).
# 4. If successful, return the result. If ValueError, return "Invalid Number". 
#    If ZeroDivisionError, return "Cannot divide by zero".

def parse_and_divide(str_a, str_b):
    try:
        converta=float(str_a)
        convertb=float(str_b)
        return converta/convertb

    except ValueError:
        return "Invaild Error "
    
    except ZeroDivisionError:
        return "cannot be divided by 0"
    return None

# Test:
print(parse_and_divide("10", "2")) # Should print 5.0
print(parse_and_divide("abc", "2")) # Should print "Invalid Number"
print(parse_and_divide("10", "0")) # Should print "Cannot divide by zero"


# =====================================================================
# TASK 2: Raising Exceptions with raise
# =====================================================================
# You already know how to catch errors. Now we learn how to throw them.
#
# INSTRUCTIONS:
# 1. Complete the `verify_age` function.
# 2. If age is less than 0 or greater than 120, raise a `ValueError` 
#    with message "Age must be between 0 and 120".
# 3. If age is valid, print "Age verified".

def verify_age(age):
    try:
        if age < 0 or age > 120:
            return "Age is Valid"


    except ValueError:
        return "Age must be between 0 and 120 "

print(verify_age(133))

# =====================================================================
# TASK 3: Defining and Using Custom Exceptions
# =====================================================================
# Today we define our first custom exception class.
#
# INSTRUCTIONS:
# 1. Create a class `NegativeBalanceError` inheriting from `Exception`.
# 2. Complete `withdraw_funds` function. If balance - amount is less than 0,
#    raise your `NegativeBalanceError` with message "Insufficient balance!".

# TODO: Define NegativeBalanceError here
class NegativeBalanceError(Exception):
        pass
def withdraw_funds(balance, amount):
    # TODO: Check condition and raise custom error
        if  balance - amount < 0:
            raise NegativeBalanceError("number must be greater then 0")

        return balance - amount

# Test:
try:
    withdraw_funds(100, 150)
except NegativeBalanceError as e:
    print("Caught error:", e) # Should print "Caught error: Insufficient balance!"