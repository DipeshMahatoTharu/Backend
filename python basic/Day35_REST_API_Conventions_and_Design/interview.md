# Day 35 — Real-World Backend Engineering Interview

These questions test your system architecture skills regarding REST API design, backward compatibility, and pagination.

---

### Question 1: REST vs GraphQL vs gRPC — How to Choose
**Interview Scenario:**
> *"When designing a new backend architecture, how do you decide whether to expose a RESTful API, a GraphQL interface, or gRPC services?"*

#### Senior Mentor Answer & Key Points:
1. **REST (Default for Public & Mobile APIs)**:
   - **Strengths**: Universal HTTP compatibility, browser-native caching via `ETag` and `Cache-Control`, simple debugging with cURL, strong standard status codes.
   - **Weaknesses**: Potential over-fetching or under-fetching of fields.
2. **GraphQL (Complex Aggregated Frontends)**:
   - **Strengths**: Client specifies exact fields requested; prevents over-fetching and allows consolidating multiple REST calls into a single query.
   - **Weaknesses**: Complex backend query parsing; vulnerable to expensive recursive queries; hard to cache at the CDN HTTP layer (since queries use `POST /graphql`).
3. **gRPC (Internal Microservices & High Throughput)**:
   - **Strengths**: Binary serialization with Protocol Buffers (Protobuf) is 5–10x faster and smaller than JSON; built-in streaming over HTTP/2; strict schema contracts.
   - **Weaknesses**: Not browser-friendly without gRPC-Web proxies; human-unreadable binary payload makes ad-hoc debugging harder.

---

### Question 2: Designing Keyset (Cursor) Pagination for Billions of Records
**Interview Scenario:**
> *"Why does `SELECT * FROM orders ORDER BY created_at LIMIT 20 OFFSET 1000000;` kill PostgreSQL/MySQL performance? How does cursor pagination solve this?"*

#### Senior Mentor Answer & Key Points:
1. **The Cost of SQL `OFFSET`**:
   - The database engine cannot jump directly to row 1,000,000. It must read and sort all 1,000,020 rows from disk, apply filter predicates, and then discard the first 1,000,000 rows. This causes high I/O and query latency measured in seconds.
2. **The Keyset / Cursor Solution**:
   - Instead of skipping rows, use indexed column filtering:
     ```sql
     SELECT * FROM orders
     WHERE (created_at, id) < ('2026-09-01 10:00:00', 49201)
     ORDER BY created_at DESC, id DESC
     LIMIT 20;
     ```
   - The B-Tree index locates the exact starting row in $O(\log N)$ time and reads only 20 rows.
3. **Opaque Cursors**:
   - Base64-encode the tuple `('2026-09-01 10:00:00', 49201)` into an opaque string `?cursor=MjAyNi0wOS0wMSAxMDowMDowMCw0OTIwMQ==` so clients do not depend on internal database column names.
