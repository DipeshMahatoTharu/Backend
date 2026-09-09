-- =====================================================================
-- Day 30 SQL Practice — Relational Table Joins
-- =====================================================================

-- Table schema reference:
-- customers (id, name, email, country)
-- orders (id, customer_id, order_date, total_amount, status)
-- order_items (id, order_id, product_id, quantity, unit_price)
-- products (id, name, category, price)
-- employees (id, name, role, manager_id)

-- =====================================================================
-- TASK 1: Standard INNER JOIN
-- =====================================================================
-- Write an INNER JOIN between 'customers' and 'orders':
-- Return: customer name, email, order id, order date, and total amount.
-- Only include orders with status = 'COMPLETED'.
-- Order by order_date DESC.

-- TODO: Write INNER JOIN query below:




-- =====================================================================
-- TASK 2: Detecting Unmatched Records (LEFT JOIN + IS NULL)
-- =====================================================================
-- In marketing, finding registered users who have NEVER made a purchase
-- is essential for re-engagement campaigns.
-- Write a LEFT JOIN to return the name and email of all customers
-- who have 0 associated orders in the orders table.

-- TODO: Write LEFT JOIN query below:




-- =====================================================================
-- TASK 3: 4-Table Itemized Receipt Join
-- =====================================================================
-- Write a query joining:
-- customers -> orders -> order_items -> products
-- Return:
-- 1. customer name
-- 2. order id
-- 3. product name
-- 4. quantity purchased
-- 5. unit_price charged
-- 6. line total: (quantity * unit_price)
-- Filter for order id = 1001.

-- TODO: Write 4-table join query below:




-- =====================================================================
-- TASK 4: Self-Join for Organizational Hierarchy
-- =====================================================================
-- In the 'employees' table, each employee has a 'manager_id' that
-- references the 'id' of another employee in the same table.
-- Write a query that returns:
-- 1. employee name as 'employee'
-- 2. employee role as 'role'
-- 3. manager's name as 'reports_to' (or 'TOP EXECUTIVE' if manager_id is NULL)
-- Use a LEFT JOIN so employees without managers (CEOs) are not excluded!

-- TODO: Write Self-Join query below:




-- =====================================================================
-- TASK 5: Aggregation over LEFT JOIN with COALESCE
-- =====================================================================
-- Generate a sales leaderboard listing EVERY customer:
-- Return: customer name, country, total orders placed, and total gross spend.
-- Customers who have placed 0 orders must show total spend as $0.00 (use COALESCE).
-- Order by total gross spend descending.

-- TODO: Write aggregated LEFT JOIN query below:


