# Day 31 Debugging — Deadlocks, Unhandled Rollbacks & Scalar Subquery Crashes

import sqlite3

# =====================================================================
# BUGGY SCENARIO 1: The Multi-Row Scalar Subquery Crash
# =====================================================================
# Goal: Find all products that have the exact same price as the 'Office Desk'.
# Problem: A new vendor added a second product named 'Office Desk' with a different price.
# The subquery `SELECT price FROM products WHERE name = 'Office Desk'` now returns 2 rows!
# The outer query crashes with `OperationalError: subquery returned more than 1 row`!

def buggy_find_same_price_products(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # BUG: Scalar comparison '=' crashes if subquery returns > 1 row!
    cursor.execute("""
        SELECT id, name, price 
        FROM products 
        WHERE price = (SELECT price FROM products WHERE name = 'Office Desk');
    """)
    return cursor.fetchall()

# ---------------------------------------------------------------------
# QUESTION: Why does scalar comparison '=' fail on multi-row subqueries, and
# how does the 'IN' or 'ANY' operator fix it?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite using the IN operator to safely handle multiple matching items.
# ---------------------------------------------------------------------
def fixed_find_same_price_products(conn: sqlite3.Connection):
    pass


# =====================================================================
# BUGGY SCENARIO 2: Missing ROLLBACK on Python Exceptions
# =====================================================================
# Goal: Debit customer account and generate receipt.
# Problem: If the receipt generation throws an exception, the function exits
# without calling `conn.rollback()`.
# In long-lived connection pools, this connection remains stuck in a dirty
# open transaction state, locking database rows and poisoning subsequent queries!

def buggy_checkout_process(conn: sqlite3.Connection, user_id: int, cost: float):
    cursor = conn.cursor()
    cursor.execute("BEGIN TRANSACTION;")
    cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?;", (cost, user_id))
    
    # Simulate an unforeseen exception (e.g. email service timeout, divide by zero)
    raise ZeroDivisionError("Failed while calculating taxes!")
    
    # COMMIT is never reached, and NO ROLLBACK is in place!
    cursor.execute("COMMIT;")

# ---------------------------------------------------------------------
# QUESTION: How do try/except blocks or context managers guarantee ROLLBACK?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Wrap in try/except/rollback logic to guarantee clean connection rollback.
# ---------------------------------------------------------------------
def fixed_checkout_process(conn: sqlite3.Connection, user_id: int, cost: float):
    pass


# =====================================================================
# BUGGY SCENARIO 3: Deadlock Order Inversion
# =====================================================================
# Scenario: Two concurrent backend workers are executing balance transfers:
# Worker 1: Transfer from Account A (1) to Account B (2).
# Worker 2: Transfer from Account B (2) to Account A (1).
# Worker 1 locks A, waiting for B.
# Worker 2 locks B, waiting for A.
# The database enters a DEADLOCK and must kill one of the transactions!

# ---------------------------------------------------------------------
# QUESTION: What is the universal rule for lock ordering that completely
# eliminates circular deadlocks in financial transfers?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED LOGIC:
# Explain how sorting account IDs (e.g. always lock min(A, B) first, then max(A, B))
# guarantees that deadlocks cannot occur:
# ---------------------------------------------------------------------
def fixed_lock_order_explanation():
    """
    To prevent deadlocks: Always acquire locks in consistent numerical order!
    First lock: min(from_id, to_id)
    Second lock: max(from_id, to_id)
    """
    pass