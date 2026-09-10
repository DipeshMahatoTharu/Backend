# Day 36 — Real-World Backend Engineering Interview

These questions evaluate your comprehension of Django's internal boot lifecycle, deployment gateways, and security configurations.

---

### Question 1: How Does Django Boot Up? (The `manage.py` and `django.setup()` Lifecycle)
**Interview Scenario:**
> *"When you execute `python manage.py runserver` or when Gunicorn boots `my_project.wsgi:application`, what actually happens under the hood before requests are served?"*

#### Senior Mentor Answer & Key Points:
1. **Setting the Environment**:
   - `manage.py` sets `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')`.
2. **`django.setup()` Invocation**:
   - Django imports and validates settings.
   - Configures logging according to `LOGGING`.
   - **App Registry Initialization (`apps.populate()`)**:
     - Imports every app specified in `INSTALLED_APPS`.
     - Imports models from each app (`<app>.models`).
     - Constructs model metadata options (`_meta`) and establishes cross-model relationships.
     - Registers model signal handlers.
3. **Handler Ready**:
   - Loads middleware chain in reverse order to build the onion execution pipeline.
   - Handlers are now primed to accept incoming HTTP requests.

---

### Question 2: Why Does HTTP Host Header Poisoning Require `ALLOWED_HOSTS`?
**Interview Scenario:**
> *"Why does Django raise `DisallowedHost` when `DEBUG=False` if `ALLOWED_HOSTS` is empty? What attack does this prevent?"*

#### Senior Mentor Answer & Key Points:
1. **The Attack (Host Header Poisoning)**:
   - When generating password reset emails or canonical links, web applications often construct URLs dynamically using the incoming HTTP `Host` header: `f"https://{request.get_host()}/reset-password/?token={token}"`.
   - An attacker can forge the `Host` header in their HTTP request: `Host: evil-phishing-site.com`.
   - If the server accepts this, the password reset email sent to the victim contains a link redirecting to the attacker's server, leaking the password reset token!
2. **Django's Defense**:
   - Django strictly validates `request.get_host()` against `ALLOWED_HOSTS`. If the header does not match, Django raises `SuspiciousOperation` and returns `400 Bad Request`, preventing token theft.
