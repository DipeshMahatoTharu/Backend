"""
Day 35: REST API Conventions & Design — Practice
Hands-on exercises covering REST URI parsing, query filtering, and paginated response envelopes.
"""
from typing import List, Dict, Any, Optional
import urllib.parse
import base64

# ---------------------------------------------------------------------
# Task 1: REST Query Parameter Parser
# ---------------------------------------------------------------------
def parse_query_params(query_string: str) -> Dict[str, Any]:
    """
    Parses an HTTP query string (e.g. 'category=tech&price_min=50&sort=-created_at&limit=10')
    into a structured dictionary with appropriate type conversions:
    - Integer strings converted to int.
    - Floating strings converted to float.
    - 'sort' converted into a list of tuples: [('created_at', 'desc')].
    """
    raw_params = urllib.parse.parse_qs(query_string, keep_blank_values=False)
    parsed: Dict[str, Any] = {}

    for key, values in raw_params.items():
        val = values[0]
        if key == "sort":
            sort_fields = []
            for item in val.split(","):
                item = item.strip()
                if item.startswith("-"):
                    sort_fields.append((item[1:], "desc"))
                else:
                    sort_fields.append((item, "asc"))
            parsed["sort"] = sort_fields
        elif val.isdigit():
            parsed[key] = int(val)
        else:
            try:
                parsed[key] = float(val)
            except ValueError:
                parsed[key] = val

    return parsed


# ---------------------------------------------------------------------
# Task 2: Standard Paginated Envelope Formatter
# ---------------------------------------------------------------------
def format_paginated_envelope(
    items: List[Dict[str, Any]],
    total_count: int,
    page: int,
    page_size: int,
    base_url: str
) -> Dict[str, Any]:
    """
    Wraps a list of items into an industry-standard REST pagination envelope.
    Includes metadata: count, next URL, previous URL, page, page_size, total_pages.
    """
    total_pages = (total_count + page_size - 1) // page_size if total_count > 0 else 1
    next_url = f"{base_url}?page={page + 1}&page_size={page_size}" if page < total_pages else None
    prev_url = f"{base_url}?page={page - 1}&page_size={page_size}" if page > 1 else None

    return {
        "count": total_count,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size,
        "next": next_url,
        "previous": prev_url,
        "results": items
    }


# ---------------------------------------------------------------------
# Task 3: Opaque Cursor Generator & Decoder
# ---------------------------------------------------------------------
def encode_cursor(last_id: int) -> str:
    """Encodes a record primary key into an opaque URL-safe base64 cursor."""
    return base64.urlsafe_b64encode(f"cursor:{last_id}".encode("utf-8")).decode("utf-8")

def decode_cursor(cursor_str: str) -> Optional[int]:
    """Decodes an opaque URL-safe base64 cursor back into an integer ID."""
    try:
        raw = base64.urlsafe_b64decode(cursor_str.encode("utf-8")).decode("utf-8")
        prefix, pk = raw.split(":")
        if prefix != "cursor":
            return None
        return int(pk)
    except Exception:
        return None


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 35 Practice Tests ---")

    # Test Task 1
    query = "category=electronics&limit=25&min_rating=4.5&sort=-rating,price"
    params = parse_query_params(query)
    assert params["category"] == "electronics"
    assert params["limit"] == 25
    assert params["min_rating"] == 4.5
    assert params["sort"] == [("rating", "desc"), ("price", "asc")]

    # Test Task 2
    items = [{"id": 1, "title": "Clean Code"}, {"id": 2, "title": "Design Patterns"}]
    envelope = format_paginated_envelope(items, total_count=45, page=1, page_size=2, base_url="/api/v1/books")
    assert envelope["count"] == 45
    assert envelope["total_pages"] == 23
    assert envelope["next"] == "/api/v1/books?page=2&page_size=2"
    assert envelope["previous"] is None
    assert len(envelope["results"]) == 2

    # Test Task 3
    encoded = encode_cursor(1045)
    assert isinstance(encoded, str)
    decoded = decode_cursor(encoded)
    assert decoded == 1045
    assert decode_cursor("invalid_base64!!") is None

    print("All Day 35 practice assertions passed successfully!")
