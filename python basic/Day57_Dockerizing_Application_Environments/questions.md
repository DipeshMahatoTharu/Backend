# Day 57 — Dockerizing Application Environments Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 57.1 Multi-Stage Builds & Security
**QUESTION:**
Why does compiling C-extensions in a builder stage and copying only binary wheels to a clean runner stage dramatically reduce the attack surface and image size of a production container?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 57.2 The Non-Root Container Security Rule
**QUESTION:**
Why should a Docker container NEVER run application processes as `root` (UID 0)? What security disaster can occur if an application has a Remote Code Execution (RCE) vulnerability inside a container running as root?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 57.3 The Database Readiness Race Condition in Docker Compose
**QUESTION:**
Why does `depends_on: ['db']` in Docker Compose NOT guarantee that PostgreSQL is ready to accept SQL connections when Django boots? How do `service_healthy` conditions or `wait-for-it.sh` scripts prevent boot crashes?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
