# Day 38 — Django Template Engine & Static Files Architecture

## 🎯 Learning Objectives
- Master the Django Template Language (DTL): variables (`{{ user.name }}`), tags (`{% for %}`, `{% if %}`), and filters (`|upper`, `|date`).
- Implement robust template inheritance patterns using `base.html`, `{% block content %}`, and `{% extends %}`.
- Understand automatic HTML escaping and how Django protects against Cross-Site Scripting (XSS) by default.
- Configure static asset management: `STATIC_URL`, `STATIC_ROOT`, and `STATICFILES_DIRS`.
- Understand the role of `python manage.py collectstatic` in production deployments behind Nginx or AWS S3.

---

## 📚 Core Backend Concepts

### 1. Template Inheritance Hierarchy
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}My Portal{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
</head>
<body>
    <header>{% include 'partials/navbar.html' %}</header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

### 2. Built-in Security: Auto-Escaping
Django templates auto-escape dangerous HTML characters (`<`, `>`, `&`, `"`, `'`) to prevent XSS:
- `{{ user_bio }}` -> Safe (escapes `<script>` into `&lt;script&gt;`).
- `{{ user_bio|safe }}` -> **Unsafe**: Disables escaping. Only use when HTML is sanitized server-side with Bleach.

### 3. Static Files in Development vs Production
- **Development (`DEBUG=True`)**:
  - `django.contrib.staticfiles` automatically serves assets from each app's `static/` folder and `STATICFILES_DIRS`.
- **Production (`DEBUG=False`)**:
  - Django does **not** serve static files (too slow for Python WSGI).
  - Run `python manage.py collectstatic` to gather all assets into `STATIC_ROOT`.
  - Nginx, Caddy, or a CDN (Cloudflare/S3) serves `STATIC_ROOT` directly at wire speed.

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Deconstruct DTL syntax, XSS prevention, and answer [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build template variable resolvers in [`practice.py`](practice.py), and fix asset traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Minimal Template Engine & Static Asset Resolver in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
