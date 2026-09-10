"""
Day 53: Troubleshooting & Debugging ORM — Practice
Hands-on exercises covering SQL query counting, duplicate query detection, and column payload reduction.
"""
from typing import List, Dict, Any, Set

# ---------------------------------------------------------------------
# Task 1: Duplicate SQL Query Detector (N+1 Linter)
# ---------------------------------------------------------------------
def detect_duplicate_queries(queries: List[str]) -> Dict[str, int]:
    """
    Analyzes raw SQL query list and returns queries that executed more than once.
    """
    counts: Dict[str, int] = {}
    for q in queries:
        clean = " ".join(q.strip().split())
        counts[clean] = counts.get(clean, 0) + 1
    return {q: c for q, c in counts.items() if c > 1}


# ---------------------------------------------------------------------
# Task 2: Column Payload Reducer (`only` simulation)
# ---------------------------------------------------------------------
def apply_only_fields(records: List[Dict[str, Any]], allowed_fields: Set[str]) -> List[Dict[str, Any]]:
    """
    Simulates QuerySet.only(): Strips out fields not in allowed_fields.
    Always preserves 'id'.
    """
    keep = set(allowed_fields)
    keep.add("id")
    return [{k: v for k, v in r.items() if k in keep} for r in records]


# ---------------------------------------------------------------------
# Task 3: Query Duration Monitor
# ---------------------------------------------------------------------
def flag_slow_queries(query_log: List[Dict[str, Any]], threshold_seconds: float = 0.1) -> List[Dict[str, Any]]:
    """
    Filters queries whose execution duration exceeds threshold_seconds.
    """
    return [q for q in query_log if q.get("time", 0.0) >= threshold_seconds]


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 53 Practice Tests ---")

    # Test Task 1: Duplicate queries
    sqls = [
        "SELECT * FROM users WHERE id = 1",
        "SELECT * FROM users WHERE id = 1",
        "SELECT * FROM orders WHERE user_id = 1"
    ]
    dups = detect_duplicate_queries(sqls)
    assert len(dups) == 1
    assert dups["SELECT * FROM users WHERE id = 1"] == 2

    # Test Task 2: only fields
    rows = [{"id": 1, "title": "Post", "heavy_blob": "0x1234567890", "bio": "Long text"}]
    slim = apply_only_fields(rows, {"title"})
    assert "title" in slim[0] and "id" in slim[0]
    assert "heavy_blob" not in slim[0] and "bio" not in slim[0]

    # Test Task 3: Slow query flagging
    log = [
        {"sql": "SELECT 1;", "time": 0.002},
        {"sql": "SELECT * FROM large_table;", "time": 0.350}
    ]
    slow = flag_slow_queries(log, threshold_seconds=0.1)
    assert len(slow) == 1
    assert slow[0]["time"] == 0.350

    print("All Day 53 practice assertions passed successfully!")
