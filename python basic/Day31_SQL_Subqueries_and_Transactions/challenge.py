"""
============================================================
DAY 31 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: Atomic Bank Balance Transfer & Audit Trail Engine

In fintech and payment backends (Stripe, PayPal, Banks), financial
transfers must satisfy strict ACID properties. If a server crashes
or network drops halfway through a transfer, transactions must ROLLBACK
completely so that money is never lost or magically created.

============================================================
REQUIREMENTS:
============================================================
1. Function `setup_banking_db(conn: sqlite3.Connection)`:
   - Sets up:
     * `accounts` (id INTEGER PRIMARY KEY, owner TEXT, balance REAL CHECK(balance >= 0), is_frozen INTEGER DEFAULT 0)
     * `transfer_ledger` (id INTEGER PRIMARY KEY AUTOINCREMENT, from_id INTEGER, to_id INTEGER,
                         amount REAL, status TEXT, note TEXT, created_at TEXT)
   - Seeds initial accounts:
     * 1: Alice ($1000.00)
     * 2: Bob ($500.00)
     * 3: Charlie ($200.00, is_frozen = 1)

2. Function `execute_atomic_transfer(...) -> tuple[bool, str]`:
   - Parameters:
     * `conn`: sqlite3.Connection
     * `from_id`: int
     * `to_id`: int
     * `amount`: float
     * `simulate_crash`: bool (if True, raises an error right after debiting from_id)

   - Rules:
     * Transaction must be atomic (all operations succeed, or all rollback).
     * Validate both accounts exist.
     * Validate neither account is frozen (`is_frozen == 0`).
     * Validate `amount > 0`.
     * Check that `from_id` has sufficient balance (`balance >= amount`).
     * If `simulate_crash` is True, raise RuntimeError("Simulated network outage mid-transfer").
     * On any error or exception, ensure `conn.rollback()` is executed.
     * On success, debit sender, credit recipient, log to `transfer_ledger`, and `conn.commit()`.
     * Return `(True, "Transfer successful")` or `(False, "<Reason>")`.
"""

import sqlite3
from datetime import datetime
from typing import Any


def setup_banking_db(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            owner TEXT NOT NULL,
            balance REAL NOT NULL CHECK (balance >= 0.0),
            is_frozen INTEGER NOT NULL DEFAULT 0
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transfer_ledger (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_id INTEGER,
            to_id INTEGER,
            amount REAL NOT NULL,
            status TEXT NOT NULL,
            note TEXT,
            created_at TEXT NOT NULL
        );
    """)

    # Seed accounts
    cursor.executemany("""
        INSERT INTO accounts (id, owner, balance, is_frozen) VALUES (?, ?, ?, ?);
    """, [
        (1, 'Alice', 1000.00, 0),
        (2, 'Bob', 500.00, 0),
        (3, 'Charlie (Frozen)', 200.00, 1)
    ])
    conn.commit()


def execute_atomic_transfer(
    conn: sqlite3.Connection,
    from_id: int,
    to_id: int,
    amount: float,
    simulate_crash: bool = False
) -> tuple[bool, str]:
    """
    Executes an ACID-compliant money transfer between two accounts.
    """
    # TODO: Implement atomic transfer logic with try/except/rollback
    pass


def get_account_balances(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute("SELECT id, owner, balance, is_frozen FROM accounts ORDER BY id ASC;")
    return [{"id": r[0], "owner": r[1], "balance": r[2], "is_frozen": r[3]} for r in cursor.fetchall()]


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    print("Testing Atomic Bank Transfer Engine...")
    conn = sqlite3.connect(":memory:")
    # Disable autocommit to manually manage transactions
    conn.isolation_level = None
    setup_banking_db(conn)

    print("\nInitial Balances:")
    print(get_account_balances(conn))

    # Test 1: Successful transfer ($200 Alice -> Bob)
    success, msg = execute_atomic_transfer(conn, from_id=1, to_id=2, amount=200.00)
    print(f"\nTest 1 (Valid Transfer): {success} - {msg}")
    print("Balances:", get_account_balances(conn))

    # Test 2: Transfer to frozen account (Should reject without balance change)
    success, msg = execute_atomic_transfer(conn, from_id=1, to_id=3, amount=50.00)
    print(f"\nTest 2 (Frozen Account): {success} - {msg}")
    print("Balances:", get_account_balances(conn))

    # Test 3: Insufficient balance ($5000 Alice -> Bob)
    success, msg = execute_atomic_transfer(conn, from_id=1, to_id=2, amount=5000.00)
    print(f"\nTest 3 (Insufficient Funds): {success} - {msg}")
    print("Balances:", get_account_balances(conn))

    # Test 4: Crash simulation (Atomicity test)
    # Alice attempts to transfer $300 to Bob, but system crashes midway!
    try:
        success, msg = execute_atomic_transfer(conn, from_id=1, to_id=2, amount=300.00, simulate_crash=True)
    except Exception as e:
        print(f"\nTest 4 (Simulated Crash Caught): {e}")
    print("Balances after crash rollback (Alice should still have $800, NOT $500!):")
    print(get_account_balances(conn))

    conn.close()
    print("\nBanking transaction tests complete.")