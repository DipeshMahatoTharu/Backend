# Day 48 — DRF Token Auth & JWT Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 48.1 Database Tokens vs Stateless JWTs
**QUESTION:**
Why does standard DRF `TokenAuthentication` require a database lookup on every single API request, while JWT does not? What is the architectural penalty of database tokens under 50,000 requests per second?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 48.2 The JWT Revocation Problem
**QUESTION:**
If a user's phone is stolen, why can you not easily "log out" a stateless JWT from the backend before its `exp` time arrives? How does Token Blacklisting with Redis solve this?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 48.3 Where Should Frontend Apps Store JWTs?
**QUESTION:**
Why is storing JWT access tokens in browser `localStorage` vulnerable to Cross-Site Scripting (XSS)? Why is storing refresh tokens in `HttpOnly, Secure, SameSite=Strict` cookies superior?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
