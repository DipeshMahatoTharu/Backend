# Day 27 — SQL Fundamentals & Relational Schema Design

## 🎯 Learning Objectives
- Master Data Definition Language (DDL): `CREATE TABLE`, `ALTER TABLE`, and `DROP TABLE`.
- Understand relational constraints: `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, and `DEFAULT`.
- Choose the correct column data types (`INT`, `VARCHAR`, `TEXT`, `NUMERIC`/`DECIMAL`, `BOOLEAN`, `TIMESTAMP`).
- Learn the fundamental categories of SQL: DDL, DML, DQL, and TCL.
- Design normalized schemas that enforce database-level referential integrity.

---

## 📚 Core Backend Concepts

### 1. SQL Command Categories
Relational database management systems (PostgreSQL, MySQL, SQLite) categorize SQL commands into:
- **DDL (Data Definition Language)**: Defines schema structure (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`).
- **DML (Data Manipulation Language)**: Modifies table records (`INSERT`, `UPDATE`, `DELETE`).
- **DQL (Data Query Language)**: Retrieves records (`SELECT`).
- **TCL (Transaction Control Language)**: Manages atomic transactions (`COMMIT`, `ROLLBACK`, `SAVEPOINT`).

### 2. Constraints & Referential Integrity
Backend logic must never rely solely on application-level validation. Databases must enforce business rules through constraints:
- **`PRIMARY KEY`**: Unique identifier for each row (enforces uniqueness and non-nullability).
- **`FOREIGN KEY`**: Establishes relationships between tables and enforces referential integrity.
- **`CHECK (condition)`**: Enforces business logic directly in the database (e.g. `CHECK (price >= 0.0)`).
- **`UNIQUE`**: Guarantees no two rows have duplicate values in that column (e.g. `email`).
- **`NOT NULL`**: Prevents empty/null entries.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount NUMERIC(10, 2) NOT NULL CHECK (total_amount >= 0.0),
    status VARCHAR(20) DEFAULT 'PENDING',
    CONSTRAINT fk_orders_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### 3. Data Types Decision Guide
- **Strings**: Use `VARCHAR(n)` when length has a known maximum (e.g. usernames, emails). Use `TEXT` for unbounded text (blog posts, descriptions).
- **Money/Currency**: **NEVER** use `FLOAT` or `REAL` for financial balances due to floating-point rounding errors! Always use `NUMERIC(precision, scale)` or `DECIMAL(10, 2)`.
- **Timestamps**: Always store timestamps in UTC using `TIMESTAMP WITH TIME ZONE` (`TIMESTAMPTZ`).

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + CONCEPT DRILLS (60 min)**:
  - 40 min: Review DDL syntax, constraint types, and data modeling above.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day27/questions.md)**.

- **HOUR 2 — SQL PRACTICE & DEBUGGING (60 min)**:
  - 35 min: Write the DDL schema scripts in **[`practice.sql`](file:///d:/Backend/python%20basic/Day27/practice.sql)**.
  - 25 min: Diagnose schema bugs and constraint violations in **[`debugging.py`](file:///d:/Backend/python%20basic/Day27/debugging.py)**.

- **HOUR 3 — INTERVIEW & PORTFOLIO CHALLENGE (60 min)**:
  - 20 min: Study senior backend database scenarios in **[`interview.md`](file:///d:/Backend/python%20basic/Day27/interview.md)**.
  - 20 min: Solve the blank-page schema design in **[`whiteboard.sql`](file:///d:/Backend/python%20basic/Day27/whiteboard.sql)**.
  - 20 min: Run and verify the complete SQLite schema test harness in **[`challenge.py`](file:///d:/Backend/python%20basic/Day27/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Read concepts and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day27/questions.md)**
- [ ] Completed all DDL tasks in **[`practice.sql`](file:///d:/Backend/python%20basic/Day27/practice.sql)**
- [ ] Fixed all constraint and schema bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day27/debugging.py)**
- [ ] Solved whiteboard schema design in **[`whiteboard.sql`](file:///d:/Backend/python%20basic/Day27/whiteboard.sql)**
- [ ] Passed schema verification tests in **[`challenge.py`](file:///d:/Backend/python%20basic/Day27/challenge.py)**
- [ ] Studied backend interview answers in **[`interview.md`](file:///d:/Backend/python%20basic/Day27/interview.md)**