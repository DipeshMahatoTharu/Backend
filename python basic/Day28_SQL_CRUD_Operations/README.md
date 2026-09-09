# Day 28 — SQL CRUD Operations, Filtering & Safe State Transitions

## 🎯 Learning Objectives
- Master Data Manipulation Language (DML) commands: `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.
- Write high-performance filtering queries using `WHERE`, logical operators (`AND`, `OR`, `NOT`), range checks (`BETWEEN`), sets (`IN`), and pattern matching (`LIKE`, `ILIKE`).
- Implement safe updates and understand why naked `UPDATE` or `DELETE` queries without `WHERE` cause company outages.
- Architect **Soft Delete** patterns (`is_deleted`, `deleted_at`) to preserve audit trails and prevent catastrophic data loss.
- Master result set sorting (`ORDER BY`) and pagination (`LIMIT`, `OFFSET`).

---

## 📚 Core Backend Concepts

### 1. The CRUD Query Lifecycle
- **Create (`INSERT`)**:
  ```sql
  -- Single row insert
  INSERT INTO products (name, price, stock) VALUES ('Mechanical Keyboard', 89.99, 15);

  -- High-performance batch insert (single round-trip to database)
  INSERT INTO products (name, price, stock) VALUES 
      ('Mouse Pad', 15.00, 50),
      ('USB-C Hub', 35.50, 30);
  ```
- **Read (`SELECT`)**:
  ```sql
  SELECT id, name, price FROM products 
  WHERE price BETWEEN 20.00 AND 100.00 
    AND stock > 0 
    AND is_deleted = FALSE
  ORDER BY price DESC, name ASC 
  LIMIT 10 OFFSET 0;
  ```
- **Update (`UPDATE`)**:
  ```sql
  -- ALWAYS specify a WHERE clause!
  UPDATE products 
  SET price = price * 0.90, updated_at = CURRENT_TIMESTAMP 
  WHERE category_id = 5 AND is_available = TRUE;
  ```
- **Delete (`DELETE`) vs Soft Delete**:
  ```sql
  -- DANGEROUS: Permanent loss of record and FK cascade risks
  DELETE FROM users WHERE id = 42;

  -- PRODUCTION BEST PRACTICE: Soft Delete
  UPDATE users 
  SET is_deleted = TRUE, deleted_at = CURRENT_TIMESTAMP 
  WHERE id = 42;
  ```

### 2. The Three-Valued Logic of SQL (NULL Handling)
In SQL, `NULL` does not mean "zero" or "empty string"—it means **UNKNOWN**.
Because of this, `NULL = NULL` evaluates to `UNKNOWN` (falsy), **NOT TRUE**!
- Never use `WHERE column = NULL` or `WHERE column != NULL`.
- Always use `WHERE column IS NULL` or `WHERE column IS NOT NULL`.

### 3. Pagination: `LIMIT` & `OFFSET`
REST APIs return paginated responses to protect backend memory:
$$\text{OFFSET} = (\text{page} - 1) \times \text{page\_size}$$
For example, for page 3 with 20 items per page: `LIMIT 20 OFFSET 40`.

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + CONCEPT DRILLS (60 min)**:
  - 40 min: Review CRUD syntax, pattern matching, NULL logic, and pagination.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/questions.md)**.

- **HOUR 2 — SQL PRACTICE & DEBUGGING (60 min)**:
  - 35 min: Write the CRUD queries in **[`practice.sql`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/practice.sql)**.
  - 25 min: Diagnose real-world SQL injection and update bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/debugging.py)**.

- **HOUR 3 — INTERVIEW & PORTFOLIO CHALLENGE (60 min)**:
  - 20 min: Study offset vs cursor pagination in **[`interview.md`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/interview.md)**.
  - 20 min: Write the multi-criteria search query on **[`whiteboard.sql`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/whiteboard.sql)**.
  - 20 min: Build the E-Commerce Product Search & Pagination Engine in **[`challenge.py`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Read concepts and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/questions.md)**
- [ ] Completed all CRUD tasks in **[`practice.sql`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/practice.sql)**
- [ ] Fixed all bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/debugging.py)**
- [ ] Solved whiteboard challenge in **[`whiteboard.sql`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/whiteboard.sql)**
- [ ] Built and verified search engine in **[`challenge.py`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/challenge.py)**
- [ ] Studied backend interview answers in **[`interview.md`](file:///d:/Backend/python%20basic/Day28_SQL_CRUD_Operations/interview.md)**