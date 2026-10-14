# Day 48 — DRF Token Authentication & JSON Web Tokens (JWT)

## 🎯 Learning Objectives
- Compare Database Token Authentication (`rest_framework.authtoken`) vs Stateless JSON Web Tokens (`djangorestframework-simplejwt`).
- Master the 3 parts of a JWT: Header, Payload (Claims: `exp`, `iat`, `user_id`), and Signature.
- Understand Access Tokens (short-lived: 5-15 mins) vs Refresh Tokens (long-lived: 7-30 days).
- Implement Token Rotation & Blacklisting to revoke compromised JWT sessions.
- Enforce `Authorization: Bearer <token>` HTTP header parsing.

---

## 📚 Core Backend Concepts

### 1. The Physical Anatomy of a JWT
A JWT consists of 3 Base64URL-encoded segments separated by dots (`.`):
```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMDEsImV4cCI6MTc4OTA5MjgwMH0.db53F8q...
[-------- HEADER --------] . [--------- PAYLOAD ---------] . [--- SIGNATURE ---]
```
1. **Header**: Specifies cryptographic signing algorithm (e.g. `{"alg": "HS256", "typ": "JWT"}`).
2. **Payload**: Claims metadata (e.g. `{"user_id": 101, "exp": 1789092800}`).
3. **Signature**: `HMACSHA256(Base64URL(header) + "." + Base64URL(payload), SECRET_KEY)`.

### 2. Stateless Verification Lifecycle
- Unlike sessions or database tokens, the backend does **not** query the database to verify a JWT!
- It recalculates the signature using `SECRET_KEY`. If the signature matches and `exp` is in the future, the identity is cryptographically proven in sub-millisecond time.

### 3. Refresh Token Rotation
```text
Client                       Server
  |                            |
  |--- POST /token/refresh --->| (Sends old refresh token)
  |                            |
  |<-- Access + NEW Refresh ---| (Server returns fresh access token + brand new refresh token)
  |                            | (Old refresh token is blacklisted!)
```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Deconstruct JWT signatures, claims, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build JWT encoders and validators in [`practice.py`](practice.py), and fix token traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Stateless JWT Issuer & Blacklist Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
