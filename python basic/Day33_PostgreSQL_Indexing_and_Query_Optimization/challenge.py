"""
============================================================
DAY 33 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: High-Throughput Database Query Profiler & Index Advisor

In production backends, database administrators (DBAs) and senior backend engineers
monitor query logs to detect "Slow Queries" and automatically recommend missing indexes.

Your challenge is to build a Python class `DatabaseIndexAdvisor` that:
1. Profiles a suite of query workloads against unindexed tables.
2. Identifies sequential scans (`SCAN`).
3. Recommends and applies targeted indexes.
4. Validates that the execution plan changes from `SCAN` to `SEARCH USING INDEX`.
5. Quantifies performance speedup percentages.
"""

import sqlite3
import time
from typing import List, Tuple, Dict, Any

class DatabaseIndexAdvisor:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def inspect_query_plan(self, query: str, params: tuple = ()) -> List[str]:
        """Runs EXPLAIN QUERY PLAN and returns formatted plan details."""
        cursor = self.conn.cursor()
        cursor.execute(f"EXPLAIN QUERY PLAN {query}", params)
        rows = cursor.fetchall()
        return [row[3] for row in rows]

    def has_sequential_scan(self, query: str, params: tuple = ()) -> bool:
        """Returns True if the query plan contains a sequential SCAN."""
        plan_steps = self.inspect_query_plan(query, params)
        return any("SCAN" in step and "USING INDEX" not in step for step in plan_steps)

    def benchmark_query_ms(self, query: str, params: tuple = (), iterations: int = 5) -> float:
        """Measures average execution duration in milliseconds."""
        cursor = self.conn.cursor()
        start = time.perf_counter()
        for _ in range(iterations):
            cursor.execute(query, params)
            _ = cursor.fetchall()
        return ((time.perf_counter() - start) / iterations) * 1000

    def recommend_index(self, table_name: str, columns: List[str], index_name: str) -> None:
        """Creates an index on the specified table and columns."""
        cols_str = ", ".join(columns)
        sql = f"CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({cols_str});"
        self.conn.execute(sql)
        self.conn.commit()


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
    
    # Seed 10,000 products
    products = [(f"SKU-{i}", "ELECTRONICS" if i % 2 == 0 else "BOOKS", i * 1.5, i % 100) for i in range(10000)]
    cursor.executemany("INSERT INTO products (sku, category, price, stock) VALUES (?, ?, ?, ?);", products)
    conn.commit()
    
    advisor = DatabaseIndexAdvisor(conn)
    query = "SELECT * FROM products WHERE sku = ?;"
    params = ("SKU-8500",)
    
    # 1. Before indexing
    is_slow_before = advisor.has_sequential_scan(query, params)
    time_before = advisor.benchmark_query_ms(query, params)
    print(f"[*] Before Indexing:")
    print(f"    Sequential Scan Detected: {is_slow_before}")
    print(f"    Execution Time: {time_before:.4f} ms")
    print(f"    Plan: {advisor.inspect_query_plan(query, params)}")
    
    # 2. Apply Recommendation
    advisor.recommend_index("products", ["sku"], "idx_products_sku")
    
    # 3. After indexing
    is_slow_after = advisor.has_sequential_scan(query, params)
    time_after = advisor.benchmark_query_ms(query, params)
    print(f"\n[+] After Indexing (B-Tree):")
    print(f"    Sequential Scan Detected: {is_slow_after}")
    print(f"    Execution Time: {time_after:.4f} ms")
    print(f"    Plan: {advisor.inspect_query_plan(query, params)}")
    print(f"    Speedup: {time_before / max(time_after, 0.0001):.1f}x faster!")
    
    conn.close()

if __name__ == "__main__":
    run_advisor_demonstration()
