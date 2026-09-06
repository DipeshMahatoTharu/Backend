# Write a program that:

# Asks for two numbers.
# try:
#     num1=int(input("Enter num1 :"))

#     num2=int(input("Enter num2 :"))
#     # Prints their division.

#     print(num1/num2)

# # If the user enters letters:
# # Print:
# except ValueError:
#     print("Please enter numbers only. ")

# except ZeroDivisionError:
#     print(" Cannot divide by zero.")
    
    

# Please enter numbers only.
# If the second number is 0:
# Print:
# Cannot divide by zero.

# Write a program:

# Ask the user for a number.
try:
    number=int(input("enter the number :"))
    print(100/number)

except ValueError:
    print("Please enter number only ")

except ZeroDivisionError:
    print("Cannot divide by zero ")

else:
    print("Messege printed Successful ")

# Print:
# 100 / number
# Handle:
# ValueError
# ZeroDivisionError
# If everything works correctly, print:


# Write a program that:

# Asks the user for two numbers.
try:
    num1=int(input("Enter num1 :"))

    num2=int(input("Enter num2 :"))
    # Prints their division.

    print(num1/num2)
except ZeroDivisionError:
    print("number cannot be divisible by 2")

except ValueError:
    print("It should be number ")
else:
    print("Success")
    

finally:
    print("Program ended ")

    
# Prints their division.
# Handles:
# ValueError
# ZeroDivisionError
# If successful, print:
# Calculation successful!
# In finally, print:
# Program ended.