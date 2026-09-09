# Day 29 Debugging — Aggregate Misuse, HAVING traps & NULLs

import sqlite3

# =====================================================================
# BUGGY SCENARIO 1: Aggregates in the WHERE Clause
# =====================================================================
# Goal: Find departments with total budget expenditure greater than $100,000.
# Problem: The developer put SUM(salary) inside the WHERE clause!
# SQLite/PostgreSQL crashes immediately with:
# `sqlite3.OperationalError: misuse of aggregate function SUM()`

def buggy_get_high_budget_depts(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # CRASH: Aggregates are not evaluated yet during the WHERE phase!
    cursor.execute("""
        SELECT department, SUM(salary) 
        FROM employees 
        WHERE SUM(salary) > 100000 
        GROUP BY department;
    """)
    return cursor.fetchall()

# ---------------------------------------------------------------------
# QUESTION: Why cannot aggregate functions be evaluated in the WHERE clause?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the query using the correct HAVING clause.
# ---------------------------------------------------------------------
def fixed_get_high_budget_depts(conn: sqlite3.Connection):
    pass


# =====================================================================
# BUGGY SCENARIO 2: Non-Aggregated Column in SELECT
# =====================================================================
# Goal: Find the highest paid employee in each department.
# Problem: The developer selected `name` along with `MAX(salary)` and
# grouped only by `department`.
# In PostgreSQL, this query is rejected with `column employees.name must appear in the GROUP BY clause`.
# In SQLite, it returns an arbitrary, non-deterministic employee name!

def buggy_get_top_earner_per_dept(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # BUG: Non-deterministic row returned for 'name'!
    cursor.execute("""
        SELECT department, name, MAX(salary)
        FROM employees
        GROUP BY department;
    """)
    return cursor.fetchall()

# ---------------------------------------------------------------------
# QUESTION: How does a window function (e.g. ROW_NUMBER()) or subquery solve this?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite using a subquery to guarantee the correct matching employee name.
# ---------------------------------------------------------------------
def fixed_get_top_earner_per_dept(conn: sqlite3.Connection):
    pass


# =====================================================================
# BUGGY SCENARIO 3: Distorted Average by Ignoring NULLs
# =====================================================================
# Goal: Calculate the average commission per sales agent across a 5-person team.
# Two agents earned $1000 and $2000. Three agents earned $0 (stored as NULL).
# Expected team average: (1000 + 2000 + 0 + 0 + 0) / 5 = $600.00.
# Problem: AVG(commission) completely ignores NULLs, calculating:
# (1000 + 2000) / 2 = $1500.00! The company reports false financial metrics.

def buggy_calculate_avg_commission(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # BUG: SQL AVG() drops NULL rows from both numerator and denominator!
    cursor.execute("SELECT AVG(commission) FROM sales_agents;")
    return cursor.fetchone()[0]

# ---------------------------------------------------------------------
# QUESTION: How does COALESCE(commission, 0) correct the computation?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite using COALESCE to include zero-commission agents in the average.
# ---------------------------------------------------------------------
def fixed_calculate_avg_commission(conn: sqlite3.Connection):
    pass