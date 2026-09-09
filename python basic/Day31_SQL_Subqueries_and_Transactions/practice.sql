-- =====================================================================
-- Day 31 SQL Practice — Subqueries, CTEs & Transactions
-- =====================================================================

-- Table schema reference:
-- accounts (id, user_name, balance, is_frozen)
-- ledger (id, from_account_id, to_account_id, amount, status, created_at)
-- products (id, name, category, price)
-- orders (id, customer_id, total_amount, status)

-- =====================================================================
-- TASK 1: Correlated Scalar Subquery
-- =====================================================================
-- Write a query to find all products that are priced HIGHER than
-- the AVERAGE price of products in their OWN category.
-- Return: product name, category, price, and category average price.
-- Order by category ASC, price DESC.

-- TODO: Write correlated subquery below:




-- =====================================================================
-- TASK 2: Semi-Join with EXISTS
-- =====================================================================
-- Write a query to find all customers who have placed at least one order
-- with total_amount > 500.00 using the EXISTS operator.
-- (Do not use an INNER JOIN or IN operator).

-- TODO: Write query using EXISTS below:




-- =====================================================================
-- TASK 3: Multi-Stage CTE (Common Table Expression)
-- =====================================================================
-- Using WITH:
-- 1. Create CTE 'CustomerSpend' calculating total spend per customer.
-- 2. Create CTE 'AverageSpend' calculating the average of those customer totals.
-- 3. Final SELECT: Return all customers whose lifetime spend is ABOVE
--    the average customer spend, along with how much above they are.

-- TODO: Write CTE query below:




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


