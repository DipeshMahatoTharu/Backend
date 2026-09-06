# Day 27 — Real-World Backend Engineering Interview

These questions test your understanding of database design, referential integrity, and production schema trade-offs.

---

### Question 1: Foreign Key Deletion Cascades & Data Loss
**Interview Scenario:**
> *"Explain the difference between `ON DELETE CASCADE`, `ON DELETE SET NULL`, and `ON DELETE RESTRICT`. Give a real-world scenario where an unthinking `ON DELETE CASCADE` caused catastrophic data loss in a financial or e-commerce system."*

#### Senior Mentor Answer & Key Points:
1. **The Rules**:
   - `CASCADE`: Deleting the parent row automatically deletes all matching child rows.
   - `SET NULL`: Deleting the parent row sets the child's foreign key column to `NULL` (requires the column to be nullable).
   - `RESTRICT` / `NO ACTION`: Aborts and rejects the deletion if any child rows reference the parent.
2. **The Catastrophic Incident Scenario**:
   - Consider a schema where an `orders` or `invoices` table has `user_id REFERENCES users(id) ON DELETE CASCADE`.
   - A customer requests GDPR account deletion ("Delete my profile"). A junior engineer issues `DELETE FROM users WHERE id = 42;`.
   - Because of `ON DELETE CASCADE`, the database instantly purges all historical invoices, financial payments, and transaction audit logs for that customer!
   - This violates legal tax compliance regulations requiring 7-year audit trails and corrupts financial accounting reconciliations.
3. **Best Practice**:
   - Use `ON DELETE RESTRICT` for financial transactions, audit logs, and payments.
   - Use soft-deletes (`is_deleted = TRUE` or `deleted_at = NOW()`) on the `users` table instead of hard `DELETE`.

---

### Question 2: UUID vs Auto-Incrementing Integer Primary Keys
**Interview Scenario:**
> *"Should backend databases use Auto-Incrementing Integers (`BIGSERIAL`) or UUIDs (v4/v7) for Primary Keys? What are the security, performance, and distributed systems trade-offs?"*

#### Senior Mentor Answer & Key Points:
1. **Auto-Incrementing Integers (`BIGINT` / `SERIAL`)**:
   - **Pros**: Compact (8 bytes), extremely fast B-Tree indexing, sequential insertions prevent B-tree page fragmentation.
   - **Cons**: Security risk (ID Enumeration / Insecure Direct Object Reference). An attacker seeing `/api/orders/1001` can easily guess `/api/orders/1002` or estimate company transaction volume. Does not work well in distributed multi-region databases where nodes generate keys independently.
2. **UUIDs (Universally Unique Identifiers)**:
   - **Pros**: Globally unique across distributed microservices; client or backend can generate the ID before contacting the DB; completely obscures system volume from URL sniffers.
   - **Cons**: Consumes 16 bytes (double the space); Random UUIDv4 causes severe B-tree index fragmentation in large tables, reducing write throughput.
3. **The Industry Gold Standard**:
   - Use **UUIDv7** (time-ordered UUIDs) which combine chronological sorting with randomness, eliminating B-tree fragmentation while maintaining global uniqueness.
   - Or maintain an internal sequential `BIGINT` primary key for foreign key joins, and expose an external `public_uuid` to API clients.

---

### Question 3: Normalization vs Production Denormalization
**Interview Scenario:**
> *"What is Database Normalization (1NF, 2NF, 3NF)? Why do production backends with millions of daily queries sometimes deliberately choose to denormalize tables?"*

#### Senior Mentor Answer & Key Points:
1. **Normalization Levels**:
   - **1NF**: Atomic values (no arrays or comma-separated lists in a column); each table has a primary key.
   - **2NF**: Meets 1NF + no partial dependency (all non-key columns depend on the entire primary key).
   - **3NF**: Meets 2NF + no transitive dependency (non-key columns do not depend on other non-key columns).
2. **Why Normalize**: Eliminates update anomalies, prevents duplicate data, and guarantees data consistency.
3. **Why Denormalize in High-Scale Production**:
   - Querying a 3NF schema for an e-commerce order history screen requires joining 5 to 7 tables (`orders`, `users`, `order_items`, `products`, `vendors`, `addresses`, `discounts`).
   - At high QPS (queries per second), multi-table joins exhaust database CPU and increase query latency.
   - Backends intentionally duplicate frequently read data (e.g., storing `cached_customer_name` directly on the `orders` table, or storing pre-aggregated `total_order_count` on the `user` table) to enable fast single-table `SELECT` queries without expensive joins.