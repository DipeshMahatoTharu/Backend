# Day 29 — SQL Aggregations & Grouping Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 29.1 `WHERE` vs `HAVING` Mechanics
**QUESTION:**
Explain the exact mechanical and performance differences between `WHERE` and `HAVING`:
1. At what point in the SQL logical query execution pipeline does each run?
2. Why is `SELECT department, SUM(sales) FROM stores WHERE SUM(sales) > 10000 GROUP BY department;` invalid SQL syntax?
3. If a filter can be written in either `WHERE` or `HAVING` (e.g. `WHERE status = 'ACTIVE'`), which one should you always choose and why?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 29.2 `COUNT(*)` vs `COUNT(column)` vs `COUNT(1)`
**QUESTION:**
1. Given a table with 10 rows where 3 rows have `referral_code = NULL`:
   - What does `SELECT COUNT(*) FROM users;` return?
   - What does `SELECT COUNT(referral_code) FROM users;` return?
2. Is `COUNT(1)` faster than `COUNT(*)` in modern PostgreSQL or MySQL? Explain how query optimizers treat them.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 29.3 Non-Aggregated Columns in `SELECT`
**QUESTION:**
Explain why the following query causes an error in standard SQL (or non-deterministic output in older MySQL versions):
```sql
SELECT department, employee_name, MAX(salary)
FROM employees
GROUP BY department;
```
If you want to find the highest-paid employee's name in each department, what technique (window function or subquery) should you use?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 29.4 Handling `NULL` in `AVG()` and `SUM()`
**QUESTION:**
Suppose an employee table has four employees with bonus values: `[500, 1500, NULL, 0]`.
1. What does `SELECT AVG(bonus) FROM employees;` evaluate to?
2. How do you write the query so that employees with `NULL` bonus are treated as 0 for the company-wide average calculation?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 29.5 Window Functions vs `GROUP BY`
**QUESTION:**
What is the primary difference between a `GROUP BY` aggregation and a Window Function (e.g. `SUM(amount) OVER (PARTITION BY user_id)` or `ROW_NUMBER() OVER (...)`) in terms of the number of rows returned?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________