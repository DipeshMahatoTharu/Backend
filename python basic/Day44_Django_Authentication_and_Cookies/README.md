# Day 44 — Django Authentication, Session Storage & Password Hashing

## 🎯 Learning Objectives
- Master Django's authentication system: `User` model, `authenticate()`, `login(request, user)`, and `logout(request)`.
- Understand session mechanics: the `sessionid` cookie, session stores (database, cache/Redis, signed cookies).
- Understand password cryptography: Salt generation, PBKDF2 with SHA-256, iteration work factor, and why passwords must never be stored in plaintext.
- Implement defense against Session Fixation by cycling session keys upon authentication.
- Understand constant-time string comparisons (`hmac.compare_digest`) to prevent timing side-channel attacks.

---

## 📚 Core Backend Concepts

### 1. The Anatomy of a Django Password Hash
Django stores password hashes in the format:
```text
pbkdf2_sha256$600000$salt_string$hashed_derived_key
```
- `pbkdf2_sha256`: The key derivation function.
- `600000`: Work factor (iterations) to slow down GPU brute-force attacks.
- `salt_string`: Cryptographic salt ensuring identical passwords produce distinct hashes.
- `hashed_derived_key`: The final 256-bit hash.

### 2. The Authentication Lifecycle
```python
from django.contrib.auth import authenticate, login, logout

# 1. Verify credentials (constant-time password comparison)
user = authenticate(request, username='dipesh', password='SecurePassword123')
if user is not None:
    # 2. Attach user to session (cycles session ID to prevent fixation)
    login(request, user)
    # request.user is now populated across all subsequent requests!
else:
    # Invalid credentials
    pass
```

### 3. Session Backend Options
- **`django.contrib.sessions.backends.db` (Default)**: Stores session data in `django_session` database table.
- **`django.contrib.sessions.backends.cache`**: Stores sessions in Redis or Memcached (blazing fast, reduces database load).
- **`django.contrib.sessions.backends.signed_cookies`**: Stores encrypted sessions directly in client cookies (stateless, zero server storage).

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review PBKDF2 hashing, session cookies, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build session managers and hashers in [`practice.py`](practice.py), and fix auth traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Secure Authentication & Session Lifecycle Manager in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
