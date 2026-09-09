# Day 31 — Subqueries, CTEs & ACID Transactions in Backend Systems

## 🎯 Learning Objectives
- Write scalar, multi-row, and correlated subqueries with `IN`, `EXISTS`, and `NOT EXISTS`.
- Structure complex, multi-stage queries using **Common Table Expressions (CTEs)** (`WITH` syntax).
- Master the **ACID** properties of database transactions: Atomicity, Consistency, Isolation, and Durability.
- Manage atomic workflows using `BEGIN`, `COMMIT`, `ROLLBACK`, and `SAVEPOINT`.
- Prevent double-spending and inventory race conditions using row-level locking (`SELECT FOR UPDATE`).

---

## 📚 Core Backend Concepts

### 1. Subqueries vs Common Table Expressions (CTEs)
A **Subquery** is a query nested inside another query:
```sql
-- Scalar subquery (returns a single value):
SELECT name, price 
FROM products 
WHERE price > (SELECT AVG(price) FROM products);
```

A **CTE (`WITH`)** makes complex SQL clean and readable:
```sql
WITH HighValueCustomers AS (
    SELECT customer_id, SUM(total_amount) AS lifetime_spend
    FROM orders
    GROUP BY customer_id
    HAVING SUM(total_amount) > 1000.00
)
SELECT c.name, c.email, h.lifetime_spend
FROM customers c
JOIN HighValueCustomers h ON c.id = h.customer_id;
```

### 2. `EXISTS` vs `IN`
When checking if related rows exist in large tables, prefer `EXISTS`:
- `IN (SELECT id FROM ...)`: Gathers all IDs into a set in memory first.
- `EXISTS (SELECT 1 FROM ... WHERE ...)`: Short-circuits immediately upon finding the first matching row, resulting in superior performance.

### 3. ACID Transactions: The Backbone of Backend Reliability
Every money transfer, ticket purchase, or order placement requires **Atomicity**:
- **Atomicity**: Either all operations succeed or all are rolled back. No partial state!
- **Consistency**: Database transitions only between valid states conforming to constraints.
- **Isolation**: Concurrent transactions execute as if they were running sequentially.
- **Durability**: Once committed, changes survive server crashes and power loss.

```sql
BEGIN;

-- Step 1: Lock row and deduct balance
UPDATE accounts SET balance = balance - 100.00 WHERE id = 1 AND balance >= 100.00;

-- Step 2: Add balance to recipient
UPDATE accounts SET balance = balance + 100.00 WHERE id = 2;

-- Step 3: Record audit log
INSERT INTO transaction_logs (from_id, to_id, amount) VALUES (1, 2, 100.00);

COMMIT; -- Or ROLLBACK if any step fails!
```

### 4. Preventing Race Conditions: Pessimistic Locking
In high-concurrency ticket sales (e.g., concert tickets with 1 seat remaining):
```sql
-- Acquires an exclusive row lock:
SELECT * FROM seats WHERE id = 50 FOR UPDATE;
-- Other transactions attempting to SELECT ... FOR UPDATE on row 50 will block until COMMIT!
```

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + CONCEPT DRILLS (60 min)**:
  - 40 min: Review CTE syntax, subquery types, ACID transactions, and locking.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/questions.md)**.

- **HOUR 2 — SQL PRACTICE & DEBUGGING (60 min)**:
  - 35 min: Write the subqueries, CTEs, and transaction scripts in **[`practice.sql`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/practice.sql)**.
  - 25 min: Diagnose deadlocks and subquery scalar errors in **[`debugging.py`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/debugging.py)**.

- **HOUR 3 — INTERVIEW & PORTFOLIO CHALLENGE (60 min)**:
  - 20 min: Study transaction isolation levels and race conditions in **[`interview.md`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/interview.md)**.
  - 20 min: Solve the 2nd highest salary challenge on **[`whiteboard.sql`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/whiteboard.sql)**.
  - 20 min: Build the Atomic Bank Transfer Engine in **[`challenge.py`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Read concepts and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/questions.md)**
- [ ] Completed all CTE & transaction tasks in **[`practice.sql`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/practice.sql)**
- [ ] Fixed all bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/debugging.py)**
- [ ] Solved whiteboard challenge in **[`whiteboard.sql`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/whiteboard.sql)**
- [ ] Passed atomic bank transfer tests in **[`challenge.py`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/challenge.py)**
- [ ] Studied backend interview answers in **[`interview.md`](file:///d:/Backend/python%20basic/Day31_SQL_Subqueries_and_Transactions/interview.md)**