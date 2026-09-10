# Day 59 — Real-World Backend Engineering Interview

These questions cover the most frequent, high-stakes questions asked in senior backend engineering interviews.

---

### Question 1: How Do You Design a Scalable URL Shortener (Bitly) in Django?
**Interview Scenario:**
> *"Design a URL Shortener that handles 100 million active URLs and 10,000 redirects per second. What database schema, encoding algorithm, and caching strategy do you use?"*

#### Senior Mentor Answer & Key Points:
1. **Base62 Encoding vs Random Hashes**:
   - Do NOT use MD5/SHA256 (requires collision detection).
   - Use an auto-incrementing 64-bit integer ID and convert it to Base62 (`[0-9a-zA-Z]`).
   - A 7-character Base62 string yields $62^7 pprox 3.5	ext{ trillion}$ unique URLs!
2. **Database Schema**:
   ```sql
   CREATE TABLE urls (
       id BIGSERIAL PRIMARY KEY,
       short_code VARCHAR(10) UNIQUE NOT NULL,
       original_url TEXT NOT NULL,
       created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
   );
   ```
3. **Caching Strategy (Redis)**:
   - 99% of traffic is redirects (reads). Cache active short codes in Redis: `short_code -> original_url`.
   - The view checks Redis first. On cache hit, returns `301 Moved Permanently` (browser caches) or `302 Found` (if analytics/click tracking is required).

---

### Question 2: How Do You Handle Database Deadlocks in Distributed Systems?
**Interview Scenario:**
> *"Two background workers simultaneously execute bank transfers between Account 1 and Account 2. Worker A transfers from 1 to 2; Worker B transfers from 2 to 1. The database halts with `DeadlockDetected`. How do you fix this?"*

#### Senior Mentor Answer & Key Points:
1. **The Circular Wait Hazard**:
   - Worker A locks Account 1 (`SELECT FOR UPDATE WHERE id = 1`) and tries to lock Account 2.
   - Worker B locks Account 2 (`SELECT FOR UPDATE WHERE id = 2`) and tries to lock Account 1.
   - Neither can proceed: Deadlock!
2. **The Global Resource Ordering Defense**:
   - Always acquire locks in a strictly defined order (e.g. numerical order of Primary Key):
     ```python
     acc_first_id = min(from_id, to_id)
     acc_second_id = max(from_id, to_id)

     with transaction.atomic():
         acc1 = Account.objects.select_for_update().get(id=acc_first_id)
         acc2 = Account.objects.select_for_update().get(id=acc_second_id)
     ```
   - Both workers now attempt to lock the lower ID first. The second worker simply waits for the first to complete, eliminating the circular wait entirely.
