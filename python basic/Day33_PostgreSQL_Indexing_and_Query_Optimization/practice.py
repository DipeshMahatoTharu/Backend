"""
============================================================
DAY 33 PRACTICE — POSTGRESQL & SQL INDEXING BENCHMARKS
============================================================

Learn how indexes transform full-table scans into instant O(log N) searches.
You will profile queries using EXPLAIN QUERY PLAN and measure actual execution times.
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
    1. Run EXPLAIN QUERY PLAN on:
       `SELECT * FROM customers WHERE email = ?`
    2. Measure the exact execution time in milliseconds over 10 iterations.
    3. Return a tuple: (plan_results, average_execution_time_ms)

    HINT:
    Use `time.perf_counter()` before and after the 10-iteration loop,
    then compute elapsed time in ms: ((t_end - t_start) / 10) * 1000.
    """
    # TODO: Implement unindexed email search profiling and return (plan, elapsed_ms)
    cursor=conn.cursor()
    
    
    cursor.execute("""
                   EXPLAIN QUERY PLAN
                   SELECT *FROM customers 
                   WHERE email =?
                   
                   
                   
                   """,(target_email,))
    plan_result=cursor.fetchall()
    
    start_time=time.perf_counter()
    for i in range(10):
        cursor.execute("""
                    
                    SELECT * FROM customers 
                    WHERE email=?
                    """,(target_email,))
    
        cursor.fetchone()

    end_time=time.perf_counter()

    avg_time=((end_time-start_time)/10)*1000    
    print(plan_result , avg_time)
    
    return plan_result , avg_time


# conn = sqlite3.connect(":memory:")

# setup_benchmark_db(conn, 50000)

# cursor = conn.cursor()
# cursor.execute("SELECT email FROM customers LIMIT 1")
# target_email = cursor.fetchone()[0]

# plan_result, avg_time = profile_unindexed_email_search(
#     conn, target_email
# )

# print("Query plan:", plan_result)
# print(f"Average execution time: {avg_time:.4f} ms")

# conn.close()
# =====================================================================
# TASK 2: Create B-Tree Index & Benchmark the Improvement
# =====================================================================
def create_email_index_and_benchmark(conn: sqlite3.Connection, target_email: str):
    """
    INSTRUCTIONS:
    1. Create a B-Tree index on `email`:
       `CREATE INDEX IF NOT EXISTS idx_customers_email ON customers (email);`
    2. Commit the change to ensure the index is written to the schema.
    3. Run EXPLAIN QUERY PLAN to verify the database switched to an INDEX SEARCH.
    4. Measure average execution time over 10 iterations and compare with Task 1.
    5. Return a tuple: (plan_results, average_execution_time_ms)

    HINT:
    Execute the CREATE INDEX statement, run `conn.commit()`, and then repeat
    the benchmark loop using the same `time.perf_counter()` measurement approach.
    """
    # TODO: Create index on customers(email) and benchmark the improvement
    cursor=conn.cursor()
    cursor.execute("""
                   
                   CREATE index IF NOT EXISTS idx_customers_email 
                   ON customers(email)
                   """)
    
    conn.commit()
    
    cursor.execute("""  EXPLAIN QUERY PLAN
                           SELECT * FROM customers 
                           WHERE email =?
                           """,(target_email,))
    plan_result=cursor.fetchall()
    
    
    s_time=time.perf_counter()
    for i in range (10):
        cursor.execute("""
                       
                       SELECT * FROM customers 
                       WHERE email =?
                       """,(target_email,))
        cursor.fetchone()
    
    
    e_time = time.perf_counter()

    average_execution_time_ms = ((e_time - s_time) / 10) * 1000
    return plan_result,average_execution_time_ms


# =====================================================================
# TASK 3: Composite Index (Country + Status) & Leftmost Prefix Rule
# =====================================================================
def demonstrate_composite_index(conn: sqlite3.Connection):
    """
    INSTRUCTIONS:
    1. Create a composite index on (country, status):
       `CREATE INDEX IF NOT EXISTS idx_cust_country_status ON customers (country, status);`
    2. Inspect query plan when filtering by both columns:
       `SELECT id FROM customers WHERE country = 'NP' AND status = 'ACTIVE';`
    3. Inspect query plan when filtering ONLY by the second column (violating leftmost prefix):
       `SELECT id FROM customers WHERE status = 'ACTIVE';`
    4. Return a tuple: (plan_both_columns, plan_status_only)

    HINT:
    B-Trees on (A, B) are sorted primarily by A. A query filtering only on B
    cannot jump directly to the target leaf nodes and will revert to a table scan.
    """
    # TODO: Create composite index and inspect both query plans
    cursor=conn.cursor()
    cursor.execute("""
                   CREATE INDEX IF NOT EXISTS idx_cust_country_status
                   ON customers(country,status)
                   """)
    cursor.execute("""
                   EXPLAIN QUERY PLAN
                   SELECT id FROM customers 
                   WHERE country = 'NP' AND status ='ACTIVE'
                   """)
    
    plan_both=cursor.fetchall()
    
    cursor.execute("""
                  EXPLAIN QUERY PLAN
                   SELECT id FROM customers 
                   WHERE status ='ACTIVE'
                   """)
    plan_status=cursor
    
    
    return plan_both ,plan_status
    conn.commit()



if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    setup_benchmark_db(conn, num_records=20000)
    
    test_email = "dipesh.mahato1000@example.com"
    
    print("--- 1. UNINDEXED SEARCH ---")
    res1 = profile_unindexed_email_search(conn, test_email)
    if res1 is None:
        print("[!] Task 1 TODO: Implement profile_unindexed_email_search() to measure sequential scan.\n")
        time_raw = None
    else:
        plan_raw, time_raw = res1
        print(f"[+] Task 1 Plan: {plan_raw}")
        print(f"[+] Task 1 Avg Time: {time_raw:.4f} ms\n")
    
    print("--- 2. INDEXED SEARCH (B-TREE) ---")
    res2 = create_email_index_and_benchmark(conn, test_email)
    if res2 is None:
        print("[!] Task 2 TODO: Implement create_email_index_and_benchmark() to create index and benchmark.\n")
    else:
        plan_idx, time_idx = res2
        print(f"[+] Task 2 Plan: {plan_idx}")
        print(f"[+] Task 2 Avg Time: {time_idx:.4f} ms")
        if time_raw:
            speedup = time_raw / max(time_idx, 0.0001)
            print(f"[+] Speedup Factor: {speedup:.1f}x FASTER!\n")
        else:
            print()
    
    print("--- 3. COMPOSITE INDEX & LEFTMOST PREFIX RULE ---")
    res3 = demonstrate_composite_index(conn)
    if res3 is None:
        print("[!] Task 3 TODO: Implement demonstrate_composite_index() to test composite index prefix rule.\n")
    else:
        plan_both, plan_skip = res3
        print(f"[+] Plan with (country, status): {plan_both}")
        print(f"[+] Plan with (status only):     {plan_skip}\n")
    
    conn.close()
