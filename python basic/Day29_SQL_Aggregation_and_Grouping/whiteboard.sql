/*
============================================================
DAY 29 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: Department Payroll Analytics & Threshold Reporting

In backend data engineering and system design interviews, you will
often be asked to write complex aggregation queries on a whiteboard
to summarize metrics across organizational hierarchies.

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Given a company payroll table `employees` with columns:
  (id, name, department, role, salary, hire_date, is_active)

Write an optimal SQL query that:
1. Filters only active employees (`is_active = TRUE`).
2. Groups the dataset by `department`.
3. Computes:
   - `department`: Name of the department
   - `headcount`: Number of active employees
   - `avg_salary`: Average salary rounded to 2 decimal places
   - `max_salary`: Highest salary in that department
   - `total_payroll`: Total sum of all salaries in that department
4. Filters the aggregated groups (HAVING) to ONLY include departments that:
   - Have at least 3 active employees (`headcount >= 3`)
   - Have an average salary greater than $65,000.00 (`avg_salary > 65000.00`)
5. Sorts the output by `total_payroll DESC`.

------------------------------------------------------------
2. CONSTRAINTS & EXECUTION ORDER:
------------------------------------------------------------
- Pure SQL (compatible with PostgreSQL and SQLite).
- Remember the SQL clause execution order:
  FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY

============================================================
MY APPROACH & QUERY BREAKDOWN:
============================================================
Explain which filter belongs in WHERE vs HAVING:
- WHERE filters: ___________________________________________
- HAVING filters: __________________________________________
- Performance considerations (Indexes): ____________________

============================================================
MY RAW SQL QUERY (Write on blank paper first!):
============================================================

-- TODO: Write your pure SQL aggregation query below:

*/