# Day 35 — Transactions, MVCC & Concurrency Locking Questions

Please answer each question thoroughly in the spaces provided below.

---

### 35.1 PostgreSQL MVCC Under The Hood
**QUESTION:**
Explain how PostgreSQL achieves non-blocking reads and writes using Multi-Version Concurrency Control (MVCC). What are the hidden system columns `xmin` and `xmax`, and why does PostgreSQL require an background `VACUUM` process?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 35.2 Concurrency Anomalies (Dirty Read vs Non-Repeatable Read vs Phantom Read)
**QUESTION:**
Define each of the three classic SQL concurrency phenomena:
1. **Dirty Read**
2. **Non-Repeatable Read (Fuzzy Read)**
3. **Phantom Read**
Why does PostgreSQL's `Repeatable Read` isolation level protect against Phantom Reads, even though standard ANSI SQL only requires `Serializable` to do so?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 35.3 Pessimistic vs Optimistic Locking
**QUESTION:**
1. How does **Pessimistic Locking** (`SELECT ... FOR UPDATE`) work, and what is its primary danger under high concurrency?
2. How does **Optimistic Locking** (e.g. using a `version INTEGER` column and `WHERE id = ? AND version = ?`) work, and why is it preferred for web systems where users take several minutes to fill out a form before clicking "Submit"?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 35.4 The `SKIP LOCKED` Clause
**QUESTION:**
Explain the purpose of `SELECT ... FOR UPDATE SKIP LOCKED` in background task processing and ticket booking engines. What problem occurs if you run 10 concurrent worker processes with standard `FOR UPDATE` without `SKIP LOCKED`?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 35.5 Deadlocks: Cause, Detection & Prevention
**QUESTION:**
1. What sequence of operations causes a relational database deadlock between two concurrent transactions?
2. What is the fundamental architectural rule for ordering database operations across your application code to guarantee that deadlocks can never occur?

**MY ANSWER:**
____________________________________________________
____________________________________________________
