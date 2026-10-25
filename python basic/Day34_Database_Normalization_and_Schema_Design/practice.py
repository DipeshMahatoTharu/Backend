"""
============================================================
DAY 34 PRACTICE — SCHEMA NORMALIZATION & REFACTORING
============================================================

Transform a horribly denormalized, redundant "Spaghetti Table" into 
clean, strict 3NF Relational Tables with Foreign Key integrity.
"""

import sqlite3

def setup_unnormalized_table(conn: sqlite3.Connection):
    """Creates a broken, unnormalized single-table design."""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS legacy_sales_dump;")
    cursor.execute("""
        CREATE TABLE legacy_sales_dump (
            sale_id INTEGER PRIMARY KEY,
            customer_name TEXT,
            customer_email TEXT,
            customer_city TEXT,
            product_name TEXT,
            product_category TEXT,
            product_price REAL,
            quantity_sold INTEGER,
            sale_date TEXT
        );
    """)
    
    # Notice the massive data redundancy and update anomalies:
    sales_data = [
        (1, "Dipesh Mahato", "dipesh@example.com", "Kathmandu", "Mechanical Keyboard", "Hardware", 120.0, 1, "2026-10-01"),
        (2, "Dipesh Mahato", "dipesh@example.com", "Kathmandu", "Gaming Mouse", "Hardware", 60.0, 2, "2026-10-02"),
        (3, "Anjali Sharma", "anjali@example.com", "Pokhara", "Python Mastery Book", "Education", 45.0, 1, "2026-10-03"),
        (4, "Dipesh Mahato", "dipesh@example.com", "Kathmandu", "USB-C Hub", "Hardware", 30.0, 1, "2026-10-04"),
    ]
    cursor.executemany("INSERT INTO legacy_sales_dump VALUES (?,?,?,?,?,?,?,?,?);", sales_data)
    conn.commit()


# =====================================================================
# TASK 1: Design 3NF Schema & Migrate Data
# =====================================================================
def migrate_to_3nf_schema(conn: sqlite3.Connection):
    """
    INSTRUCTIONS:
    Split legacy_sales_dump into 3 clean, normalized tables:
    1. `customers`: id, name, email (UNIQUE), city
    2. `products`: id, name, category, price
    3. `orders`: id, customer_id (FK), order_date
    4. `order_items`: id, order_id (FK), product_id (FK), quantity, unit_price
    """
    cursor = conn.cursor()
    
    
    # Enable foreign key enforcement in SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # 1. Customers Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            city TEXT NOT NULL
        );
    """)
    
    # 2. Products Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL CHECK(price > 0)
        );
    """)
    
    # 3. Orders Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE RESTRICT
        );
    """)
    
    # 4. Order Items (Junction / Line Item Table)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            unit_price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
        );
    """)
    conn.commit()
    print("[+] 3NF Schema created successfully with foreign key constraints.")


def populate_normalized_data(conn: sqlite3.Connection):
    """Seeds normalized tables from the legacy table."""
    cursor = conn.cursor()
    
    # Insert Customers (Deduplicated)
    cursor.execute("""
        INSERT OR IGNORE INTO customers (name, email, city)
        SELECT DISTINCT customer_name, customer_email, customer_city
        FROM legacy_sales_dump;
    """)
    
    # Insert Products (Deduplicated)
    cursor.execute("""
        INSERT OR IGNORE INTO products (name, category, price)
        SELECT DISTINCT product_name, product_category, product_price
        FROM legacy_sales_dump;
    """)
    conn.commit()
    print("[+] Customers and Products successfully migrated with 0 duplicates.")


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    setup_unnormalized_table(conn)
    migrate_to_3nf_schema(conn)
    populate_normalized_data(conn)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers;")
    print("\n--- Normalized Customers ---")
    for row in cursor.fetchall():
        print(row)
        
    cursor.execute("SELECT * FROM products;")
    print("\n--- Normalized Products ---")
    for row in cursor.fetchall():
        print(row)
    conn.close()
