# Day 38 — Django Template Engine & Static Files Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 38.1 Auto-Escaping and XSS Prevention
**QUESTION:**
How does Django protect against Cross-Site Scripting (XSS) in templates by default? Under what specific scenario is using the `|safe` filter acceptable, and what precautions must be taken?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 38.2 `STATIC_ROOT` vs `STATICFILES_DIRS`
**QUESTION:**
Explain the exact difference between `STATICFILES_DIRS` and `STATIC_ROOT`. What fatal error occurs if you point both settings to the same directory?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 38.3 Why Web Frameworks Shouldn't Serve Static Files in Production
**QUESTION:**
Why does Django's WSGI application refuse to serve static assets when `DEBUG = False`? Why is offloading static files to Nginx, Cloudflare, or AWS S3 critical for backend performance?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
