# 🟢 Q1 — Create tuple

# Create a tuple with:

# 10, 20, 30, 40
num=(10,20,30,40)
print(num)

# 👉 Print it

# 🟢 Q2 — Access value
t = (5, 10, 15, 20)
print(t[0])
print(t[-1])

# 👉 Print:

# first element
# last element
# 🟢 Q3 — Length of tuple
t = (1, 2, 3, 4, 5)
total_element=len(t)
print(total_element)
# 👉 Find how many elements are inside

# 🟢 Q4 — Check value exists
t = (10, 20, 30, 40)
if 30 in t:
    print("30 exist ")
else:
    print("30 not exited ")

# 👉 Check if 30 exists in tuple

# Print:

# "Found"
# "Not Found"
# 🟢 Q5 — Loop tuple
t = (1, 2, 3, 4)
for all in t:
    print(all)

# 👉 Print all values one by one using loop

# 🔥 CHALLENGE (IMPORTANT)
# Q6 — Tuple inside tuple
t = (1, (2, 3), 4)
for value in t[1]:
    print(value)



# 👉 Print:

# 2
# 3

# (Hint: nested access)