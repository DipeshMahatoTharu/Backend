# Day 30 — Real-World Backend Engineering Interview

These questions test your understanding of database join algorithms, index strategies for foreign keys, and ORM join optimization.

---

### Question 1: Database Internal Join Algorithms
**Interview Scenario:**
> *"When looking at an `EXPLAIN` query plan in PostgreSQL, you see terms like `Nested Loop`, `Hash Join`, and `Merge Join`. What are the internal mechanics of each algorithm, and how does the cost-based optimizer decide which one to use?"*

#### Senior Mentor Answer & Key Points:
1. **Nested Loop Join**:
   - For every row in the outer table, it scans the inner table (ideally using a B-tree index on the join key).
   - **Time Complexity**: $O(N \times \log M)$ where $N$ is outer rows and $M$ is inner rows.
   - **When Chosen**: When one table is very small (or filtered to few rows) and the other table has a fast index on the join key.
2. **Hash Join**:
   - Scans the smaller table and builds an in-memory hash table on the join attribute. Then scans the larger table and probes the hash table.
   - **Time Complexity**: $O(N + M)$.
   - **When Chosen**: When joining large, unsorted tables with equality conditions (`ON a.id = b.a_id`) and sufficient `work_mem`.
3. **Merge Join**:
   - Both tables must already be sorted by the join key (e.g. from an existing B-tree index). The engine advances two pointers down both tables simultaneously.
   - **Time Complexity**: $O(N + M)$ if pre-sorted, or $O(N \log N + M \log M)$ if sorting is required.
   - **When Chosen**: Ideal for large joins where data is already indexed in sorted order or when performing full table scans.

---

### Question 2: Why Databases Don't Auto-Index Foreign Keys
**Interview Scenario:**
> *"When you define a Primary Key in PostgreSQL or MySQL, an index is automatically created. But when you define a `FOREIGN KEY (user_id) REFERENCES users(id)`, PostgreSQL does NOT automatically create an index on `user_id`. Why? What happens to `JOIN` and `DELETE` performance if you forget to add one?"*

#### Senior Mentor Answer & Key Points:
1. **Why No Automatic Index?**:
   - A primary key requires an index to enforce uniqueness. A foreign key only points to an already-indexed primary key in the parent table; it does not inherently require uniqueness in the child table.
   - Creating an index on every FK consumes disk space and slows down every `INSERT` into the child table.
2. **The Performance Penalties of Omitting FK Indexes**:
   - **JOIN Performance**: Every query that joins `users` to `orders` (`ON users.id = orders.user_id`) must perform a sequential full-table scan on the millions of rows in `orders` instead of a fast index lookup.
   - **Parent Deletion Lockout**: If you execute `DELETE FROM users WHERE id = 1;` with `ON DELETE CASCADE` or `RESTRICT`, the database must scan the entire `orders` table to check if matching child rows exist. Without an index, this triggers a full table scan and table-level locks that block concurrent writes!
3. **Rule of Thumb**: 99% of foreign key columns in backend databases should have an explicit B-tree index.

---

### Question 3: Django ORM: `select_related` vs `prefetch_related`
**Interview Scenario:**
> *"What is the N+1 query problem in Django ORM? How does `select_related` fix it using an SQL JOIN, how does `prefetch_related` fix it using separate SQL queries, and which one do you use for `ForeignKey` vs `ManyToManyField`?"*

#### Senior Mentor Answer & Key Points:
1. **The N+1 Problem**:
   - Querying 100 orders and looping through them to print `order.customer.name` executes 1 initial query for the orders, plus 100 separate queries (1 per customer) = 101 database round-trips!
2. **`select_related` (SQL JOIN)**:
   - Modifies the SQL query directly to perform an `INNER JOIN` or `LEFT JOIN` in a single database round-trip.
   - **Use Case**: Single-valued relationships: `ForeignKey` (one-to-many from child side) and `OneToOneField`.
   - **Example**: `Order.objects.select_related('customer').all()`.
3. **`prefetch_related` (Separate Queries + Python Join)**:
   - Executes 2 queries: Query 1 fetches all orders; Query 2 fetches all related records with `WHERE id IN (...)`. Django joins the objects in Python memory.
   - **Use Case**: Multi-valued relationships: `ManyToManyField` and reverse foreign keys (e.g. `customer.orders.all()`). A single SQL join on M2M would result in a massive Cartesian product of duplicate rows.