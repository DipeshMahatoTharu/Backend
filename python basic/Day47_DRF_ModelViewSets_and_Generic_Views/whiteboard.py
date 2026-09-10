"""
============================================================
DAY 47 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Dynamic REST Router URL Generator

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a URL router generator `generate_rest_endpoints(resource_name: str, supported_actions: list) -> list`
that outputs the complete table of standard REST URL routes for a given resource.

Standard Actions:
- "list": ("GET", f"/api/v1/{resource_name}/")
- "create": ("POST", f"/api/v1/{resource_name}/")
- "retrieve": ("GET", f"/api/v1/{resource_name}/<id>/")
- "update": ("PUT", f"/api/v1/{resource_name}/<id>/")
- "partial_update": ("PATCH", f"/api/v1/{resource_name}/<id>/")
- "destroy": ("DELETE", f"/api/v1/{resource_name}/<id>/")

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Return a list of tuples: `[(http_method, url_path, action_name)]`.
- Preserve the exact standard order.

============================================================
MY APPROACH:
============================================================
1. Define static mapping of standard DRF actions to (method, url_template).
2. Filter by `supported_actions` preserving order.
3. Return assembled routes.
"""
from typing import List, Tuple

STANDARD_MAPPINGS = [
    ("list", "GET", "/api/v1/{resource}/"),
    ("create", "POST", "/api/v1/{resource}/"),
    ("retrieve", "GET", "/api/v1/{resource}/<id>/"),
    ("update", "PUT", "/api/v1/{resource}/<id>/"),
    ("partial_update", "PATCH", "/api/v1/{resource}/<id>/"),
    ("destroy", "DELETE", "/api/v1/{resource}/<id>/"),
]

def generate_rest_endpoints(resource_name: str, supported_actions: List[str]) -> List[Tuple[str, str, str]]:
    routes = []
    for action_name, method, tpl in STANDARD_MAPPINGS:
        if action_name in supported_actions:
            path = tpl.format(resource=resource_name)
            routes.append((method, path, action_name))
    return routes


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    # Read-only resource
    read_only = generate_rest_endpoints("articles", ["list", "retrieve"])
    assert len(read_only) == 2
    assert read_only[0] == ("GET", "/api/v1/articles/", "list")
    assert read_only[1] == ("GET", "/api/v1/articles/<id>/", "retrieve")

    # Full CRUD resource
    all_actions = ["list", "create", "retrieve", "update", "partial_update", "destroy"]
    crud_routes = generate_rest_endpoints("products", all_actions)
    assert len(crud_routes) == 6
    assert crud_routes[5] == ("DELETE", "/api/v1/products/<id>/", "destroy")

    print("Whiteboard Day 47 challenge passed successfully!")
