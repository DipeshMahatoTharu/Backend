"""
Day 44: Django Authentication & Cookies — Debugging
Diagnose and fix 3 critical authentication and session security vulnerabilities.
"""
import hmac
from typing import Dict, Any

# ---------------------------------------------------------------------
# Bug 1: Timing Attack on Password Hash Comparison
# Problem: An engineer checked passwords using `candidate == target_hash`.
# Standard string `==` exits on the first mismatched byte, allowing attackers
# to measure microsecond latency differences to reverse engineer hashes.
# Fix: Use `hmac.compare_digest()` for constant-time comparison.
# ---------------------------------------------------------------------
def compare_hashes_secure(candidate: str, target: str) -> bool:
    # BUGGY VERSION:
    # return candidate == target # Leaks timing information!

    # FIXED VERSION:
    return hmac.compare_digest(candidate, target)


# ---------------------------------------------------------------------
# Bug 2: Plaintext Password Assignment
# Problem: A developer created a user by doing `user.password = raw_password`
# instead of `user.set_password(raw_password)`. Passwords were saved as plain text!
# Fix: Force PBKDF2 password setting.
# ---------------------------------------------------------------------
class MockUserModel:
    def __init__(self):
        self.password = ""

    def set_password(self, raw_password: str):
        import hashlib
        self.password = f"pbkdf2_sha256$fake${hashlib.sha256(raw_password.encode()).hexdigest()}"

def update_user_password(user: MockUserModel, raw_pass: str):
    # BUGGY VERSION:
    # user.password = raw_pass # Saved in plaintext!

    # FIXED VERSION:
    user.set_password(raw_pass)


# ---------------------------------------------------------------------
# Bug 3: Insecure Cookies Exposing Session to JavaScript
# Problem: Session cookie was issued without `HttpOnly`, allowing Cross-Site
# Scripting (XSS) attacks to steal `document.cookie`.
# Fix: Enforce `httponly=True` and `secure=True`.
# ---------------------------------------------------------------------
def build_cookie_headers(session_id: str) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return {"Set-Cookie": f"sessionid={session_id}; Path=/"}

    # FIXED VERSION:
    return {
        "Set-Cookie": f"sessionid={session_id}; Path=/; HttpOnly; Secure; SameSite=Lax"
    }


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    assert compare_hashes_secure("hash123", "hash123") is True
    assert compare_hashes_secure("hash123", "hash999") is False

    # Test Bug 2 fix
    usr = MockUserModel()
    update_user_password(usr, "Secret123")
    assert usr.password != "Secret123"
    assert usr.password.startswith("pbkdf2_sha256$")

    # Test Bug 3 fix
    header = build_cookie_headers("sess_999")
    assert "HttpOnly" in header["Set-Cookie"]
    assert "Secure" in header["Set-Cookie"]

    print("All Day 44 debugging fixes verified successfully!")
