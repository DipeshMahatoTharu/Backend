# Lesson 1: What is a Dictionary?

# A dictionary stores:

# key → value

# Example:

# student = {
#     "name": "Dipesh",
#     "age": 20,
#     "course": "CS"
# }

# Here:

# "name"   → key
# "Dipesh" → value

# "age"    → key
# 20       → value





# student ={
#     "name":"20"
# }



# Lesson 2: Access Values
# print(student["name"])
# print(student["age"])

# Output:

# Dipesh
# 20


# Lesson 3: Update Values
# student["age"] = 21

# Now age becomes 21.

# 🧠 Lesson 4: Add New Key
# student["city"] = "Kathmandu"

# Now the dictionary has a new key/value pair.

# 🧠 Lesson 5: Loop Through Dictionary
# for key in student:
#     print(key, student[key])

# Output:

# name Dipesh
# age 21
# course CS
# city Kathmandu




# Question 1

# Create:

# person = {
#     "name": "Dipesh",
#     "country": "Nepal"
# }

# Print the name.



person={
    "name":"dipesh",
    "country": "nepal"

    
}

print(person["name"])



# Question 2

# Create:

# car = {
#     "brand": "Toyota",
#     "year": 2022
# }

# Print the year.
car = {
    "brand": "Toyota",
    "year": 2022
}


print(car["year"])
# Question 3

# Create:

# student = {
#     "name": "Ram",
#     "marks": 80
# }

# Update marks to 90 and print the dictionary.
student = {
    "name": "Ram",
    "marks": 80
}

student["marks"]=90
print(student["marks"])


# Question 4

# Create:

# book = {
#     "title": "Python Basics"
# }

# Add:

# "author": "Dipesh"

# Print the dictionary.
book = {
    "title": "Python Basics"
}
book["author"]="Dipesh"
print(book)
# Question 5

# Create:

# student = {
#     "name": "Hari",
#     "age": 19,
#     "city": "Pokhara"
# }
# Use a loop to print all keys and values.

student = {
    "name": "Hari",
    "age": 19,
    "city": "Pokhara"
}


for loop in student:
    print(loop ,student[loop] )