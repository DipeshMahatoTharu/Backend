# Day 9 Dictionary Challenge (30 Questions)
#  Easy (1–10)
# Q1
# student = {
#     "name": "Dipesh",
#     "age": 20
# }

# Print only age.
# Q2

# Add:

# "country": "Nepal"


# Q3

# Update age to 21.

# Q4

# Print all keys.

# Expected:

# name
# age
# country
# Q5
# student = {
#     "name": "Dipesh",
#     "age": 20
# }
# print(student["age"])

# student["country"]= "Nepal"
# student["age"]="21"


# print(student)


# for num in student:
#     print(num)
#     print(student[num])




# Print all values.

# Q6

# Count how many keys exist.
# Check if "age" exists.
# if "age" in student:
#     print("age exist")
# else:
#     print("age doesnt exist")
        
        
# count =0
# for counting in student:
#     count =count +1  
    
# print(count)
# Expected:

# 3
# Q7


# Print:

# Found

# or

# Not Found
# Q8

# Check if "city" exists.
# if "city" in student:
#     print("city exist")
# else:
#     print("city doesnt exist")
        
# Q9

# Create:

# Print all subjects.

# Q10

# Print all marks.

# 🟡 Medium (11–20)
# Q11

# Print only marks greater than 80.



# for subject in marks:
#     # if marks[subject] > 80:
#     #     print(subject)
#     

# print(total_marks)

# # Q12

# # Calculate total marks.



# Q13

# Calculate average marks.
marks = {
    "math": 80,
    "science": 90,
    "english": 70
}
total_marks=0
average=0


for subject in marks:
    total_marks =marks[subject] +total_marks
    average=total_marks/3



print(average)


# Q14

# Find highest mark.

# Q15

# Find lowest mark.

# Q16

# Count how many students passed.

# students = {
#     "Ram": 80,
#     "Hari": 30,
#     "Sita": 90,
#     "Gita": 40
# }

# Pass mark = 40

# Q17

# Print only passed students.

# Q18

# Print only failed students.

# Q19

# Count how many subjects exist.

# Q20

# Print:

# Math -> 80
# Science -> 90
# English -> 70

# using f-strings.

# 🔴 Challenge (21–30)
# Q21

# Count frequency of letters:

# word = "banana"

# Expected:

# b = 1
# a = 3
# n = 2
# Q22

# Count frequency:

# word = "programming"
# Q23

# Find most repeated letter.

# Q24

# Find least repeated letter.

# Q25

# Print letters appearing more than once.

# Q26

# Count words:

# sentence = "python python django python"

# Expected:

# python = 3
# django = 1
# Q27

# Find most repeated word.

# Q28

# Create a phonebook dictionary.

# Search a name and print the number.

# Q29

# Merge two dictionaries.

# Q30 ⭐

# Build a mini student system:

# students = {
#     "Ram": 80,
#     "Hari": 60,
#     "Sita": 90
# }

# Print:

# Top student: Sita
# Average marks: 76.67