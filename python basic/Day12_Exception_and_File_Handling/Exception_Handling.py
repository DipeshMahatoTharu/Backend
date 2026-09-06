# 🟢 Q1

# Ask the user for a number.

# Print:

# 100 / number

# If an error occurs, print:

# Invalid input


try:
    number=int(input("enter a number : "))
    print(100/number)

except:
    print("Invalid input ")
    
    










# 🟢 Q2

# Ask for an age.

# Convert it to an integer.

# If the user types letters, print:

# Age must be a number.


try:
    age=int(input("enter the age : "))
    print(age)
except:
    print("Age must be a number")








# 🟢 Q3

# Ask for two numbers.
try:
    num1=int(input("Enter first numeber"))
    num2=int(input("Enter second numeber"))

    print(num1/num2)

except:
 
    print("Cannot be divide by 0")

# Print their division.

# If the second number is 0, print:

# Cannot divide by zero.
