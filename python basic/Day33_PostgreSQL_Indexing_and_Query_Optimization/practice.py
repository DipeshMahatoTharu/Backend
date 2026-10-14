"""
============================================================
DAY 33 PRACTICE — POSTGRESQL & SQL INDEXING BENCHMARKS
============================================================

Learn how indexes transform full-table scans into instant O(log N) searches.
We will profile queries using EXPLAIN QUERY PLAN and measure actual execution times.
"""

import sqlite3
import time
import random
import string

def setup_benchmark_db(conn: sqlite3.Connection, num_records: int = 50000):
    """Creates a sample database table and populates it with realistic records."""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS customers;")
    cursor.execute("""
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            country TEXT NOT NULL,
            status TEXT NOT NULL,
            account_balance REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    print(f"[*] Seeding {num_records} records for indexing benchmarks...")
    first_names = ["James", "Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "Dipesh", "Aarav"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Miller", "Wilson", "Mahato", "Sharma", "Patel"]
    countries = ["NP", "US", "UK", "IN", "CA", "AU", "DE"]
    statuses = ["ACTIVE", "PENDING", "SUSPENDED", "CLOSED"]
    
    records = []
    for i in range(num_records):
        fn = random.choice(first_names)
        ln = random.choice(last_names)
        email = f"{fn.lower()}.{ln.lower()}{i}@example.com"
        country = random.choice(countries)
        status = random.choice(statuses)
        balance = round(random.uniform(10.0, 50000.0), 2)
        records.append((fn, ln, email, country, status, balance))
        
    cursor.executemany("""
        INSERT INTO customers (first_name, last_name, email, country, status, account_balance)
        VALUES (?, ?, ?, ?, ?, ?);
    """, records)
    conn.commit()
    print("[+] Seeding complete!\n")


# =====================================================================
# TASK 1: Measure Unindexed Query (Sequential Scan)
# =====================================================================
def profile_unindexed_email_search(conn: sqlite3.Connection, target_email: str):
    """
    INSTRUCTIONS:
    1. Run EXPLAIN QUERY PLAN on `SELECT * FROM customers WHERE email = ?`
    2. Measure the exact execution time in milliseconds over 10 iterations.
    3. Return the execution plan text and average execution time in ms.
    """
    cursor = conn.cursor()
    
    # 1. Inspect Query Plan
    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM customers WHERE email = ?", (target_email,))
    plan = cursor.fetchall()
    
    # 2. Measure Execution Time
    start = time.perf_counter()
    for _ in range(10):
        cursor.execute("SELECT * FROM customers WHERE email = ?", (target_email,))
        _ = cursor.fetchone()
    elapsed_ms = (time.perf_counter() - start) / 10 * 1000
    
    return plan, elapsed_ms


# =====================================================================
# TASK 2: Create B-Tree Index & Benchmark the Improvement
# =====================================================================
def create_email_index_and_benchmark(conn: sqlite3.Connection, target_email: str):
    """
    INSTRUCTIONS:
    1. Create a B-Tree index on `email`: `CREATE INDEX idx_customers_email ON customers (email);`
    2. Re-run EXPLAIN QUERY PLAN to verify the database switched to an INDEX SCAN / SEARCH.
    3. Measure the execution time over 10 iterations and compare with Task 1.
    """
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_customers_email ON customers (email);")
    conn.commit()
    
    # Check plan
    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM customers WHERE email = ?", (target_email,))
    plan = cursor.fetchall()
    
    # Measure
    start = time.perf_counter()
    for _ in range(10):
        cursor.execute("SELECT * FROM customers WHERE email = ?", (target_email,))
        _ = cursor.fetchone()
    elapsed_ms = (time.perf_counter() - start) / 10 * 1000
    
    return plan, elapsed_ms


# =====================================================================
# TASK 3: Composite Index (Country + Status) & Leftmost Prefix Rule
# =====================================================================
def demonstrate_composite_index(conn: sqlite3.Connection):
    """
    INSTRUCTIONS:
    1. Create a composite index: `CREATE INDEX idx_cust_country_status ON customers (country, status);`
    2. Check the query plan for `WHERE country = 'NP' AND status = 'ACTIVE'`.
    3. Check the query plan for `WHERE status = 'ACTIVE'` (Bypassing leftmost column).
    """
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_cust_country_status ON customers (country, status);")
    conn.commit()
    
    # Both columns (uses composite index)
    cursor.execute("EXPLAIN QUERY PLAN SELECT id FROM customers WHERE country = 'NP' AND status = 'ACTIVE';")
    plan_both = cursor.fetchall()
    
    # Only status (skips leftmost column - causes scan!)
    cursor.execute("EXPLAIN QUERY PLAN SELECT id FROM customers WHERE status = 'ACTIVE';")
    plan_skipped_leftmost = cursor.fetchall()
    
    return plan_both, plan_skipped_leftmost


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    setup_benchmark_db(conn, num_records=20000)
    
    test_email = "dipesh.mahato1000@example.com"
    
    print("--- 1. UNINDEXED SEARCH ---")
    plan_raw, time_raw = profile_unindexed_email_search(conn, test_email)
    print(f"Plan: {plan_raw}")
    print(f"Avg Time: {time_raw:.4f} ms\n")
    
    print("--- 2. INDEXED SEARCH (B-TREE) ---")
    plan_idx, time_idx = create_email_index_and_benchmark(conn, test_email)
    print(f"Plan: {plan_idx}")
    print(f"Avg Time: {time_idx:.4f} ms")
    print(f"Speedup Factor: {time_raw / max(time_idx, 0.0001):.1f}x FASTER!\n")
    
    print("--- 3. COMPOSITE INDEX & LEFTMOST PREFIX RULE ---")
    plan_both, plan_skip = demonstrate_composite_index(conn)
    print(f"Plan with (country, status): {plan_both}")
    print(f"Plan with (status only):     {plan_skip}")
    conn.close()
