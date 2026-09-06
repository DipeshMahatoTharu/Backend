-- =====================================================================
-- Day 27 SQL Practice — DDL, Data Types & Table Constraints
-- =====================================================================

-- TASK 1: Create the 'users' table
-- Requirements:
-- 1. id: Integer, Auto-incrementing Primary Key (SERIAL or AUTO_INCREMENT).
-- 2. username: Variable length string up to 50 characters, must be UNIQUE and NOT NULL.
-- 3. email: Variable length string up to 255 characters, must be UNIQUE and NOT NULL.
-- 4. is_active: Boolean with a default value of TRUE.
-- 5. created_at: Timestamp defaulting to current timestamp.

-- TODO: Write CREATE TABLE users statement below:




-- =====================================================================
-- TASK 2: Create the 'categories' table
-- Requirements:
-- 1. id: Integer, Primary Key.
-- 2. name: VARCHAR(100), UNIQUE, NOT NULL.
-- 3. slug: VARCHAR(100), UNIQUE, NOT NULL.

-- TODO: Write CREATE TABLE categories statement below:




-- =====================================================================
-- TASK 3: Create the 'products' table with Constraints
-- Requirements:
-- 1. id: Integer, Primary Key.
-- 2. category_id: Integer, Foreign Key referencing categories(id) ON DELETE SET NULL.
-- 3. name: VARCHAR(255), NOT NULL.
-- 4. price: DECIMAL(10, 2), NOT NULL, must be greater than or equal to 0.00 (CHECK constraint).
-- 5. stock_quantity: INT, NOT NULL, DEFAULT 0, must be greater than or equal to 0 (CHECK constraint).
-- 6. is_available: BOOLEAN, DEFAULT TRUE.

-- TODO: Write CREATE TABLE products statement below:




-- =====================================================================
-- TASK 4: Create the 'orders' table
-- Requirements:
-- 1. id: Integer, Primary Key.
-- 2. user_id: Integer, Foreign Key referencing users(id) ON DELETE CASCADE.
-- 3. order_status: VARCHAR(20) DEFAULT 'PENDING' CHECK (order_status IN ('PENDING', 'PAID', 'SHIPPED', 'CANCELLED')).
-- 4. total_amount: DECIMAL(12, 2) NOT NULL CHECK (total_amount >= 0.0).
-- 5. order_date: TIMESTAMP DEFAULT CURRENT_TIMESTAMP.

-- TODO: Write CREATE TABLE orders statement below:




-- =====================================================================
-- TASK 5: ALTER TABLE operations
-- Requirements:
-- 1. Add a new column 'phone_number VARCHAR(20)' to the 'users' table.
-- 2. Add a UNIQUE constraint on 'products(name)'.

-- TODO: Write ALTER TABLE statements below:


