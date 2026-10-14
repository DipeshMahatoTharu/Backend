# Day 34 — Database Normalization & Schema Design Conceptual Questions

Please answer each question thoroughly in the spaces provided below.

---

### 34.1 Normal Forms (1NF, 2NF, 3NF) Breakdown
**QUESTION:**
Explain the specific flaw violated by each of the following scenarios:
1. A table `students` stores `enrolled_courses` as `"Math, CS, Physics"` in a single text column. Which normal form does this violate?
2. A table `order_items` has a composite primary key `(order_id, product_id)`. It also contains `product_name` and `product_price`. Which normal form does this violate, and why?
3. A table `employees` has columns `(emp_id, emp_name, department_id, department_name, department_manager)`. Which normal form does this violate, and why?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 34.2 Foreign Key Deletion Semantics
**QUESTION:**
Explain the real-world operational differences between these Foreign Key actions on delete:
1. `ON DELETE CASCADE`
2. `ON DELETE SET NULL`
3. `ON DELETE RESTRICT` / `ON DELETE NO ACTION` (or Django's `models.PROTECT`)
In a financial banking system with `accounts` and `transactions`, which deletion policy must you choose, and why is `CASCADE` an absolute disaster?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 34.3 Auto-Increment vs UUIDv4 Primary Keys
**QUESTION:**
1. Why does using random `UUIDv4` as a clustered Primary Key in PostgreSQL or MySQL cause high disk I/O and B-Tree page splits as the table grows to tens of millions of rows?
2. How does the hybrid approach (using an internal `BIGSERIAL` integer for primary key/joins, and exposing an external `UUID` / `public_id` to API consumers) give the best of both worlds?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 34.4 Many-to-Many Relationships & Junction Tables
**QUESTION:**
When modeling a Many-to-Many relationship (e.g. `Students` and `Courses`), why is an intermediary Junction Table required? What additional metadata columns belong in this junction table rather than in `Students` or `Courses`?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 34.5 When and Why Denormalize?
**QUESTION:**
In a high-scale e-commerce system with 50,000 requests/second, why might storing `order_total_amount` directly on the `orders` table (denormalization) be preferred over calculating `SUM(quantity * unit_price)` from `order_items` on every query? What mechanism prevents this denormalized value from getting out of sync?

**MY ANSWER:**
____________________________________________________
____________________________________________________
