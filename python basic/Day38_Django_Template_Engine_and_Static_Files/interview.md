# Day 38 — Real-World Backend Engineering Interview

These questions test your mastery of web presentation layers, production asset delivery, and frontend security.

---

### Question 1: How Does `collectstatic` Work in a Production CI/CD Pipeline?
**Interview Scenario:**
> *"In local development, images and CSS load perfectly. When deploying to AWS ECS with Nginx and Gunicorn, all styling disappears with 404s. Walk through how static asset pipelines must be configured for production."*

#### Senior Mentor Answer & Key Points:
1. **The Root Cause**:
   - In local development, `runserver` automatically serves static files from individual app `static/` directories.
   - When `DEBUG=False` in production, Django stops serving static files completely for security and performance reasons.
2. **The 3-Step Production Pipeline**:
   - **Step 1 (Settings)**:
     - Set `STATICFILES_DIRS = [BASE_DIR / 'static']` (where source assets live).
     - Set `STATIC_ROOT = BASE_DIR / 'staticfiles'` (empty folder where production assets will be compiled).
     - Set `STATIC_URL = '/static/'`.
   - **Step 2 (Build Step)**:
     - In the Docker build or CI/CD script, run: `python manage.py collectstatic --noinput`. This copies every app's assets into `STATIC_ROOT`.
   - **Step 3 (Nginx Web Server)**:
     - Configure Nginx to serve the static folder directly:
       ```nginx
       location /static/ {
           alias /app/staticfiles/;
           expires 30d;
           add_header Cache-Control "public, no-transform";
       }
       ```

---

### Question 2: Why Django Template Auto-Escaping Is Not Enough for HTML Attributes
**Interview Scenario:**
> *"If Django auto-escapes HTML characters, can a vulnerability still occur if you render `<a href="{{ user_website }}">Website</a>`?"*

#### Senior Mentor Answer & Key Points:
1. **The `javascript:` Protocol Vulnerability**:
   - Django's default auto-escaping converts `<`, `>`, `&`, `"`, and `'`.
   - If `user_website` is `javascript:alert(document.cookie)`, no special HTML characters exist!
   - The resulting HTML is `<a href="javascript:alert(document.cookie)">Website</a>`.
   - When a user clicks the link, the JavaScript executes inside their browser session!
2. **The Defense**:
   - Always validate URLs in forms/serializers to ensure the protocol starts with `http://` or `https://` before saving to the database.
