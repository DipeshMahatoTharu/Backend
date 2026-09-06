"""
============================================================
DAY 27 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: Relational Database Schema Builder & Constraint Validator

Using Python's built-in `sqlite3` engine, build an automated script
that executes your DDL schema and verifies that all relational
integrity rules (Primary Keys, Foreign Keys, Unique, and Check constraints)
properly reject invalid backend transactions.

============================================================
REQUIREMENTS:
============================================================
1. Implement `setup_database(conn)`:
   - Enable Foreign Keys in SQLite: `conn.execute("PRAGMA foreign_keys = ON;")`.
   - Create tables:
     * `users` (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL)
     * `categories` (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL)
     * `products` (id INTEGER PRIMARY KEY AUTOINCREMENT, category_id INTEGER, name TEXT NOT NULL,
                  price REAL NOT NULL CHECK(price >= 0), stock INTEGER NOT NULL DEFAULT 0 CHECK(stock >= 0),
                  FOREIGN KEY(category_id) REFERENCES categories(id) ON DELETE SET NULL)
     * `orders` (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL,
                status TEXT CHECK(status IN ('PENDING', 'PAID', 'SHIPPED')),
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE)

2. Implement test functions:
   - `test_duplicate_email_rejected(conn)`: Asserts `sqlite3.IntegrityError` on duplicate user email.
   - `test_negative_price_rejected(conn)`: Asserts `sqlite3.IntegrityError` on price < 0.
   - `test_invalid_foreign_key_rejected(conn)`: Asserts `sqlite3.IntegrityError` when creating an order for user_id 9999.
   - `test_cascade_delete(conn)`: Verifies that deleting a user deletes their corresponding orders.
"""

import sqlite3


def setup_database(conn: sqlite3.Connection) -> None:
    """Executes the DDL schema to set up tables and constraint checks."""
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # TODO: Write CREATE TABLE statements for users, categories, products, orders
    pass


def test_duplicate_email_rejected(conn: sqlite3.Connection) -> bool:
    """Returns True if duplicate email raises IntegrityError, False otherwise."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email) VALUES ('u1', 'test@test.com');")
    try:
        cursor.execute("INSERT INTO users (username, email) VALUES ('u2', 'test@test.com');")
        return False # Should have failed!
    except sqlite3.IntegrityError:
        return True


def test_negative_price_rejected(conn: sqlite3.Connection) -> bool:
    """Returns True if price < 0 raises IntegrityError, False otherwise."""
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO products (name, price, stock) VALUES ('Invalid Item', -10.50, 5);")
        return False
    except sqlite3.IntegrityError:
        return True


def test_invalid_foreign_key_rejected(conn: sqlite3.Connection) -> bool:
    """Returns True if referencing non-existent user raises IntegrityError."""
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO orders (user_id, status) VALUES (9999, 'PENDING');")
        return False
    except sqlite3.IntegrityError:
        return True


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    print("Testing Relational Database Schema & Constraints...")
    conn = sqlite3.connect(":memory:")
    
    setup_database(conn)
    print("Schema setup completed.")
    
    # Run tests
    print(f"Duplicate Email Check: {test_duplicate_email_rejected(conn)}")
    print(f"Negative Price Check: {test_negative_price_rejected(conn)}")
    print(f"Foreign Key Integrity Check: {test_invalid_foreign_key_rejected(conn)}")
    
    conn.close()
    print("Database test run complete.")