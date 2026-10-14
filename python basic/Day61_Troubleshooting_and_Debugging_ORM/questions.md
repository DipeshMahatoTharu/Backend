# Day 53 — ORM Troubleshooting & Debugging Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 53.1 `EXPLAIN` vs `EXPLAIN ANALYZE`
**QUESTION:**
What is the crucial difference between `EXPLAIN` and `EXPLAIN ANALYZE` in PostgreSQL? Why must you be careful running `EXPLAIN ANALYZE` on a `DELETE` or `UPDATE` statement in production?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 53.2 The `defer()` Trap in Loops
**QUESTION:**
Explain how using `.defer('heavy_field')` can inadvertently cause an N+1 query problem if a developer accesses `obj.heavy_field` inside a template loop later on.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 53.3 Database Connection Pooling with `CONN_MAX_AGE`
**QUESTION:**
What does Django's `CONN_MAX_AGE` setting do? Why does closing and reopening a TCP connection to PostgreSQL on every single HTTP request kill API throughput?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
