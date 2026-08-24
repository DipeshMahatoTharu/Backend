# Day 22 Functions & Scope Debugging

# =====================================================================
# BUGGY SCENARIO 1: Mutable Default Argument Trap
# =====================================================================
# Goal: Build a function that adds item tags. Each call should generate
# a fresh list of tags if no list is passed.
# Explain why the code below shares tags across calls, and fix it.

def add_tag(tag, tag_list=[]):
    tag_list.append(tag)
    return tag_list

# Running code:
first = add_tag("Django")
second = add_tag("REST")

print("First Call Tags:", first)
print("Second Call Tags:", second) # Why does second include "Django"?

# ---------------------------------------------------------------------
# QUESTION: Why does using a mutable default argument list share state?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the function using None as a default argument.
# ---------------------------------------------------------------------


# =====================================================================
# BUGGY SCENARIO 2: Modifying Global Variables without keyword
# =====================================================================
# Goal: Maintain a global database connection status flags.
# The code below fails to update the global status variable. Fix it.

connection_status = "DISCONNECTED"

def connect_to_database():
    # Attempting to change status
    connection_status = "CONNECTED"
    print("Inside function status:", connection_status)

# Running code:
connect_to_database()
print("Global scope status:", connection_status) # Why is this still DISCONNECTED?

# ---------------------------------------------------------------------
# QUESTION: What is wrong and how do you update a global variable?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the function to update the global status variable.
# ---------------------------------------------------------------------