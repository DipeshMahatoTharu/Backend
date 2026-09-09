/*
============================================================
DAY 31 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: The "Nth Highest Salary" & Department Salary Comparison via CTE

Finding the Nth highest salary is one of the most famous and frequently
asked SQL whiteboard interview questions in tech company screenings.

------------------------------------------------------------
1. PROBLEM STATEMENT 1: Second Highest Salary
------------------------------------------------------------
Given a table `employees` with columns:
  (id, name, department, salary)

Write an optimal SQL query to find the SECOND HIGHEST distinct salary.
If there is no second highest salary (e.g. only 1 employee exists, or all
employees have identical salaries), the query must return NULL.

Note: You CANNOT simply use `ORDER BY salary DESC LIMIT 1 OFFSET 1`
because if the two highest earners both earn $100k, OFFSET 1 will
incorrectly return $100k instead of the second distinct highest salary!

------------------------------------------------------------
2. PROBLEM STATEMENT 2: Department Outperformers (CTE)
------------------------------------------------------------
Write a query using a Common Table Expression (`WITH`) that:
1. Calculates the average salary of each department in a CTE.
2. Joins the CTE back to the employees table.
3. Returns: employee name, department, salary, and the department average salary.
4. Only includes employees whose salary is HIGHER than their department's average.
5. Sorts by department ASC, then (salary - dept_avg) DESC.

============================================================
MY APPROACH (Explain how MAX() with subquery handles duplicates & NULL):
============================================================
Write your explanation here:

____________________________________________________
____________________________________________________
____________________________________________________

============================================================
MY RAW SQL QUERIES (Write on blank paper first!):
============================================================

-- Problem 1: Second Highest Salary (handles duplicates and returns NULL if none)
-- TODO: Write query below:




-- Problem 2: Department Outperformers using CTE (WITH)
-- TODO: Write query below:

*/