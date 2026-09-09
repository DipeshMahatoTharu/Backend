"""
============================================================
DAY 29 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: Financial Revenue & Customer Lifetime Value Analytics Reporter

In SaaS and E-Commerce backends, engineering teams write aggregated
SQL queries to feed executive business intelligence dashboards,
track monthly recurring revenue (MRR), and rank VIP customer cohorts.

============================================================
REQUIREMENTS:
============================================================
1. Function `setup_analytics_db(conn: sqlite3.Connection)`:
   - Sets up:
     * `customers` (id INTEGER PRIMARY KEY, name TEXT, tier TEXT)
     * `orders` (id INTEGER PRIMARY KEY, customer_id INTEGER, order_date TEXT,
                total_amount REAL, status TEXT,
                FOREIGN KEY(customer_id) REFERENCES customers(id))
   - Seeds sample customer records and orders across multiple months.

2. Function `get_monthly_revenue_report(conn: sqlite3.Connection) -> list[dict]`:
   - Returns monthly aggregated performance for 'COMPLETED' orders.
   - Output dictionary per row:
     {
         "month": str ("YYYY-MM"),
         "completed_orders": int,
         "total_revenue": float (rounded to 2 decimals),
         "average_order_value": float (rounded to 2 decimals)
     }
   - Group by month using `strftime('%Y-%m', order_date)`.
   - Ordered by month ascending.

3. Function `get_customer_ltv_report(conn: sqlite3.Connection, min_spend: float = 200.0) -> list[dict]`:
   - Groups orders by customer to calculate Customer Lifetime Value (LTV).
   - Only includes customers whose total completed spend >= min_spend (using `HAVING`).
   - Output dictionary per row:
     {
         "customer_id": int,
         "customer_name": str,
         "tier": str,
         "lifetime_spend": float,
         "order_count": int
     }
   - Ordered by lifetime_spend descending.
"""

import sqlite3
from typing import Any


def setup_analytics_db(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            tier TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            total_amount REAL NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );
    """)

    customers = [
        (1, 'Alice Enterprise', 'GOLD'),
        (2, 'Bob Retail', 'SILVER'),
        (3, 'Charlie Dev', 'BRONZE'),
        (4, 'Diana Startup', 'GOLD')
    ]
    cursor.executemany("INSERT INTO customers (id, name, tier) VALUES (?, ?, ?);", customers)

    orders = [
        (1, '2026-07-15', 500.00, 'COMPLETED'),
        (1, '2026-07-20', 350.00, 'COMPLETED'),
        (2, '2026-07-25', 120.00, 'COMPLETED'),
        (3, '2026-07-28', 50.00, 'CANCELLED'),  # Should be ignored in revenue
        (1, '2026-08-05', 800.00, 'COMPLETED'),
        (2, '2026-08-10', 95.00, 'COMPLETED'),
        (4, '2026-08-18', 1200.00, 'COMPLETED'),
        (3, '2026-09-01', 75.00, 'COMPLETED'),
        (4, '2026-09-02', 450.00, 'COMPLETED')
    ]
    cursor.executemany("""
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (?, ?, ?, ?);
    """, orders)
    conn.commit()


def get_monthly_revenue_report(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    """Generates monthly completed revenue aggregations."""
    cursor = conn.cursor()
    # TODO: Implement SELECT with strftime('%Y-%m', order_date), COUNT, SUM, AVG
    # Filter WHERE status = 'COMPLETED'
    # GROUP BY month ORDER BY month ASC
    pass


def get_customer_ltv_report(conn: sqlite3.Connection, min_spend: float = 200.0) -> list[dict[str, Any]]:
    """Calculates customer lifetime value using GROUP BY and HAVING."""
    cursor = conn.cursor()
    # TODO: Join customers and orders, GROUP BY customer, filter HAVING SUM(total_amount) >= min_spend
    # ORDER BY lifetime_spend DESC
    pass


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    print("Testing Financial Revenue & LTV Analytics Reporter...")
    conn = sqlite3.connect(":memory:")
    setup_analytics_db(conn)
    print("Database seeded with sample transactions.")

    monthly = get_monthly_revenue_report(conn)
    print("\nMonthly Revenue Breakdown:")
    for m in (monthly or []):
        print(f"  Month: {m['month']} | Orders: {m['completed_orders']} | Revenue: ${m['total_revenue']} | AOV: ${m['average_order_value']}")

    vip = get_customer_ltv_report(conn, min_spend=500.0)
    print("\nVIP Customers (LTV >= $500):")
    for v in (vip or []):
        print(f"  {v['customer_name']} ({v['tier']}): ${v['lifetime_spend']} across {v['order_count']} orders")

    conn.close()
    print("\nAnalytics tests complete.")