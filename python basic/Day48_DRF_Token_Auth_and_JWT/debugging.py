"""
Day 48: DRF Token Auth & JWT — Debugging
Diagnose and fix 3 critical JWT authentication flaws.
"""
from typing import Dict, Any, Optional

# ---------------------------------------------------------------------
# Bug 1: Missing Expiration Verification
# Problem: An engineer decoded JWT payloads without checking `exp`.
# Expired tokens remained valid forever!
# Fix: Enforce `exp > current_timestamp`.
# ---------------------------------------------------------------------
import time

def is_token_expired(payload: Dict[str, Any], current_time: Optional[int] = None) -> bool:
    now = current_time if current_time is not None else int(time.time())
    # BUGGY VERSION:
    # return False # Never checked exp!

    # FIXED VERSION:
    return payload.get("exp", 0) <= now


# ---------------------------------------------------------------------
# Bug 2: Missing 'Bearer ' Prefix in Authorization Header
# Problem: A view did `token = request.headers['Authorization']` without stripping
# the 'Bearer ' prefix, causing decoding to fail on `'Bearer eyJ...'`.
# Fix: Strip 'Bearer ' cleanly.
# ---------------------------------------------------------------------
def extract_bearer_token(auth_header: Optional[str]) -> Optional[str]:
    # BUGGY VERSION:
    # return auth_header

    # FIXED VERSION:
    if not auth_header or not auth_header.startswith("Bearer "):
        return None
    return auth_header[7:].strip()


# ---------------------------------------------------------------------
# Bug 3: Using Refresh Token as Access Token
# Problem: An API endpoint accepted a refresh token to perform actions,
# bypassing the short expiration intended for access tokens.
# Fix: Enforce `token_type == 'access'`.
# ---------------------------------------------------------------------
def validate_token_type(payload: Dict[str, Any], expected: str = "access") -> bool:
    # BUGGY VERSION:
    # return True

    # FIXED VERSION:
    return payload.get("token_type") == expected


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    past = {"exp": 1000}
    future = {"exp": 9999999999}
    assert is_token_expired(past, current_time=2000) is True
    assert is_token_expired(future, current_time=2000) is False

    # Test Bug 2 fix
    assert extract_bearer_token("Bearer eyJhbGciOi...") == "eyJhbGciOi..."
    assert extract_bearer_token("Basic dXNlcjpwYXNz") is None

    # Test Bug 3 fix
    assert validate_token_type({"token_type": "access"}, "access") is True
    assert validate_token_type({"token_type": "refresh"}, "access") is False

    print("All Day 48 debugging fixes verified successfully!")
