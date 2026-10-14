# Day 34 — HTTP Methods & Status Codes Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 34.1 Idempotency in Payment Gateways
**QUESTION:**
Why is `POST` inherently non-idempotent, and how do payment APIs (like Stripe) use `Idempotency-Key` HTTP headers to guarantee that network retries never double-charge a customer?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 34.2 401 Unauthorized vs 403 Forbidden
**QUESTION:**
Explain the exact technical distinction between HTTP `401` and `403`. When should a backend engineer return `404 Not Found` instead of `403 Forbidden` for security reasons?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 34.3 The "200 OK with Error Body" Anti-Pattern
**QUESTION:**
Why is returning `200 OK` with `{"success": false, "message": "Item not found"}` considered dangerous in modern backend engineering? What breaks at the proxy, CDN, and monitoring levels?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
