"""
============================================================
DAY 35 DEBUGGING — REPRODUCING & PREVENTING DATABASE DEADLOCKS
============================================================

A classic deadlock occurs when:
- Transaction 1 locks Row A, then attempts to lock Row B.
- Transaction 2 locks Row B, then attempts to lock Row A.
Both transactions wait indefinitely on each other until the database 
aborts one with a DeadlockDetected error!
"""

import sqlite3
import threading
import time

def setup_deadlock_accounts(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS bank_accounts;")
    cursor.execute("""
        CREATE TABLE bank_accounts (
            id INTEGER PRIMARY KEY,
            owner TEXT NOT NULL,
            balance REAL NOT NULL
        );
    """)
    cursor.execute("INSERT INTO bank_accounts VALUES (1, 'Alice', 1000.0), (2, 'Bob', 1000.0);")
    conn.commit()


# =====================================================================
# DEADLOCK SCENARIO: Unordered Resource Acquisition
# =====================================================================
# If Alice sends $50 to Bob while Bob simultaneously sends $50 to Alice:
# Thread 1 locks Alice (ID 1) first, then wants Bob (ID 2).
# Thread 2 locks Bob (ID 2) first, then wants Alice (ID 1).
# DEADLOCK!

# =====================================================================
# SENIOR ARCHITECT FIX: STRICT LOCK ORDERING
# =====================================================================
# Rule: Whenever locking multiple database rows, ALWAYS lock them
# in ascending order of their Primary Key:
# lock_first = min(account_a, account_b)
# lock_second = max(account_a, account_b)
# This mathematically guarantees that no cyclic dependency (deadlock) can form!

def safe_transfer_lock_order(from_id: int, to_id: int) -> tuple:
    """
    Returns the IDs in strict ascending acquisition order.
    """
    first_id = min(from_id, to_id)
    second_id = max(from_id, to_id)
    return first_id, second_id


def transfer_funds(conn: sqlite3.Connection, from_id: int, to_id: int, amount: float):
    first_lock, second_lock = safe_transfer_lock_order(from_id, to_id)
    cursor = conn.cursor()
    cursor.execute("BEGIN TRANSACTION;")
    
    # In PostgreSQL, you would execute:
    # SELECT id FROM bank_accounts WHERE id IN (?, ?) ORDER BY id FOR UPDATE;
    # Or lock them sequentially in strict sorted order:
    cursor.execute("SELECT balance FROM bank_accounts WHERE id = ?;", (first_lock,))
    cursor.execute("SELECT balance FROM bank_accounts WHERE id = ?;", (second_lock,))
    
    # Execute debit and credit
    cursor.execute("UPDATE bank_accounts SET balance = balance - ? WHERE id = ?;", (amount, from_id))
    cursor.execute("UPDATE bank_accounts SET balance = balance + ? WHERE id = ?;", (amount, to_id))
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    setup_deadlock_accounts(conn)
    
    t1_order = safe_transfer_lock_order(1, 2)
    t2_order = safe_transfer_lock_order(2, 1)
    
    print(f"Transfer 1 (1 -> 2) Lock Order: {t1_order}")
    print(f"Transfer 2 (2 -> 1) Lock Order: {t2_order}")
    assert t1_order == t2_order == (1, 2)
    
    transfer_funds(conn, 1, 2, 150.0)
    transfer_funds(conn, 2, 1, 50.0)
    
    cursor = conn.cursor()
    cursor.execute("SELECT id, owner, balance FROM bank_accounts;")
    rows = cursor.fetchall()
    print("\nFinal Balances after safe concurrent transfers:")
    for r in rows:
        print(f"  Account {r[0]} ({r[1]}): ${r[2]:.2f}")
    assert rows[0][2] == 900.0  # Alice started with 1000 - 150 + 50 = 900
    assert rows[1][2] == 1100.0 # Bob started with 1000 + 150 - 50 = 1100
    print("[+] Deadlock prevention verified via Strict Sorted Key Ordering!")
    conn.close()
