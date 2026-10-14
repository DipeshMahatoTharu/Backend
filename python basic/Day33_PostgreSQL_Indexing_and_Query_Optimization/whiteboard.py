"""
============================================================
DAY 33 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Senior Database Architect — E-Commerce Index Design

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
You are the Lead Backend Engineer for an e-commerce platform with 10 million orders.
Your database dashboard reveals that the customer order history API endpoint
is timing out under peak traffic:

SLOW QUERY:
SELECT id, order_number, total_amount, created_at
FROM orders
WHERE customer_id = 48291
  AND status = 'COMPLETED'
ORDER BY created_at DESC
LIMIT 20;

Currently, the only index on `orders` is the PRIMARY KEY (`id`).

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
1. Propose the exact optimal composite index DDL to make this query run in < 2ms.
2. Explain the exact order of columns in your composite index and justify it 
   using the equality-first rule and sorting behavior.
3. Explain whether this index allows PostgreSQL to avoid an in-memory Sort (Sort Key / Top-N Heapsort).
4. Implement a Python demonstration class `OrderQueryOptimizer` that creates the table,
   adds the optimal index, and verifies the query plan avoids temporary sorting.

------------------------------------------------------------
MY APPROACH & JUSTIFICATION:
------------------------------------------------------------
Write your explanation here:
1. Optimal Index:
   CREATE INDEX idx_orders_customer_status_created 
   ON orders (customer_id, status, created_at DESC);

2. Justification:
   - `customer_id = ?` (Equality) filters to a tiny subset of orders.
   - `status = ?` (Equality) further narrows matching rows.
   - `created_at DESC` allows the B-Tree index to be read directly in descending order,
     eliminating the expensive `filesort` / `Sort: Top-N Heapsort` step!
   - Including `id`, `order_number`, `total_amount` in an `INCLUDE` clause (Covering Index)
     or letting PostgreSQL fetch them from heap allows instant response.

============================================================
MY CODE:
============================================================
"""

import sqlite3

class OrderQueryOptimizer:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def setup_schema(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                order_number TEXT NOT NULL,
                status TEXT NOT NULL,
                total_amount REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.conn.commit()

    def apply_optimal_index(self):
        cursor = self.conn.cursor()
        # Equality columns first, then range/sorting column:
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_orders_cust_status_date
            ON orders (customer_id, status, created_at DESC);
        """)
        self.conn.commit()

    def get_query_plan(self, customer_id: int, status: str):
        cursor = self.conn.cursor()
        cursor.execute("""
            EXPLAIN QUERY PLAN
            SELECT id, order_number, total_amount, created_at
            FROM orders
            WHERE customer_id = ? AND status = ?
            ORDER BY created_at DESC
            LIMIT 20;
        """, (customer_id, status))
        return cursor.fetchall()


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    optimizer = OrderQueryOptimizer(conn)
    optimizer.setup_schema()
    optimizer.apply_optimal_index()
    plan = optimizer.get_query_plan(48291, "COMPLETED")
    print("Optimal Execution Plan:")
    for step in plan:
        print("  ->", step)
    conn.close()
