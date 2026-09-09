# Day 28 — SQL CRUD Operations Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 28.1 The "Naked" UPDATE / DELETE Disaster
**QUESTION:**
What happens if a backend migration or maintenance script executes `UPDATE users SET is_active = FALSE;` or `DELETE FROM orders;` without a `WHERE` clause? How do production database settings (like MySQL's `sql_safe_updates` or transaction wrappers) prevent accidental catastrophe?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 28.2 SQL Three-Valued Logic & `NULL`
**QUESTION:**
1. Why does `SELECT * FROM users WHERE middle_name = NULL;` always return 0 records, even if there are rows where `middle_name` is null?
2. What is three-valued logic in SQL (TRUE, FALSE, UNKNOWN)?
3. What is the correct syntax to filter for missing or existing optional values?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 28.3 Pattern Matching: `LIKE` vs `ILIKE`
**QUESTION:**
1. What is the difference between `LIKE` and `ILIKE` in PostgreSQL?
2. Explain what the `%` and `_` wildcards represent in SQL pattern matching.
3. Why does searching with a leading wildcard (e.g. `WHERE email LIKE '%@gmail.com'`) prevent the database from using a standard B-tree index?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 28.4 Soft Deletes vs Hard Deletes
**QUESTION:**
What is a "Soft Delete" pattern? Why do enterprise systems (banking, healthcare, SaaS) almost never execute raw `DELETE FROM` statements on core business records? What is the main downside of soft deletes when querying large tables?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 28.5 The "Deep Paging" Problem (`LIMIT` & `OFFSET`)
**QUESTION:**
Suppose a products table contains 10,000,000 rows. Explain why executing:
`SELECT * FROM products ORDER BY id LIMIT 20 OFFSET 5000000;`
is extremely slow and causes high database I/O, even when `id` is an indexed primary key.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________