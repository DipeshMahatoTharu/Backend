"""
============================================================
DAY 45 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Multi-Tenant Object Access Control Evaluator

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
In a multi-tenant SaaS application, records belong to specific Organizations.
Implement `can_access_record(user: dict, record: dict, action: str) -> bool` that verifies:
1. Tenant Isolation: `user["org_id"] == record["org_id"]`. If organizations differ, always return `False`.
2. Action Authorization:
   - "read": Allowed for all organization members.
   - "edit": Allowed if `user["id"] == record["owner_id"]` OR `user["role"] == "org_admin"`.
   - "delete": Allowed ONLY if `user["role"] == "org_admin"`.
   - Any unknown action returns `False`.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Return boolean `True` or `False`.
- Never leak cross-tenant data even if user is an admin in their own org!

============================================================
MY APPROACH:
============================================================
1. Check tenant boundary: `user.get("org_id") == record.get("org_id")`. If not, return False.
2. Evaluate `action`:
   - "read": return True
   - "edit": return user["id"] == record["owner_id"] or user["role"] == "org_admin"
   - "delete": return user["role"] == "org_admin"
3. Return False for unknown actions.
"""
from typing import Dict, Any

def can_access_record(user: Dict[str, Any], record: Dict[str, Any], action: str) -> bool:
    # 1. Strict Tenant Boundary Isolation
    if user.get("org_id") != record.get("org_id"):
        return False

    # 2. Action evaluation
    role = user.get("role", "member")
    is_owner = user.get("id") == record.get("owner_id")

    if action == "read":
        return True
    elif action == "edit":
        return is_owner or role == "org_admin"
    elif action == "delete":
        return role == "org_admin"

    return False


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    doc_org1 = {"id": 100, "org_id": 1, "owner_id": 10, "title": "Quarterly Plan"}

    user_a = {"id": 10, "org_id": 1, "role": "member"}       # Owner in Org 1
    user_b = {"id": 11, "org_id": 1, "role": "member"}       # Peer in Org 1
    admin_org1 = {"id": 99, "org_id": 1, "role": "org_admin"} # Admin in Org 1
    admin_org2 = {"id": 88, "org_id": 2, "role": "org_admin"} # Admin in Org 2

    # 1. Tenant boundary: Org 2 admin CANNOT access Org 1 doc
    assert can_access_record(admin_org2, doc_org1, "read") is False
    assert can_access_record(admin_org2, doc_org1, "delete") is False

    # 2. Read access
    assert can_access_record(user_a, doc_org1, "read") is True
    assert can_access_record(user_b, doc_org1, "read") is True

    # 3. Edit access
    assert can_access_record(user_a, doc_org1, "edit") is True   # Owner can edit
    assert can_access_record(user_b, doc_org1, "edit") is False  # Peer cannot edit
    assert can_access_record(admin_org1, doc_org1, "edit") is True # Org Admin can edit

    # 4. Delete access
    assert can_access_record(user_a, doc_org1, "delete") is False # Member owner cannot delete
    assert can_access_record(admin_org1, doc_org1, "delete") is True # Org admin can delete

    print("Whiteboard Day 45 challenge passed successfully!")
