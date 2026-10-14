"""
============================================================
DAY 35 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Dynamic REST Nested URI Router & Parameter Extractor

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a lightweight REST URL Pattern Matcher `match_route(pattern, path)` that:
1. Matches parametrized URI templates (e.g. `/api/v1/users/{user_id}/orders/{order_id}`).
2. Extracts path parameters into a dictionary `{ "user_id": 42, "order_id": 105 }` with integers auto-converted.
3. Returns `None` if the path does not match the pattern.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Match exact number of segments.
- Segments wrapped in `{name}` are dynamic parameters.
- If parameter value consists purely of digits, cast to `int`.

============================================================
MY APPROACH:
============================================================
1. Strip leading and trailing slashes and split pattern and path by `/`.
2. Check if segment counts match; if not, return None.
3. Compare segment by segment:
   - If pattern segment starts with `{` and ends with `}`, extract parameter name.
   - If segment contains digits, convert to int.
   - Otherwise, verify exact string match.
"""
from typing import Optional, Dict, Any

def match_route(pattern: str, path: str) -> Optional[Dict[str, Any]]:
    pat_segments = [s for s in pattern.strip("/").split("/") if s]
    path_segments = [s for s in path.strip("/").split("/") if s]

    if len(pat_segments) != len(path_segments):
        return None

    params: Dict[str, Any] = {}

    for p_seg, val_seg in zip(pat_segments, path_segments):
        if p_seg.startswith("{") and p_seg.endswith("}"):
            param_name = p_seg[1:-1]
            if val_seg.isdigit():
                params[param_name] = int(val_seg)
            else:
                params[param_name] = val_seg
        else:
            if p_seg != val_seg:
                return None

    return params


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    pattern = "/api/v1/users/{user_id}/orders/{order_id}"
    path1 = "/api/v1/users/42/orders/999"
    res1 = match_route(pattern, path1)
    assert res1 == {"user_id": 42, "order_id": 999}

    # Non-matching path
    path2 = "/api/v1/users/42/reviews/999"
    assert match_route(pattern, path2) is None

    # Length mismatch
    path3 = "/api/v1/users/42/orders"
    assert match_route(pattern, path3) is None

    # String parameter
    pattern_slug = "/api/v1/articles/{slug}"
    res_slug = match_route(pattern_slug, "/api/v1/articles/django-orm-tips")
    assert res_slug == {"slug": "django-orm-tips"}

    print("Whiteboard Day 35 challenge passed successfully!")
