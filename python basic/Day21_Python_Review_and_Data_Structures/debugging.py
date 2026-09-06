# Day 21 Data Structures Debugging

# =====================================================================
# BUGGY SCENARIO 1: List mutation during iteration
# =====================================================================
# Goal: Remove all users that have "banned" status.
# Explain why the code below skips removing some banned users, and fix it.

users_list = [
    {"username": "user1", "status": "active"},
    {"username": "user2", "status": "banned"},
    {"username": "user3", "status": "banned"}, # This one gets skipped! Why?
    {"username": "user4", "status": "active"}
]

def clean_banned_users(users):
    for u in users[:]:
        if u["status"] == "banned":
            users.remove(u)
    return users

# Run print:
print(clean_banned_users(users_list))

# ---------------------------------------------------------------------
# QUESTION: Why did user3 get skipped during iteration?
#
# MY ANSWER:
# When an item is removed from a list during a for loop, the remaining items immediately shift to the left to fill the gap. When user2 (Index 1) was deleted, user3 shifted left into Index 1. However, the loop's internal counter automatically moved forward to check Index 2. Because user3 shifted into a position the loop had already checked, it was skipped entirely.
#
# CORRECTED CODE:
# TODO: Rewrite the function to fix the mutation bug safely.
# ---------------------------------------------------------------------


# =====================================================================
# BUGGY SCENARIO 2: Dictionary Key Lookup Error (KeyError)
# =====================================================================
# Goal: Retrieve a configuration parameter. If not found, return "default_val".
# The code below crashes with a KeyError when accessing a missing key.
# Fix it without using try-except (hint: use a dictionary method).

configs = {
    "host": "localhost",
    "port": 8000
}
default_val=[]
def get_config_value(config_dict, key):
    # This crashes if key is not found (e.g. key="ssl")
    return config_dict.get(key, "default_val")
print(get_config_value(configs, "host"))   
print(get_config_value(configs, "ss1"))   

# ---------------------------------------------------------------------
# QUESTION: How do you safely lookup keys that might be missing in a dict?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the function below to return "default_val" if key is missing.
# ---------------------------------------------------------------------