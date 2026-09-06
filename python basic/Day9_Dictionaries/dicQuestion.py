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
# marks = {
#     "math": 80,
#     "science": 90,
#     "english": 70
# }
# total_marks=0
# average=0
# hightesrtmarks=0
# lowestmarks=999999

# for subject in marks:
#     total_marks =marks[subject] +total_marks
#     average=total_marks/3
#     total_marks=


# print(average)

# for subject in marks:
#     if marks[subject] > hightesrtmarks:
#         hightesrtmarks=marks[subject]
#     if marks[subject] < lowestmarks:
#         lowestmarks=marks[subject]


# print(lowestmarks)
        
# print(hightesrtmarks)
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

# student=0
# passed_student=0
# pass_marks=40
# subject=0


# for marks in students:
#     student=student + 1 
#     subject=subject +1 
#     if students[marks] >=  40:
#         print(f"{marks}  passed ")
#         passed_student= passed_student + 1 
#     else:
#         print(f"{marks} Failed")


# print(f"{student} students are  existed ")

# print(f"{passed_student} student passed ." )

# print(f"{subject} student are there." )


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
# b=0
# a=0
# n=0
# for fre in word:
#     if fre == "b" :
#         b+=1
#     elif fre == "a" : 
#         a+=1
#     elif fre == "n":
#         n+=1
# print(b)
# print(a)
# print(n)
        
# word = "banana"
# freq = {}

# for letter in word:
#     if letter in freq:
#         freq[letter] += 1
#     else:
#         freq[letter] = 1

# print(freq)
        
# Expected:

# b = 1
# a = 3
# n = 2
# Q22

# Count frequency:

word = "programming"

fre={}
higest =0
highest_letter = ""

leastnum=99999
least_letter=""
for letter in word:
    if letter in fre:
        fre[letter]+=1
    else:
        fre[letter]=1
    
    
print(fre)



        
# Q23

# # Find most repeated letter.
# for rep in fre:
#     if fre[rep] > higest:
#         higest = fre[rep]
#         highest_letter=rep
# print(higest)
# print(highest_letter)
# # Q24

# # Find least repeated letter.
# for rep in fre:
#     if fre[rep] < leastnum:
#         leastnum=fre[rep]
#         least_letter=rep
              
# print(least_letter)   
# print(leastnum)
# # Q25
# letter_more_then_one=""
# # Print letters appearing more than once.
# for rep in fre:
#     if fre[rep] > 1:
#        print(rep) 
# print(letter_more_then_one)       

# Q26

# Count words:

# sentence = "python python django python"
# word=sentence.split()

# repeated=0
# most_repeated_sentence=""
# print(word)
# freq = {}


# for number in word:
#     if number in freq:
#         freq[number]+=1
#     else:
#         freq[number]=1
    
# for word in freq:
#     if freq[word] >repeated:
#         repeated=freq[word]
#         most_repeated_sentence=word


# print(freq)
# print(most_repeated_sentence)

         
     
     
        
# print(freq) 




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
phonebook = {
    "Ram": "9800000001",
    "Sita": "9800000002"
}

name = input("Enter name: ")

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