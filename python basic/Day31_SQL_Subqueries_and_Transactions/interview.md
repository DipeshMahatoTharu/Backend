# Day 31 — Real-World Backend Engineering Interview

These questions test your understanding of database transaction isolation, concurrency control, and distributed systems architecture.

---

### Question 1: Transaction Isolation Levels & Concurrency Anomalies
**Interview Scenario:**
> *"Explain the four ANSI SQL transaction isolation levels. What concurrency anomalies (Dirty Read, Non-Repeatable Read, Phantom Read) does each level prevent, and what is the default in PostgreSQL?"*

#### Senior Mentor Answer & Key Points:
1. **The Three Concurrency Anomalies**:
   - **Dirty Read**: Transaction A reads uncommitted modifications made by Transaction B. If B rolls back, A based its decisions on data that never existed.
   - **Non-Repeatable Read**: Transaction A reads a row. Transaction B updates/deletes that row and commits. Transaction A reads the row again and observes modified or missing values.
   - **Phantom Read**: Transaction A reads a range of rows matching a predicate (e.g. `WHERE age > 30`). Transaction B inserts a new row matching that predicate and commits. Transaction A queries the same range again and sees "phantom" new rows.
2. **Isolation Levels Matrix**:
   | Isolation Level | Dirty Reads | Non-Repeatable Reads | Phantom Reads |
   | :--- | :---: | :---: | :---: |
   | **Read Uncommitted** | Possible | Possible | Possible |
   | **Read Committed** *(PostgreSQL Default)* | **Prevented** | Possible | Possible |
   | **Repeatable Read** | **Prevented** | **Prevented** | **Prevented** (in Postgres MVCC) |
   | **Serializable** | **Prevented** | **Prevented** | **Prevented** |
3. **Trade-offs**: Higher isolation levels eliminate anomalies by increasing lock contention or serial execution checks, reducing maximum write throughput.

---

### Question 2: Optimistic Locking vs Pessimistic Locking
**Interview Scenario:**
> *"You are building an inventory checkout service for a flash sale where 10,000 customers are trying to buy 50 available PlayStation 5 consoles simultaneously. When would you use Optimistic Locking vs Pessimistic Locking?"*

#### Senior Mentor Answer & Key Points:
1. **Pessimistic Locking (`SELECT ... FOR UPDATE`)**:
   - Explicitly locks the database row until the transaction commits or rolls back:
     ```sql
     SELECT stock FROM items WHERE id = 101 FOR UPDATE;
     UPDATE items SET stock = stock - 1 WHERE id = 101;
     ```
   - **Pros**: 100% deterministic; zero conflicts because concurrent requests queue up behind the lock.
   - **Cons**: High database lock contention; if transactions take too long (e.g. calling external Stripe APIs while holding the DB lock), connection pools get exhausted.
2. **Optimistic Locking (Version Column)**:
   - Does not lock rows on read. Instead, checks a `version` integer on write:
     ```sql
     UPDATE items 
     SET stock = stock - 1, version = version + 1 
     WHERE id = 101 AND version = 5 AND stock > 0;
     ```
   - If another request updated the item first, the row count is 0, signaling a collision. The application catches this and retries.
   - **Pros**: Zero database locks; fast when conflicts are rare.
   - **Cons**: In heavy contention (10,000 users competing for 50 items), 99.5% of optimistic retries fail, wasting server CPU.
3. **The Flash Sale Architecture**:
   - In extreme flash sales, neither direct DB locking pattern is ideal! Backends use in-memory Redis atomic operations (`DECR` / Lua script) to validate stock in sub-milliseconds, then enqueue orders asynchronously via message queues (Kafka/RabbitMQ) for asynchronous database persistence.

---

### Question 3: Distributed Transactions: Two-Phase Commit (2PC) vs Saga Pattern
**Interview Scenario:**
> *"In a microservices architecture, placing an order requires deducting funds in the `Payments Service` (PostgreSQL A) and reserving stock in the `Inventory Service` (PostgreSQL B). Why don't modern teams use Two-Phase Commit (2PC) across microservices, and how does the Saga Pattern solve this?"*

#### Senior Mentor Answer & Key Points:
1. **Why Two-Phase Commit (2PC) Fails in Cloud Microservices**:
   - 2PC acts as a distributed lock across multiple databases. If the network hiccups or one service is slow, all participants hold database locks open indefinitely, leading to cascading failures, latency spikes, and system-wide unavailability.
2. **The Saga Pattern**:
   - Breaks the distributed transaction into a sequence of local transactions coordinated through event messages (Choreography) or a central workflow orchestrator (Orchestration).
   - Each local transaction updates its own database and emits an event.
3. **Compensating Transactions (Rollback Mechanism)**:
   - If Service B fails (e.g. inventory out of stock), the Saga orchestrator sends compensating events to undo previous steps:
     * Step 1: Payment Service charges credit card (Local TX).
     * Step 2: Inventory Service fails (Out of stock).
     * Compensating Step: Payment Service executes an automatic refund (Compensating TX) to restore eventual consistency.