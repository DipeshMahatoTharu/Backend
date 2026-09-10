"""
Day 49: DRF Object-Level Permissions — Practice
Hands-on exercises covering custom BasePermission classes, SAFE_METHODS checks, and permission composition.
"""
from typing import Dict, Any, List, Optional

SAFE_METHODS = ("GET", "HEAD", "OPTIONS")

class RequestContext:
    def __init__(self, user_id: Optional[int], method: str = "GET", is_admin: bool = False):
        self.user_id = user_id
        self.method = method.upper()
        self.is_authenticated = user_id is not None
        self.is_admin = is_admin

class BasePermission:
    def has_permission(self, request: RequestContext) -> bool:
        return True
    def has_object_permission(self, request: RequestContext, obj: Dict[str, Any]) -> bool:
        return True

# ---------------------------------------------------------------------
# Task 1: IsAuthenticated Permission
# ---------------------------------------------------------------------
class IsAuthenticated(BasePermission):
    def has_permission(self, request: RequestContext) -> bool:
        return request.is_authenticated


# ---------------------------------------------------------------------
# Task 2: IsOwnerOrReadOnly Permission
# ---------------------------------------------------------------------
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request: RequestContext, obj: Dict[str, Any]) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.is_authenticated and obj.get("owner_id") == request.user_id


# ---------------------------------------------------------------------
# Task 3: Composite Permission Runner (AND logic)
# ---------------------------------------------------------------------
def check_all_permissions(permissions: List[BasePermission], request: RequestContext, obj: Optional[Dict[str, Any]] = None) -> bool:
    for p in permissions:
        if not p.has_permission(request):
            return False
        if obj is not None and not p.has_object_permission(request, obj):
            return False
    return True


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 49 Practice Tests ---")

    doc = {"id": 1, "title": "My Article", "owner_id": 42}

    # Test Task 1 & 2: Anonymous user reading doc
    anon_req = RequestContext(user_id=None, method="GET")
    perm_owner_or_ro = IsOwnerOrReadOnly()
    assert perm_owner_or_ro.has_object_permission(anon_req, doc) is True

    # Anonymous user editing doc -> False
    anon_put = RequestContext(user_id=None, method="PUT")
    assert perm_owner_or_ro.has_object_permission(anon_put, doc) is False

    # Owner editing doc -> True
    owner_put = RequestContext(user_id=42, method="PUT")
    assert perm_owner_or_ro.has_object_permission(owner_put, doc) is True

    # Non-owner editing doc -> False
    other_put = RequestContext(user_id=99, method="PUT")
    assert perm_owner_or_ro.has_object_permission(other_put, doc) is False

    # Test Task 3: Composite checking
    perms = [IsAuthenticated(), IsOwnerOrReadOnly()]
    assert check_all_permissions(perms, owner_put, doc) is True
    assert check_all_permissions(perms, other_put, doc) is False
    assert check_all_permissions(perms, anon_req, doc) is False  # Fails IsAuthenticated

    print("All Day 49 practice assertions passed successfully!")
