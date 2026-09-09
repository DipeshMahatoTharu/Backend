"""
============================================================
DAY 28 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: E-Commerce Product Catalog Search & Pagination Engine

In real backend APIs (Django, FastAPI), product catalog endpoints
allow clients to filter by keywords, price ranges, categories, stock
status, sort orders, and page through results with LIMIT & OFFSET.

This project implements a dynamic, SQL-injection safe catalog search
engine using Python and SQLite.

============================================================
REQUIREMENTS:
============================================================
1. Function `setup_catalog_db(conn: sqlite3.Connection)`:
   - Creates `products` table with:
     * id INTEGER PRIMARY KEY AUTOINCREMENT
     * name TEXT NOT NULL
     * category TEXT NOT NULL
     * price REAL NOT NULL
     * stock INTEGER NOT NULL DEFAULT 0
     * is_deleted INTEGER NOT NULL DEFAULT 0 (0 = Active, 1 = Soft Deleted)
   - Seeds 10 diverse products.

2. Function `search_products(...) -> dict`:
   - Parameters:
     * `keyword`: Optional[str] (searches product name with LIKE '%kw%')
     * `category`: Optional[str] (exact match)
     * `min_price`: Optional[float] (price >= min_price)
     * `max_price`: Optional[float] (price <= max_price)
     * `in_stock_only`: bool (if True, stock > 0)
     * `sort_by`: str ("price", "name", or "id", defaults to "price")
     * `sort_order`: str ("ASC" or "DESC", defaults to "ASC")
     * `page`: int (1-indexed page number, defaults to 1)
     * `page_size`: int (number of items per page, defaults to 3)

   - Requirements:
     * NEVER use string formatting or f-strings for user inputs (prevent SQL injection)!
     * Always filter out soft-deleted items (`is_deleted = 0`).
     * Calculate `total_count` of matching items.
     * Calculate `total_pages = math.ceil(total_count / page_size)`.
     * Return:
       {
           "total": int,
           "page": int,
           "page_size": int,
           "total_pages": int,
           "results": list[dict]
       }
"""

import sqlite3
import math
from typing import Optional, Any


def setup_catalog_db(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL DEFAULT 0,
            is_deleted INTEGER NOT NULL DEFAULT 0
        );
    """)
    
    # Seed 10 sample products
    products = [
        ('MacBook Pro 16', 'Electronics', 2499.00, 10, 0),
        ('Dell XPS 15', 'Electronics', 1899.00, 0, 0),       # Out of stock
        ('Sony WH-1000XM5', 'Electronics', 399.00, 15, 0),
        ('Mechanical Keyboard', 'Electronics', 120.00, 25, 0),
        ('Ergonomic Office Chair', 'Furniture', 299.00, 8, 0),
        ('Standing Desk', 'Furniture', 450.00, 4, 0),
        ('Desk Lamp LED', 'Furniture', 45.00, 0, 0),        # Out of stock
        ('Fluent Python 2nd Ed', 'Books', 55.00, 50, 0),
        ('Designing Data-Intensive Apps', 'Books', 48.00, 30, 0),
        ('Discontinued Monitor', 'Electronics', 150.00, 2, 1) # Soft deleted!
    ]
    cursor.executemany("""
        INSERT INTO products (name, category, price, stock, is_deleted)
        VALUES (?, ?, ?, ?, ?);
    """, products)
    conn.commit()


def search_products(
    conn: sqlite3.Connection,
    keyword: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    in_stock_only: bool = False,
    sort_by: str = "price",
    sort_order: str = "ASC",
    page: int = 1,
    page_size: int = 3
) -> dict[str, Any]:
    """
    Executes a dynamic, parameter-safe SQL search query with pagination.
    """
    # TODO: Implement dynamic query building using '?' placeholders
    # 1. Base WHERE clause: is_deleted = 0
    # 2. Append conditions for keyword, category, min_price, max_price, in_stock_only
    # 3. Query total count first
    # 4. Apply ORDER BY and LIMIT ? OFFSET ?
    # 5. Return structured pagination dictionary
    pass


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    print("Testing Product Catalog Search Engine...")
    conn = sqlite3.connect(":memory:")
    setup_catalog_db(conn)
    print("Database seeded with sample products.")

    # Test 1: Category filter + in stock only
    r1 = search_products(conn, category="Electronics", in_stock_only=True, page=1, page_size=2)
    print(f"Test 1 (Electronics in stock): {r1}")

    # Test 2: Price range filter
    r2 = search_products(conn, min_price=40.0, max_price=60.0, sort_by="price", sort_order="DESC")
    print(f"Test 2 (Price $40 - $60): {r2}")

    # Test 3: Soft-deleted item exclusion check
    r3 = search_products(conn, keyword="Discontinued")
    print(f"Test 3 (Soft-deleted 'Discontinued' item found): {r3}")

    conn.close()
    print("Catalog search tests complete.")