# Day 22 Practice — Arguments, Scopes, and Closures

# =====================================================================
# TASK 1: Arbitrary Arguments (*args)
# =====================================================================
# You already know how to pass named arguments. Today we will write
# a utility function that sums an arbitrary list of numbers.
#
# INSTRUCTIONS:
# 1. Complete `calculate_sum` using `*args` to collect input numbers.
# 2. Return the sum of all arguments. If no numbers are passed, return 0.0.

def calculate_sum(*args):
    # TODO: Implement this using args tuple loop
    total =0.0 
    for num in args:
        total =total + num
    return total
    
# Test:
print(calculate_sum(1, 2, 3, 4)) # Should print 10.0
print(calculate_sum()) # Should print 0.0


# =====================================================================
# TASK 2: Enclosing Scope & closures
# =====================================================================
# Today we learn how to preserve state using nested function closures.
#
# INSTRUCTIONS:
# 1. Complete the `make_counter` outer function.
# 2. Declare a local variable `count` initialized to 0.
# 3. Inside, define a nested function `increment` that uses the `nonlocal` 
#    keyword to update `count` by 1 on every invocation.
# 4. Return the inner `increment` function object.

def make_counter():
   
    count=0
    
    def increment():
        # TODO: Declare nonlocal count and update it
        nonlocal count
        count +=1
        return count
        
    return increment

# Test:
counter = make_counter()
print(counter()) # Should print 1
print(counter()) # Should print 2


# =====================================================================
# TASK 3: Functions as Arguments (Higher-Order Functions)
# =====================================================================
# In backend APIs, you might apply different pricing strategies dynamically.
#
# INSTRUCTIONS:
# 1. Complete `apply_pricing_strategy` which accepts a raw price and a strategy function.
# 2. Apply the strategy function to the price and return the result.

def discount_strategy(price):
    return price * 0.9 # 10% off

def tax_strategy(price):
    return price * 1.13 # 13% tax

def apply_pricing_strategy(price, strategy_func):
    return strategy_func(price)

# Test:
print(apply_pricing_strategy(100.0, discount_strategy)) # Should print 90.0
print(apply_pricing_strategy(100.0, tax_strategy)) # Should print 113.0