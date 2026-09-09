-- =====================================================================
-- Day 29 SQL Practice — Aggregations, GROUP BY & HAVING
-- =====================================================================

-- Table schema reference:
-- CREATE TABLE products (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(150),
--     category VARCHAR(50),
--     price NUMERIC(10, 2),
--     stock INT,
--     is_available BOOLEAN
-- );

-- =====================================================================
-- TASK 1: Global Summary Statistics
-- =====================================================================
-- Compute the overall catalog summary:
-- 1. Total number of products as 'total_products'
-- 2. Average price rounded to 2 decimal places as 'avg_price'
-- 3. Minimum price as 'min_price'
-- 4. Maximum price as 'max_price'
-- 5. Total inventory units in stock as 'total_units'

-- TODO: Write SELECT query below:




-- =====================================================================
-- TASK 2: Category-Level Aggregation & Inventory Value
-- =====================================================================
-- Group the products table by 'category' and compute:
-- 1. Category name
-- 2. Total products in that category
-- 3. Average price of products in that category
-- 4. Total warehouse value for that category: SUM(price * stock)
-- Filter out products where stock = 0 BEFORE aggregating.
-- Order by total warehouse value descending.

-- TODO: Write category aggregation query below:




-- =====================================================================
-- TASK 3: Filtering Groups with HAVING
-- =====================================================================
-- Find all categories that meet BOTH of the following conditions:
-- 1. Has MORE than 2 distinct products (COUNT(*) > 2)
-- 2. Has an average product price GREATER than $50.00
-- Order results by average price descending.

-- TODO: Write query using GROUP BY and HAVING below:




-- =====================================================================
-- TASK 4: Multi-Column Grouping
-- =====================================================================
-- Group products by BOTH 'category' AND 'is_available'.
-- Compute: category, is_available, product count, and total stock.
-- Order by category ASC, is_available DESC.

-- TODO: Write multi-column grouping query below:




-- =====================================================================
-- TASK 5: Monthly Order & Revenue Analytics
-- =====================================================================
-- Given an 'orders' table (id, customer_id, order_date, total_amount, status):
-- Write a query to report monthly performance for COMPLETED orders:
-- 1. Month formatted as 'YYYY-MM' (SQLite: strftime('%Y-%m', order_date), Postgres: TO_CHAR(order_date, 'YYYY-MM'))
-- 2. Total order count
-- 3. Total gross revenue
-- 4. Average order value (AOV) rounded to 2 decimal places
-- Filter only status = 'COMPLETED'.
-- Order chronologically by month ascending.

-- TODO: Write monthly analytics query below:


