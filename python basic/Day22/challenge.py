"""
============================================================
DAY 22 PROJECT — ORDER PROCESSING SYSTEM
============================================================

Your goal is to build an Order Processing System using pure, modular 
functions. In backend development, views and endpoints should remain 
thin, delegating heavy logic to reusable helper functions.

------------------------------------------------------------
STEP 1: DEFINE MODULAR FUNCTIONS
------------------------------------------------------------
Implement the following independent functions:

1. `validate_order(order_dict)`: 
   - Accepts a dictionary (e.g., `{"items": [{"name": "A", "price": 10, "qty": 2}], "coupon": "SAVE10"}`).
   - Returns True if order is valid (has items, items have positive price/qty). Returns False otherwise.
   
2. `calculate_total(items)`:
   - Sums the subtotal price (price * qty) of all items in the list.
   
3. `apply_discount(subtotal, coupon_code)`:
   - If coupon is "SAVE10", subtract 10% from the subtotal.
   - If coupon is "SAVE20", subtract 20%.
   - Otherwise, return original subtotal.
   
4. `calculate_tax(amount, tax_rate=0.13)`:
   - Multiplies amount by tax_rate (default 13% VAT).
   
5. `format_order_summary(order_dict, final_total)`:
   - Returns a string summarizing order details.

------------------------------------------------------------
STEP 2: PIPELINE ORCHESTRATOR
------------------------------------------------------------
Write a main orchestrator function `process_order_pipeline(order_dict)` that 
combines all modular functions to run a full processing pipeline:
- Validate -> Calculate subtotal -> Apply discount -> Add tax -> Format summary.

------------------------------------------------------------
STEP 3: ADVANTAGE OF MODULARITY
------------------------------------------------------------
Describe why decoupling this logic into individual functions is better than 
writing one large `process_order()` function containing all the code.

============================================================
MY LOGICAL EVALUATION:
============================================================
Describe your findings here:

____________________________________________________
____________________________________________________


============================================================
MY CODE:
============================================================
Write your modular functions and pipeline orchestrator below:

____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
"""