# Day 34 — Database Normalization (1NF–3NF), Schema Design & ER Modeling

## 🎯 Learning Objectives
- Master Relational Database Normalization: **1NF, 2NF, 3NF**, and BCNF.
- Understand the trade-offs between **Strict Normalization** (write integrity) and **Intentional Denormalization** (read performance).
- Design production-grade schemas with **Junction Tables**, Foreign Key constraint actions (`CASCADE`, `SET NULL`, `PROTECT/RESTRICT`).
- Compare Primary Key strategies: **Auto-increment BIGINT** vs **UUIDv4** vs **ULID/Snowflake ID**.
- Model real-world systems on a whiteboard (E-commerce, Uber/Ride-sharing, Multi-tenant SaaS).

---

## 📚 Core Backend Concepts

### 1. The Normal Forms Demystified
- **First Normal Form (1NF)**:
  - Each column contains atomic (indivisible) values (no CSV strings like `"electronics,books"` stored in one cell!).
  - Each record must be uniquely identifiable (needs a Primary Key).
  - No repeating groups.
- **Second Normal Form (2NF)**:
  - Must be in 1NF.
  - No **Partial Dependencies**: Every non-key column must depend on the *entire* primary key, not just part of a composite primary key.
- **Third Normal Form (3NF)**:
  - Must be in 2NF.
  - No **Transitive Dependencies**: Non-key attributes must NOT depend on other non-key attributes ($A \to B \to C$).
  - *Example*: In an `orders` table with `(order_id, customer_id, customer_email, customer_address)`, `customer_email` depends on `customer_id`, not `order_id`! It must be moved to a `customers` table.

### 2. When to Intentionally Denormalize in Production
In read-heavy systems (e.g. Amazon product catalog, analytics, social media feeds), strictly normalized schemas require joining 8–10 tables per request, causing massive CPU load.
- **Strategic Denormalization**: Storing redundant summary data (e.g. `order_total_amount`, `cached_author_name`, or `comment_count` on a post).
- **Rule of Thumb**: Normalize by default for transactional integrity (OLTP); denormalize selectively for heavy read bottlenecks with automated cache/trigger invalidation.

### 3. Primary Key Architecture: BIGSERIAL vs UUIDv4
| Feature | BIGSERIAL (Auto-Increment 64-bit int) | UUIDv4 (128-bit random) |
| :--- | :--- | :--- |
| **Storage** | 8 bytes (compact) | 16 bytes (2x storage) |
| **Index B-Tree Impact** | Append-only sequential; 0% page splits | Random values; causes severe B-Tree page splits & fragmentation |
| **Security** | Predictable (`/users/102` -> `/users/103` ID enumeration attack!) | Cryptographically unguessable |
| **Distributed Systems** | Requires central database coordinator | Can be generated independently on any microservice without DB collision |

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + NORMALIZATION DRILLS (60 min)**:
  - 40 min: Review 1NF, 2NF, 3NF rules, PK tradeoffs, and FK deletion semantics.
  - 20 min: Complete schema normalization analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/questions.md)**.

- **HOUR 2 — SCHEMA CODING & MIGRATION DRILLS (60 min)**:
  - 35 min: Implement schema normalization refactoring script in **[`practice.py`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/practice.py)**.
  - 25 min: Fix foreign key cascades and orphan row bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/debugging.py)**.

- **HOUR 3 — WHITEBOARD ER DESIGN & INTERVIEW (60 min)**:
  - 20 min: Study Senior Database Architect interview questions in **[`interview.md`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/interview.md)**.
  - 20 min: Complete the blank-page Ride-Sharing ER Schema on **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/whiteboard.py)**.
  - 20 min: Build the Multi-Tenant E-Commerce Relational Engine in **[`challenge.py`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Answered normalization questions in **[`questions.md`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/questions.md)**
- [ ] Refactored denormalized schema in **[`practice.py`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/practice.py)**
- [ ] Fixed orphan records and cascade deletion in **[`debugging.py`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/debugging.py)**
- [ ] Designed Ride-Sharing Schema on **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/whiteboard.py)**
- [ ] Passed relational schema constraints in **[`challenge.py`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/challenge.py)**
- [ ] Mastered Database Design interview questions in **[`interview.md`](file:///d:/Backend/python%20basic/Day34_Database_Normalization_and_Schema_Design/interview.md)**
