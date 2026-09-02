# Day 21 Practice — Data Manipulation & Processing

# =====================================================================
# TASK 1: Filtering Nested Records
# =====================================================================
# In backend APIs, you often need to filter records based on active filters.
#
# INSTRUCTIONS:
# 1. Complete the `get_active_users` function.
# 2. Return a list of usernames of all users whose "is_active" status is True.

users = [
    {"username": "dipesh", "is_active": True},
    {"username": "anjali", "is_active": False},
    {"username": "ram", "is_active": True},
    {"username": "shyam", "is_active": False}
]

def get_active_users(user_list):
    active_username=[]
    for user in user_list:
        if user["is_active"] == True:
            active_username.append(user["username"])
    return active_username

# Test:
print(get_active_users(users)) 


# =====================================================================
# TASK 2: Sorting Data by Nested Key
# =====================================================================
# Backend search tables must sort products by price.
#
# INSTRUCTIONS:
# 1. Use the `sorted()` function with a lambda key.
# 2. Sort the `products` list below by the "price" key in descending order.

products = [
    {"name": "Laptop", "price": 85000.0},
    {"name": "Mouse", "price": 1500.0},
    {"name": "Keyboard", "price": 3000.0},
    {"name": "Monitor", "price": 15000.0}
]

def sort_products_by_price(product_list):
    # TODO: Implement sorting descending
    # sorted=[]
    # for sort in product_list:
    #     reverese =True
    #     sort["name"] =reverese
    return sorted(product_list , key=lambda x: x["name"],reverse=True) #one liner
        
    

# Test:
print(sort_products_by_price(products))


# =====================================================================
# TASK 3: List Indexing (enumerate)
# =====================================================================
# Print items with their ranks (1-indexed).
#
# INSTRUCTIONS:
# 1. Complete the `print_leaderboard` function.
# 2. Return a list of strings in format "Rank. Name" (e.g. "1. Dipesh").

players = ["Dipesh", "Anjali", "Ramesh", "Sita"]

# def get_leaderboard(names_list):
#     # TODO: Implement using enumerate() starting at index 1
#     return []

# Test:
# print(get_leaderboard(players))


# =====================================================================
# TASK 4: Parallel Collections (zip)
# =====================================================================
# Combine product keys and their quantity lists into a dictionary.
#
# INSTRUCTIONS:
# 1. Complete the `combine_to_inventory` function.
# 2. Return a dictionary mapping keys to quantities using `zip()`.

keys = ["P101", "P102", "P103"]
quantities = [50, 12, 90]

def combine_to_inventory(item_ids, stock_counts):
    # TODO: Implement using zip()
    return {}

# Test:
# print(combine_to_inventory(keys, quantities)) # Should print {'P101': 50, 'P102': 12, 'P103': 90}