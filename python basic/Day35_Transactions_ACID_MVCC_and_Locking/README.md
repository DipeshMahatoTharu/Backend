# Day 35 — PostgreSQL Transactions, ACID, MVCC & Concurrency Locking

## 🎯 Learning Objectives
- Deeply understand PostgreSQL's **Multi-Version Concurrency Control (MVCC)**: hidden system attributes (`xmin`, `xmax`, `ctid`), dead tuples, and the role of `VACUUM`.
- Master the 4 **Transaction Isolation Levels**: *Read Committed*, *Repeatable Read*, and *Serializable*, and the concurrency phenomena they prevent (Dirty Read, Non-Repeatable Read, Phantom Read, Serialization Anomaly).
- Implement Pessimistic Concurrency Control: **`SELECT ... FOR UPDATE`** and **`SELECT ... FOR UPDATE SKIP LOCKED`** (the gold standard for high-throughput message queues and booking engines).
- Compare **Optimistic Locking** (version columns / timestamps) with **Pessimistic Locking**.
- Diagnose and prevent **Database Deadlocks**.

---

## 📚 Core Backend Concepts

### 1. How PostgreSQL MVCC Really Works
In traditional databases, readers block writers and writers block readers. In PostgreSQL, **"Readers never block writers, and writers never block readers."**
- When you execute an `UPDATE`, PostgreSQL does NOT overwrite the row in place.
- It inserts a **brand new version of the row (tuple)** with its `xmin` set to the current transaction ID, and marks the old row's `xmax` with the current transaction ID!
- Readers continue reading the old version until the new transaction commits.
- **Dead Tuples**: Once all transactions that could see the old tuple finish, the old tuple becomes "dead".
- **`VACUUM` / Autovacuum**: Background worker that cleans up dead tuples and marks the space reusable in the Free Space Map (FSM).

### 2. Transaction Isolation Levels & Concurrency Anomalies
| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Serialization Anomaly |
| :--- | :--- | :--- | :--- | :--- |
| **Read Uncommitted** *(Postgres treats as Read Committed)* | ❌ Prevented | Allowed | Allowed | Allowed |
| **Read Committed** *(PostgreSQL Default)* | ❌ Prevented | Allowed | Allowed | Allowed |
| **Repeatable Read** | ❌ Prevented | ❌ Prevented | ❌ Prevented *(in Postgres!)* | Allowed |
| **Serializable** | ❌ Prevented | ❌ Prevented | ❌ Prevented | ❌ Prevented |

### 3. Concurrency Locking: `SELECT FOR UPDATE` vs `SKIP LOCKED`
- **Pessimistic Locking (`SELECT FOR UPDATE`)**:
  ```sql
  -- Locks the specific account row until the transaction commits/rollbacks
  SELECT balance FROM accounts WHERE id = 101 FOR UPDATE;
  UPDATE accounts SET balance = balance - 100 WHERE id = 101;
  COMMIT;
  ```
  Any other concurrent worker trying to lock account `101` will block and wait.
- **Queue Worker Pattern (`SKIP LOCKED`)**:
  ```sql
  -- Instantly claims the next available unprocessed task without blocking other workers!
  SELECT * FROM background_tasks 
  WHERE status = 'PENDING' 
  ORDER BY id ASC 
  LIMIT 1 
  FOR UPDATE SKIP LOCKED;
  ```

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + MVCC & ISOLATION DRILLS (60 min)**:
  - 40 min: Study MVCC internals, isolation levels, and lock types.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/questions.md)**.

- **HOUR 2 — LOCKING PRACTICE & DEADLOCK DIAGNOSIS (60 min)**:
  - 35 min: Implement thread-safe concurrent booking in **[`practice.py`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/practice.py)**.
  - 25 min: Reproduce and resolve database deadlocks in **[`debugging.py`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/debugging.py)**.

- **HOUR 3 — WHITEBOARD CONCURRENCY & INTERVIEW (60 min)**:
  - 20 min: Study Senior Backend Concurrency interview questions in **[`interview.md`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/interview.md)**.
  - 20 min: Solve the blank-page Ticket Booking concurrency engine on **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/whiteboard.py)**.
  - 20 min: Build the Resilient Distributed Flash-Sale Inventory Engine in **[`challenge.py`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Studied MVCC and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/questions.md)**
- [ ] Simulated concurrency and row locking in **[`practice.py`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/practice.py)**
- [ ] Diagnosed and prevented deadlocks in **[`debugging.py`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/debugging.py)**
- [ ] Solved blank-page ticket lock challenge in **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/whiteboard.py)**
- [ ] Passed high-concurrency race condition tests in **[`challenge.py`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/challenge.py)**
- [ ] Mastered Senior Concurrency interview questions in **[`interview.md`](file:///d:/Backend/python%20basic/Day35_Transactions_ACID_MVCC_and_Locking/interview.md)**
