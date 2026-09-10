"""
Day 45 Daily Challenge: Enterprise RBAC Authorization Engine & Security Middleware

Problem:
Implement a comprehensive authorization and security middleware engine that:
1. Enforces Role-Based Access Control (Roles -> Permissions mapping).
2. Supports Object-Level ownership verification.
3. Automatically injects OWASP security headers (HSTS, X-Frame-Options, CSP, nosniff).
4. Handles unauthorized requests with clean 401 Unauthenticated or 403 Forbidden responses.
"""
from typing import Dict, List, Set, Any, Optional, Callable

class AuthContext:
    def __init__(self, user_id: Optional[int], roles: List[str]):
        self.user_id = user_id
        self.roles = roles
        self.is_authenticated = user_id is not None

class SecurityEngine:
    def __init__(self):
        self.role_permissions: Dict[str, Set[str]] = {
            "admin": {"*"},
            "editor": {"post.create", "post.update", "post.delete_own"},
            "viewer": {"post.read"}
        }

    def check_permission(self, ctx: AuthContext, perm: str) -> bool:
        if not ctx.is_authenticated:
            return False
        for r in ctx.roles:
            perms = self.role_permissions.get(r, set())
            if "*" in perms or perm in perms:
                return True
        return False

    def check_object_ownership(self, ctx: AuthContext, resource_owner_id: int) -> bool:
        if not ctx.is_authenticated:
            return False
        if "admin" in ctx.roles:
            return True
        return ctx.user_id == resource_owner_id

    def process_request(self, ctx: AuthContext, required_perm: str, resource_owner_id: Optional[int], handler: Callable) -> Dict[str, Any]:
        # 1. Authentication check
        if not ctx.is_authenticated:
            return {"status": 401, "body": {"error": "Authentication required"}}

        # 2. Global permission check
        if not self.check_permission(ctx, required_perm):
            return {"status": 403, "body": {"error": f"Missing permission: {required_perm}"}}

        # 3. Object-level check (if required)
        if resource_owner_id is not None and not self.check_object_ownership(ctx, resource_owner_id):
            return {"status": 403, "body": {"error": "Access denied: you do not own this resource"}}

        # 4. Execute handler & inject headers
        response_body = handler()
        return {
            "status": 200,
            "headers": {
                "X-Frame-Options": "DENY",
                "X-Content-Type-Options": "nosniff",
                "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
            },
            "body": response_body
        }


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    engine = SecurityEngine()

    def dummy_action():
        return {"data": "Secure payload"}

    # 1. Unauthenticated request -> 401
    anon_ctx = AuthContext(user_id=None, roles=[])
    res1 = engine.process_request(anon_ctx, "post.create", None, dummy_action)
    assert res1["status"] == 401

    # 2. Authenticated but missing permission -> 403
    viewer_ctx = AuthContext(user_id=10, roles=["viewer"])
    res2 = engine.process_request(viewer_ctx, "post.create", None, dummy_action)
    assert res2["status"] == 403

    # 3. Authenticated, has permission, but fails object ownership -> 403
    editor_ctx = AuthContext(user_id=20, roles=["editor"])
    res3 = engine.process_request(editor_ctx, "post.update", resource_owner_id=99, handler=dummy_action)
    assert res3["status"] == 403

    # 4. Authenticated, has permission, owns resource -> 200 + Security headers
    res4 = engine.process_request(editor_ctx, "post.update", resource_owner_id=20, handler=dummy_action)
    assert res4["status"] == 200
    assert res4["headers"]["X-Frame-Options"] == "DENY"
    assert res4["body"]["data"] == "Secure payload"

    # 5. Admin bypasses object ownership -> 200
    admin_ctx = AuthContext(user_id=999, roles=["admin"])
    res5 = engine.process_request(admin_ctx, "post.update", resource_owner_id=20, handler=dummy_action)
    assert res5["status"] == 200

    print("All SecurityEngine challenge tests passed successfully!")
