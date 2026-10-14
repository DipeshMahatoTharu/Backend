# Day 33 — Real-World PostgreSQL Indexing & Optimization Interview Q&A

### Q1: Walk me through what happens under the hood when PostgreSQL executes a query with a B-Tree index versus without one.
**Answer:**
- **Without an Index (Sequential Scan / Heap Scan)**:
  PostgreSQL must read every $8\text{KB}$ page from the table on disk into RAM (`shared_buffers`). If a table is $10\text{GB}$ with 20 million rows, the operating system executes thousands of disk I/O operations, scanning every tuple one-by-one to evaluate the `WHERE` condition. Time complexity is $O(N)$, causing high latency and exhausting disk I/O bandwidth.
- **With a B-Tree Index (Index Scan)**:
  A B-Tree index is an ordered, balanced multi-way tree stored in separate $8\text{KB}$ pages. PostgreSQL begins at the **Root Page**, evaluates the search key, follows a pointer down internal branch pages, and reaches a **Leaf Page** in $O(\log N)$ steps (typically only 3 to 4 page reads even for millions of rows). The leaf page contains the indexed value and a Tuple ID (`TID` = Block Number, Offset). PostgreSQL then reads only the specific heap block to fetch the full row.

---

### Q2: What is an "Index-Only Scan", and why is it the holy grail of PostgreSQL query performance?
**Answer:**
An **Index-Only Scan** occurs when every column requested by the `SELECT` query is present directly inside the index itself (either as an indexed key or via the `INCLUDE` clause of a covering index).
- In a normal Index Scan, the engine must still visit the heap table pages to fetch non-indexed columns.
- In an Index-Only Scan, PostgreSQL reads **zero heap pages**, retrieving all data directly from the index in memory.
- **Critical Catch**: To return data without checking the heap, PostgreSQL consults the **Visibility Map** to verify whether the page has all-visible tuples (i.e. no uncommitted MVCC transactions). If the visibility map is not up to date (e.g. before an `AUTOVACUUM` has run), PostgreSQL is still forced to verify heap pages.

---

### Q3: What is the "Leftmost Prefix Rule" in composite indexing, and how do you decide column order?
**Answer:**
A composite index on `(A, B, C)` is physically sorted in the B-Tree primarily by `A`, then by `B` for duplicate `A`s, and then by `C`.
- Queries filtering on `A`, or `(A, B)`, or `(A, B, C)` can fully utilize the index.
- Queries filtering only on `B` or `C` cannot use the index effectively because the tree is not sorted by `B` first (analogous to looking up phone numbers in a phonebook by first name when the book is sorted by last name).
- **Rule of Thumb for Column Order**:
  1. Place columns evaluated with **exact equality (`=`)** first.
  2. Place columns evaluated with **range conditions (`>`, `<`, `BETWEEN`)** or used in `ORDER BY` last.

---

### Q4: When does adding an index actually hurt application performance?
**Answer:**
1. **Write Overhead (Write Amplification)**: Every `INSERT`, `UPDATE`, and `DELETE` on a table must update not only the heap table but also every B-Tree index on that table. If a table has 12 indexes, one insert triggers 13 write operations!
2. **Page Splits & Bloat**: Updating an indexed column requires re-balancing tree pages, causing disk fragmentation, page splits, and bloated index files.
3. **RAM Cache Contention**: Indexes take up space in PostgreSQL's `shared_buffers` and the OS page cache. Too many indexes push frequently accessed table data out of memory into slow disk storage.
4. **Planner Confusion**: Having too many overlapping indexes increases the query planner's time to choose the optimal path.

---

### Q5: How do you optimize `SELECT * FROM users WHERE LOWER(email) = 'user@example.com'`?
**Answer:**
Standard B-Tree indexes on `email` cannot be used because applying `LOWER()` transforms the runtime value, which does not match the raw case stored in the index.
- **Solution 1 (PostgreSQL Functional Index)**:
  ```sql
  CREATE INDEX idx_users_lower_email ON users (LOWER(email));
  ```
- **Solution 2 (Application-Level Normalization)**:
  Normalize all emails to lowercase before saving in Python/Django:
  `user.email = email.strip().lower()`. This avoids extra index overhead and allows a standard unique B-Tree index.
