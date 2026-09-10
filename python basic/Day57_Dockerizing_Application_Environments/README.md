# Day 57 — Docker, Multi-Stage Builds & Docker Compose

## 🎯 Learning Objectives
- Master containerization fundamentals: Images, Containers, Layers, and the Docker daemon.
- Build production-ready multi-stage `Dockerfile`s to shrink image sizes from 1.2GB to <150MB.
- Configure `.dockerignore` to prevent leaking Git history, virtual environments, and secrets into images.
- Orchestrate multi-container environments using `docker-compose.yml` (Django + PostgreSQL + Redis).
- Write production `entrypoint.sh` scripts that wait for database readiness before running migrations.

---

## 📚 Core Backend Concepts

### 1. Multi-Stage Dockerfile Architecture
```dockerfile
# Stage 1: Build Wheels & Dependencies
FROM python:3.11-slim as builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Stage 2: Final Lean Runtime Image
FROM python:3.11-slim
WORKDIR /app
# Security: Create non-root user
RUN useradd -m -u 1000 appuser
RUN apt-get update && apt-get install -y --no-install-recommends libpq5 curl && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*
COPY . /app
USER appuser
EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "my_project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### 2. Multi-Container `docker-compose.yml`
```yaml
version: '3.8'
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: backend_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secretpassword
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started

volumes:
  postgres_data:
```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review Docker multi-stage builds, compose files, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build Dockerfile linters and wait loops in [`practice.py`](practice.py), and fix container traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Multi-Container Compose & Entrypoint Orchestrator in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
