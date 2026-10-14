# Day 58 — Caching Systems & Redis Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 58.1 Cache-Aside vs Write-Through
**QUESTION:**
Compare the Cache-Aside pattern versus the Write-Through pattern. Which pattern is preferred for read-heavy Django REST APIs and why?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 58.2 Cache Stampede (Thundering Herd)
**QUESTION:**
What happens to your database when a high-traffic cache key (e.g. 5,000 requests/sec) expires without locking? How does probabilistic early expiration (XFetch) or distributed mutex locking solve this?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 58.3 Celery Architecture: Producer, Broker, Worker, Result Backend
**QUESTION:**
Deconstruct the four core components of a Celery async architecture: Producer (Django), Broker (Redis/RabbitMQ), Worker (Celery Daemon), and Result Backend (Redis/Postgres).

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
