"""
============================================================
DAY 41 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: In-Memory Relational Batch Fetcher (Prefetch Engine)

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a function `batch_prefetch(parents: list, children: list, parent_key: str, foreign_key: str, target_attr: str) -> list`
that performs an optimal in-memory prefetch join.

Input:
parents = [{"id": 1, "name": "Author 1"}, {"id": 2, "name": "Author 2"}]
children = [{"id": 10, "author_id": 1, "title": "Book A"}, {"id": 11, "author_id": 1, "title": "Book B"}]

Output:
Returns `parents` where each parent has a list attached at `target_attr` (`books`):
Author 1 has `books` = [Book A, Book B], Author 2 has `books` = [].

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Complexity must be O(P + C) where P = len(parents) and C = len(children).
- Do NOT use nested loops (O(P * C))!

============================================================
MY APPROACH:
============================================================
1. Group children into a dictionary: `grouped[child[foreign_key]] = [child1, child2]`.
2. Iterate through parents once, attaching `grouped.get(parent[parent_key], [])` to `target_attr`.
"""
from typing import List, Dict, Any
from collections import defaultdict

def batch_prefetch(
    parents: List[Dict[str, Any]],
    children: List[Dict[str, Any]],
    parent_key: str,
    foreign_key: str,
    target_attr: str
) -> List[Dict[str, Any]]:
    # Step 1: Hash map grouping (O(C) time)
    grouped = defaultdict(list)
    for c in children:
        fk_val = c.get(foreign_key)
        if fk_val is not None:
            grouped[fk_val].append(c)

    # Step 2: Attach to parents (O(P) time)
    for p in parents:
        pk_val = p.get(parent_key)
        p[target_attr] = grouped.get(pk_val, [])

    return parents


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    authors = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    books = [
        {"id": 101, "author_id": 1, "title": "Python Pro"},
        {"id": 102, "author_id": 1, "title": "Django Deep Dive"}
    ]

    result = batch_prefetch(authors, books, parent_key="id", foreign_key="author_id", target_attr="books")
    assert len(result[0]["books"]) == 2
    assert result[0]["books"][0]["title"] == "Python Pro"
    assert len(result[1]["books"]) == 0

    print("Whiteboard Day 41 challenge passed successfully!")
