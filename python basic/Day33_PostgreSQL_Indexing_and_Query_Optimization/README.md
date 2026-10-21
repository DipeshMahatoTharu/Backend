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
PostgreSQL B-Tree indexes are self-balancing search trees organized into 8KB disk pages (root, internal branches, and leaf pages).
- **Time Complexity**: Search, insertion, and deletion are all $O(\log N)$.
- **Leaf Nodes**: Contain the indexed column value and a `TID` (Tuple ID / pointer: `(block_number, offset)`) pointing to the physical row on the heap.
- **Double-Linked Leaves**: Leaf pages form a doubly-linked list, making range queries (`WHERE age BETWEEN 20 AND 30`) and ordering (`ORDER BY created_at DESC`) fast.

### 2. Dissecting `EXPLAIN (ANALYZE, BUFFERS)`
Never guess why a SQL query is slow. Run:
```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT id, username, email FROM users WHERE email = 'dev@example.com';
```
Key metrics to analyze:
- **Seq Scan (Sequential Scan)**: Reads every page on disk from start to finish. Efficient for tiny tables (<1,000 rows), disastrous for tables with millions of rows.
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

## 📅 Today's Structure & Learning Flow

- **PART 1 — DAILY REVISION (~15 min)**:
  - Complete the rapid recall and function challenge in [revision.py](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/revision.py).
  - Track your progress in `revision_tracker.md`.

- **PART 2 — QUERY PROFILING & BENCHMARKS (~50 min)**:
  - Implement query profiling on unindexed tables in [practice.py](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/practice.py).
  - Create B-Tree indexes and measure the actual speedup factor.
  - Demonstrate composite index behavior and the leftmost prefix rule.

- **PART 3 — DEBUGGING INDEX TRAPS (~40 min)**:
  - Resolve expression index invalidation with `LOWER()` in [debugging.py](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/debugging.py).
  - Fix prefix query invalidation (`SUBSTR` vs trailing wildcard).
  - Explain the PostgreSQL type coercion trap.

- **PART 4 — ARCHITECTURE INTERVIEW & ADVISOR MINI-PROJECT (~75 min)**:
  - Formulate technical answers to Senior PostgreSQL Indexing interview questions in [interview.md](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/interview.md).
  - Build the automated query profiler and index recommender engine in [challenge.py](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/challenge.py).

---

## 🏁 Completion Checklist
- [ ] Completed 15-minute recall challenge in [revision.py](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/revision.py)
- [ ] Profiled sequential vs index scans in [practice.py](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/practice.py)
- [ ] Fixed expression index and composite index bugs in [debugging.py](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/debugging.py)
- [ ] Formulated independent answers in [interview.md](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/interview.md)
- [ ] Implemented and verified `DatabaseIndexAdvisor` in [challenge.py](file:///d:/Backend/python%20basic/Day33_PostgreSQL_Indexing_and_Query_Optimization/challenge.py)
