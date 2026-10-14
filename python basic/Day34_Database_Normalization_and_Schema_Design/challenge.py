"""
============================================================
DAY 34 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: Multi-Tenant B2B E-Commerce Relational Engine

In SaaS and multi-tenant architectures, companies (tenants) have their own
isolated stores, products, inventory warehouses, and orders.

Build a Python Relational Schema Manager `MultiTenantStoreManager` that:
1. Implements tables:
   - `tenants` (id, company_name, subdomain [UNIQUE], is_active)
   - `warehouses` (id, tenant_id [FK], location_name, address)
   - `products` (id, tenant_id [FK], sku, title, price)
   - `inventory` (id, warehouse_id [FK], product_id [FK], stock_count, UNIQUE(warehouse_id, product_id))
2. Implements methods to:
   - Create the relational schema with check constraints and foreign keys.
   - Register a new tenant.
   - Add products and stock across multiple warehouses.
   - Query stock for a given product across all tenant warehouses.
"""

import sqlite3
from typing import List, Tuple, Dict, Any

class MultiTenantStoreManager:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def setup_schema(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tenants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                subdomain TEXT UNIQUE NOT NULL,
                is_active INTEGER DEFAULT 1
            );
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS warehouses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tenant_id INTEGER NOT NULL,
                location_name TEXT NOT NULL,
                FOREIGN KEY (tenant_id) REFERENCES tenants(id) ON DELETE CASCADE
            );
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tenant_id INTEGER NOT NULL,
                sku TEXT NOT NULL,
                title TEXT NOT NULL,
                price REAL NOT NULL CHECK(price > 0),
                UNIQUE(tenant_id, sku),
                FOREIGN KEY (tenant_id) REFERENCES tenants(id) ON DELETE CASCADE
            );
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                warehouse_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                stock_count INTEGER NOT NULL CHECK(stock_count >= 0),
                UNIQUE(warehouse_id, product_id),
                FOREIGN KEY (warehouse_id) REFERENCES warehouses(id) ON DELETE CASCADE,
                FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
            );
        """)
        self.conn.commit()

    def create_tenant(self, company_name: str, subdomain: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tenants (company_name, subdomain) VALUES (?, ?);", (company_name, subdomain))
        self.conn.commit()
        return cursor.lastrowid

    def add_warehouse(self, tenant_id: int, location_name: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO warehouses (tenant_id, location_name) VALUES (?, ?);", (tenant_id, location_name))
        self.conn.commit()
        return cursor.lastrowid

    def add_product(self, tenant_id: int, sku: str, title: str, price: float) -> int:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO products (tenant_id, sku, title, price) VALUES (?, ?, ?, ?);", (tenant_id, sku, title, price))
        self.conn.commit()
        return cursor.lastrowid

    def set_inventory(self, warehouse_id: int, product_id: int, count: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO inventory (warehouse_id, product_id, stock_count) VALUES (?, ?, ?)
            ON CONFLICT(warehouse_id, product_id) DO UPDATE SET stock_count = excluded.stock_count;
        """, (warehouse_id, product_id, count))
        self.conn.commit()

    def get_total_product_stock(self, tenant_id: int, sku: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT COALESCE(SUM(i.stock_count), 0)
            FROM products p
            LEFT JOIN inventory i ON p.id = i.product_id
            WHERE p.tenant_id = ? AND p.sku = ?;
        """, (tenant_id, sku))
        return cursor.fetchone()[0]


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    manager = MultiTenantStoreManager(conn)
    manager.setup_schema()
    
    # Create tenant
    tenant_id = manager.create_tenant("Apex Gear Nepal", "apexgear")
    
    # Create warehouses
    w1 = manager.add_warehouse(tenant_id, "Kathmandu Central Depot")
    w2 = manager.add_warehouse(tenant_id, "Pokhara Hub")
    
    # Create product
    prod_id = manager.add_product(tenant_id, "JKT-001", "GoreTex Mountain Jacket", 149.99)
    
    # Distribute stock
    manager.set_inventory(w1, prod_id, 35)
    manager.set_inventory(w2, prod_id, 15)
    
    total = manager.get_total_product_stock(tenant_id, "JKT-001")
    print(f"Total stock for JKT-001 across all warehouses: {total} units (Expected 50)")
    assert total == 50
    print("[+] Multi-Tenant relational store tests passed with 100% integrity!")
    conn.close()
