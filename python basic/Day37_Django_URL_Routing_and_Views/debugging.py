"""
Day 37: Django URL Routing & Views — Debugging
Diagnose and fix 3 common URL routing and view response traps.
"""
from typing import Dict, Any, Tuple
import json

# ---------------------------------------------------------------------
# Bug 1: View Returning Raw Python Dict Instead of HttpResponse/JsonResponse
# Problem: A developer wrote a view returning `{'status': 'ok'}` which causes
# Django to crash with `ValueError: The view didn't return an HttpResponse object.`
# Fix: Wrap dictionaries in JsonResponse.
# ---------------------------------------------------------------------
class JsonResponse:
    def __init__(self, data: Any, status: int = 200):
        self.status = status
        self.headers = {"Content-Type": "application/json"}
        self.content = json.dumps(data)

def user_status_view(user_id: int):
    # BUGGY VERSION:
    # return {"user_id": user_id, "status": "active"} # Crashes Django!

    # FIXED VERSION:
    return JsonResponse({"user_id": user_id, "status": "active"}, status=200)


# ---------------------------------------------------------------------
# Bug 2: Missing Trailing Slash in URL Pattern
# Problem: Pattern registered as 'api/orders' without a trailing slash causes
# unpredictable redirect loops when clients request '/api/orders/'.
# Fix: Normalize patterns to end with trailing slashes.
# ---------------------------------------------------------------------
def normalize_route_pattern(route: str) -> str:
    # BUGGY VERSION:
    # return route

    # FIXED VERSION:
    clean = route.strip("/")
    return f"{clean}/" if clean else ""


# ---------------------------------------------------------------------
# Bug 3: Accessing Query Parameters with `request.POST`
# Problem: In a GET request, filtering parameters like `?page=2&q=python`
# were accessed via `request.POST.get('page')`, returning `None`.
# Fix: Use `request.GET` for query strings.
# ---------------------------------------------------------------------
class MockRequest:
    def __init__(self, get_params: Dict[str, str], post_params: Dict[str, str]):
        self.GET = get_params
        self.POST = post_params

def get_page_number(request: MockRequest) -> int:
    # BUGGY VERSION:
    # page = request.POST.get("page", "1")

    # FIXED VERSION:
    page = request.GET.get("page", "1")
    return int(page)


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    resp = user_status_view(101)
    assert isinstance(resp, JsonResponse)
    assert resp.status == 200
    assert "user_id" in resp.content

    # Test Bug 2 fix
    assert normalize_route_pattern("api/orders") == "api/orders/"
    assert normalize_route_pattern("/api/orders/") == "api/orders/"

    # Test Bug 3 fix
    req = MockRequest(get_params={"page": "5"}, post_params={})
    assert get_page_number(req) == 5

    print("All Day 37 debugging fixes verified successfully!")
