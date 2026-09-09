# Day 30 — SQL Table Joins Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 30.1 `ON` vs `WHERE` in a `LEFT JOIN`
**QUESTION:**
Explain with an example why placing a condition like `AND orders.created_at >= '2026-01-01'` in the `ON` clause yields a fundamentally different result than placing `WHERE orders.created_at >= '2026-01-01'` in a `LEFT JOIN` query.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 30.2 The Cartesian Product (Cross Join Disaster)
**QUESTION:**
1. What is a Cartesian Product, and under what circumstances does SQL execute one?
2. If Table A has 100,000 rows and Table B has 100,000 rows, how many rows does an accidental Cartesian Product produce?
3. What impact does this have on CPU, memory, and database connection pools in production?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 30.3 Self-Joins & Hierarchical Data
**QUESTION:**
1. What is a Self-Join?
2. Why is a `LEFT JOIN` almost always preferred over an `INNER JOIN` when querying self-referencing tables like `employees` with a `manager_id` column (think about the CEO/top-level executive)?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 30.4 Missing Indexes on Foreign Key Columns
**QUESTION:**
In relational databases like PostgreSQL and MySQL, primary key columns are automatically indexed by default. Are Foreign Key columns automatically indexed? What happens to join performance when joining a 10-million-row `order_items` table on `order_id` if no index was created on `order_items(order_id)`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 30.5 The One-to-Many Join Duplicate Trap
**QUESTION:**
Suppose one customer has 3 orders. If you run:
`SELECT c.id, c.name, o.id FROM customers c JOIN orders o ON c.id = o.customer_id;`
Why does the customer's name appear 3 times in the result set? If you add `SUM(c.account_balance)` to this query, explain why the balance is incorrectly tripled and how you prevent this math error.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________