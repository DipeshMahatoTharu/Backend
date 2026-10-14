"""
Day 35: REST API Conventions & Design — Debugging
Diagnose and fix 3 common REST architectural design flaws.
"""
from typing import Dict, Any, Tuple

# ---------------------------------------------------------------------
# Bug 1: Verbs in URI Paths (RPC Anti-Pattern)
# Problem: An API exposes `/api/v1/books/get_all`, `/api/v1/books/create_item`,
# and `/api/v1/books/delete_by_id?id=4`.
# Fix: Map the actions to HTTP methods over standard resource nouns `/api/v1/books`.
# ---------------------------------------------------------------------
def canonicalize_route(raw_path: str, raw_method: str) -> Tuple[str, str]:
    """
    Converts legacy RPC paths into clean RESTful (method, path) tuples.
    """
    # BUGGY VERSION: Allowed RPC endpoints
    # return raw_method, raw_path

    # FIXED VERSION:
    if raw_path == "/api/v1/books/get_all":
        return "GET", "/api/v1/books"
    elif raw_path == "/api/v1/books/create_item":
        return "POST", "/api/v1/books"
    elif raw_path.startswith("/api/v1/books/delete_by_id"):
        # e.g. /api/v1/books/delete_by_id?id=4 -> DELETE /api/v1/books/4
        import urllib.parse
        parsed = urllib.parse.urlparse(raw_path)
        qs = urllib.parse.parse_qs(parsed.query)
        item_id = qs.get("id", [""])[0]
        return "DELETE", f"/api/v1/books/{item_id}"
    return raw_method, raw_path


# ---------------------------------------------------------------------
# Bug 2: PUT used for Partial Updates (Accidental Field Deletion)
# Problem: A client called PUT `/api/v1/users/1` sending only `{"name": "Alice"}`.
# Because PUT specifies complete resource replacement, the server wiped out the user's
# email and phone number!
# Fix: Enforce PATCH for partial updates and PUT for full replacements.
# ---------------------------------------------------------------------
def update_user_record(existing_user: Dict[str, Any], new_data: Dict[str, Any], method: str) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return new_data # Completely wiped out fields not sent!

    # FIXED VERSION:
    if method.upper() == "PATCH":
        # Partial update: merge fields
        updated = existing_user.copy()
        updated.update(new_data)
        return updated
    elif method.upper() == "PUT":
        # Complete replacement: requires all required fields
        required_fields = ["id", "name", "email"]
        for rf in required_fields:
            if rf not in new_data:
                raise ValueError(f"PUT requires full resource representation including '{rf}'.")
        return new_data
    raise ValueError("Invalid update method")


# ---------------------------------------------------------------------
# Bug 3: Inconsistent Pluralization & Inconsistent Envelope
# Problem: Some endpoints return a bare array `[{...}]` while others return `{"items": [...]}`.
# Standardize on a predictable envelope.
# ---------------------------------------------------------------------
def standardize_response(data: Any) -> Dict[str, Any]:
    # BUGGY VERSION: Returning inconsistent structures
    # return data

    # FIXED VERSION:
    if isinstance(data, list):
        return {"count": len(data), "data": data}
    return {"data": data}


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    m, p = canonicalize_route("/api/v1/books/get_all", "GET")
    assert m == "GET" and p == "/api/v1/books"
    m, p = canonicalize_route("/api/v1/books/delete_by_id?id=42", "GET")
    assert m == "DELETE" and p == "/api/v1/books/42"

    # Test Bug 2 fix
    user = {"id": 1, "name": "Dipesh", "email": "dipesh@example.com"}
    patched = update_user_record(user, {"name": "Dipesh Tharu"}, "PATCH")
    assert patched["name"] == "Dipesh Tharu"
    assert patched["email"] == "dipesh@example.com"  # Preserved!

    # Test Bug 3 fix
    resp = standardize_response([1, 2, 3])
    assert "count" in resp and resp["count"] == 3

    print("All Day 35 debugging fixes verified successfully!")
