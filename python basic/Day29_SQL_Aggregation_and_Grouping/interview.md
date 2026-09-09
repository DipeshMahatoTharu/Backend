# Day 29 — Real-World Backend Engineering Interview

These questions test your understanding of database aggregation internals, query planner execution algorithms, and high-scale analytical architectures.

---

### Question 1: Why is `SELECT COUNT(*)` Slow in PostgreSQL?
**Interview Scenario:**
> *"A developer writes `SELECT COUNT(*) FROM transactions;` on a PostgreSQL database with 50 million rows to show total transactions on the admin dashboard. The query takes 8 seconds and spikes disk I/O to 100%. Why doesn't PostgreSQL store a simple row-count counter in its metadata like MySQL MyISAM did, and how do you optimize this?"*

#### Senior Mentor Answer & Key Points:
1. **The MVCC (Multi-Version Concurrency Control) Constraint**:
   - In PostgreSQL, transactions run concurrently under snapshot isolation.
   - At any given millisecond, different concurrent transactions may see different numbers of rows (some rows were inserted by uncommitted transactions, others were soft/hard-deleted by transactions in progress).
   - Because row visibility depends on transaction IDs (`xmin`/`xmax`), PostgreSQL cannot maintain a single global row counter. It must scan the table or index pages to check row visibility for the current transaction's snapshot.
2. **Production Solutions**:
   - **Fast Approximation (Admin UI)**: If exact precision is not needed, query PostgreSQL system catalog statistics in sub-millisecond time:
     ```sql
     SELECT reltuples::bigint AS estimate FROM pg_class WHERE relname = 'transactions';
     ```
   - **Redis Counter Cache**: Increment a Redis key (`INCR transactions_count`) on every completed transaction insert.
   - **Trigger-Maintained Summary Table**: Use an atomic database trigger to update a single-row counter table.

---

### Question 2: Query Execution Engines: HashAggregate vs GroupAggregate
**Interview Scenario:**
> *"When inspecting an `EXPLAIN ANALYZE` output for a query with `GROUP BY`, what is the difference between a `HashAggregate` node and a `GroupAggregate` node? What happens when available memory (`work_mem`) is exceeded?"*

#### Senior Mentor Answer & Key Points:
1. **HashAggregate**:
   - The database builds an in-memory hash table where keys are the `GROUP BY` column values and values are the running aggregate accumulators.
   - **When Used**: When data is unsorted and the number of distinct groups fits within `work_mem`. Very fast $O(N)$ execution.
   - **Memory Spill**: If distinct groups exceed `work_mem`, the hash table spills to disk temporary files, causing massive performance drops.
2. **GroupAggregate (Sort-Based)**:
   - Requires input rows to already be sorted by the grouping columns (either via an existing B-tree index or an explicit `Sort` node).
   - As it reads rows sequentially, it accumulates metrics until the grouping key changes, then outputs the summarized row.
   - **When Used**: Ideal for large tables with existing indexes or when the number of groups is enormous, since memory usage is $O(1)$.

---

### Question 3: Live Aggregations vs Materialized Views at 10,000 QPS
**Interview Scenario:**
> *"Your SaaS platform has an analytics dashboard viewed by 50,000 active businesses. Calculating each business's monthly sales requires running multi-table `SUM()` and `AVG()` queries over 100 million records. Running this live on every page reload crashes the primary database. How do you re-architect this?"*

#### Senior Mentor Answer & Key Points:
1. **The Anti-Pattern**: Running analytical OLAP queries directly on the primary OLTP database serving customer checkouts and updates.
2. **Architecture Pattern 1: PostgreSQL Materialized Views**:
   - Create a precomputed summary:
     ```sql
     CREATE MATERIALIZED VIEW monthly_sales_summary AS
     SELECT business_id, DATE_TRUNC('month', order_date) AS month, SUM(total) AS revenue
     FROM orders GROUP BY 1, 2;
     ```
   - Refresh periodically in the background: `REFRESH MATERIALIZED VIEW CONCURRENTLY monthly_sales_summary;`.
3. **Architecture Pattern 2: Read Replicas & CQRS (Command Query Responsibility Segregation)**:
   - Direct all write operations (`INSERT`, `UPDATE`) to the Primary DB.
   - Replicate data via WAL streaming to Read Replicas dedicated to heavy dashboard analytical queries.
4. **Architecture Pattern 3: Analytical OLAP Engines**:
   - Stream transaction events via Kafka/Debezium into specialized columnar databases (ClickHouse, Snowflake, DuckDB) optimized specifically for multi-billion-row aggregations at sub-second speeds.