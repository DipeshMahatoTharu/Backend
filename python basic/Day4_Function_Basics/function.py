# A function is a block of code that you can reuse.

# Instead of writing:

# print("Hello")
# print("Hello")
# print("Hello")

# def greet():
#     print("Hello")

# greet()
# greet()
# greet()


# Create a function called:

# show_name()

# When called, it should print:

# My name is Dipesh

# def show_name():
#     print("My name is Dipesh")



# show_name()

# Day 4 - Question 3 (Next Level)

# Create a function:

# def add():

# Inside it:

# Create two variables:

# a = 10
# b = 20
# Print their sum.

# Expected output:

# 30

# Call the function once.
# def add():
#     a = 10
#     b = 20
#     print(a + b)

# add()
# Next Level (Question 4)

# Now let’s upgrade slightly:

# Create a function:
# def subtract(a, b):

# Inside:

# subtract a and b
# print result

# Then:

# take input from user
# call function
# Expected flow:
# Enter num one: 50  
# Enter num two: 20  
# 30



# def subtract(a,b):
#     print(a-b)
    
# a=int(input("Enter num one :"))
# b=int(input("Enter num two :"))

# subtract(a,b)

    
    
# Next Question (Level up)
# Create a function:
# def check_number(n):

# Inside:

# if number is positive → print "Positive"
# if number is negative → print "Negative"
# if zero → print "Zero"

# Then:

# take input from user
# call function



def check_number(n):
    if n > 0:
        print("Number is Positive :")
    elif n < 0 :
        print("Number is Negative")
    else:
        print("Zero")
    
b=int(input("Enter num  :"))   
check_number(b)