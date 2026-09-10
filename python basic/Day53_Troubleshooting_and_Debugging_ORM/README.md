# Day 53 — Troubleshooting, Query Profiling & ORM Debugging

## 🎯 Learning Objectives
- Master Django query inspection using `django.db.connection.queries` and Django Debug Toolbar.
- Understand database query execution plans: `EXPLAIN` and `EXPLAIN ANALYZE`.
- Prevent query regressions using `self.assertNumQueries(N)` in test suites.
- Optimize column payloads with `.only(*fields)` and `.defer(*fields)` for large text and binary fields.
- Resolve database connection leaks and configure connection pooling (`CONN_MAX_AGE`).

---

## 📚 Core Backend Concepts

### 1. Inspecting Executed SQL Queries
In local development with `DEBUG = True`:
```python
from django.db import connection

# Run queries
users = list(User.objects.filter(is_active=True)[:5])

# Print query history and execution times
for q in connection.queries:
    print(f"[{q['time']}s] {q['sql']}")
```

### 2. `assertNumQueries` in Automated Tests
```python
from django.test import TestCase

class PerformanceTests(TestCase):
    def test_post_list_query_count(self):
        # Enforce that listing 50 posts NEVER exceeds 2 database queries!
        with self.assertNumQueries(2):
            response = self.client.get('/api/v1/posts/')
            self.assertEqual(response.status_code, 200)
```
If an engineer accidentally introduces an N+1 query, the CI build immediately fails!

### 3. `only()` and `defer()` Optimization
- **`defer('large_biography', 'pdf_payload')`**: Loads all columns except the deferred heavy fields.
- **`only('id', 'title')`**: Loads ONLY the specified columns.
- **Caution**: If deferred fields are accessed later in Python, Django executes an extra query per object to fetch them!

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review SQL execution plans, query logging, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build query counters and index analyzers in [`practice.py`](practice.py), and fix ORM traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Real-Time Query Profiler & N+1 Alert Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
