# Day 32 — PostgreSQL Setup, Python Drivers & Connection Management

## 🎯 Learning Objectives
- Connect Python applications to PostgreSQL using the industry-standard `psycopg2` driver.
- Execute parameterized queries safely using tuples (`%s`) to prevent SQL injection.
- Manage database transactions cleanly with explicit `commit()` and `rollback()` handling.
- Retrieve query results as Python dictionaries using `RealDictCursor`.
- Understand the basics of connection reuse using `ThreadedConnectionPool`.

---

## 📚 Core Backend Concepts

### 1. Connecting Python to PostgreSQL
In production, your Python backend connects to PostgreSQL over a network socket. Connection details should always be loaded from environment variables rather than hardcoded in source code:
```python
import os
import psycopg2

conn = psycopg2.connect(
    dbname=os.environ.get("DB_NAME", "postgres"),
    user=os.environ.get("DB_USER", "postgres"),
    password=os.environ.get("DB_PASSWORD", ""),
    host=os.environ.get("DB_HOST", "localhost"),
    port=os.environ.get("DB_PORT", "5432")
)
```

### 2. Parameterized Queries (Preventing SQL Injection)
Never use Python f-strings or string concatenation (`+`) to build SQL queries. An attacker could enter `' OR '1'='1` into a login form and bypass authentication or drop tables.
- **Vulnerable Code**:
  ```python
  # DANGEROUS: SQL Injection vulnerability!
  query = f"SELECT * FROM users WHERE email = '{user_email}';"
  cursor.execute(query)
  ```
- **Safe Code**:
  ```python
  # SAFE: The driver escapes and validates the parameter tuple
  query = "SELECT * FROM users WHERE email = %s;"
  cursor.execute(query, (user_email,))
  ```

### 3. Explicit Transactions (Commit & Rollback)
By default, `psycopg2` starts a transaction automatically on the first SQL command.
- To persist database writes (`INSERT`, `UPDATE`, `DELETE`), you must explicitly call `conn.commit()`.
- If an exception occurs, you must call `conn.rollback()` to cancel pending changes and leave the connection in a clean state:
```python
try:
    cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s;", (100, sender_id))
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s;", (100, recipient_id))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Transaction failed, changes rolled back: {e}")
```

### 4. Dictionary Cursors (`RealDictCursor`)
Standard cursors return rows as plain tuples: `(1, "dipesh", "dipesh@example.com")`. In web backends and APIs, you want dictionaries where keys match column names:
```python
from psycopg2.extras import RealDictCursor

with conn.cursor(cursor_factory=RealDictCursor) as cur:
    cur.execute("SELECT id, username, email FROM users WHERE id = %s;", (user_id,))
    user = cur.fetchone()
    # user is now a dictionary: {"id": 1, "username": "dipesh", "email": "dipesh@example.com"}
``` 

### 5. Basic Connection Pooling
Opening a new TCP connection on every web request is slow and consumes database server memory. A connection pool keeps a small set of open, authenticated connections ready for immediate checkout:
```python
from psycopg2.pool import ThreadedConnectionPool

pool = ThreadedConnectionPool(minconn=1, maxconn=10, dsn="postgresql://postgres:secret@localhost:5432/app_db")

# In an API view / request handler:
conn = pool.getconn()
try:
    # Execute queries using conn...
    conn.commit()
finally:
    # ALWAYS return the connection back to the pool:
    pool.putconn(conn)
```

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN & CONCEPTS (60 min)**:
  - 35 min: Study driver connectivity, parameterized queries, and commit/rollback lifecycles.
  - 25 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day32_PostgreSQL_Database_Configurations/questions.md)**.

- **HOUR 2 — PRACTICE & DEBUGGING (60 min)**:
  - 35 min: Implement the 4 core driver tasks in **[`practice.py`](file:///d:/Backend/python%20basic/Day32_PostgreSQL_Database_Configurations/practice.py)**.
  - 25 min: Diagnose connection leaks and uncommitted transaction bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day32_PostgreSQL_Database_Configurations/debugging.py)**.

- **HOUR 3 — CHALLENGE & INTERVIEW (60 min)**:
  - 20 min: Review core SQL driver interview questions in **[`interview.md`](file:///d:/Backend/python%20basic/Day32_PostgreSQL_Database_Configurations/interview.md)**.
  - 20 min: Write a safe transactional script on **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day32_PostgreSQL_Database_Configurations/whiteboard.py)**.
  - 20 min: Complete the Resilient Connection Repository challenge in **[`challenge.py`](file:///d:/Backend/python%20basic/Day32_PostgreSQL_Database_Configurations/challenge.py)**.

---

## 🏁 Definition of Done for Day 32
- [ ] Explained why parameterized queries (`%s` with a tuple) are mandatory for database security.
- [ ] Completed Tasks 1 to 4 in **[`practice.py`](file:///d:/Backend/python%20basic/Day32_PostgreSQL_Database_Configurations/practice.py)** with clean commits and rollbacks.
- [ ] Verified that connections checked out from a pool are safely returned in a `finally` block.
- [ ] Answered conceptual driver questions in **[`questions.md`](file:///d:/Backend/python%20basic/Day32_PostgreSQL_Database_Configurations/questions.md)**.