"""
Day 48 Daily Challenge: Stateless JWT Issuer & Blacklist Engine

Problem:
Implement an enterprise-grade Token Service simulating `djangorestframework-simplejwt`:
1. Issue Token Pair: Generates short-lived `access_token` (15 mins) and long-lived `refresh_token` (7 days).
2. Token Verification: Validates signatures, expiration, and checks blacklist.
3. Refresh Token Rotation: Accepts valid refresh token, blacklists it, and issues a fresh token pair.
4. Blacklist: Revokes refresh tokens upon user logout.
"""
import base64
import json
import hmac
import hashlib
import time
import uuid
from typing import Dict, Any, Tuple, Optional, Set

def b64url_enc(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode("utf-8")

def b64url_dec(s: str) -> bytes:
    pad = 4 - (len(s) % 4)
    if pad != 4: s += "=" * pad
    return base64.urlsafe_b64decode(s.encode("utf-8"))

class JWTService:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.blacklist: Set[str] = set()

    def _generate_token(self, payload: Dict[str, Any], exp_seconds: int) -> str:
        header = {"alg": "HS256", "typ": "JWT"}
        data = dict(payload)
        data["jti"] = str(uuid.uuid4())
        data["iat"] = int(time.time())
        data["exp"] = int(time.time()) + exp_seconds

        h_b64 = b64url_enc(json.dumps(header).encode("utf-8"))
        p_b64 = b64url_enc(json.dumps(data).encode("utf-8"))
        signing_input = f"{h_b64}.{p_b64}"
        sig = hmac.new(self.secret_key.encode("utf-8"), signing_input.encode("utf-8"), hashlib.sha256).digest()
        return f"{signing_input}.{b64url_enc(sig)}"

    def issue_token_pair(self, user_id: int) -> Dict[str, str]:
        access = self._generate_token({"user_id": user_id, "token_type": "access"}, exp_seconds=900)
        refresh = self._generate_token({"user_id": user_id, "token_type": "refresh"}, exp_seconds=86400 * 7)
        return {"access": access, "refresh": refresh}

    def decode_and_verify(self, token: str, expected_type: str) -> Dict[str, Any]:
        parts = token.split(".")
        if len(parts) != 3:
            raise ValueError("Malformed token")
        h_str, p_str, sig_str = parts
        signing_input = f"{h_str}.{p_str}"
        expected_sig = hmac.new(self.secret_key.encode("utf-8"), signing_input.encode("utf-8"), hashlib.sha256).digest()
        if not hmac.compare_digest(b64url_enc(expected_sig), sig_str):
            raise ValueError("Invalid token signature")

        payload = json.loads(b64url_dec(p_str).decode("utf-8"))
        if payload.get("exp", 0) < time.time():
            raise ValueError("Token expired")
        if payload.get("jti") in self.blacklist:
            raise ValueError("Token has been blacklisted")
        if payload.get("token_type") != expected_type:
            raise ValueError(f"Expected {expected_type} token, received {payload.get('token_type')}")

        return payload

    def refresh(self, refresh_token: str) -> Dict[str, str]:
        payload = self.decode_and_verify(refresh_token, expected_type="refresh")
        # Blacklist old refresh token (Token Rotation)
        self.blacklist.add(payload["jti"])
        # Issue brand new pair
        return self.issue_token_pair(payload["user_id"])

    def logout(self, refresh_token: str):
        payload = self.decode_and_verify(refresh_token, expected_type="refresh")
        self.blacklist.add(payload["jti"])


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    jwt_svc = JWTService(secret_key="my-production-jwt-secret-key-32-chars")

    # 1. Issue pair
    tokens = jwt_svc.issue_token_pair(user_id=100)
    access_tok = tokens["access"]
    refresh_tok = tokens["refresh"]

    # 2. Verify access
    p_access = jwt_svc.decode_and_verify(access_tok, expected_type="access")
    assert p_access["user_id"] == 100

    # 3. Rotate refresh token
    new_tokens = jwt_svc.refresh(refresh_tok)
    assert new_tokens["access"] != access_tok
    assert new_tokens["refresh"] != refresh_tok

    # 4. Verify old refresh token is rejected (Blacklisted)
    try:
        jwt_svc.refresh(refresh_tok)
        assert False, "Old refresh token should be blacklisted!"
    except ValueError as ve:
        assert "blacklisted" in str(ve)

    # 5. Logout
    jwt_svc.logout(new_tokens["refresh"])
    try:
        jwt_svc.decode_and_verify(new_tokens["refresh"], expected_type="refresh")
        assert False, "Logged-out token should be rejected"
    except ValueError as ve:
        assert "blacklisted" in str(ve)

    print("All JWTService challenge tests passed successfully!")
