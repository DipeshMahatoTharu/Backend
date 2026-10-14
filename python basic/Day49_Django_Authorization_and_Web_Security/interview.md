# Day 45 — Real-World Backend Engineering Interview

These questions test your understanding of web security, authorization models, and OWASP Top 10 vulnerabilities.

---

### Question 1: How Do You Protect an Entire Django Application Against Insecure Direct Object Reference (IDOR)?
**Interview Scenario:**
> *"A penetration testing firm found that modifying `id=42` to `id=43` in the URL `/invoices/download?id=42` allows any user to download competitors' invoices. What architectural pattern guarantees this cannot happen anywhere in the codebase?"*

#### Senior Mentor Answer & Key Points:
1. **The Root Cause of IDOR**:
   - Querying objects purely by primary key (`Invoice.objects.get(id=id)`) without filtering by the requesting user or tenant.
2. **The 3-Tier Defense Strategy**:
   - **Tier 1 (QuerySet Scoping)**:
     - Never query the global model table. Scope queries to the user:
       ```python
       # Good
       invoice = get_object_or_404(request.user.invoices.all(), id=id)
       ```
   - **Tier 2 (Custom Model Managers)**:
     - Implement multi-tenant managers that automatically append `WHERE org_id = current_tenant` to every query:
       ```python
       class TenantModel(models.Model):
           org = models.ForeignKey(Organization, on_delete=models.CASCADE)
           objects = TenantManager()
       ```
   - **Tier 3 (DRF Object Permissions)**:
     - Enforce `has_object_permission(self, request, view, obj)` in API views.

---

### Question 2: Why `python manage.py check --deploy` is Mandatory in CI/CD
**Interview Scenario:**
> *"What checks does `python manage.py check --deploy` perform, and why should it gate your production build pipeline?"*

#### Senior Mentor Answer & Key Points:
1. **Automated Security Verification**:
   - Django includes built-in security linters that inspect `settings.py` for common production misconfigurations:
     - `security.W018`: `DEBUG` set to `True`.
     - `security.W004`: `SECURE_HSTS_SECONDS` not set.
     - `security.W012`: `SESSION_COOKIE_SECURE` not set (session cookies transmitted over insecure HTTP).
     - `security.W016`: `CSRF_COOKIE_SECURE` not set.
     - `security.W008`: `SECURE_SSL_REDIRECT` not set.
2. **CI/CD Gating**:
   - Adding `python manage.py check --deploy --fail-level WARNING` ensures that no container or code with unhardened security flags can be deployed to production.
