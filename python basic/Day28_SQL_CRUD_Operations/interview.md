# Day 28 — Real-World Backend Engineering Interview

These questions test your understanding of query performance, pagination at scale, and database security.

---

### Question 1: The "Deep Paging" Problem: Offset vs Cursor Pagination
**Interview Scenario:**
> *"Our mobile app has an infinite-scroll feed of user posts. The junior engineer implemented it using `LIMIT 20 OFFSET (page * 20)`. Once users scroll to page 500, the API response time jumps from 15ms to 1,200ms. Why does `OFFSET` slow down at scale, and how does Keyset/Cursor Pagination solve this?"*

#### Senior Mentor Answer & Key Points:
1. **The Flaw of `OFFSET`**:
   - `OFFSET 10000 LIMIT 20` requires the database engine to scan and discard 10,000 rows before returning the 20 requested rows.
   - Even with a B-tree index, the storage engine must traverse the index tree 10,020 times.
   - Concurrency issue: If a new post is added while a user is on page 1, when they scroll to page 2, the items shift, causing duplicate posts to appear on the client screen.
2. **The Keyset (Cursor-Based) Solution**:
   - Instead of skipping rows with `OFFSET`, remember the last seen record's unique sort value (cursor):
     ```sql
     -- Instead of LIMIT 20 OFFSET 10000:
     SELECT id, title, created_at FROM posts
     WHERE created_at < '2026-09-09 12:00:00'
     ORDER BY created_at DESC, id DESC
     LIMIT 20;
     ```
   - With an index on `(created_at, id)`, the database jumps directly to the cursor row in $O(\log N)$ time and reads only 20 rows, maintaining consistent 5ms latency regardless of whether you are on page 1 or page 10,000.

---

### Question 2: Soft Deletes & Partial Indexes in PostgreSQL
**Interview Scenario:**
> *"We implemented soft deletes (`is_deleted = true`) on our `orders` table. Now every single query in our Django backend must include `WHERE is_deleted = false`. Over 5 years, 90% of our 50 million orders are marked deleted. Queries are crawling. How do you fix this?"*

#### Senior Mentor Answer & Key Points:
1. **The Problem**:
   - Regular B-tree indexes index every single row, including the 45 million deleted rows.
   - When searching for active orders, the database must traverse bloated index trees.
2. **The Solution: Partial Indexes**:
   - PostgreSQL allows **Partial Indexes** that only index rows satisfying a predicate:
     ```sql
     CREATE INDEX idx_active_orders_user 
     ON orders (user_id, created_at) 
     WHERE is_deleted = FALSE;
     ```
   - The index size shrinks by 90%, fits entirely into RAM buffer cache, and provides lightning-fast index scans for all active user queries.
3. **Table Partitioning / Archiving**:
   - Alternatively, partition the table by date or move soft-deleted records older than 1 year to an `orders_archive` cold-storage table to keep the active table small.

---

### Question 3: How Parameterized Queries Stop SQL Injection
**Interview Scenario:**
> *"Why does `cursor.execute('SELECT * FROM users WHERE username = %s', (user_input,))` completely prevent SQL injection, whereas `cursor.execute(f'SELECT * FROM users WHERE username = \'{user_input}\'')` does not? What happens at the database protocol level?"*

#### Senior Mentor Answer & Key Points:
1. **String Formatting (Vulnerable)**:
   - The Python application concatenates the user input into the SQL string.
   - The entire string is sent to the database parser as a single code payload.
   - The SQL parser cannot distinguish between SQL keywords (`OR`, `DROP`, `--`) and user data, executing attacker commands with database permissions.
2. **Parameterized / Prepared Statements (Secure)**:
   - The query structure and the query data are transmitted in two completely separate packets/steps:
     * **Step 1 (Prepare)**: The database receives the query template `SELECT * FROM users WHERE username = $1` and parses/compiles the execution plan.
     * **Step 2 (Execute)**: The database receives the literal parameter values in a separate data packet.
   - Even if the input is `' OR '1'='1' --`, the database treats the entire input strictly as a literal string value to compare against `username`, making syntax manipulation mathematically impossible.