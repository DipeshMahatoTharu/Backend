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


# word = "Dipesh"
# count=0
# for letter in word:
#     if letter.lower() in "aeiou":
#         count=count +1 

   
# print(count)
    
    
    
#     Question 1: Print ONLY consonants
# word = "programming"
# Task:

# Print only consonants.

# Expected output:
# p
# r
# g
# r
# m
# m
# n
# g

# word = "programming"
# for letter in word:
#     if letter.lower() not in "aeiou":
#         print (letter)


# Question 2: Count vowels in sentence
# sentence = "I am learning Python"
# Task:

# Count how many vowels are in the sentence.

# Expected output:
# 6


# sentence = "I am learning Python"
# count=0
# for letter in sentence:
#     if letter.lower() in "aeiou":
#         count =count +1

        
# print(count)



# 🔵 Question 3: Count each letter frequency
# 
# Task:

# Print frequency of each letter.

# Expected output:
# h = 1
# e = 1
# l = 2
# o = 1

    # word = "hello"
    # freq = {}

    # for letter in word:
    #     if letter in freq:
    #         freq[letter] += 1
    #     else:
    #         freq[letter] = 1

    # for key in freq:
    #     print(f"{key} = {freq[key]}")





    # word = "hello"

    # freq={}

    # for letter in word:
    #     if letter in freq:
    #         freq[letter] +=1
    #     else: 
    #         freq[letter] =1

    # for key in freq:
    #     print(f"{key} = {freq[key]}")
            

# 🔥 Bonus Challenge (Hard)

# Check if a word is Pangram letter check (simple version):

# 👉 Does the word contain all vowels (a, e, i, o, u)?

# word = "education"
# Expected output:
# All vowels present

# OR

# Missing vowels
# 💡 Hints
# Consonant check:
# if letter not in "aeiou"
# Vowel check:
# if letter in "aeiou"
# Dictionary idea:
# freq = {}