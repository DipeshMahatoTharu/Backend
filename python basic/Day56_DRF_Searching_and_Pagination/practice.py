"""
Day 50: DRF Searching & Pagination — Practice
Hands-on exercises covering search filtering, multi-column ordering, and pagination envelopes.
"""
from typing import List, Dict, Any, Optional

# ---------------------------------------------------------------------
# Task 1: Search Filter Matcher
# ---------------------------------------------------------------------
def apply_search_filter(items: List[Dict[str, Any]], query: str, search_fields: List[str]) -> List[Dict[str, Any]]:
    """
    Filters items where any specified field matches search query:
    - If field starts with '^': string starts with query (case-insensitive).
    - If field starts with '=': exact match (case-insensitive).
    - Otherwise: substring match (case-insensitive).
    """
    if not query:
        return items

    q_lower = query.lower()
    matched = []

    for it in items:
        found = False
        for field in search_fields:
            if field.startswith("^"):
                fname = field[1:]
                val = str(it.get(fname, "")).lower()
                if val.startswith(q_lower): found = True; break
            elif field.startswith("="):
                fname = field[1:]
                val = str(it.get(fname, "")).lower()
                if val == q_lower: found = True; break
            else:
                val = str(it.get(field, "")).lower()
                if q_lower in val: found = True; break
        if found:
            matched.append(it)

    return matched


# ---------------------------------------------------------------------
# Task 2: Multi-Column Ordering Filter
# ---------------------------------------------------------------------
def apply_ordering(items: List[Dict[str, Any]], ordering_param: str) -> List[Dict[str, Any]]:
    """
    Sorts items by comma-separated ordering string: '-price,title'.
    """
    if not ordering_param:
        return items

    result = list(items)
    sort_keys = [s.strip() for s in ordering_param.split(",") if s.strip()]

    # Sort in reverse order of precedence to achieve multi-key sort
    for key in reversed(sort_keys):
        desc = key.startswith("-")
        fname = key[1:] if desc else key
        result.sort(key=lambda x: x.get(fname, 0), reverse=desc)

    return result


# ---------------------------------------------------------------------
# Task 3: LimitOffset Pagination Simulator
# ---------------------------------------------------------------------
def paginate_limit_offset(items: List[Dict[str, Any]], limit: int, offset: int) -> Dict[str, Any]:
    total_count = len(items)
    paged = items[offset:offset + limit]
    return {
        "count": total_count,
        "next": f"?limit={limit}&offset={offset + limit}" if offset + limit < total_count else None,
        "previous": f"?limit={limit}&offset={max(0, offset - limit)}" if offset > 0 else None,
        "results": paged
    }


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 50 Practice Tests ---")

    dataset = [
        {"id": 1, "title": "MacBook Air", "sku": "APL-01", "price": 999},
        {"id": 2, "title": "MacBook Pro", "sku": "APL-02", "price": 1999},
        {"id": 3, "title": "Dell XPS", "sku": "DEL-01", "price": 1200},
    ]

    # Test Task 1: Search
    res_start = apply_search_filter(dataset, "Mac", ["^title"])
    assert len(res_start) == 2

    res_exact = apply_search_filter(dataset, "APL-01", ["=sku"])
    assert len(res_exact) == 1 and res_exact[0]["id"] == 1

    # Test Task 2: Ordering
    ordered = apply_ordering(dataset, "-price")
    assert ordered[0]["title"] == "MacBook Pro"

    # Test Task 3: LimitOffset
    envelope = paginate_limit_offset(dataset, limit=2, offset=0)
    assert envelope["count"] == 3
    assert len(envelope["results"]) == 2
    assert envelope["next"] == "?limit=2&offset=2"

    print("All Day 50 practice assertions passed successfully!")
