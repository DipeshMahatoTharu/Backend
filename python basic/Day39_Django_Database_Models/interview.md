# Day 39 — Real-World Backend Engineering Interview

These questions test your understanding of database schema design, migration mechanics, and concurrency.

---

### Question 1: How Do You Execute Zero-Downtime Migrations on Large Production Databases?
**Interview Scenario:**
> *"You need to rename a column `full_name` to `legal_name` on a table with 20 million active user rows in PostgreSQL without any downtime. What happens if you simply run `ALTER TABLE users RENAME COLUMN ...`?"*

#### Senior Mentor Answer & Key Points:
1. **The Instant Outage Risk**:
   - In a zero-downtime rolling deployment, older backend containers running old code are still actively executing queries like `SELECT full_name FROM users;`.
   - If you rename the column instantly in the database, all running instances will crash with `psycopg2.errors.UndefinedColumn`!
2. **The 3-Phase Expand/Contract Pattern**:
   - **Phase 1 (Expand)**: Add the new column `legal_name` as nullable. Deploy application code that writes to **both** `full_name` and `legal_name`, but reads from `full_name`.
   - **Phase 2 (Backfill)**: Run an asynchronous background script (via Celery or batch SQL) to copy `full_name` values into `legal_name` in small batches (e.g. 1,000 rows at a time) to prevent locking table pages.
   - **Phase 3 (Switch & Contract)**: Deploy application code that reads and writes exclusively to `legal_name`. Finally, run a migration to drop `full_name`.

---

### Question 2: Why `auto_now` Can Break Bulk Database Operations
**Interview Scenario:**
> *"Why does `Article.objects.filter(status='draft').update(status='published')` NOT update the `updated_at = models.DateTimeField(auto_now=True)` timestamp?"*

#### Senior Mentor Answer & Key Points:
1. **SQL Level vs Python Level**:
   - `QuerySet.update()` is converted directly into a single SQL statement: `UPDATE articles SET status = 'published' WHERE status = 'draft';`.
   - Django never instantiates the individual `Article` Python objects!
   - Because `auto_now` is implemented inside Python in the model's `.pre_save()` method, it is **never executed** during bulk `update()` calls.
2. **The Fix**:
   - Explicitly update the timestamp in the query:
     ```python
     from django.utils import timezone
     Article.objects.filter(status='draft').update(
         status='published',
         updated_at=timezone.now()
     )
     ```
