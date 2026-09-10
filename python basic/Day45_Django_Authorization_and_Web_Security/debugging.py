"""
Day 45: Django Authorization & Web Security — Debugging
Diagnose and fix 3 common authorization vulnerabilities and security misconfigurations.
"""
from typing import Dict, Any, Optional

# ---------------------------------------------------------------------
# Bug 1: IDOR in Profile Update View
# Problem: An endpoint takes `target_user_id` from the URL and updates bio
# without verifying that `request.user.id == target_user_id`.
# Any logged-in user can change anyone's profile!
# Fix: Enforce ownership check.
# ---------------------------------------------------------------------
def update_profile(current_user_id: int, target_user_id: int, new_bio: str) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return {"updated_user": target_user_id, "bio": new_bio} # Anyone can update anyone!

    # FIXED VERSION:
    if current_user_id != target_user_id:
        raise PermissionError("Forbidden: Cannot modify another user's profile.")
    return {"updated_user": target_user_id, "bio": new_bio}


# ---------------------------------------------------------------------
# Bug 2: Missing `X-Frame-Options` Allowing Clickjacking
# Problem: An administrative banking portal did not set X-Frame-Options.
# An attacker embedded the portal in a transparent iframe on `claim-prize.com`.
# Fix: Include `X-Frame-Options: DENY`.
# ---------------------------------------------------------------------
def build_portal_response(body_html: str) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return {"status": 200, "headers": {}, "body": body_html}

    # FIXED VERSION:
    return {
        "status": 200,
        "headers": {"X-Frame-Options": "DENY"},
        "body": body_html
    }


# ---------------------------------------------------------------------
# Bug 3: Role Escalation via Missing Superuser Guard
# Problem: An editor can promote other users to admin because the view
# only checked `@login_required` instead of `@user_passes_test(lambda u: u.is_superuser)`.
# Fix: Enforce superuser authorization.
# ---------------------------------------------------------------------
def promote_user_to_admin(requester_is_superuser: bool, target_user: Dict[str, Any]) -> Dict[str, Any]:
    # BUGGY VERSION:
    # target_user['is_staff'] = True

    # FIXED VERSION:
    if not requester_is_superuser:
        raise PermissionError("Only superusers can grant administrative roles.")
    target_user["is_staff"] = True
    return target_user


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    try:
        update_profile(current_user_id=1, target_user_id=2, new_bio="Hacked bio")
        assert False, "Should raise PermissionError"
    except PermissionError:
        pass
    assert update_profile(1, 1, "My bio")["bio"] == "My bio"

    # Test Bug 2 fix
    resp = build_portal_response("<h1>Portal</h1>")
    assert resp["headers"].get("X-Frame-Options") == "DENY"

    # Test Bug 3 fix
    try:
        promote_user_to_admin(requester_is_superuser=False, target_user={})
        assert False, "Should raise PermissionError"
    except PermissionError:
        pass
    assert promote_user_to_admin(True, {})["is_staff"] is True

    print("All Day 45 debugging fixes verified successfully!")
