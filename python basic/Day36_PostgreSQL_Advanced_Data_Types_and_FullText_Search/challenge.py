"""
============================================================
DAY 36 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: High-Performance JSONB Product Catalog & Dynamic Filter Engine

In modern e-commerce (Amazon, eBay), products have wildly different 
attributes:
- Laptops have `{"ram_gb": 32, "cpu": "M3 Max", "screen_inches": 16}`
- Shoes have `{"size": 10.5, "color": "black", "waterproof": true}`
- T-Shirts have `{"size": "XL", "material": "cotton", "colors": ["red", "blue"]}`

Storing every possible attribute as a relational table column requires 
500+ mostly NULL columns. Using PostgreSQL `JSONB` with GIN indexing gives 
infinite schema flexibility with sub-millisecond query speeds!

Your challenge:
Build `DynamicProductCatalog`:
1. `add_product(sku: str, title: str, category: str, attributes: dict)`
2. `filter_by_json_attribute(key_path: str, expected_val: Any) -> List[dict]`
3. `search_by_array_tag(tag: str) -> List[dict]`
"""

import sqlite3
import json
from typing import List, Dict, Any

class DynamicProductCatalog:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self._init_schema()

    def _init_schema(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sku TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                attributes JSON NOT NULL,
                tags JSON NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.conn.commit()

    def add_product(self, sku: str, title: str, category: str, attributes: dict, tags: list):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO products (sku, title, category, attributes, tags)
            VALUES (?, ?, ?, ?, ?);
        """, (sku, title, category, json.dumps(attributes), json.dumps(tags)))
        self.conn.commit()

    def filter_by_attribute(self, key_path: str, expected_value: Any) -> List[Dict[str, Any]]:
        """
        Queries nested JSON attribute.
        e.g. key_path = 'specs.ram_gb', expected_value = 32
        """
        cursor = self.conn.cursor()
        cursor.execute(f"""
            SELECT id, sku, title, category, attributes, tags
            FROM products
            WHERE json_extract(attributes, '$.{key_path}') = ?;
        """, (expected_value,))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                "id": row[0],
                "sku": row[1],
                "title": row[2],
                "category": row[3],
                "attributes": json.loads(row[4]),
                "tags": json.loads(row[5])
            })
        return results

    def filter_by_tag(self, target_tag: str) -> List[Dict[str, Any]]:
        """
        Searches within a JSON array column (simulating PostgreSQL array containment @>).
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT products.id, products.sku, products.title, products.category, products.attributes, products.tags
            FROM products, json_each(products.tags)
            WHERE json_each.value = ?;
        """, (target_tag,))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                "id": row[0],
                "sku": row[1],
                "title": row[2],
                "category": row[3],
                "attributes": json.loads(row[4]),
                "tags": json.loads(row[5])
            })
        return results


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    catalog = DynamicProductCatalog(conn)
    
    # 1. Add heterogeneous products
    catalog.add_product(
        sku="LAP-001",
        title="MacBook Pro 16",
        category="Electronics",
        attributes={"specs": {"ram_gb": 36, "cpu": "M3 Pro", "storage_tb": 1}},
        tags=["apple", "laptop", "premium", "developer"]
    )
    catalog.add_product(
        sku="LAP-002",
        title="Dell XPS 15",
        category="Electronics",
        attributes={"specs": {"ram_gb": 32, "cpu": "Intel i9", "storage_tb": 1}},
        tags=["dell", "laptop", "windows"]
    )
    catalog.add_product(
        sku="SHOE-001",
        title="Nike Pegasus 40",
        category="Footwear",
        attributes={"specs": {"size": 10.5, "color": "white", "waterproof": False}},
        tags=["nike", "running", "shoes"]
    )
    
    # Test 1: Filter by nested JSON attribute
    pro_laptops = catalog.filter_by_attribute("specs.ram_gb", 36)
    print(f"Products with 36GB RAM: {len(pro_laptops)}")
    assert len(pro_laptops) == 1
    assert pro_laptops[0]["sku"] == "LAP-001"
    
    # Test 2: Filter by array tag
    running_gear = catalog.filter_by_tag("running")
    print(f"Products tagged 'running': {len(running_gear)}")
    assert len(running_gear) == 1
    assert running_gear[0]["sku"] == "SHOE-001"
    
    print("[+] Dynamic JSONB Product Catalog passed all flexible attribute assertions!")
    conn.close()
