# Day 27 Debugging — SQL Schema Design & Constraint Violations

import sqlite3

# =====================================================================
# BUGGY SCENARIO 1: Table Creation Order Dependency Bug
# =====================================================================
# Goal: Create a two-table relational database schema for authors and books.
# Problem: The developer ran `CREATE TABLE books` first, which references
# `authors(id)`. Because `authors` does not exist yet, the migration
# crashes with `sqlite3.OperationalError: no such table: main.authors`!

def buggy_create_tables(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # BUG: Referencing authors before authors table exists!
    cursor.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER REFERENCES authors(id)
        );
    """)
    cursor.execute("""
        CREATE TABLE authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)

# ---------------------------------------------------------------------
# QUESTION: Why does table dependency order matter during DDL migrations?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the function in proper dependency order.
# ---------------------------------------------------------------------
def fixed_create_tables(conn: sqlite3.Connection):
    pass


# =====================================================================
# BUGGY SCENARIO 2: Silent Foreign Key Failure in SQLite
# =====================================================================
# Goal: Prevent orders from being created for non-existent users.
# Problem: In SQLite, foreign key enforcement is DISABLED by default!
# Unless `PRAGMA foreign_keys = ON;` is explicitly executed per connection,
# invalid foreign keys are inserted without error, corrupting relational integrity.

def buggy_insert_order(conn: sqlite3.Connection, invalid_user_id: int):
    # Notice: PRAGMA foreign_keys = ON is missing!
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (user_id, status) VALUES (?, 'PENDING');", (invalid_user_id,))
    conn.commit()

# ---------------------------------------------------------------------
# QUESTION: Why must backend frameworks (and SQLite drivers) explicitly
# verify foreign key pragma settings?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite to enable foreign keys and catch the constraint violation.
# ---------------------------------------------------------------------
def fixed_insert_order(conn: sqlite3.Connection, invalid_user_id: int) -> bool:
    pass