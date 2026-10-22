"""
============================================================
DAY 33 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: High-Throughput Database Query Profiler & Index Advisor

In production backends, database administrators (DBAs) and senior backend engineers
monitor query logs to detect slow queries and automatically recommend missing indexes.

Your challenge is to implement the `DatabaseIndexAdvisor` class:
1. Profiles query workloads against unindexed tables.
2. Identifies sequential scans (`SCAN`).
3. Recommends and applies targeted indexes.
4. Validates that the execution plan changes from `SCAN` to `SEARCH USING INDEX`.
5. Quantifies performance speedup.
"""

import sqlite3  
import time
from typing import List, Tuple, Dict, Any

class DatabaseIndexAdvisor:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def inspect_query_plan(self, query: str, params: tuple = ()) -> List[str]:
        """
        Runs EXPLAIN QUERY PLAN on the given query and returns plan step details.
        Expected return: A list of string descriptions from the EXPLAIN QUERY PLAN output.
        
        HINT:
        SQLite's EXPLAIN QUERY PLAN returns rows with 4 columns:
        (id, parent, notused, detail). Extract the 'detail' column (index 3).
        """
        # TODO: Execute EXPLAIN QUERY PLAN and return list of detail strings
        cursor=self.conn.cursor()
        cursor.execute("""
                        EXPLAIN QUERY PLAN 
                       
                       """+query,params)
        row=cursor.fetchall()
        self.conn.commit()
        return 
        print(row)

        
        
        raise NotImplementedError("TODO: Implement inspect_query_plan()")

    def has_sequential_scan(self, query: str, params: tuple = ()) -> bool:
        """
        Analyzes the query plan and returns True if an unindexed table scan is present.
        
        HINT:
        Call `self.inspect_query_plan(query, params)` and inspect each step string.
        Look for steps that contain 'SCAN' while not containing 'USING INDEX'.
        """
        # TODO: Determine if the plan contains an unindexed sequential scan
        raise NotImplementedError("TODO: Implement has_sequential_scan()")

    def benchmark_query_ms(self, query: str, params: tuple = (), iterations: int = 5) -> float:
        """
        Measures the average execution time of the query over `iterations` runs in milliseconds.
        
        HINT:
        Record `time.perf_counter()` before and after running the query in a loop,
        fetch the rows inside the loop, and return the average time multiplied by 1000.
        """
        # TODO: Measure average execution duration in milliseconds
        raise NotImplementedError("TODO: Implement benchmark_query_ms()")

    def recommend_index(self, table_name: str, columns: List[str], index_name: str) -> None:
        """
        Creates a B-Tree index on the given table and column list, then commits.
        
        HINT:
        Join the column list with commas and construct:
        `CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({cols_str});`
        Remember to commit using `self.conn.commit()`.
        """
        # TODO: Create the recommended index and commit
        raise NotImplementedError("TODO: Implement recommend_index()")


# =====================================================================
# DEMONSTRATION & TEST HARNESS
# =====================================================================
def run_advisor_demonstration():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            sku TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        );
    """)
    
    print("[*] Seeding 10,000 product records for Index Advisor test...")
    products = [(i, f"SKU-{i:05d}", "ELECTRONICS" if i % 2 == 0 else "BOOKS", i * 1.5, i % 100) for i in range(10000)]
    cursor.executemany("INSERT INTO products (id, sku, category, price, stock) VALUES (?, ?, ?, ?, ?);", products)
    conn.commit()
    print("[+] Seeding complete!\n")
    
    advisor = DatabaseIndexAdvisor(conn)
    query = "SELECT * FROM products WHERE sku = ?;"
    params = ("SKU-08500",)
    
    # 1. Step 1: Query Plan Inspection
    print("--- 1. Testing inspect_query_plan() ---")
    try:
        plan_before = advisor.inspect_query_plan(query, params)
        print(f"[+] Query Plan: {plan_before}")
    except NotImplementedError:
        print("[!] inspect_query_plan() is not implemented yet.\n")
        plan_before = None

    # 2. Step 2: Sequential Scan Detection
    print("--- 2. Testing has_sequential_scan() ---")
    try:
        is_slow = advisor.has_sequential_scan(query, params)
        print(f"[+] Sequential Scan Detected (Expected True): {is_slow}")
    except NotImplementedError:
        print("[!] has_sequential_scan() is not implemented yet.\n")

    # 3. Step 3: Benchmarking
    print("--- 3. Testing benchmark_query_ms() ---")
    try:
        time_before = advisor.benchmark_query_ms(query, params, iterations=10)
        print(f"[+] Execution Time (Before Index): {time_before:.4f} ms")
    except NotImplementedError:
        print("[!] benchmark_query_ms() is not implemented yet.\n")
        time_before = None

    # 4. Step 4: Index Recommendation & Creation
    print("--- 4. Testing recommend_index() ---")
    try:
        advisor.recommend_index("products", ["sku"], "idx_products_sku")
        print("[+] Index recommendation applied: `idx_products_sku` on `products(sku)`")
    except NotImplementedError:
        print("[!] recommend_index() is not implemented yet.\n")

    # 5. Step 5: Verification after Indexing
    print("--- 5. Verifying Query Improvement Post-Index ---")
    try:
        plan_after = advisor.inspect_query_plan(query, params)
        is_slow_after = advisor.has_sequential_scan(query, params)
        time_after = advisor.benchmark_query_ms(query, params, iterations=10)
        
        print(f"[+] New Query Plan: {plan_after}")
        print(f"[+] Sequential Scan Detected (Expected False): {is_slow_after}")
        print(f"[+] Execution Time (After Index): {time_after:.4f} ms")
        if time_before:
            speedup = time_before / max(time_after, 0.0001)
            print(f"[+] Optimization Speedup: {speedup:.1f}x FASTER!")
    except NotImplementedError:
        print("[!] Complete all 4 methods to run the full end-to-end advisor verification.")

    conn.close()

if __name__ == "__main__":
    run_advisor_demonstration()
