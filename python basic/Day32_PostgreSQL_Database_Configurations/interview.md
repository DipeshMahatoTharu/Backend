# Day 32 — Real-World Backend Engineering Interview

These questions test your understanding of PostgreSQL connection scaling, proxy pooling with PgBouncer, and production server performance tuning.

---

### Question 1: PgBouncer vs Application Connection Pools
**Interview Scenario:**
> *"You deploy a Django backend across 5 Kubernetes pods. Each pod runs Gunicorn with 8 worker processes. In total, you have 40 Gunicorn workers. When traffic spikes during marketing campaigns, PostgreSQL logs show `FATAL: remaining connection slots are reserved for non-replication superuser connections` and the entire site crashes. Why did this happen, and how does PgBouncer resolve it?"*

#### Senior Mentor Answer & Key Points:
1. **The Math of Connection Explosion**:
   - Gunicorn uses pre-forked worker processes. Each process runs independently and maintains its own local connection pool (e.g. `CONN_MAX_AGE` in Django).
   - If each worker opens 10 connections, 40 workers attempt to open $40 \times 10 = 400$ connections.
   - If Kubernetes auto-scales to 15 pods during a traffic spike, connections jump to $15 \times 8 \times 10 = 1,200$ connections!
   - Default PostgreSQL `max_connections` is 100. Even tuned databases struggle when connections exceed 300–500 because each connection is an OS process with heavy memory and context-switching overhead.
2. **The PgBouncer Architecture**:
   - PgBouncer runs as a lightweight intermediary daemon sitting right in front of PostgreSQL.
   - Client workers connect to PgBouncer. PgBouncer maintains a tiny pool of, say, 30 persistent connections to PostgreSQL.
   - Using **Transaction Pooling**, PgBouncer assigns a server connection to a client worker only for the brief duration of an active transaction (e.g. 5ms), and immediately reassigns it to another worker as soon as the transaction finishes.
   - This allows 1,000 application worker processes to smoothly share 30 PostgreSQL connections with near-zero latency overhead.

---

### Question 2: Prepared Statements & PgBouncer Transaction Mode
**Interview Scenario:**
> *"Why do standard Prepared Statements or `SET search_path` statements fail or cause cross-tenant bugs when using PgBouncer in Transaction Pooling mode?"*

#### Senior Mentor Answer & Key Points:
1. **Session State vs Transaction Pooling**:
   - In Transaction Pooling mode, a client worker might execute Transaction 1 on PostgreSQL Server Connection #4, and Transaction 2 on PostgreSQL Server Connection #7.
   - Server Connection #4 and #7 are shared dynamically across all clients.
2. **The Danger of Session-Level Changes**:
   - If Client A runs `SET TIMEZONE = 'Asia/Kathmandu'` or executes a prepared statement `PREPARE my_query AS ...` on Server Connection #4, that state persists on Connection #4!
   - When Client B inherits Connection #4 for their next transaction, they inherit Client A's timezone and cannot prepare `my_query` because it already exists (`ERROR: prepared statement already exists`).
3. **Solutions**:
   - Modern drivers (like `psycopg3` or `asyncpg`) support protocol-level unnamed prepared statements that do not leak session state.
   - Or use PgBouncer's `server_reset_query = DISCARD ALL` configuration, which clears session state before assigning a connection to the next client.

---

### Question 3: Core PostgreSQL Memory Parameters Tuning
**Interview Scenario:**
> *"You are provisioning a dedicated PostgreSQL production database on a 64 GB RAM Ubuntu server. What are the four most critical memory settings in `postgresql.conf`, and how do you size them?"*

#### Senior Mentor Answer & Key Points:
1. **`shared_buffers`**:
   - Dedicated RAM buffer cache for caching table and index disk pages.
   - **Recommended Sizing**: Set to approximately **25% of total system RAM** (e.g. 16 GB on a 64 GB server). Setting it higher is counterproductive because PostgreSQL relies on the Linux OS page cache for double-buffering.
2. **`work_mem`**:
   - Memory allocated for complex query operations like in-memory sorts (`ORDER BY`), HashAggregates (`GROUP BY`), and HashJoins.
   - **Critical Note**: Allocated **per operation, per connection**! If a single query has 3 joins and a sort, it can consume $4 \times \text{work\_mem}$.
   - **Recommended Sizing**: Start around 16 MB to 64 MB. Setting it too high can cause kernel Out-Of-Memory (OOM) crashes under high concurrency.
3. **`maintenance_work_mem`**:
   - Memory used for maintenance operations: `VACUUM`, `CREATE INDEX`, and `ALTER TABLE ADD FOREIGN KEY`.
   - **Recommended Sizing**: 1 GB to 2 GB (since only background autovacuum or DBA migrations use this).
4. **`effective_cache_size`**:
   - An estimate given to the query planner of how much total memory is available for caching data (sum of `shared_buffers` + Linux OS Page Cache).
   - **Recommended Sizing**: Typically **50% to 75% of total system RAM** (e.g. 32 GB to 48 GB on a 64 GB server). It does not allocate actual memory; it simply guides the planner to favor index scans over sequential disk scans when data fits in RAM.