# Day 33 — PostgreSQL Indexing, B-Trees & Query Optimization

## 🎯 Learning Objectives
- Master PostgreSQL Indexing internal structures: **B-Tree**, Hash, and GIN indexes.
- Dissect and interpret query execution plans using `EXPLAIN (ANALYZE, BUFFERS)`.
- Understand the difference between **Sequential Scan**, **Index Scan**, **Index Only Scan**, and **Bitmap Heap Scan**.
- Apply the **Leftmost Prefix Rule** on composite (multi-column) indexes.
- Design **Partial Indexes** (`WHERE is_active = TRUE`) and **Expression/Functional Indexes** (`LOWER(email)`).
- Learn when indexes *hurt* performance (insert/update overhead, write amplification, disk bloat).

---

## 📚 Core Backend Concepts

### 1. B-Tree Index Mechanics Under the Hood
PostgreSQL B-Tree indexes are self-balancing search trees organized into $8\text{KB}$ disk pages (root, internal branches, and leaf pages).
- **Time Complexity**: Search, insertion, and deletion are all $O(\log N)$.
- **Leaf Nodes**: Contain the indexed column value and a `TID` (Tuple ID / pointer: `(block_number, offset)`) pointing to the physical row on the heap.
- **Double-Linked Leaves**: Leaf pages form a doubly-linked list, making range queries (`WHERE age BETWEEN 20 AND 30`) and ordering (`ORDER BY created_at DESC`) lightning fast.

### 2. Dissecting `EXPLAIN (ANALYZE, BUFFERS)`
Never guess why a SQL query is slow. Run:
```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT id, username, email FROM users WHERE email = 'dev@example.com';
```
Key metrics to analyze:
- **Seq Scan (Sequential Scan)**: Reads every page on disk from start to finish. Good for small tables (<1,000 rows), disastrous for tables with millions of rows.
- **Index Scan**: Traverses the B-Tree index to find the pointer, then accesses the heap table page to retrieve the full row.
- **Index Only Scan**: Traverses the B-Tree and retrieves ALL requested columns directly from the index without touching the heap table (requires a covering index and up-to-date visibility map).
- **Bitmap Heap Scan**: Used when multiple index rows match; constructs a memory bitmap of pages to access the heap in sequential disk order.
- **Buffers: shared hit vs read**: `shared hit` means data was found in RAM (PostgreSQL shared buffers / cache); `shared read` means PostgreSQL had to issue a disk I/O read!

### 3. The Leftmost Prefix Rule (Composite Indexes)
If you create a composite index:
```sql
CREATE INDEX idx_orders_user_status_date ON orders (user_id, status, created_at);
```
- ✅ Fast: `WHERE user_id = 5` (uses index)
- ✅ Fast: `WHERE user_id = 5 AND status = 'PAID'` (uses index)
- ✅ Fast: `WHERE user_id = 5 AND status = 'PAID' AND created_at >= '2026-01-01'` (uses index)
- ❌ Index Ignored / Inefficient: `WHERE status = 'PAID'` (bypasses leftmost column!)
- ❌ Index Ignored / Inefficient: `WHERE created_at >= '2026-01-01'` (bypasses leftmost column!)

### 4. Expression & Partial Indexes
```sql
-- Expression Index: Makes case-insensitive lookups instant
CREATE INDEX idx_users_lower_email ON users (LOWER(email));

-- Partial Index: Indexes only unpaid orders (5% of data), saving 95% RAM & disk!
CREATE INDEX idx_orders_pending ON orders (created_at) WHERE status = 'PENDING';
```

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + CONCEPT DRILLS (60 min)**:
  - 40 min: Study B-Tree mechanics, Scan types, and composite index rules.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/questions.md)**.

- **HOUR 2 — INDEXING PRACTICE & DEBUGGING (60 min)**:
  - 35 min: Implement query profiling and index benchmark scripts in **[`practice.py`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/practice.py)**.
  - 25 min: Fix index invalidation and slow queries in **[`debugging.py`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/debugging.py)**.

- **HOUR 3 — INTERVIEW & PORTFOLIO CHALLENGE (60 min)**:
  - 20 min: Study Senior PostgreSQL Indexing interview questions in **[`interview.md`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/interview.md)**.
  - 20 min: Solve the blank-page query tuning challenge on **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/whiteboard.py)**.
  - 20 min: Build the E-Commerce Query Optimizer Engine in **[`challenge.py`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Read B-Tree concepts and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/questions.md)**
- [ ] Profiled sequential vs index scans in **[`practice.py`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/practice.py)**
- [ ] Fixed expression index and composite index bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/debugging.py)**
- [ ] Solved blank-page index design on **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/whiteboard.py)**
- [ ] Passed optimization benchmarks in **[`challenge.py`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/challenge.py)**
- [ ] Mastered Senior PostgreSQL interview questions in **[`interview.md`](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/interview.md)**
