# Day 6 (Loops + Functions combo)

# We will build:

# number patterns
# sum of numbers
# mini calculators using loops
# real logic problems\
    
# Question 1

# Create a function:

# def show_number(n):

#  It should print:

# Number is: n

# Then:

# use a loop from 1 to 5
# call function inside loop


# def show_number(n):
#     print("Number is :",n)

# for i in range(5):
#     show_number(i)



# Question 2

# Create:

# def square(n):

# Then:

# loop from 1 to 5
# print square of each number using function
# Expected output:
# 1
# 4
# 9
# 16
# 25

# def square(n):
#     return n*n
# for i in range(1 ,6):
#     result=square(i)
#     print(f"square of {i} is :{result}")


# Create:
# def is_even(n):

# Then:

# loop from 1 to 10
# print:
# number
# "Even" or "Odd" using function

def is_even(n):
    if n %2==0:
        return "Even"
    else:
        return "Odd"

for i in range(1,11):
    print(f"{i} is {is_even(i)}")