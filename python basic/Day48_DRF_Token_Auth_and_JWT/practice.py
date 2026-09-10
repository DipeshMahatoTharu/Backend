"""
Day 48: DRF Token Auth & JWT — Practice
Hands-on exercises covering JWT base64url encoding, HMAC-SHA256 signature verification, and expiration validation.
"""
import base64
import json
import hmac
import hashlib
import time
from typing import Dict, Any, Tuple, Optional

# ---------------------------------------------------------------------
# Task 1: Base64URL Encoding & Decoding Helpers
# ---------------------------------------------------------------------
def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")

def b64url_decode(data_str: str) -> bytes:
    padding = 4 - (len(data_str) % 4)
    if padding != 4:
        data_str += "=" * padding
    return base64.urlsafe_b64decode(data_str.encode("utf-8"))


# ---------------------------------------------------------------------
# Task 2: JWT Signer & Verifier
# ---------------------------------------------------------------------
def create_jwt(payload: Dict[str, Any], secret_key: str, expires_in_seconds: int = 900) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    payload_copy = dict(payload)
    payload_copy["exp"] = int(time.time()) + expires_in_seconds
    payload_copy["iat"] = int(time.time())

    h_bytes = b64url_encode(json.dumps(header).encode("utf-8"))
    p_bytes = b64url_encode(json.dumps(payload_copy).encode("utf-8"))
    signing_input = f"{h_bytes}.{p_bytes}"

    signature = hmac.new(secret_key.encode("utf-8"), signing_input.encode("utf-8"), hashlib.sha256).digest()
    sig_str = b64url_encode(signature)

    return f"{signing_input}.{sig_str}"

def verify_jwt(token: str, secret_key: str) -> Tuple[bool, Optional[Dict[str, Any]], str]:
    parts = token.split(".")
    if len(parts) != 3:
        return False, None, "Invalid token format"

    h_str, p_str, sig_str = parts
    signing_input = f"{h_str}.{p_str}"

    # Recalculate signature
    expected_sig = hmac.new(secret_key.encode("utf-8"), signing_input.encode("utf-8"), hashlib.sha256).digest()
    if not hmac.compare_digest(b64url_encode(expected_sig), sig_str):
        return False, None, "Signature verification failed"

    # Decode payload
    try:
        payload = json.loads(b64url_decode(p_str).decode("utf-8"))
    except Exception:
        return False, None, "Malformed payload"

    # Check expiration
    if payload.get("exp", 0) < time.time():
        return False, None, "Token has expired"

    return True, payload, "Valid"


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 48 Practice Tests ---")

    secret = "my-super-secret-key-32-chars-long"

    # Test Task 1 & 2
    tok = create_jwt({"user_id": 42, "role": "admin"}, secret, expires_in_seconds=3600)
    is_valid, payload, msg = verify_jwt(tok, secret)
    assert is_valid is True
    assert payload["user_id"] == 42
    assert payload["role"] == "admin"
    assert msg == "Valid"

    # Test Tampered Token
    tampered = tok[:-5] + "XXXXX"
    is_valid, _, msg = verify_jwt(tampered, secret)
    assert is_valid is False
    assert "Signature verification failed" in msg

    # Test Expired Token
    expired_tok = create_jwt({"user_id": 99}, secret, expires_in_seconds=-10)
    is_valid, _, msg = verify_jwt(expired_tok, secret)
    assert is_valid is False
    assert "expired" in msg

    print("All Day 48 practice assertions passed successfully!")
