"""
============================================================
DAY 33 DEBUGGING — INDEX INVALIDATION & QUERY TRAPS
============================================================

Learn to identify and fix silent bugs where indexes exist in the schema,
but PostgreSQL/SQL engines are forced to ignore them and do full table scans!
"""

import sqlite3

def setup_debugging_db(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            signup_year INTEGER NOT NULL,
            is_active INTEGER NOT NULL DEFAULT 1
        );
    """)
    # Add index on email
    cursor.execute("CREATE INDEX idx_users_email ON users (email);")
    # Add index on signup_year
    cursor.execute("CREATE INDEX idx_users_year ON users (signup_year);")
    conn.commit()


# =====================================================================
# BUGGY SCENARIO 1: The Function-Wrapping Index Invalidation
# =====================================================================
# Problem: You want a case-insensitive search for users by email.
# The table has 5 million rows and an index on `email`.
# But this query takes 3,500ms and maxes out the CPU! Why?
def buggy_case_insensitive_search(conn: sqlite3.Connection, search_email: str):
    cursor = conn.cursor()
    # BUG: Wrapping the indexed column inside LOWER() prevents the database
    # from using `idx_users_email` because the index stores original case values!
    cursor.execute("""
        SELECT id, username, email 
        FROM users 
        WHERE LOWER(email) = LOWER(?);
    """, (search_email,))
    return cursor.fetchall()

# ---------------------------------------------------------------------
# QUESTION: Why does applying a function like LOWER(), DATE(), or YEAR()
# on an indexed column disable normal B-Tree index lookup?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED SOLUTION:
# In PostgreSQL, you solve this by creating an EXPRESSION / FUNCTIONAL INDEX:
# CREATE INDEX idx_users_lower_email ON users (LOWER(email));
# Or by ensuring emails are normalized (lowercased) prior to database insertion.
# ---------------------------------------------------------------------
def fixed_case_insensitive_setup(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # In SQLite / PostgreSQL, create an expression index on LOWER(email)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_lower_email ON users (LOWER(email));")
    conn.commit()


# =====================================================================
# BUGGY SCENARIO 2: Implicit Type Coercion Invalidation
# =====================================================================
# Problem: In PostgreSQL, phone_number is VARCHAR(20) and indexed.
# A junior developer queries:
# SELECT * FROM users WHERE phone_number = 9860793587; (Passed as an INTEGER!)
# PostgreSQL coerces phone_number into numeric for every row, triggering a SEQ SCAN!
def explain_type_coercion_trap():
    """
    Returns an architectural explanation of why datatype mismatches 
    cause silent query plan degradations in Python/PostgreSQL drivers.
    """
    explanation = (
        "In PostgreSQL, comparing a VARCHAR column to an INTEGER forces PostgreSQL to "
        "cast every row in the table to numeric: CAST(phone_number AS numeric) = 9860793587. "
        "Because the cast is applied per row, the B-Tree index on VARCHAR cannot be traversed, "
        "resulting in a 100% Sequential Scan. Always pass parameters with matching Python types!"
    )
    return explanation


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    setup_debugging_db(conn)
    fixed_case_insensitive_setup(conn)
    
    cursor = conn.cursor()
    cursor.execute("EXPLAIN QUERY PLAN SELECT id FROM users WHERE LOWER(email) = 'test@example.com';")
    plan = cursor.fetchall()
    print("Plan using Expression Index:", plan)
    print("\nType Coercion Lesson:\n", explain_type_coercion_trap())
    conn.close()
