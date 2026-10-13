-- Active: 1791819057946@@127.0.0.1@3306
    -- =====================================================================
    -- Day 31 SQL Practice — Subqueries, CTEs & Transactions
    -- =====================================================================

    -- Table schema reference:
    -- accounts (id, user_name, balance, is_frozen)
    -- ledger (id, from_account_id, to_account_id, amount, status, created_at)
    -- products (id, name, category, price)
    -- orders (id, customer_id, total_amount, status)

-- ==========================================
-- TABLE 1: products
-- ==========================================
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(100),
    price DECIMAL(10, 2)
);

-- ==========================================
-- TABLE 2: accounts
-- ==========================================
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    user_name VARCHAR(100),
    balance DECIMAL(10, 2),
    is_frozen BOOLEAN
);

-- ==========================================
-- TABLE 3: ledger
-- ==========================================
CREATE TABLE ledger (
    id INTEGER PRIMARY KEY,
    from_account_id INTEGER,
    to_account_id INTEGER,
    amount DECIMAL(10, 2),
    status VARCHAR(30),
    created_at TIMESTAMP
);

-- ==========================================
-- TABLE 4: orders
-- ==========================================
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total_amount DECIMAL(10, 2),
    status VARCHAR(30)
);



-- PRODUCTS
INSERT INTO products (id, name, category, price) VALUES
(1, 'Keyboard', 'Accessories', 80),
(2, 'Mouse', 'Accessories', 40),
(3, 'Headphones', 'Accessories', 120),
(4, 'Laptop', 'Electronics', 1200),
(5, 'Monitor', 'Electronics', 300),
(6, 'Webcam', 'Electronics', 100),
(7, 'Novel', 'Books', 20),
(8, 'SQL Guide', 'Books', 50),
(9, 'Python Guide', 'Books', 80);

-- ACCOUNTS
INSERT INTO accounts (id, user_name, balance, is_frozen) VALUES
(1, 'Ram', 500, FALSE),
(2, 'Sita', 1200, FALSE),
(3, 'Hari', 100, TRUE),
(4, 'Gita', 800, FALSE);

-- LEDGER
INSERT INTO ledger
(id, from_account_id, to_account_id, amount, status, created_at)
VALUES
(1, 1, 2, 100, 'COMPLETED', '2026-10-12 09:00:00'),
(2, 2, 4, 200, 'COMPLETED', '2026-10-12 10:00:00'),
(3, 1, 3, 50, 'PENDING',   '2026-10-12 11:00:00'),
(4, 4, 1, 75, 'COMPLETED', '2026-10-12 12:00:00'),
(5, 3, 2, 150, 'COMPLETED', '2026-10-12 13:00:00');

-- ORDERS
INSERT INTO orders (id, customer_id, total_amount, status) VALUES
(1, 101, 500, 'PAID'),
(2, 102, 1200, 'PAID'),
(3, 101, 300, 'PENDING'),
(4, 103, 800, 'PAID'),
(5, 104, 200, 'CANCELLED'),
(6, 102, 600, 'PAID');
    -- =====================================================================
    -- TASK 1: Correlated Scalar Subquery
    -- =====================================================================
    -- Write a query to find all products that are priced HIGHER than
    -- the AVERAGE price of products in their OWN category.
    -- Return: product name, category, price, and category average price.
    -- Order by category ASC, price DESC.

    -- TODO: Write correlated subquery below:

SELECT name,category,price, (
    SELECT
    AVG(price)
    FROM products as p2
    WHERE p2.category=products.category
) AS category_average_price

FROM products
ORDER BY category,price DESC;



-- =====================================================================
-- TASK 2: Semi-Join with EXISTS
-- =====================================================================
-- Write a query to find all customers who have placed at least one order
-- with total_amount > 500.00 using the EXISTS operator.
-- (Do not use an INNER JOIN or IN operator).

-- TODO: Write query using EXISTS below:

SELECT  a.id 
FROM accounts AS a
WHERE EXISTS(
    SELECT o.id 
    FROM orders AS o
    WHERE o.customer_id=a.id
)



-- =====================================================================
-- TASK 3: Multi-Stage CTE (Common Table Expression)
-- =====================================================================
-- Using WITH:
-- 1. Create CTE 'CustomerSpend' calculating total spend per customer.
-- 2. Create CTE 'AverageSpend' calculating the average of those customer totals.
-- 3. Final SELECT: Return all customers whose lifetime spend is ABOVE
--    the average customer spend, along with how much above they are.

-- TODO: Write CTE query below:
WITH CustomerSpend AS(
    SELECT customer_id,
    SUM(total_amount) AS lifetime_spend
    FROM orders
    GROUP BY customer_id
),
AverageSpend AS(
    SELECT AVG(lifetime_spend) AS customers_total
    FROM CustomerSpend

)
SELECT * FROM AverageSpend;

-- =====================================================================
-- TASK 4: Safe Bank Transfer Transaction Script
-- =====================================================================
-- Write a complete transaction script that safely transfers $150.00
-- from Account 1 (Alice) to Account 2 (Bob):
-- 1. START the transaction.
-- 2. Debit Account 1 by $150.00 ONLY if Account 1 balance >= $150.00 and is_frozen = FALSE.
-- 3. Credit Account 2 by $150.00 ONLY if is_frozen = FALSE.
-- 4. Insert an audit record into the 'ledger' table.
-- 5. COMMIT the transaction.

-- TODO: Write transaction script below:




-- =====================================================================
-- TASK 5: Rollback and Savepoint
-- =====================================================================
-- Write a script demonstrating SAVEPOINT:
-- 1. BEGIN transaction.
-- 2. Insert temporary record into ledger.
-- 3. Create SAVEPOINT sp1.
-- 4. Try updating an invalid account balance.
-- 5. ROLLBACK TO SAVEPOINT sp1.
-- 6. COMMIT valid initial state.

-- TODO: Write SAVEPOINT script below:


