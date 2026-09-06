# 🟢 Q1 — Write to file

# Create a file called notes.txt and write:
# file=open("D:/Backend/python basic/Day12/notes.txt","w")
# file.write("Python is easy \nBackend is powerful \nI am learning Django \n")


# Python is easy
# Backend is powerful
# I am learning Django

# 👉 Then read and print it.

# 🟢 Q2 — Append data
# file=open("D:/Backend/python basic/Day12/notes.txt","a")
# file.write("File handling is important\n")

# file.close()
# Add this line to the same file:

# File handling is important

#  Then read and print again.
file=open("D:/Backend/python basic/Day12/notes.txt","r")

content=file.read()
# #  Q3 — Count words

# print(content)
# words=content.split()
# # (Hint: use split())
# print(words)

#  Q4 — Find word

# Check if "Django" exists in file:
if "Django" in content:
    print("found")
else:
    print("Not found")
# Print:

# "Found"
# "Not Found"


#  Q5 — Line count
countingline=0
# 👉 Print how many lines are in the file
spliting_lines=content.splitlines()
for count in spliting_lines:
    countingline +=1
    
print(countingline)

newtext=content.replace("Python","Java")

print(newtext)

# Replace:

# Python → Java

#  Save updated content in file

updatefile=open("D:/Backend/python basic/Day12/notes.txt","w")
updatefile.write(newtext)
updatefile.close() 

updatefile=open("D:/Backend/python basic/Day12/notes.txt","r")
print(updatefile.read())
updatefile.close() 


