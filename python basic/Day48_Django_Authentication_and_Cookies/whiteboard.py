"""
============================================================
DAY 44 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Constant-Time PBKDF2 Password Verifier & Hash Upgrader

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a password authentication and upgrade validator:
`verify_and_needs_rehash(password: str, stored_hash: str, desired_iterations: int = 600000) -> tuple[bool, bool]`
that:
1. Verifies the user's password in constant time. Returns `(False, False)` if wrong.
2. If correct, checks if the hash's iteration count is lower than `desired_iterations`.
   Returns `(True, True)` if credentials are valid BUT the hash needs an upgrade to stronger iterations.
   Returns `(True, False)` if credentials are valid and iteration strength is up-to-date.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Return `(is_valid: bool, needs_rehash: bool)`.
- Use `hmac.compare_digest` for the hash match.

============================================================
MY APPROACH:
============================================================
1. Parse `stored_hash`: format `pbkdf2_sha256$<iterations>$<salt>$<hash>`.
2. Compute candidate hash with parsed iterations and salt.
3. Compare using `hmac.compare_digest`.
4. If valid, check if `iterations < desired_iterations`.
"""
import hashlib
import hmac
from typing import Tuple

def verify_and_needs_rehash(password: str, stored_hash: str, desired_iterations: int = 600000) -> Tuple[bool, bool]:
    parts = stored_hash.split("$")
    if len(parts) != 4 or parts[0] != "pbkdf2_sha256":
        return False, False

    iterations = int(parts[1])
    salt = bytes.fromhex(parts[2])
    target = parts[3]

    candidate = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations).hex()

    if not hmac.compare_digest(candidate, target):
        return False, False

    needs_rehash = iterations < desired_iterations
    return True, needs_rehash


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    salt = b"1234567890abcdef"
    # Legacy hash with only 10,000 iterations
    legacy_derived = hashlib.pbkdf2_hmac("sha256", b"secret", salt, 10000).hex()
    legacy_hash = f"pbkdf2_sha256$10000${salt.hex()}${legacy_derived}"

    # Modern hash with 600,000 iterations
    modern_derived = hashlib.pbkdf2_hmac("sha256", b"secret", salt, 600000).hex()
    modern_hash = f"pbkdf2_sha256$600000${salt.hex()}${modern_derived}"

    # Test 1: Wrong password
    valid, rehash = verify_and_needs_rehash("wrong", legacy_hash, desired_iterations=600000)
    assert valid is False and rehash is False

    # Test 2: Valid password, needs rehash
    valid, rehash = verify_and_needs_rehash("secret", legacy_hash, desired_iterations=600000)
    assert valid is True and rehash is True

    # Test 3: Valid password, up-to-date
    valid, rehash = verify_and_needs_rehash("secret", modern_hash, desired_iterations=600000)
    assert valid is True and rehash is False

    print("Whiteboard Day 44 challenge passed successfully!")
