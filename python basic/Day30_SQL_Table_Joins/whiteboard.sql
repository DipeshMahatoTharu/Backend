/*
============================================================
DAY 30 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: Multi-Table Customer Purchase Summary (LEFT JOIN + Aggregation)

In backend engineering interviews, candidates are frequently asked
to write a comprehensive query that joins multiple tables to generate
a customer order overview without losing customers who have no orders
or duplicating aggregation counts.

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Given a relational schema:
- `customers` (id, name, email, country)
- `orders` (id, customer_id, order_date, status)
- `order_items` (id, order_id, product_id, quantity, unit_price)

Write an optimal SQL query that:
1. Filters customers from country = 'Nepal'.
2. Performs a LEFT JOIN to their orders and order_items.
3. Groups by customer id, name, and email.
4. Calculates:
   - `customer_id`
   - `customer_name`
   - `total_orders`: Count of distinct orders placed (must be 0 if no orders)
   - `total_items_bought`: Sum of all items purchased across all orders (0 if none)
   - `total_expenditure`: Sum of (quantity * unit_price) rounded to 2 decimals ($0.00 if none)
5. Sorts the output by `total_expenditure DESC`, then `customer_name ASC`.

------------------------------------------------------------
2. CONSTRAINTS & CRITICAL TRAPS:
------------------------------------------------------------
- You MUST use `COUNT(DISTINCT orders.id)` because joining order_items
  duplicates the order row!
- You MUST use `COALESCE(..., 0)` so that customers with 0 orders do not display NULL.

============================================================
MY APPROACH & JOIN STRATEGY:
============================================================
Explain your join path and why COUNT(DISTINCT) is required:

____________________________________________________
____________________________________________________
____________________________________________________

============================================================
MY RAW SQL QUERY (Write on blank paper first!):
============================================================

-- TODO: Write your pure SQL multi-table join query below:

*/