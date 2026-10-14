"""
Day 49 Daily Challenge: Object-Level Permission Evaluation Engine with Bitwise Combiners

Problem:
Implement a standalone permission system supporting:
1. BasePermission classes with `has_permission` and `has_object_permission`.
2. Bitwise operators `&` (AND) and `|` (OR) combining permission instances.
3. A controller method `check_object_permissions(request, obj)` that evaluates composite trees.
"""
from typing import Dict, Any, Optional

SAFE_METHODS = ("GET", "HEAD", "OPTIONS")

class RequestContext:
    def __init__(self, user_id: Optional[int], method: str = "GET", is_admin: bool = False):
        self.user_id = user_id
        self.method = method.upper()
        self.is_authenticated = user_id is not None
        self.is_admin = is_admin

class Permission:
    def has_permission(self, request: RequestContext) -> bool:
        return True
    def has_object_permission(self, request: RequestContext, obj: Dict[str, Any]) -> bool:
        return True

    def __and__(self, other: 'Permission') -> 'Permission':
        return AndPermission(self, other)

    def __or__(self, other: 'Permission') -> 'Permission':
        return OrPermission(self, other)

class AndPermission(Permission):
    def __init__(self, p1: Permission, p2: Permission):
        self.p1 = p1
        self.p2 = p2

    def has_permission(self, request: RequestContext) -> bool:
        return self.p1.has_permission(request) and self.p2.has_permission(request)

    def has_object_permission(self, request: RequestContext, obj: Dict[str, Any]) -> bool:
        return self.p1.has_object_permission(request, obj) and self.p2.has_object_permission(request, obj)

class OrPermission(Permission):
    def __init__(self, p1: Permission, p2: Permission):
        self.p1 = p1
        self.p2 = p2

    def has_permission(self, request: RequestContext) -> bool:
        return self.p1.has_permission(request) or self.p2.has_permission(request)

    def has_object_permission(self, request: RequestContext, obj: Dict[str, Any]) -> bool:
        return self.p1.has_object_permission(request, obj) or self.p2.has_object_permission(request, obj)


# Concrete permissions
class IsAuthenticated(Permission):
    def has_permission(self, request: RequestContext) -> bool:
        return request.is_authenticated

class IsAdminUser(Permission):
    def has_permission(self, request: RequestContext) -> bool:
        return request.is_admin
    def has_object_permission(self, request: RequestContext, obj: Dict[str, Any]) -> bool:
        return request.is_admin

class IsOwner(Permission):
    def has_object_permission(self, request: RequestContext, obj: Dict[str, Any]) -> bool:
        return request.is_authenticated and obj.get("owner_id") == request.user_id


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    doc = {"id": 1, "title": "Confidential", "owner_id": 10}

    # Policy: Must be authenticated AND (must be owner OR must be admin)
    policy = IsAuthenticated() & (IsOwner() | IsAdminUser())

    # 1. Owner access
    req_owner = RequestContext(user_id=10, is_admin=False)
    assert policy.has_permission(req_owner) is True
    assert policy.has_object_permission(req_owner, doc) is True

    # 2. Admin access (not owner)
    req_admin = RequestContext(user_id=99, is_admin=True)
    assert policy.has_permission(req_admin) is True
    assert policy.has_object_permission(req_admin, doc) is True

    # 3. Regular user (not owner, not admin)
    req_other = RequestContext(user_id=55, is_admin=False)
    assert policy.has_permission(req_other) is True
    assert policy.has_object_permission(req_other, doc) is False

    # 4. Anonymous user
    req_anon = RequestContext(user_id=None)
    assert policy.has_permission(req_anon) is False

    print("All Permission Combiner challenge tests passed successfully!")
