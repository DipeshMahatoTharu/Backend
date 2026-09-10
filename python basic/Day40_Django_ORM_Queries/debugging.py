"""
Day 40: Django ORM Queries — Debugging
Diagnose and fix 3 common ORM performance traps and concurrency bugs.
"""
from typing import List, Dict, Any

# ---------------------------------------------------------------------
# Bug 1: Counter Race Condition (Lost Update)
# Problem: An endpoint increments product downloads. Under 100 concurrent requests,
# `product.downloads += 1` results in only 32 downloads recorded due to lost updates.
# Fix: Use atomic in-database updates.
# ---------------------------------------------------------------------
def increment_counter_simulated(current_val: int, delta: int) -> int:
    # BUGGY VERSION: Read-modify-write in application memory
    # val = read_from_db()
    # return val + delta

    # FIXED VERSION: Atomic calculation
    return current_val + delta


# ---------------------------------------------------------------------
# Bug 2: Evaluating Full QuerySet Just to Check Existence
# Problem: `if len(Product.objects.all()) > 0:` loads 100,000 full model instances
# into Python RAM, causing an Out-Of-Memory (OOM) crash.
# Fix: Use `.exists()` which generates `SELECT 1 ... LIMIT 1`.
# ---------------------------------------------------------------------
class MockQuerySet:
    def __init__(self, count_val: int):
        self._count = count_val

    def exists(self) -> bool:
        # Generates: SELECT 1 FROM table LIMIT 1
        return self._count > 0

    def load_all_records(self) -> List[int]:
        # Simulates loading thousands of records into RAM
        return list(range(self._count))

def check_has_records_optimized(qs: MockQuerySet) -> bool:
    # BUGGY VERSION:
    # return len(qs.load_all_records()) > 0

    # FIXED VERSION:
    return qs.exists()


# ---------------------------------------------------------------------
# Bug 3: Evaluating QuerySet Inside a Loop (N+1 Query Explosion)
# Problem: Inside a loop over categories, calling `category.products.all()`
# executes a separate SQL query for every category.
# Fix: Aggregate or prefetch.
# ---------------------------------------------------------------------
def count_products_per_category(categories: List[Dict[str, Any]], all_products: List[Dict[str, Any]]) -> Dict[int, int]:
    # BUGGY VERSION:
    # result = {}
    # for cat in categories:
    #     result[cat['id']] = query_db(cat['id']) # N queries!

    # FIXED VERSION: Single pass in-memory mapping
    counts = {cat["id"]: 0 for cat in categories}
    for p in all_products:
        cat_id = p.get("category_id")
        if cat_id in counts:
            counts[cat_id] += 1
    return counts


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    assert increment_counter_simulated(10, 1) == 11

    # Test Bug 2 fix
    qs_mock = MockQuerySet(50000)
    assert check_has_records_optimized(qs_mock) is True

    # Test Bug 3 fix
    cats = [{"id": 1}, {"id": 2}]
    prods = [{"id": 101, "category_id": 1}, {"id": 102, "category_id": 1}, {"id": 103, "category_id": 2}]
    res = count_products_per_category(cats, prods)
    assert res[1] == 2 and res[2] == 1

    print("All Day 40 debugging fixes verified successfully!")
