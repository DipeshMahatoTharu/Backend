# Day 29 — SQL Aggregations, Grouping & Analytical Reporting

## 🎯 Learning Objectives
- Master SQL aggregate functions: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, and `MAX()`.
- Group dataset rows into summarized analytical buckets using `GROUP BY`.
- Understand the critical distinction between pre-aggregation row filtering (`WHERE`) and post-aggregation group filtering (`HAVING`).
- Learn how `NULL` values affect aggregate computations (e.g., `COUNT(*)` vs `COUNT(column)`).
- Write production-grade financial reporting and metric aggregation queries.

---

## 📚 Core Backend Concepts

### 1. Aggregate Functions & NULL Semantics
Aggregate functions collapse multiple rows into a single summary value:
- `COUNT(*)`: Counts all rows in the group, regardless of whether columns contain `NULL`.
- `COUNT(column)`: Counts only rows where `column` is **NOT NULL**.
- `AVG(column)`: Computes the sum divided by the number of non-NULL rows.
  * *Warning*: If salaries are `[100, 200, NULL]`, `AVG(salary)` is `(100 + 200) / 2 = 150`, **NOT** `100`! If you want NULLs treated as zero, use `AVG(COALESCE(salary, 0))`.

### 2. The `GROUP BY` Rule
Every column present in your `SELECT` list must either:
1. Be enclosed inside an aggregate function (`SUM`, `COUNT`, etc.), OR
2. Be explicitly listed in the `GROUP BY` clause.

```sql
-- CORRECT:
SELECT department, role, COUNT(*), ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department, role;
```

### 3. `WHERE` vs `HAVING`
This is one of the most tested questions in backend interviews:
- **`WHERE`**: Evaluates individual rows **BEFORE** grouping. Cannot reference aggregate functions like `SUM()`.
- **`HAVING`**: Evaluates summarized groups **AFTER** aggregation. Used to filter based on aggregated metrics.

```sql
SELECT department, AVG(salary) AS avg_sal
FROM employees
WHERE status = 'ACTIVE'               -- 1. Filters rows first
GROUP BY department
HAVING AVG(salary) > 80000.00;        -- 2. Filters grouped results second
```

### 4. SQL Logical Execution Order
To master complex queries, memorize how the database engine executes SQL clauses:
1. `FROM` (and `JOIN`)
2. `WHERE`
3. `GROUP BY`
4. `HAVING`
5. `SELECT`
6. `ORDER BY`
7. `LIMIT` / `OFFSET`

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + CONCEPT DRILLS (60 min)**:
  - 40 min: Review aggregate mechanics, NULL behavior, and `WHERE` vs `HAVING`.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/questions.md)**.

- **HOUR 2 — SQL PRACTICE & DEBUGGING (60 min)**:
  - 35 min: Write the aggregation queries in **[`practice.sql`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/practice.sql)**.
  - 25 min: Diagnose grouping bugs and misuse of aggregates in **[`debugging.py`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/debugging.py)**.

- **HOUR 3 — INTERVIEW & PORTFOLIO CHALLENGE (60 min)**:
  - 20 min: Study PostgreSQL MVCC `COUNT(*)` bottlenecks in **[`interview.md`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/interview.md)**.
  - 20 min: Write the department salary whiteboard query on **[`whiteboard.sql`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/whiteboard.sql)**.
  - 20 min: Build the Financial Revenue & CLV Analytics Engine in **[`challenge.py`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Read concepts and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/questions.md)**
- [ ] Completed all aggregation tasks in **[`practice.sql`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/practice.sql)**
- [ ] Fixed all bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/debugging.py)**
- [ ] Solved whiteboard challenge in **[`whiteboard.sql`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/whiteboard.sql)**
- [ ] Passed revenue analytics tests in **[`challenge.py`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/challenge.py)**
- [ ] Studied backend interview answers in **[`interview.md`](file:///d:/Backend/python%20basic/Day29_SQL_Aggregation_and_Grouping/interview.md)**