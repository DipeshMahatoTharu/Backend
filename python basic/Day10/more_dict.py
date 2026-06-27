# Step 2 – Dictionary Operations (New)

# Practice these on your own.

# Start with:

marks = {
    "Science": 90,
    "Maths": 80,
    "English": 40
}
# Q1. Add a new subject
marks["Computer"]=95
print(marks)

# Add:

# Computer = 95
# Q2. Update a mark

# Change:
marks["English"]=75

# English = 75
# Q3. Delete a subject
del marks["Maths"]

# Delete:

# Maths
# Q4. Check if a key exists
if "Science" in marks:
    print("Scienc exists")
else:
    print("Science not found ")

# Check whether:

# Science

# exists.

# Print:

# Science exists

# or

# Science not found
# Q5. Check another key
if "History" in marks:
    print("History exists")
else:
    print("history not found ")
# Check whether:

# History

# exists.

# Print:

# History exists

# or

# History not found


print(marks)
