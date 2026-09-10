"""
Day 49: DRF Object-Level Permissions — Debugging
Diagnose and fix 3 common object permission vulnerabilities.
"""
from typing import Dict, Any, Optional

SAFE_METHODS = ("GET", "HEAD", "OPTIONS")

# ---------------------------------------------------------------------
# Bug 1: Missing `self.check_object_permissions()`
# Problem: A developer implemented a custom `put()` in an APIView, but queried
# the model directly via `Article.objects.get(pk=pk)` without calling
# `self.check_object_permissions(request, obj)`.
# Fix: Ensure object permissions are explicitly evaluated.
# ---------------------------------------------------------------------
class MockView:
    def __init__(self, permission_fn):
        self.permission_fn = permission_fn

    def get_object(self, obj: Dict[str, Any], user_id: int, method: str) -> Dict[str, Any]:
        # BUGGY VERSION:
        # return obj # Perm check skipped!

        # FIXED VERSION:
        if not self.permission_fn(user_id, method, obj):
            raise PermissionError("Access denied to object")
        return obj


# ---------------------------------------------------------------------
# Bug 2: Missing SAFE_METHODS Exemption in Read-Only Checks
# Problem: An engineer wrote `has_object_permission` that only checked `obj.owner == user`.
# This blocked everyone from viewing public articles via GET!
# Fix: Allow SAFE_METHODS unconditionally.
# ---------------------------------------------------------------------
def check_owner_or_read_only(user_id: Optional[int], method: str, obj: Dict[str, Any]) -> bool:
    # BUGGY VERSION:
    # return obj.get('owner_id') == user_id # Blocked GET requests!

    # FIXED VERSION:
    if method in SAFE_METHODS:
        return True
    return user_id is not None and obj.get("owner_id") == user_id


# ---------------------------------------------------------------------
# Bug 3: Crash on Anonymous User in Object Permission
# Problem: `obj.owner == request.user.id` crashes with `AttributeError`
# when `request.user` is None.
# Fix: Guard against unauthenticated requests.
# ---------------------------------------------------------------------
def safe_ownership_check(user: Optional[Dict[str, Any]], obj: Dict[str, Any]) -> bool:
    # BUGGY VERSION:
    # return obj['owner_id'] == user['id'] # Crashes if user is None!

    # FIXED VERSION:
    if not user:
        return False
    return obj.get("owner_id") == user.get("id")


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    doc = {"id": 1, "owner_id": 42}

    # Test Bug 1 fix
    view = MockView(lambda uid, m, o: o["owner_id"] == uid)
    assert view.get_object(doc, user_id=42, method="PUT")["id"] == 1
    try:
        view.get_object(doc, user_id=99, method="PUT")
        assert False, "Should raise PermissionError"
    except PermissionError:
        pass

    # Test Bug 2 fix
    assert check_owner_or_read_only(None, "GET", doc) is True
    assert check_owner_or_read_only(None, "DELETE", doc) is False

    # Test Bug 3 fix
    assert safe_ownership_check(None, doc) is False
    assert safe_ownership_check({"id": 42}, doc) is True

    print("All Day 49 debugging fixes verified successfully!")
