# Question 1

# You already saw something similar:

# marks = [80, 65, 90, 40, 75, 30]

# Print:

# 80 Passed
# 65 Passed
# 90 Passed
# 40 Passed
# 75 Passed
# 30 Failed
# Rule
# 40 or more → Passed
# Less than 40 → Failed

# Use:

# list
# loop
# if/else
# f-string

# marks=[80,65,90,40,75,30]
# for i in marks:
#     if i >= 40 :
#         print(f"{i} passed ")
#     else:
#         print(f"{i} failed ")

# Question 2

# Create:

# numbers = [10, 15, 20, 25, 30]

# Print:

# 10 is Even
# 15 is Odd
# 20 is Even
# 25 is Odd
# 30 is Even

# Use % 2.    


# numbers = [10, 15, 20, 25, 30]
# for i in numbers:
#     if i % 2 == 0:
#         print(f"{i} is Even" )
#     else:
#         print(f"{i} is odd")



# Question 3

# Create:

# names = ["Dipesh", "Ram", "Hari", "Sita"]

# Print only names that start with "S".

# Expected:

# Sita
# Hint

# You can access the first character:

# name[0]


# names = ["Dipesh", "Ram", "Hari", "Sita"]
# for i in names:
#     if i[0]== "S":
#         print(i)
    
# Question 1: Palindrome check

# A word is palindrome if it reads same forward and backward.

# Example:

# madam → same forward & backward
# Task:

# Check if a word is palindrome or not.

# word = "madam"
# Expected output:
# Palindrome


# word="madam"
# reverse=""

# for letter in word:
#     reverse = letter +reverse
# if reverse ==word:
#     print("it parandom")
# else:
#     print("Not Palindrome")



# 🔥 Question 2: Count vowels
# word = "Dipesh"
# Task:

# Count how many vowels are in the word.

# Expected output:
# 2


