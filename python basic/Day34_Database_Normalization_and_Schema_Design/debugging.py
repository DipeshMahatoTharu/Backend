"""
============================================================
DAY 34 DEBUGGING — ORPHAN ROWS & ACCIDENTAL CASCADE WIPES
============================================================

Diagnose and prevent two of the most dangerous database bugs:
1. Accidental CASCADE deletions destroying historical audit trails.
2. Orphaned records created by missing foreign key constraints.
"""

import sqlite3

def demonstrate_cascade_disaster():
    """
    BUG SCENARIO 1:
    A junior developer configured `ON DELETE CASCADE` between users and payments.
    When a user requested account deactivation, the admin ran `DELETE FROM users WHERE id = 1`.
    PostgreSQL deleted all financial transaction records for that user,
    destroying tax compliance records and violating accounting laws!
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Broken schema:
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("""
        CREATE TABLE payments (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            amount REAL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE -- DANGEROUS!
        );
    """)
    cursor.execute("INSERT INTO users VALUES (1, 'Alice');")
    cursor.execute("INSERT INTO payments VALUES (101, 1, 500.0), (102, 1, 1200.0);")
    conn.commit()
    
    # Deleting user wipes financial records!
    cursor.execute("DELETE FROM users WHERE id = 1;")
    conn.commit()
    
    cursor.execute("SELECT COUNT(*) FROM payments;")
    count = cursor.fetchone()[0]
    conn.close()
    return count  # Returns 0 - All financial records vanished!

def fixed_financial_schema():
    """
    CORRECTED SCENARIO:
    In financial/e-commerce systems:
    1. Payments should use `ON DELETE RESTRICT` (or Django `models.PROTECT`).
    2. Users should NEVER be hard-deleted; use soft deletes (`is_active = FALSE`).
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, is_active INTEGER DEFAULT 1);")
    cursor.execute("""
        CREATE TABLE payments (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE RESTRICT
        );
    """)
    cursor.execute("INSERT INTO users VALUES (1, 'Alice', 1);")
    cursor.execute("INSERT INTO payments VALUES (101, 1, 500.0);")
    conn.commit()
    
    # Attempting to delete user will raise an IntegrityError:
    try:
        cursor.execute("DELETE FROM users WHERE id = 1;")
        conn.commit()
    except sqlite3.IntegrityError as e:
        status = f"Successfully protected financial record! Error caught: {e}"
        
    conn.close()
    return status

if __name__ == "__main__":
    wiped_count = demonstrate_cascade_disaster()
    print(f"Danger of CASCADE: Remaining payments = {wiped_count} (Audit trail destroyed!)")
    protection_result = fixed_financial_schema()
    print(protection_result)
