# Day 31 — Subqueries, CTEs & ACID Transactions Questions

Write your answers in the designated spaces below each question.

---

### 31.1 The 4 ACID Properties in Banking
**QUESTION:**
Explain the 4 ACID properties using an online banking transfer where $100 is transferred from Alice's account to Bob's account:
1. Atomicity: What happens if the server crashes after debiting Alice but before crediting Bob?
2. Consistency: What role do database constraints play?
3. Isolation: What happens if Alice tries to transfer money to Bob and Charlie at the exact same millisecond?
4. Durability: Once the transaction returns "Success", where is the state stored?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 31.2 Subqueries vs CTEs (`WITH` Clause)
**QUESTION:**
1. What is a Common Table Expression (CTE), and how does its syntax compare to nested inline subqueries?
2. When should you choose a CTE over a temporary table?
3. Are CTEs in PostgreSQL 12+ optimized as inline query trees or materialized temporary buffers?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 31.3 `IN` vs `EXISTS` Performance
**QUESTION:**
Why is `WHERE EXISTS (SELECT 1 FROM orders WHERE orders.user_id = users.id)` almost always faster than `WHERE user_id IN (SELECT user_id FROM orders)` on large relational tables? How does NULL in the subquery affect `NOT IN` vs `NOT EXISTS`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 31.4 Transaction Isolation Levels
**QUESTION:**
Explain the 4 ANSI SQL Transaction Isolation Levels from lowest to highest, and identify which anomalies they prevent:
1. Read Uncommitted (Dirty Reads)
2. Read Committed (Non-Repeatable Reads)
3. Repeatable Read (Phantom Reads)
4. Serializable
What is the default isolation level in PostgreSQL?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 31.5 Pessimistic Locking (`SELECT ... FOR UPDATE`)
**QUESTION:**
Explain how a race condition occurs when two concurrent web server threads read `stock = 1`, both check `if stock > 0`, and both execute `stock = stock - 1`. How does `SELECT ... FOR UPDATE` prevent this double-selling bug?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________