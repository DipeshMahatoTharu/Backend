"""
============================================================
DAY 49 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: RBAC & Object-Level Permission Evaluation Engine

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement `evaluate_access(user: dict, obj: dict, action: str) -> bool`:
Actions: "read", "update", "delete".

Rules:
1. If `user["role"] == "admin"`: Always returns `True` for all actions and objects.
2. If `user["role"] == "auditor"`: Can perform "read" on any object, but never "update" or "delete".
3. If `user["role"] == "member"`:
   - "read": Can read if `obj["is_public"] is True` OR `obj["owner_id"] == user["id"]`.
   - "update": Can update ONLY if `obj["owner_id"] == user["id"]`.
   - "delete": Cannot delete (only admins can delete).
4. Unauthenticated users (`user is None`):
   - Can only "read" if `obj["is_public"] is True`.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Return boolean `True` or `False`.
- Handle `user=None` cleanly without crashing.

============================================================
MY APPROACH:
============================================================
1. Handle unauthenticated user.
2. Check admin role.
3. Check auditor role.
4. Check member role against action rules.
"""
from typing import Dict, Any, Optional

def evaluate_access(user: Optional[Dict[str, Any]], obj: Dict[str, Any], action: str) -> bool:
    # 1. Unauthenticated
    if user is None:
        return action == "read" and obj.get("is_public", False)

    role = user.get("role", "member")

    # 2. Admin
    if role == "admin":
        return True

    # 3. Auditor
    if role == "auditor":
        return action == "read"

    # 4. Member
    if role == "member":
        is_owner = obj.get("owner_id") == user.get("id")
        if action == "read":
            return obj.get("is_public", False) or is_owner
        elif action == "update":
            return is_owner
        elif action == "delete":
            return False

    return False


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    public_doc = {"id": 1, "owner_id": 10, "is_public": True}
    private_doc = {"id": 2, "owner_id": 10, "is_public": False}

    owner = {"id": 10, "role": "member"}
    stranger = {"id": 20, "role": "member"}
    auditor = {"id": 99, "role": "auditor"}
    admin = {"id": 1, "role": "admin"}

    # 1. Admin can do everything
    assert evaluate_access(admin, private_doc, "delete") is True

    # 2. Auditor can read private doc, but cannot update
    assert evaluate_access(auditor, private_doc, "read") is True
    assert evaluate_access(auditor, private_doc, "update") is False

    # 3. Owner can update their private doc
    assert evaluate_access(owner, private_doc, "update") is True
    assert evaluate_access(owner, private_doc, "delete") is False

    # 4. Stranger cannot read or update private doc
    assert evaluate_access(stranger, private_doc, "read") is False
    assert evaluate_access(stranger, private_doc, "update") is False
    assert evaluate_access(stranger, public_doc, "read") is True

    # 5. Anonymous
    assert evaluate_access(None, public_doc, "read") is True
    assert evaluate_access(None, private_doc, "read") is False

    print("Whiteboard Day 49 challenge passed successfully!")
