-- =====================================================================
-- Day 28 SQL Practice — CRUD Operations, Filters & Pagination
-- =====================================================================

-- Table schema reference:
-- CREATE TABLE products (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(150) NOT NULL,
--     category VARCHAR(50) NOT NULL,
--     price NUMERIC(10, 2) NOT NULL,
--     stock INT NOT NULL DEFAULT 0,
--     is_deleted BOOLEAN DEFAULT FALSE,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- =====================================================================
-- TASK 1: High-Performance Multi-Row Batch INSERT
-- =====================================================================
-- Insert 5 diverse products into the 'products' table in a single SQL statement:
-- 1. 'Logitech MX Master 3', 'Electronics', 99.99, 25
-- 2. 'Keychron Q1 Pro', 'Electronics', 199.00, 10
-- 3. 'Ergonomic Chair', 'Furniture', 350.00, 5
-- 4. 'Standing Desk 60in', 'Furniture', 499.99, 0  (Out of stock)
-- 5. 'Python Cookbook', 'Books', 45.00, 100

-- TODO: Write multi-row INSERT statement below:




-- =====================================================================
-- TASK 2: Complex Filtering with Logical Operators & Ranges
-- =====================================================================
-- Write a SELECT query that returns all products that:
-- 1. Belong to category 'Electronics' OR 'Furniture'
-- 2. Have a price BETWEEN 50.00 AND 400.00
-- 3. Are in stock (stock > 0)
-- 4. Are NOT soft-deleted (is_deleted = FALSE)

-- TODO: Write SELECT query below:




-- =====================================================================
-- TASK 3: Text Search & Sorting
-- =====================================================================
-- Write a SELECT query that searches for products whose name contains
-- 'Pro' (case-insensitive in PostgreSQL using ILIKE, or LIKE '%Pro%' / '%pro%').
-- Order the results by price descending. If prices match, sort by name ascending.

-- TODO: Write text search & sorting query below:




-- =====================================================================
-- TASK 4: Pagination (Limit & Offset)
-- =====================================================================
-- Write a query to fetch the SECOND page of products (Page 2),
-- assuming a page size of 2 items per page.
-- Filter out deleted items, and order by id ASC.

-- TODO: Write pagination query below:




-- =====================================================================
-- TASK 5: Selective UPDATE & Soft Delete
-- =====================================================================
-- 1. Apply an inflation price increase of 5% to all products in 'Electronics'.
-- 2. Soft delete the product with id = 4 by setting is_deleted = TRUE.

-- TODO: Write UPDATE and soft-delete statements below:


