# Day 56 — Production WSGI, Gunicorn Deployment & Nginx Architecture

## 🎯 Learning Objectives
- Master the production web stack: Nginx (Reverse Proxy) -> Gunicorn (WSGI HTTP Server) -> Django (Application).
- Understand Gunicorn worker models: Synchronous (`sync`), Threaded (`gthread`), and Asynchronous (`gevent`).
- Sizing worker pools using the core formula: $(2 \times \text{CPU cores}) + 1$.
- Configure Nginx reverse proxy headers: `X-Forwarded-For`, `X-Forwarded-Proto`, and `Host`.
- Configure production settings: `DEBUG=False`, `ALLOWED_HOSTS`, and `SECURE_PROXY_SSL_HEADER`.

---

## 📚 Core Backend Concepts

### 1. The Production Architecture Stack
```text
[ Browser / Mobile Client ]
           │ HTTPS (:443)
           ▼
[ Nginx Reverse Proxy ]
  - SSL Termination
  - Serves static assets directly from disk (/static/)
  - Buffers slow client connections
  - Rate limiting & DDoS filtering
           │ HTTP or UNIX Domain Socket (e.g. unix:/run/gunicorn.sock)
           ▼
[ Gunicorn WSGI Server ]
  - Master process managing N worker processes
  - Worker sizing: (2 * CPUs) + 1
           │ Calls Python callable application(environ, start_response)
           ▼
[ Django WSGI Application ]
```

### 2. Sizing Gunicorn Workers
```bash
# Sizing formula: (2 * NUM_CORES) + 1
# On a 4-core CPU server: (2 * 4) + 1 = 9 workers
gunicorn my_project.wsgi:application \
    --workers 9 \
    --worker-class gthread \
    --threads 2 \
    --bind 127.0.0.1:8000 \
    --timeout 30 \
    --access-logfile - \
    --error-logfile -
```

### 3. The `SECURE_PROXY_SSL_HEADER` Trap
When Nginx terminates HTTPS and forwards HTTP to Gunicorn, Django thinks the request is insecure HTTP!
To prevent infinite redirect loops when `SECURE_SSL_REDIRECT = True`:
```python
# settings.py
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```
And in `nginx.conf`:
```nginx
proxy_set_header X-Forwarded-Proto $scheme;
```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review Nginx/Gunicorn stack, worker sizing, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build worker capacity calculators and proxy header parsers in [`practice.py`](practice.py), and fix deployment traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Gunicorn & Nginx Reverse Proxy Simulator in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
