# Day 33 — PostgreSQL Indexing Conceptual Questions

Please answer each question thoroughly in the spaces provided below.

---

### 33.1 The Internal Mechanics of B-Tree Indexes
**QUESTION:**
Explain the internal tree architecture of a standard PostgreSQL B-Tree index. Why is search complexity $O(\log N)$, and how does the doubly-linked list at the leaf level accelerate `BETWEEN` and `ORDER BY` SQL queries?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 33.2 Sequential Scan vs Index Scan vs Index-Only Scan
**QUESTION:**
In PostgreSQL query plans:
1. What is the fundamental difference between an **Index Scan** and an **Index-Only Scan**?
2. What role does the PostgreSQL **Visibility Map** play in determining whether an Index-Only Scan must touch the heap table pages?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 33.3 The Leftmost Prefix Rule on Composite Indexes
**QUESTION:**
Suppose a table has a composite index on columns `(company_id, department_id, created_at)`.
1. Will a query with `WHERE department_id = 12` use this index efficiently? Why or why not?
2. How should you order columns in a composite index for optimal performance when one column is filtered by equality (`=`) and another column is filtered by range (`>` or `BETWEEN`)?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 33.4 Expression / Functional Indexes vs Function Calls in WHERE Clauses
**QUESTION:**
Why does the query `SELECT * FROM users WHERE LOWER(email) = 'john@example.com';` cause a Sequential Scan even if there is an index on `email`? How does creating a functional index `ON users (LOWER(email))` fix this?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 33.5 Partial Indexes & Write Overhead
**QUESTION:**
1. What is a **Partial Index**, and in what real-world backend scenario does it save significant disk space and RAM?
2. Why is adding an index on every single column considered a severe anti-pattern in high-throughput write-heavy OLTP databases?

**MY ANSWER:**
____________________________________________________
____________________________________________________
