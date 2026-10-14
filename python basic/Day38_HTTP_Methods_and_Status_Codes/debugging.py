"""
Day 34: HTTP Methods & Status Codes — Debugging
Diagnose and fix 3 production HTTP protocol anti-patterns.
"""
import json
from typing import Dict, Any, Tuple, Optional

# ---------------------------------------------------------------------
# Bug 1: Dangerous State Mutation in a GET Request
# Problem: An engineer implemented an endpoint to 'increment views and fetch stats' via GET.
# Because Web crawlers and browser pre-fetchers execute GET requests automatically,
# the view counter explodes uncontrollably.
# Fix: Separate read (GET) from mutation (POST).
# ---------------------------------------------------------------------
class ArticleAnalytics:
    def __init__(self):
        self.views = 0

    # BUGGY VERSION:
    # def handle_request(self, method: str) -> Tuple[int, Dict[str, Any]]:
    #     if method == "GET":
    #         self.views += 1 # Mutating state on safe GET request!
    #         return 200, {"views": self.views}

    # FIXED VERSION:
    def handle_request(self, method: str) -> Tuple[int, Dict[str, Any]]:
        if method == "GET":
            # Safe and idempotent: returns current count without mutation
            return 200, {"views": self.views}
        elif method == "POST":
            # Non-safe: explicitly records an interaction/view
            self.views += 1
            return 200, {"views": self.views}
        return 405, {"error": "Method Not Allowed"}


# ---------------------------------------------------------------------
# Bug 2: 200 OK with Failure Body (Masking Errors)
# Problem: A microservice returns 200 OK with `{"status": "error", "code": 404}`.
# This prevents upstream API gateways, Cloudflare caches, and load balancers
# from recognizing the failure.
# Fix: Return true HTTP status codes.
# ---------------------------------------------------------------------
class UserDirectory:
    def __init__(self):
        self._db = {1: "Alice", 2: "Bob"}

    # BUGGY VERSION:
    # def get_user(self, user_id: int) -> Tuple[int, Dict[str, Any]]:
    #     if user_id not in self._db:
    #         return 200, {"status": "error", "message": "User not found"}
    #     return 200, {"status": "success", "user": self._db[user_id]}

    # FIXED VERSION:
    def get_user(self, user_id: int) -> Tuple[int, Dict[str, Any]]:
        if user_id not in self._db:
            return 404, {"error": "Not Found", "message": f"User ID {user_id} does not exist."}
        return 200, {"id": user_id, "name": self._db[user_id]}


# ---------------------------------------------------------------------
# Bug 3: Using 401 Unauthorized for Authorization Failures
# Problem: An engineer returned 401 when an authenticated user tried to access an admin area.
# The mobile app received 401, assumed the user's JWT token was expired, wiped the session,
# and forcibly logged the user out!
# Fix: Return 403 Forbidden so the app keeps the session and shows an 'Access Denied' banner.
# ---------------------------------------------------------------------
def check_access(user: Optional[Dict[str, Any]], required_role: str) -> Tuple[int, str]:
    # BUGGY VERSION:
    # if not user:
    #     return 401, "Login required"
    # if user.get("role") != required_role:
    #     return 401, "Insufficient privileges"  # WRONG!

    # FIXED VERSION:
    if not user:
        return 401, "Authentication required. Please log in."
    if user.get("role") != required_role:
        return 403, "Forbidden. You lack sufficient permissions for this action."
    return 200, "Access granted."


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    analytics = ArticleAnalytics()
    status, data = analytics.handle_request("GET")
    assert status == 200 and data["views"] == 0  # No mutation on GET
    status, data = analytics.handle_request("POST")
    assert status == 200 and data["views"] == 1  # Mutated on POST

    # Test Bug 2 fix
    dir_svc = UserDirectory()
    status, data = dir_svc.get_user(999)
    assert status == 404
    assert "error" in data

    # Test Bug 3 fix
    assert check_access(None, "admin")[0] == 401
    assert check_access({"name": "Dipesh", "role": "editor"}, "admin")[0] == 403
    assert check_access({"name": "Root", "role": "admin"}, "admin")[0] == 200

    print("All Day 34 debugging fixes verified successfully!")
