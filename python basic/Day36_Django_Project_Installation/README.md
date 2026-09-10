# Day 36 — Django Architecture, Project Setup & Configuration

## 🎯 Learning Objectives
- Master Django's architectural philosophy: Model-View-Template (MVT) and "Batteries Included".
- Understand project structure vs app structure (`django-admin startproject` vs `python manage.py startapp`).
- Deconstruct `settings.py`: `INSTALLED_APPS`, `DATABASES`, `MIDDLEWARE`, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`.
- Understand the role of entrypoint files: `manage.py`, `wsgi.py` (synchronous web server gateway), and `asgi.py` (asynchronous server gateway).
- Implement 12-factor application configuration principles using environment variables (`python-dotenv` / `python-decouple`).

---

## 📚 Core Backend Concepts

### 1. Django MVT Architecture vs Classic MVC
| Django MVT | Classic MVC | Responsibility |
| :--- | :--- | :--- |
| **Model** | **Model** | Database schema, business rules, ORM queries |
| **View** | **Controller** | Request processing, business logic, interacting with Model, returning response |
| **Template** | **View** | Presentation layer (HTML, DTL, JSON formatting) |

### 2. Project vs App Directory Structure
```text
my_ecommerce/               <- Project Root
├── manage.py               <- CLI utility for administrative tasks
├── my_ecommerce/           <- Configuration Package
│   ├── __init__.py
│   ├── settings.py         <- Global application settings & database connections
│   ├── urls.py             <- Top-level URL routing table
│   ├── wsgi.py             <- WSGI server entrypoint for production (Gunicorn)
│   └── asgi.py             <- ASGI server entrypoint for async/websockets (Daphne/Uvicorn)
└── products/               <- Modular Django App
    ├── migrations/         <- Database migration tracking files
    ├── models.py           <- Database models
    ├── views.py            <- Request handlers
    ├── urls.py             <- App-specific route mapping
    └── apps.py             <- App configuration metadata
```

### 3. Critical Production Settings Checklist
- `DEBUG = False`: Never run in production (exposes raw code, SQL queries, and environment variables).
- `SECRET_KEY`: Must be loaded from environment variables and kept secret.
- `ALLOWED_HOSTS = ['api.yourdomain.com']`: Prevents HTTP Host header poisoning attacks.
- `SECURE_SSL_REDIRECT = True`: Forces HTTPS across all connections.

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Deconstruct MVT, `settings.py`, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build configuration validators in [`practice.py`](practice.py), and fix settings traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Django Configuration & App Registry Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
