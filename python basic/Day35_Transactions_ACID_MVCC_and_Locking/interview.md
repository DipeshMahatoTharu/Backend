# Day 35 — Real-World Concurrency, Locking & MVCC Interview Q&A

### Q1: How does PostgreSQL implement Multi-Version Concurrency Control (MVCC), and why don't readers block writers?
**Answer:**
In PostgreSQL, each table tuple has hidden system attributes:
- `xmin`: The transaction ID that inserted this tuple.
- `xmax`: The transaction ID that updated or deleted this tuple (or 0 if still active).
When an `UPDATE` occurs:
1. PostgreSQL writes a brand new tuple with its `xmin = current_tx_id`.
2. It sets the existing tuple's `xmax = current_tx_id`.
3. Any concurrent transaction whose snapshot began prior to this update still reads the old tuple because `current_tx_id` has not committed or falls outside its snapshot window.
4. Hence, readers simply read historical row versions from the heap without acquiring shared table locks, allowing writers to insert/update new versions concurrently without blocking.

---

### Q2: What is the difference between Pessimistic Locking and Optimistic Locking, and when do you use each in Django?
**Answer:**
- **Pessimistic Locking (`select_for_update()`)**:
  - **Mechanism**: Issues `SELECT ... FOR UPDATE` at the database level, placing an exclusive row-level lock on the row until the transaction ends.
  - **When to Use**: High-contention, fast-turnaround transactions where conflicts are frequent and must be prevented immediately (e.g. reserving a concert seat, deducting money from a bank wallet, updating high-volume flash-sale stock).
  ```python
  with transaction.atomic():
      account = BankAccount.objects.select_for_update().get(id=account_id)
      account.balance -= amount
      account.save()
  ```
- **Optimistic Locking**:
  - **Mechanism**: Does not lock the row. Instead, it adds a `version = models.IntegerField(default=1)` column. When updating:
    `UPDATE accounts SET balance = 400, version = version + 1 WHERE id = 101 AND version = 5;`
    If `rowcount == 0`, someone modified the row while we were preparing our update, so we abort or retry.
  - **When to Use**: Low-contention systems or long human workflows (e.g. a user editing a blog post or multi-step checkout form in a browser for 10 minutes where holding a database lock would exhaust the connection pool).

---

### Q3: What is `SELECT ... FOR UPDATE SKIP LOCKED`, and why is it essential for distributed workers?
**Answer:**
Standard `SELECT ... FOR UPDATE` forces concurrent workers to wait in line until the first worker releases its lock.
If 20 Celery/cron workers execute `SELECT * FROM tasks WHERE status = 'PENDING' LIMIT 1 FOR UPDATE;`, Worker 2 through 20 are completely blocked waiting on Worker 1.
- With `SKIP LOCKED`, PostgreSQL skips any rows that are already locked by other transactions, immediately returning the next unlocked row.
- **Result**: All 20 workers execute in parallel with 0ms waiting time and zero lock contention.

---

### Q4: How do deadlocks happen in SQL, and how do you guarantee they never occur in your backend?
**Answer:**
A deadlock occurs when two concurrent transactions have a cyclic dependency on locks:
- Transaction 1 holds a lock on Row A and requests a lock on Row B.
- Transaction 2 holds a lock on Row B and requests a lock on Row A.
PostgreSQL detects this cycle using its internal lock wait graph and throws `deadlock_detected (SQLSTATE 40P01)`.
- **The Golden Prevention Rule**:
  **Enforce Strict Global Resource Ordering**.
  Whenever updating or locking multiple records, always sort the primary keys before acquiring locks:
  ```python
  keys = sorted([from_account_id, to_account_id])
  accounts = Account.objects.filter(id__in=keys).order_by('id').select_for_update()
  ```
  Because all transactions acquire locks in the exact same order (e.g. `1` then `2`), a circular dependency is mathematically impossible.

---

### Q5: What is the difference between PostgreSQL's `Read Committed` and `Serializable` isolation levels?
**Answer:**
- **Read Committed (Default)**: Each statement in a transaction sees a snapshot of the database taken at the start of *that statement*. A query executed at the start of a transaction may see different rows if another transaction committed halfway through.
- **Serializable**: Guarantees that the execution of concurrent transactions produces the exact same outcome as if they had been executed strictly one after another (sequentially). PostgreSQL uses **Serializable Snapshot Isolation (SSI)** to track read-write dependencies without holding long-term table locks; if an anomaly (like Write Skew) is detected, PostgreSQL rolls back the transaction with a `40001 serialization_failure`, requiring the application to retry.
