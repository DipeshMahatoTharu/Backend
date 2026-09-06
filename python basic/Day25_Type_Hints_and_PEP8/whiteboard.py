"""
============================================================
DAY 25 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: Strict Type-Annotated Data Filtering & Aggregation Pipeline

In modern backend interviews, interviewers evaluate whether your
code has clean type contracts, handles malformed inputs defensively,
and computes aggregations accurately.

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Write a strictly type-annotated function `filter_and_aggregate_products`
that takes a list of raw product dictionaries, filters by category
and minimum rating, and returns an aggregated summary dictionary.

------------------------------------------------------------
2. FUNCTION SIGNATURE:
------------------------------------------------------------
def filter_and_aggregate_products(
    products: list[dict[str, Any]],
    category: str,
    min_rating: float
) -> dict[str, Any]:

------------------------------------------------------------
3. RETURN STRUCTURE:
------------------------------------------------------------
{
    "category": str,
    "count": int,
    "average_price": float, # Rounded to 2 decimals, or 0.0 if count is 0
    "matching_items": list[dict[str, Any]]
}

------------------------------------------------------------
4. REQUIREMENTS & CONSTRAINTS:
------------------------------------------------------------
- Memory/Time Complexity: O(N) time where N is the number of products.
- Case-insensitivity: Category matching must be case-insensitive ("tech" matches "Tech").
- Defensive: Some products in the list may be missing keys ("rating", "price", "category").
  Never raise a `KeyError`. Use `.get()` or safe defaults.

------------------------------------------------------------
5. EXAMPLE INPUT:
------------------------------------------------------------
products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200.0, "rating": 4.8},
    {"name": "Phone", "category": "Electronics", "price": 800.0, "rating": 4.2},
    {"name": "Book", "category": "Books", "price": 20.0, "rating": 4.9},
    {"name": "Broken Item", "category": "Electronics"} # Missing price and rating
]

============================================================
MY APPROACH (Explain O(N) time & defensive checks):
============================================================
Write your plan and complexity explanation here:

____________________________________________________
____________________________________________________
____________________________________________________

============================================================
MY RAW CODE (No autocomplete! Write on blank paper first):
============================================================

from typing import Any

def filter_and_aggregate_products(
    products: list[dict[str, Any]],
    category: str,
    min_rating: float
) -> dict[str, Any]:
    # TODO: Write your complete implementation here
    pass

"""