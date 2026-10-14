"""
Day 53: Troubleshooting & Debugging ORM — Debugging
Diagnose and fix 3 subtle ORM performance bugs.
"""
from typing import List, Dict, Any

# ---------------------------------------------------------------------
# Bug 1: QuerySet Evaluated Twice in Template / Logic
# Problem: An engineer wrote `if qs: return [x for x in qs]` which executed
# the SQL query twice because `qs` was not cached as a list.
# Fix: Cache evaluation into a local variable.
# ---------------------------------------------------------------------
class EvaluatableQuery:
    def __init__(self, data: List[int]):
        self.data = data
        self.eval_count = 0

    def get_results(self) -> List[int]:
        self.eval_count += 1
        return list(self.data)

def process_query_safely(q: EvaluatableQuery) -> List[int]:
    # BUGGY VERSION:
    # if q.get_results():
    #     return [x * 2 for x in q.get_results()] # Called twice!

    # FIXED VERSION:
    results = q.get_results()
    if results:
        return [x * 2 for x in results]
    return []


# ---------------------------------------------------------------------
# Bug 2: Accessing Deferred Fields in Loops
# Problem: A view used `Book.objects.defer('content')`, but inside the loop,
# `print(b.content)` was called, executing 100 extra individual SQL queries!
# Fix: Do not defer fields that are needed in the loop.
# ---------------------------------------------------------------------
def check_fields_to_defer(fields_to_access: set, fields_to_defer: set) -> set:
    # BUGGY VERSION:
    # return fields_to_defer # Kept deferring needed fields!

    # FIXED VERSION:
    # Never defer fields that will be accessed
    return fields_to_defer - fields_to_access


# ---------------------------------------------------------------------
# Bug 3: `count()` on Filtered Unindexed Foreign Key
# Problem: Running `Order.objects.filter(status='pending').count()` without an index
# on `status` performed a sequential table scan of 10M rows.
# Fix: Ensure query filters on indexed columns.
# ---------------------------------------------------------------------
def is_query_indexed(filter_column: str, indexed_columns: set) -> bool:
    return filter_column in indexed_columns


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    q = EvaluatableQuery([1, 2, 3])
    out = process_query_safely(q)
    assert q.eval_count == 1
    assert out == [2, 4, 6]

    # Test Bug 2 fix
    accessing = {"title", "content"}
    deferring = {"content", "heavy_metadata"}
    safe_def = check_fields_to_defer(accessing, deferring)
    assert "content" not in safe_def
    assert "heavy_metadata" in safe_def

    # Test Bug 3 fix
    assert is_query_indexed("user_id", {"id", "user_id"}) is True
    assert is_query_indexed("unindexed_status", {"id", "user_id"}) is False

    print("All Day 53 debugging fixes verified successfully!")
