# Day 32 Debugging — Connection Pool Leaks, Dirty Connections & Driver Bugs

import sqlite3

# =====================================================================
# BUGGY SCENARIO 1: The Connection Pool Leak
# =====================================================================
# Goal: Query user settings from a connection pool.
# Problem: The developer called `pool.putconn(conn)` only at the end of
# the function. If an error occurs during parsing or query execution,
# the function exits, and the connection is NEVER returned to the pool!
# After 10 exceptions, the pool is completely exhausted, taking down the API.

class MockConnectionPool:
    def __init__(self): 
        self.active = 0
        
    def getconn(self): 
        self.active += 1; 
        return sqlite3.connect(":memory:")
    
    def putconn(self, conn): 
        self.active -= 1;
        conn.close()

def buggy_fetch_profile(pool: MockConnectionPool, user_id: int):
    conn = pool.getconn()
    try:
        cursor = conn.cursor()
        # If this query or following code crashes with an error:
        cursor.execute("SELECT * FROM non_existent_table WHERE id = ?;", (user_id,))
        data = cursor.fetchone()
        
    # NEVER REACHED ON ERROR!
    finally:
        pool.putconn(conn)
    return data

# ---------------------------------------------------------------------
# QUESTION: Why is a `try...finally` block mandatory when managing pool checkouts?
# MY ANSWER:
# A try...finally block ensures that the database connection is
# returned to the pool even if an error occurs during query execution
# or processing. Without finally, the connection might not be returned,
# causing connection leaks and eventually exhausting the connection pool.


# =====================================================================
# BUGGY SCENARIO 2: Returning a "Dirty" Uncommitted Connection to the Pool
# =====================================================================
# Goal: Update customer billing plan.
# Problem: The transaction executed an UPDATE statement, encountered a validation
# error, and returned the connection to the pool WITHOUT calling `conn.rollback()`.
# The next web request that checks out this connection inherits an open, uncommitted
# transaction holding locks from the previous customer's request!

def buggy_update_subscription(conn: sqlite3.Connection, customer_id: int, new_plan: str):
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET plan = ? WHERE id = ?;", (new_plan, customer_id))
    
    # Validation error occurs
    if new_plan == "INVALID_PLAN":
        # Returning without rollback!
        conn.rollback()
        return False
        
    
    conn.commit()
    return True

# ---------------------------------------------------------------------
# QUESTION: Why must pool managers always call `rollback()` before putting
# a connection back into the available pool?
#
# MY ANSWER:
# rollback() undoes uncommitted changes when a transaction fails.
# This prevents unwanted changes from being saved and helps ensure
# that a connection is not reused with an unfinished transaction.


# =====================================================================
# BUGGY SCENARIO 3: Direct Driver SQL Injection Trap
# =====================================================================
# Goal: Search users by email.
# Problem: Developer used Python `%` string formatting instead of driver parameter tuple.
# `cur.execute("SELECT * FROM users WHERE email = '%s'" % email)` formats the string
# in Python BEFORE sending to PostgreSQL, creating a massive SQL injection hole!

def buggy_search_by_email(conn: sqlite3.Connection, user_input_email: str):
    cursor = conn.cursor()
    # VULNERABLE: Python string interpolation instead of driver parameterization!
    cursor.execute("SELECT * FROM users WHERE email = '%s'" % user_input_email)
    return cursor.fetchall()

# ---------------------------------------------------------------------
# QUESTION: What is the syntax difference between Python string `%` formatting
# and database driver parameterized tuples?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite using proper driver parameterized placeholders.
# ---------------------------------------------------------------------
def fixed_search_by_email(conn: sqlite3.Connection, user_input_email: str):
    pass