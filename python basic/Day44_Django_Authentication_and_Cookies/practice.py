"""
Day 44: Django Authentication & Cookies — Practice
Hands-on exercises covering password hashing, constant-time verification, and session cycling.
"""
import hashlib
import os
import hmac
from typing import Dict, Any, Tuple, Optional

# ---------------------------------------------------------------------
# Task 1: PBKDF2 Password Hasher & Verifier
# ---------------------------------------------------------------------
def hash_password(password: str, iterations: int = 100000, salt: Optional[bytes] = None) -> str:
    """
    Derives PBKDF2-HMAC-SHA256 hash formatted as:
    pbkdf2_sha256$<iterations>$<hex_salt>$<hex_hash>
    """
    if salt is None:
        salt = os.urandom(16)
    derived = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return f"pbkdf2_sha256${iterations}${salt.hex()}${derived.hex()}"

def verify_password(password: str, encoded_hash: str) -> bool:
    """Verifies password using constant-time comparison."""
    parts = encoded_hash.split("$")
    if len(parts) != 4 or parts[0] != "pbkdf2_sha256":
        return False
    iterations = int(parts[1])
    salt = bytes.fromhex(parts[2])
    target_hash = parts[3]

    candidate = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return hmac.compare_digest(candidate.hex(), target_hash)


# ---------------------------------------------------------------------
# Task 2: Session Store with Key Rotation
# ---------------------------------------------------------------------
class SessionStore:
    def __init__(self):
        self._sessions: Dict[str, Dict[str, Any]] = {}

    def create_session(self, data: Dict[str, Any]) -> str:
        session_key = os.urandom(20).hex()
        self._sessions[session_key] = dict(data)
        return session_key

    def rotate_session_key(self, old_key: str) -> str:
        """Rotates session key to defeat session fixation attacks."""
        if old_key not in self._sessions:
            raise KeyError("Invalid old session key")
        data = self._sessions.pop(old_key)
        new_key = os.urandom(20).hex()
        self._sessions[new_key] = data
        return new_key

    def get_session(self, key: str) -> Optional[Dict[str, Any]]:
        return self._sessions.get(key)


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 44 Practice Tests ---")

    # Test Task 1
    raw_pass = "MySecretP@ssword2026"
    stored_hash = hash_password(raw_pass, iterations=10000)  # Lower iterations for fast test
    assert stored_hash.startswith("pbkdf2_sha256$10000$")
    assert verify_password(raw_pass, stored_hash) is True
    assert verify_password("WrongPassword", stored_hash) is False

    # Test Task 2
    store = SessionStore()
    k1 = store.create_session({"user_id": 42, "role": "admin"})
    assert store.get_session(k1)["user_id"] == 42

    k2 = store.rotate_session_key(k1)
    assert k2 != k1
    assert store.get_session(k1) is None      # Old key destroyed!
    assert store.get_session(k2)["user_id"] == 42  # State preserved!

    print("All Day 44 practice assertions passed successfully!")
