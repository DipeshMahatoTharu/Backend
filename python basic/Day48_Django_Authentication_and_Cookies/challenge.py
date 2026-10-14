"""
Day 44 Daily Challenge: Secure Authentication & Session Lifecycle Manager

Problem:
Implement a full-featured Authentication Service that simulates Django's auth system:
1. User registration with password hashing (PBKDF2).
2. `authenticate(username, password)`: Returns User if valid, else None. Uses constant-time comparison.
3. `login(request, user)`: Attaches user to session, regenerates session ID (prevents fixation), sets `HttpOnly` cookie.
4. `logout(request)`: Flushes session data and clears cookies.
"""
import os
import hashlib
import hmac
from typing import Dict, Any, Optional

class User:
    def __init__(self, user_id: int, username: str, password_hash: str):
        self.id = user_id
        self.username = username
        self.password_hash = password_hash

class HttpRequest:
    def __init__(self):
        self.session: Dict[str, Any] = {}
        self.session_key: Optional[str] = None
        self.user: Optional[User] = None
        self.cookies_to_set: Dict[str, Dict[str, Any]] = {}

class AuthService:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.sessions: Dict[str, Dict[str, Any]] = {}
        self._next_id = 1

    def register(self, username: str, password: str) -> User:
        salt = os.urandom(16)
        derived = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 10000)
        p_hash = f"pbkdf2_sha256$10000${salt.hex()}${derived.hex()}"
        user = User(self._next_id, username, p_hash)
        self._next_id += 1
        self.users[username.lower()] = user
        return user

    def authenticate(self, username: str, password: str) -> Optional[User]:
        user = self.users.get(username.lower())
        if not user:
            return None

        parts = user.password_hash.split("$")
        iterations = int(parts[1])
        salt = bytes.fromhex(parts[2])
        target_hash = parts[3]

        candidate = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
        if hmac.compare_digest(candidate.hex(), target_hash):
            return user
        return None

    def login(self, request: HttpRequest, user: User):
        # Prevent session fixation: create fresh session key
        new_key = os.urandom(20).hex()
        request.session_key = new_key
        request.session = {"_auth_user_id": user.id}
        request.user = user
        self.sessions[new_key] = request.session

        # Set secure session cookie
        request.cookies_to_set["sessionid"] = {
            "value": new_key,
            "httponly": True,
            "secure": True,
            "samesite": "Lax"
        }

    def logout(self, request: HttpRequest):
        if request.session_key in self.sessions:
            del self.sessions[request.session_key]
        request.session = {}
        request.session_key = None
        request.user = None
        request.cookies_to_set["sessionid"] = {"value": "", "max_age": 0}


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    auth = AuthService()

    # 1. Register User
    u = auth.register("dipesh", "StrongPass2026!")
    assert u.id == 1
    assert "pbkdf2_sha256" in u.password_hash

    # 2. Authenticate Valid & Invalid
    assert auth.authenticate("dipesh", "StrongPass2026!") is not None
    assert auth.authenticate("dipesh", "WrongPass") is None
    assert auth.authenticate("unknown_user", "Pass") is None

    # 3. Login
    req = HttpRequest()
    authenticated_user = auth.authenticate("dipesh", "StrongPass2026!")
    auth.login(req, authenticated_user)

    assert req.user.username == "dipesh"
    assert req.session_key is not None
    assert req.cookies_to_set["sessionid"]["httponly"] is True

    # 4. Logout
    sess_id = req.session_key
    auth.logout(req)
    assert req.user is None
    assert req.session_key is None
    assert sess_id not in auth.sessions  # Purged from server memory

    print("All AuthService challenge tests passed successfully!")
