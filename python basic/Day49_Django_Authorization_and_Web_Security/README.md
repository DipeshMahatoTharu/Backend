# Day 45 — Django Authorization, RBAC & OWASP Web Security

## 🎯 Learning Objectives
- Master Authorization vs Authentication: Permissions, Groups, and Role-Based Access Control (RBAC).
- Implement view access control using decorators (`@login_required`, `@permission_required`) and CBV mixins (`LoginRequiredMixin`, `UserPassesTestMixin`).
- Diagnose and eliminate Insecure Direct Object Reference (IDOR) vulnerabilities.
- Configure critical security headers: Clickjacking (`X-Frame-Options`), Content Security Policy (CSP), and HSTS (`Strict-Transport-Security`).
- Conduct a Django production security audit with `python manage.py check --deploy`.

---

## 📚 Core Backend Concepts

### 1. IDOR (Insecure Direct Object Reference)
**The Vulnerability**:
```python
# VULNERABLE: Any user can view ANY invoice by guessing the ID!
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    return render(request, 'invoice.html', {'invoice': invoice})
```
**The Secure Fix (Object-Level Ownership Check)**:
```python
@login_required
def invoice_detail(request, invoice_id):
    # Restrict query to records owned by the authenticated user
    invoice = get_object_or_404(Invoice, pk=invoice_id, user=request.user)
    return render(request, 'invoice.html', {'invoice': invoice})
```

### 2. Core Security Headers
- `X-Frame-Options: DENY`: Prevents your website from being rendered inside an `<iframe>` on an attacker's domain (stops Clickjacking).
- `Content-Security-Policy (CSP)`: Specifies exactly which domains are trusted to execute JavaScript, fonts, and stylesheets (mitigates XSS).
- `Strict-Transport-Security (HSTS)`: Instructs browsers to communicate exclusively over HTTPS for the next year.

### 3. Production Deployment Checklist
Running `python manage.py check --deploy` verifies:
- `DEBUG = False`
- `SECURE_HSTS_SECONDS = 31536000`
- `SECURE_SSL_REDIRECT = True`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review RBAC, IDOR, security headers, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build RBAC filters in [`practice.py`](practice.py), and fix IDOR bugs in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Enterprise RBAC Authorization Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
