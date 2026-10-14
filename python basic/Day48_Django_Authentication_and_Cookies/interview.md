# Day 44 — Real-World Backend Engineering Interview

These questions assess your understanding of web authentication protocols, password storage security, and cookie defense.

---

### Question 1: Why Does Django Use PBKDF2 Instead of Raw SHA-256?
**Interview Scenario:**
> *"If SHA-256 is an unbroken cryptographic hash function, why is storing `sha256(password + salt)` considered an egregious security violation by OWASP?"*

#### Senior Mentor Answer & Key Points:
1. **Speed is the Enemy of Password Security**:
   - Standard SHA-256 is engineered for maximum throughput (verifying gigabytes of data per second).
   - Modern GPUs can compute over **10 billion SHA-256 hashes per second**.
   - If a database of salted SHA-256 hashes is leaked, an attacker can crack an 8-character password in minutes!
2. **The Key Stretching Solution (PBKDF2 / Argon2)**:
   - PBKDF2 runs the HMAC algorithm 600,000+ times in a tight loop for a single password verification.
   - For a legitimate user, 600,000 iterations takes ~100 milliseconds (unnoticeable).
   - For an attacker, attempting 1 billion passwords would take decades, rendering brute-force attacks economically and computationally impossible.

---

### Question 2: The `SameSite` Cookie Attribute & Modern Browser CSRF Protection
**Interview Scenario:**
> *"Modern browsers default cookies to `SameSite=Lax`. Does this make Django's CSRF token protection obsolete?"*

#### Senior Mentor Answer & Key Points:
1. **What `SameSite=Lax` Does**:
   - With `SameSite=Lax`, browsers withhold cookies on cross-site sub-requests (such as `POST` forms from `evil.com` or cross-origin AJAX calls), preventing traditional form-based CSRF.
2. **Why CSRF Tokens are Still Mandatory**:
   - **Top-level navigations**: `GET` requests still send `SameSite=Lax` cookies. If any GET endpoint inadvertently modifies state, it remains vulnerable.
   - **Older/Mobile Browsers**: Legacy browsers or embedded webviews do not support or properly enforce `SameSite`.
   - **Defense in Depth**: CSRF tokens provide a second, cryptographic layer of protection that does not rely on third-party browser vendor implementations.
