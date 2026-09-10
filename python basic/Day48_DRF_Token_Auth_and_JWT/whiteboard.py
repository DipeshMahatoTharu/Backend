"""
============================================================
DAY 48 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Cryptographic Bearer Token Extractor & Validator

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement an HTTP Authorization header parser:
`authenticate_header(auth_header: str, secret_key: str) -> tuple[bool, int, str]`
that:
1. Parses standard `Authorization: Bearer <token>` string.
2. Returns `(False, 0, "Invalid authorization header")` if missing or not Bearer.
3. Recomputes HMAC-SHA256 signature and validates expiration.
4. Returns `(True, user_id, "Authenticated")` if valid.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Do not use third-party JWT libraries; use Python standard `hmac`, `hashlib`, `base64`, `json`.
- Constant-time signature comparison with `hmac.compare_digest`.

============================================================
MY APPROACH:
============================================================
1. Check `auth_header.startswith("Bearer ")`. Extract token string.
2. Split token by `.`. Verify 3 parts.
3. Verify signature matches HMAC-SHA256.
4. Parse payload JSON and verify `exp > time.time()`.
"""
import base64
import json
import hmac
import hashlib
import time
from typing import Tuple

def b64_dec(s: str) -> bytes:
    pad = 4 - (len(s) % 4)
    if pad != 4: s += "=" * pad
    return base64.urlsafe_b64decode(s.encode("utf-8"))

def authenticate_header(auth_header: str, secret_key: str) -> Tuple[bool, int, str]:
    if not auth_header or not auth_header.startswith("Bearer "):
        return False, 0, "Invalid authorization header"

    raw_token = auth_header[7:].strip()
    parts = raw_token.split(".")
    if len(parts) != 3:
        return False, 0, "Malformed token"

    h_str, p_str, sig_str = parts
    signing_input = f"{h_str}.{p_str}"
    expected_sig = hmac.new(secret_key.encode("utf-8"), signing_input.encode("utf-8"), hashlib.sha256).digest()
    expected_sig_b64 = base64.urlsafe_b64encode(expected_sig).rstrip(b"=").decode("utf-8")

    if not hmac.compare_digest(expected_sig_b64, sig_str):
        return False, 0, "Signature verification failed"

    try:
        payload = json.loads(b64_dec(p_str).decode("utf-8"))
    except Exception:
        return False, 0, "Malformed payload"

    if payload.get("exp", 0) < time.time():
        return False, 0, "Token expired"

    user_id = payload.get("user_id", 0)
    return True, user_id, "Authenticated"


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    secret = "my-secret-key-32-chars-test"

    # Craft test token
    h = base64.urlsafe_b64encode(b'{"alg":"HS256"}').rstrip(b'=').decode()
    p_data = json.dumps({"user_id": 99, "exp": int(time.time()) + 300})
    p = base64.urlsafe_b64encode(p_data.encode()).rstrip(b'=').decode()
    sig = hmac.new(secret.encode(), f"{h}.{p}".encode(), hashlib.sha256).digest()
    sig_b64 = base64.urlsafe_b64encode(sig).rstrip(b'=').decode()
    valid_token = f"{h}.{p}.{sig_b64}"

    # 1. Valid header
    ok, uid, msg = authenticate_header(f"Bearer {valid_token}", secret)
    assert ok is True
    assert uid == 99

    # 2. Invalid header scheme (Basic instead of Bearer)
    ok, _, msg = authenticate_header("Basic abc", secret)
    assert ok is False

    # 3. Wrong secret
    ok, _, msg = authenticate_header(f"Bearer {valid_token}", "wrong-secret")
    assert ok is False
    assert "Signature" in msg

    print("Whiteboard Day 48 challenge passed successfully!")
