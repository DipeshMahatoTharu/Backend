# Day 33 — Real-World PostgreSQL Indexing & Optimization Interview Q&A

Practice answering these Senior/Junior Backend engineering interview questions independently before checking the reference breakdown.

---

### Q1: Walk me through what happens under the hood when PostgreSQL executes a query with a B-Tree index versus without one.

**Key Concepts to Cover:**
- 8KB disk page architecture and `shared_buffers` cache
- Sequential Scan / Heap Scan: $O(N)$ disk I/O cost
- B-Tree navigation: Root page $\to$ Branch pages $\to$ Leaf page in $O(\log N)$
- Tuple IDs (`TID`: Block Number, Offset) and heap pointer resolution

#### My Technical Explanation:
<!-- Practice explaining this in your own words before checking the mentor answer -->


<details>
<summary><b>Senior Mentor Model Answer & Technical Breakdown (Click to expand)</b></summary>

- **Without an Index (Sequential Scan / Heap Scan)**:
  PostgreSQL must read every 8KB page from the table on disk into RAM (`shared_buffers`). If a table is 10GB with 20 million rows, the operating system executes thousands of disk I/O operations, scanning every tuple one-by-one to evaluate the `WHERE` condition. Time complexity is $O(N)$, causing high latency and exhausting disk I/O bandwidth.
- **With a B-Tree Index (Index Scan)**:
  A B-Tree index is an ordered, balanced multi-way tree stored in separate 8KB pages. PostgreSQL begins at the **Root Page**, evaluates the search key, follows a pointer down internal branch pages, and reaches a **Leaf Page** in $O(\log N)$ steps (typically only 3 to 4 page reads even for millions of rows). The leaf page contains the indexed value and a Tuple ID (`TID` = Block Number, Offset). PostgreSQL then reads only the specific heap block to fetch the full row.
</details>

---

### Q2: What is an "Index-Only Scan", and why is it the holy grail of PostgreSQL query performance?

**Key Concepts to Cover:**
- Definition of Index-Only Scan vs standard Index Scan
- Covering indexes and the `INCLUDE` clause
- The critical role of the **Visibility Map** and MVCC
- What happens if `AUTOVACUUM` is delayed

#### My Technical Explanation:
<!-- Practice explaining this in your own words before checking the mentor answer -->


<details>
<summary><b>Senior Mentor Model Answer & Technical Breakdown (Click to expand)</b></summary>

An **Index-Only Scan** occurs when every column requested by the `SELECT` query is present directly inside the index itself (either as an indexed key or via the `INCLUDE` clause of a covering index).
- In a normal Index Scan, the engine must still visit the heap table pages to fetch non-indexed columns.
- In an Index-Only Scan, PostgreSQL reads **zero heap pages**, retrieving all data directly from the index in memory.
- **Critical Catch**: To return data without checking the heap, PostgreSQL consults the **Visibility Map** to verify whether the page has all-visible tuples (i.e. no uncommitted MVCC transactions). If the visibility map is not up to date (e.g. before an `AUTOVACUUM` has run), PostgreSQL is still forced to verify heap pages.
</details>

---

### Q3: What is the "Leftmost Prefix Rule" in composite indexing, and how do you decide column order?

**Key Concepts to Cover:**
- Physical ordering of multi-column indexes `(A, B, C)`
- Why queries on `(A)` or `(A, B)` use the index, but queries on `(B)` cannot
- Rule of thumb: Equality (`=`) columns vs Range (`>`, `<`, `BETWEEN`) or `ORDER BY` columns

#### My Technical Explanation:
<!-- Practice explaining this in your own words before checking the mentor answer -->


<details>
<summary><b>Senior Mentor Model Answer & Technical Breakdown (Click to expand)</b></summary>

A composite index on `(A, B, C)` is physically sorted in the B-Tree primarily by `A`, then by `B` for duplicate `A`s, and then by `C`.
- Queries filtering on `A`, or `(A, B)`, or `(A, B, C)` can fully utilize the index.
- Queries filtering only on `B` or `C` cannot use the index effectively because the tree is not sorted by `B` first (analogous to looking up phone numbers in a phonebook by first name when the book is sorted by last name).
- **Rule of Thumb for Column Order**:
  1. Place columns evaluated with **exact equality (`=`)** first.
  2. Place columns evaluated with **range conditions (`>`, `<`, `BETWEEN`)** or used in `ORDER BY` last.
</details>

---

### Q4: When does adding an index actually hurt application performance?

**Key Concepts to Cover:**
- Write amplification on `INSERT`, `UPDATE`, and `DELETE`
- Disk bloat and B-Tree page splits
- RAM cache contention (`shared_buffers` and OS page cache)
- Query planner evaluation overhead

#### My Technical Explanation:
<!-- Practice explaining this in your own words before checking the mentor answer -->


<details>
<summary><b>Senior Mentor Model Answer & Technical Breakdown (Click to expand)</b></summary>

1. **Write Overhead (Write Amplification)**: Every `INSERT`, `UPDATE`, and `DELETE` on a table must update not only the heap table but also every B-Tree index on that table. If a table has 12 indexes, one insert triggers 13 write operations!
2. **Page Splits & Bloat**: Updating an indexed column requires re-balancing tree pages, causing disk fragmentation, page splits, and bloated index files.
3. **RAM Cache Contention**: Indexes take up space in PostgreSQL's `shared_buffers` and the OS page cache. Too many indexes push frequently accessed table data out of memory into slow disk storage.
4. **Planner Confusion**: Having too many overlapping indexes increases the query planner's time to choose the optimal path.
</details>

---

### Q5: How do you optimize `SELECT * FROM users WHERE LOWER(email) = 'user@example.com'`?

**Key Concepts to Cover:**
- Why wrapping indexed columns in functions disables standard B-Tree indexes
- Solution 1: PostgreSQL functional/expression index syntax
- Solution 2: Application-layer normalization before storage

#### My Technical Explanation:
<!-- Practice explaining this in your own words before checking the mentor answer -->


<details>
<summary><b>Senior Mentor Model Answer & Technical Breakdown (Click to expand)</b></summary>

Standard B-Tree indexes on `email` cannot be used because applying `LOWER()` transforms the runtime value, which does not match the raw case stored in the index.
- **Solution 1 (PostgreSQL Functional Index)**:
  ```sql
  CREATE INDEX idx_users_lower_email ON users (LOWER(email));
  ```
- **Solution 2 (Application-Level Normalization)**:
  Normalize all emails to lowercase before saving in Python/Django:
  `user.email = email.strip().lower()`. This avoids extra index overhead and allows a standard unique B-Tree index.
</details>
