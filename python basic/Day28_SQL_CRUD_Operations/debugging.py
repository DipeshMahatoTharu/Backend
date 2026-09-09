# Day 28 Debugging — SQL Injection, Naked Updates & NULL Handling

import sqlite3

# =====================================================================
# BUGGY SCENARIO 1: The Catastrophic "Naked" UPDATE
# =====================================================================
# Goal: Deactivate a single user account with user_id = 42.
# Problem: The developer forgot the WHERE clause!
# Executing this in production deactivates EVERY user in the entire company!

def buggy_deactivate_user(conn: sqlite3.Connection, user_id: int):
    cursor = conn.cursor()
    # DISASTER: Missing WHERE user_id = ?
    cursor.execute("UPDATE users SET is_active = 0;")
    conn.commit()

# ---------------------------------------------------------------------
# QUESTION: How do transactions and WHERE clauses protect against accidental mass-updates?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite with a safe WHERE clause targeting only the specified user_id.
# ---------------------------------------------------------------------
def fixed_deactivate_user(conn: sqlite3.Connection, user_id: int):
    pass


# =====================================================================
# BUGGY SCENARIO 2: SQL Injection via F-Strings
# =====================================================================
# Goal: Find user by username from an HTTP request.
# Problem: The developer formatted the SQL string using an f-string.
# An attacker submits username = "' OR '1'='1" which dumps the entire table,
# or "'; DROP TABLE users; --" which deletes the database!

def buggy_get_user(conn: sqlite3.Connection, username: str):
    cursor = conn.cursor()
    # VULNERABLE: Direct string interpolation of untrusted input!
    query = f"SELECT * FROM users WHERE username = '{username}';"
    cursor.execute(query)
    return cursor.fetchall()

# ---------------------------------------------------------------------
# QUESTION: Why do parameterized queries ('?' or '%s') prevent SQL injection attacks?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite using parameterized placeholders.
# ---------------------------------------------------------------------
def fixed_get_user(conn: sqlite3.Connection, username: str):
    pass


# =====================================================================
# BUGGY SCENARIO 3: The NULL Equality Comparison Trap
# =====================================================================
# Goal: Find all users who have not yet set their profile phone number.
# Problem: The developer wrote `WHERE phone = NULL`.
# In SQL, NULL represents UNKNOWN. UNKNOWN = UNKNOWN is NOT true!
# The query returns 0 rows every time, masking uncompleted user profiles.

def buggy_find_unverified_phones(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # BUG: SQL does not allow equality testing with NULL!
    cursor.execute("SELECT id, username FROM users WHERE phone = NULL;")
    return cursor.fetchall()

# ---------------------------------------------------------------------
# QUESTION: Why must SQL use IS NULL instead of = NULL?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite with proper IS NULL syntax.
# ---------------------------------------------------------------------
def fixed_find_unverified_phones(conn: sqlite3.Connection):
    pass