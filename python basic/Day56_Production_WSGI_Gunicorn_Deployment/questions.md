# Day 56 — Production WSGI & Gunicorn Deployment Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 56.1 Why Gunicorn Cannot Safely Expose Port 8000 Directly to the Public Internet
**QUESTION:**
Why must you always place a reverse proxy like Nginx or AWS ALB in front of Gunicorn instead of exposing Gunicorn directly to the public internet? How do "slow clients" kill sync workers?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 56.2 Worker Types: `sync` vs `gthread` vs `gevent`
**QUESTION:**
Compare Gunicorn's `sync` workers, `gthread` workers, and `gevent` greenlet workers. When is `gthread` superior to `sync` for I/O-bound Django applications?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 56.3 The Infinite HTTPS Redirect Loop Trap
**QUESTION:**
Explain how misconfiguring `SECURE_PROXY_SSL_HEADER` and `X-Forwarded-Proto` causes an infinite HTTP 301 redirect loop when Django is deployed behind an SSL-terminating reverse proxy.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
