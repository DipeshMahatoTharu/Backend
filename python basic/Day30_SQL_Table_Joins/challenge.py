"""
============================================================
DAY 30 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: Multi-Vendor Order Fulfillment & Shipping Manifest Relational Query Engine

In multi-tenant e-commerce platforms (Amazon, Shopify), a single customer
order may contain items supplied by multiple independent vendors. The backend
must join across Vendors, Products, Orders, Customers, and OrderItems
to generate individual fulfillment shipping manifests for each supplier.

============================================================
REQUIREMENTS:
============================================================
1. Function `setup_fulfillment_db(conn: sqlite3.Connection)`:
   - Creates normalized tables:
     * `vendors` (id INTEGER PRIMARY KEY, name TEXT, email TEXT)
     * `products` (id INTEGER PRIMARY KEY, vendor_id INTEGER, name TEXT, sku TEXT, price REAL,
                  FOREIGN KEY(vendor_id) REFERENCES vendors(id))
     * `customers` (id INTEGER PRIMARY KEY, full_name TEXT, address TEXT)
     * `orders` (id INTEGER PRIMARY KEY, customer_id INTEGER, order_date TEXT, status TEXT,
                FOREIGN KEY(customer_id) REFERENCES customers(id))
     * `order_items` (id INTEGER PRIMARY KEY, order_id INTEGER, product_id INTEGER, quantity INTEGER, price_at_purchase REAL,
                     FOREIGN KEY(order_id) REFERENCES orders(id),
                     FOREIGN KEY(product_id) REFERENCES products(id))
   - Seeds sample multi-vendor data.

2. Function `generate_vendor_manifest(conn: sqlite3.Connection, vendor_id: int) -> list[dict]`:
   - Returns all items supplied by `vendor_id` across 'PAID' or 'SHIPPED' orders.
   - Requires joining: orders -> order_items -> products -> customers.
   - Dict format per item:
     {
         "order_id": int,
         "order_date": str,
         "customer_name": str,
         "shipping_address": str,
         "product_name": str,
         "sku": str,
         "quantity": int,
         "line_total": float (quantity * price_at_purchase)
     }

3. Function `get_vendor_revenue_leaderboard(conn: sqlite3.Connection) -> list[dict]`:
   - Uses LEFT JOINs from `vendors` to calculate total revenue and total units sold.
   - Must include vendors with 0 sales (revenue = $0.00).
   - Ordered by total revenue descending.
"""

import sqlite3
from typing import Any


def setup_fulfillment_db(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vendor_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            sku TEXT NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (vendor_id) REFERENCES vendors(id)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            address TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price_at_purchase REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
    """)

    # Seed data
    cursor.executemany("INSERT INTO vendors (id, name, email) VALUES (?, ?, ?);", [
        (1, 'Keychron Official', 'orders@keychron.com'),
        (2, 'Logitech Direct', 'b2b@logitech.com'),
        (3, 'Inactive Vendor LLC', 'contact@inactive.com') # 0 products sold
    ])

    cursor.executemany("INSERT INTO products (id, vendor_id, name, sku, price) VALUES (?, ?, ?, ?, ?);", [
        (101, 1, 'Keychron Q1 Pro', 'KC-Q1P', 199.00),
        (102, 1, 'Custom Keycap Set', 'KC-CAPS', 45.00),
        (103, 2, 'MX Master 3S Mouse', 'LOGI-MX3S', 99.00),
        (104, 3, 'Old Mousepad', 'PAD-OLD', 10.00)
    ])

    cursor.executemany("INSERT INTO customers (id, full_name, address) VALUES (?, ?, ?);", [
        (1, 'Dipesh Tharu', 'Kathmandu, Nepal'),
        (2, 'Anjali Sharma', 'Lalitpur, Nepal')
    ])

    cursor.executemany("INSERT INTO orders (id, customer_id, order_date, status) VALUES (?, ?, ?, ?);", [
        (1001, 1, '2026-09-08', 'PAID'),
        (1002, 2, '2026-09-09', 'PAID')
    ])

    cursor.executemany("""
        INSERT INTO order_items (order_id, product_id, quantity, price_at_purchase)
        VALUES (?, ?, ?, ?);
    """, [
        (1001, 101, 1, 199.00),  # Order 1001: 1 Keychron keyboard (Vendor 1)
        (1001, 103, 1, 99.00),   # Order 1001: 1 Logitech mouse (Vendor 2)
        (1002, 101, 2, 195.00),  # Order 1002: 2 Keychron keyboards (Vendor 1)
        (1002, 102, 1, 45.00)    # Order 1002: 1 Keycap set (Vendor 1)
    ])
    conn.commit()


def generate_vendor_manifest(conn: sqlite3.Connection, vendor_id: int) -> list[dict[str, Any]]:
    """Joins 4 tables to produce a vendor shipment manifest."""
    cursor = conn.cursor()
    # TODO: Write 4-table join returning shipping manifest items for vendor_id
    pass


def get_vendor_revenue_leaderboard(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    """Aggregates revenue per vendor, including vendors with 0 sales."""
    cursor = conn.cursor()
    # TODO: Write LEFT JOIN query calculating total revenue per vendor
    pass


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    print("Testing Multi-Vendor Fulfillment Engine...")
    conn = sqlite3.connect(":memory:")
    setup_fulfillment_db(conn)
    print("Database schema and orders initialized.")

    manifest = generate_vendor_manifest(conn, vendor_id=1)
    print("\nFulfillment Manifest for 'Keychron Official':")
    for item in (manifest or []):
        print(f"  Order #{item['order_id']} -> Ship to {item['customer_name']} at {item['shipping_address']}")
        print(f"    Item: {item['product_name']} ({item['sku']}) x{item['quantity']} = ${item['line_total']}")

    leaderboard = get_vendor_revenue_leaderboard(conn)
    print("\nVendor Revenue Leaderboard:")
    for v in (leaderboard or []):
        print(f"  Vendor: {v['vendor_name']} | Units Sold: {v['units_sold']} | Total Revenue: ${v['total_revenue']}")

    conn.close()
    print("\nFulfillment tests complete.")