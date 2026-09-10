# Day 57 — Real-World Backend Engineering Interview

These questions test your comprehension of containerization security, multi-stage compilation, and container orchestration.

---

### Question 1: How Do Multi-Stage Docker Builds Slash Django Image Sizes?
**Interview Scenario:**
> *"A developer's standard Django Docker image is 1.4 GB. After refactoring into a multi-stage Dockerfile, the image drops to 135 MB. What was removed, and why is the smaller image radically more secure?"*

#### Senior Mentor Answer & Key Points:
1. **What Bloats Single-Stage Images**:
   - Compiling Python libraries with C-extensions (like `psycopg2`, `cryptography`, `pillow`) requires heavy build dependencies: `gcc`, `g++`, `make`, `python3-dev`, and `libpq-dev`.
   - In a single-stage build, these compiler tools, header files, and apt cache archives remain baked inside the final production image!
2. **The Multi-Stage Solution**:
   - **Stage 1 (Builder)**: Installs compilers, downloads source code, and compiles `.whl` binary wheel archives into `/wheels`.
   - **Stage 2 (Runner)**: Starts from a pristine, minimal `python:3.11-slim` base. It copies **only** the pre-built `.whl` files from the builder stage, installs them, and discards the build tools entirely.
3. **Security Advantage**:
   - Compilers (`gcc`) and development headers are removed from production. If an attacker exploits an application vulnerability, they cannot compile local privilege escalation exploits inside the container!

---

### Question 2: Why `docker compose up` Without Healthchecks Fails on Cold Boots
**Interview Scenario:**
> *"In a fresh environment, running `docker compose up` causes the `web` container to crash immediately with `psycopg2.OperationalError: could not connect to server: Connection refused`. Why did this happen when `depends_on: ['db']` was set?"*

#### Senior Mentor Answer & Key Points:
1. **The Meaning of `depends_on`**:
   - By default, `depends_on` only waits until the `db` container process has **started**, not until the database engine is ready to accept socket connections!
   - PostgreSQL needs 2–5 seconds on first boot to initialize cluster directories, verify WAL logs, and bind port 5432.
2. **The Solution**:
   - Add a `healthcheck` to the database:
     ```yaml
     healthcheck:
       test: ["CMD-SHELL", "pg_isready -U postgres"]
       interval: 2s
       retries: 5
     ```
   - In the `web` service, specify:
     ```yaml
     depends_on:
       db:
         condition: service_healthy
     ```
