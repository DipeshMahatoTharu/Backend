# Day 34 — Real-World Database Normalization & Schema Design Interview Q&A

### Q1: What is Database Normalization, and what specific anomalies does 3NF eliminate?
**Answer:**
Normalization is the process of organizing relational schema columns and tables to minimize **data redundancy** and avoid **data modification anomalies**:
1. **Insertion Anomaly**: In an unnormalized table, you cannot record a new course without first enrolling a student if `student_id` is part of the primary key.
2. **Deletion Anomaly**: Deleting the last student enrolled in a course inadvertently deletes the course information entirely.
3. **Update Anomaly**: If a customer changes their address, you must update 10,000 historical order rows; missing even one creates data inconsistency.
- **3NF** ensures every non-key column depends on "the key, the whole key, and nothing but the key" (eliminates both partial and transitive dependencies).

---

### Q2: In modern cloud production, when would you intentionally violate 3NF (Denormalization)?
**Answer:**
You denormalize strategically in **read-heavy OLTP** or **analytical OLAP** workloads when joining normalized tables becomes a CPU and disk I/O bottleneck:
- **Example 1**: Caching aggregate counters (e.g. `comment_count` on a `posts` table) to avoid running `SELECT COUNT(*) FROM comments WHERE post_id = ?` on every feed request.
- **Example 2**: Snapshots of historical state (e.g. storing `unit_price_at_purchase` inside `order_items`). If the product price changes next month, historical orders must preserve what the customer actually paid.
- **Trade-off**: Denormalization trades increased write latency (keeping redundant fields in sync) and storage space for ultra-fast, single-table read queries.

---

### Q3: When should you choose `ON DELETE RESTRICT` / `PROTECT` vs `ON DELETE CASCADE`?
**Answer:**
- **Use `CASCADE` ONLY when child records have NO independent meaning without the parent**:
  - Example: `order_items` belonging to an `orders` draft, or `invoice_lines` belonging to an unapproved invoice.
- **Use `RESTRICT` / `PROTECT` for audit trails, financial records, and legal entities**:
  - Example: A user cannot be hard-deleted if they have associated payments or bank ledger entries. Deleting the parent should be blocked by the database with an `IntegrityError`, forcing the application to use a **Soft Delete** (`is_active = FALSE`, `deleted_at = NOW()`).

---

### Q4: Compare BIGINT auto-increment vs UUIDv4 as Primary Keys in PostgreSQL.
**Answer:**
- **BIGINT (BIGSERIAL)**:
  - Takes 8 bytes.
  - Generates monotonically increasing integers, which append sequentially to the rightmost leaf of the B-Tree index. This produces zero B-Tree page splits and optimal cache locality.
  - **Weakness**: Guessable/predictable IDs expose security risks if leaked in public URLs (`GET /invoices/1042`).
- **UUIDv4**:
  - Takes 16 bytes (2x storage in both heap and all foreign key indexes).
  - Random 128-bit values insert into random locations in the B-Tree index, triggering continuous disk page splits, cache churn, and table bloat once data exceeds RAM.
  - **Production Best Practice**: Use internal `BIGSERIAL` primary keys for fast joins and foreign keys, but add an indexed `public_id UUID DEFAULT gen_random_uuid()` column for public APIs.

---

### Q5: How do you model a Many-to-Many relationship with extra attributes in Django?
**Answer:**
Instead of a standard `ManyToManyField`, use a custom junction model specified with the `through` argument:
```python
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, through='Enrollment')

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course')
```
This cleanly models the relationship in 3NF while storing relationship-specific metadata.
