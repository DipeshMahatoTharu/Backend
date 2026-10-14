"""
Day 50: DRF Searching & Pagination — Debugging
Diagnose and fix 3 common search and pagination bugs.
"""
from typing import Dict, Any, List, Optional

# ---------------------------------------------------------------------
# Bug 1: Unindexed Search Causing Full Table Scans
# Problem: An engineer added `search_fields = ['bio']` on a 5M row table.
# Every search triggered a sequential scan lasting 12 seconds.
# Fix: Enforce indexed search or restrict searches to indexed fields.
# ---------------------------------------------------------------------
def validate_searchable_fields(fields: List[str], indexed_fields: set) -> List[str]:
    # BUGGY VERSION: Allowed any arbitrary unindexed text column
    # return fields

    # FIXED VERSION:
    safe_fields = []
    for f in fields:
        clean = f.lstrip("^=@$")
        if clean in indexed_fields:
            safe_fields.append(f)
        else:
            raise ValueError(f"Field '{clean}' is not indexed! Adding to search_fields will cause table scans.")
    return safe_fields


# ---------------------------------------------------------------------
# Bug 2: Crash on Non-Integer Page Number in PageNumberPagination
# Problem: When a client passed `?page=invalid`, the view crashed with `ValueError`.
# Fix: Catch invalid page inputs and raise 404 or default to page 1.
# ---------------------------------------------------------------------
def parse_page_param(raw_param: Optional[str]) -> int:
    # BUGGY VERSION:
    # return int(raw_param) # Crashes on None or "abc"

    # FIXED VERSION:
    if not raw_param:
        return 1
    try:
        page = int(raw_param)
        return page if page > 0 else 1
    except ValueError:
        return 1


# ---------------------------------------------------------------------
# Bug 3: CursorPagination Missing Ordering Attribute
# Problem: Using CursorPagination without defining `ordering` causes
# random and inconsistent page results.
# Fix: Ensure ordering is defined.
# ---------------------------------------------------------------------
def get_cursor_ordering(viewset_ordering: Optional[str], default_ordering: str = "-created_at") -> str:
    # BUGGY VERSION:
    # return viewset_ordering # Returns None!

    # FIXED VERSION:
    return viewset_ordering or default_ordering


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    indexed = {"title", "sku", "email"}
    assert validate_searchable_fields(["^title", "=sku"], indexed) == ["^title", "=sku"]
    try:
        validate_searchable_fields(["unindexed_column"], indexed)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    # Test Bug 2 fix
    assert parse_page_param(None) == 1
    assert parse_page_param("not_a_number") == 1
    assert parse_page_param("-5") == 1
    assert parse_page_param("3") == 3

    # Test Bug 3 fix
    assert get_cursor_ordering(None) == "-created_at"
    assert get_cursor_ordering("price") == "price"

    print("All Day 50 debugging fixes verified successfully!")
