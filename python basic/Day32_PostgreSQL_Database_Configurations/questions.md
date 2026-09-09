# Day 32 — PostgreSQL Configurations & Python Drivers Questions

Write your answers in the designated spaces below each question.

---

### 32.1 Connection Overhead & Connection Pools
**QUESTION:**
1. Why does establishing a new PostgreSQL TCP connection for every incoming HTTP request cause severe latency and memory exhaustion?
2. What are `minconn` and `maxconn` in a connection pool, and what happens when an application worker requests a connection when all `maxconn` connections are currently checked out?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 32.2 Connection Leaks
**QUESTION:**
What is a "Connection Leak" in Python backend services? If a function checks out a connection from `pool.getconn()`, performs queries, encounters an unexpected `ZeroDivisionError`, and returns without calling `pool.putconn(conn)`, what will eventually happen to the entire web application?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 32.3 Cursor Factories (`RealDictCursor`)
**QUESTION:**
By default, `psycopg2.cursor()` returns database rows as plain Python tuples (e.g. `(1, "dipesh", "dipesh@test.com")`).
1. Why is this inconvenient when serializing JSON responses in REST APIs?
2. What does `psycopg2.extras.RealDictCursor` do, and how does it map column names to Python dictionary keys?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 32.4 Driver Transaction Semantics
**QUESTION:**
In `psycopg2`, does `conn = psycopg2.connect(...)` start an implicit transaction automatically? If you run an `INSERT` statement and exit without calling `conn.commit()`, what happens to your inserted data?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 32.5 PgBouncer Pooling Modes
**QUESTION:**
Compare the three operational pooling modes of PgBouncer:
1. Session Pooling
2. Transaction Pooling
3. Statement Pooling
Why is Transaction Pooling the most common mode in high-traffic Django / REST API deployments, and what PostgreSQL features (like `SET TIMEZONE` or prepared statements) require special configuration under transaction pooling?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________