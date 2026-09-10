"""
Day 45: Django Authorization & Web Security — Practice
Hands-on exercises covering RBAC evaluation, IDOR prevention, and security header injection.
"""
from typing import Dict, Any, List, Optional, Set

# ---------------------------------------------------------------------
# Task 1: RBAC Permission Evaluator
# ---------------------------------------------------------------------
class UserIdentity:
    def __init__(self, user_id: int, roles: List[str], permissions: Optional[Set[str]] = None):
        self.user_id = user_id
        self.roles = roles
        self.permissions = permissions or set()

def has_permission(user: Optional[UserIdentity], required_perm: str, role_perm_matrix: Dict[str, Set[str]]) -> bool:
    """
    Checks if user possesses required_perm through direct permissions or via assigned roles.
    """
    if not user:
        return False
    if "admin" in user.roles:
        return True  # Superuser bypass
    if required_perm in user.permissions:
        return True
    for r in user.roles:
        if required_perm in role_perm_matrix.get(r, set()):
            return True
    return False


# ---------------------------------------------------------------------
# Task 2: IDOR-Safe Object Resolver
# ---------------------------------------------------------------------
class Document:
    def __init__(self, doc_id: int, owner_id: int, is_public: bool, title: str):
        self.id = doc_id
        self.owner_id = owner_id
        self.is_public = is_public
        self.title = title

def get_document_secure(docs_db: Dict[int, Document], doc_id: int, requesting_user_id: int) -> Document:
    """
    Prevents IDOR: Only returns the document if it is public OR owned by the requester.
    Raises PermissionError if unauthorized, KeyError if not found.
    """
    if doc_id not in docs_db:
        raise KeyError("Document not found")
    doc = docs_db[doc_id]
    if not doc.is_public and doc.owner_id != requesting_user_id:
        raise PermissionError("Access denied: You do not own this private document.")
    return doc


# ---------------------------------------------------------------------
# Task 3: Security Header Injector
# ---------------------------------------------------------------------
def inject_security_headers(headers: Dict[str, str]) -> Dict[str, str]:
    """Enforces OWASP recommended transport and rendering headers."""
    sec_headers = dict(headers)
    sec_headers["X-Frame-Options"] = "DENY"
    sec_headers["X-Content-Type-Options"] = "nosniff"
    sec_headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    sec_headers["Content-Security-Policy"] = "default-src 'self'"
    return sec_headers


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 45 Practice Tests ---")

    # Test Task 1: RBAC
    matrix = {
        "editor": {"articles.create", "articles.edit"},
        "viewer": {"articles.view"}
    }
    u_editor = UserIdentity(1, roles=["editor"])
    assert has_permission(u_editor, "articles.create", matrix) is True
    assert has_permission(u_editor, "users.delete", matrix) is False

    u_admin = UserIdentity(2, roles=["admin"])
    assert has_permission(u_admin, "users.delete", matrix) is True

    # Test Task 2: IDOR prevention
    db = {
        101: Document(101, owner_id=1, is_public=False, title="Confidential Tax Report"),
        102: Document(102, owner_id=2, is_public=True, title="Public Roadmap")
    }
    # Owner access private
    assert get_document_secure(db, 101, requesting_user_id=1).title == "Confidential Tax Report"
    # Other user access public
    assert get_document_secure(db, 102, requesting_user_id=1).title == "Public Roadmap"
    # Other user attempts private IDOR
    try:
        get_document_secure(db, 101, requesting_user_id=2)
        assert False, "Should raise PermissionError"
    except PermissionError:
        pass

    # Test Task 3: Security headers
    resp_headers = inject_security_headers({})
    assert resp_headers["X-Frame-Options"] == "DENY"
    assert "max-age=31536000" in resp_headers["Strict-Transport-Security"]

    print("All Day 45 practice assertions passed successfully!")
