"""
Day 41: Django Relationships & Prefetching — Practice
Hands-on exercises covering N+1 query simulation, join resolution, and batch prefetching.
"""
from typing import Dict, List, Any, Optional

# ---------------------------------------------------------------------
# Task 1: Query Execution Counter & N+1 Simulator
# ---------------------------------------------------------------------
class MockDatabase:
    def __init__(self):
        self.query_log: List[str] = []
        self.customers = {1: {"id": 1, "name": "Alice"}, 2: {"id": 2, "name": "Bob"}}
        self.orders = [
            {"id": 101, "customer_id": 1, "total": 99.0},
            {"id": 102, "customer_id": 1, "total": 149.0},
            {"id": 103, "customer_id": 2, "total": 45.0},
        ]

    def query_all_orders(self) -> List[Dict[str, Any]]:
        self.query_log.append("SELECT * FROM orders;")
        return list(self.orders)

    def query_customer_by_id(self, customer_id: int) -> Dict[str, Any]:
        self.query_log.append(f"SELECT * FROM customers WHERE id = {customer_id};")
        return self.customers.get(customer_id, {})

    def query_customers_by_ids(self, ids: List[int]) -> List[Dict[str, Any]]:
        id_str = ", ".join(map(str, ids))
        self.query_log.append(f"SELECT * FROM customers WHERE id IN ({id_str});")
        return [self.customers[cid] for cid in ids if cid in self.customers]


# ---------------------------------------------------------------------
# Task 2: Simulating select_related (In-Memory Join)
# ---------------------------------------------------------------------
def simulate_select_related(orders: List[Dict[str, Any]], customers_table: Dict[int, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Joins customer record directly into each order dictionary under 'customer'.
    Simulates SQL: SELECT * FROM orders INNER JOIN customers ON orders.customer_id = customers.id;
    """
    joined = []
    for o in orders:
        record = dict(o)
        record["customer"] = customers_table.get(o["customer_id"])
        joined.append(record)
    return joined


# ---------------------------------------------------------------------
# Task 3: Simulating prefetch_related (Batch Query)
# ---------------------------------------------------------------------
def simulate_prefetch_related(db: MockDatabase) -> List[Dict[str, Any]]:
    """
    1. Query all orders.
    2. Collect unique customer IDs.
    3. Query customers in a single batch with WHERE id IN (...).
    4. Attach customers in Python memory.
    Total queries: Exactly 2!
    """
    orders = db.query_all_orders()
    cust_ids = list({o["customer_id"] for o in orders})
    cust_rows = db.query_customers_by_ids(cust_ids)
    cust_map = {c["id"]: c for c in cust_rows}

    for o in orders:
        o["customer"] = cust_map.get(o["customer_id"])
    return orders


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 41 Practice Tests ---")

    # Test Task 1: N+1 demonstration
    db = MockDatabase()
    raw_orders = db.query_all_orders()
    for o in raw_orders:
        c = db.query_customer_by_id(o["customer_id"])
    assert len(db.query_log) == 4  # 1 order query + 3 customer queries!

    # Test Task 2: select_related simulation
    joined_res = simulate_select_related(db.orders, db.customers)
    assert len(joined_res) == 3
    assert joined_res[0]["customer"]["name"] == "Alice"

    # Test Task 3: prefetch_related (only 2 queries)
    db_clean = MockDatabase()
    prefetched = simulate_prefetch_related(db_clean)
    assert len(db_clean.query_log) == 2  # Exactly 2 queries!
    assert prefetched[0]["customer"]["name"] == "Alice"
    assert prefetched[2]["customer"]["name"] == "Bob"

    print("All Day 41 practice assertions passed successfully!")
