# Day 50 — Real-World Backend Engineering Interview

These questions test your understanding of API scalability, search performance, and pagination architecture.

---

### Question 1: How Do You Scale Search to Millions of Records Without ElasticSearch?
**Interview Scenario:**
> *"Your API has 10 million products. Using `search_fields = ['title', 'description']` causes 10-second queries because Django executes `WHERE title ILIKE '%query%' OR description ILIKE '%query%'` (which cannot use standard B-tree indexes). How do you fix this in PostgreSQL without adding ElasticSearch?"*

#### Senior Mentor Answer & Key Points:
1. **The B-Tree Failure**:
   - Standard B-Tree indexes only optimize prefix matches (`ILIKE 'query%'`). Leading wildcards (`'%query%'`) force a full sequential scan of all 10 million rows!
2. **PostgreSQL Trigram (pg_trgm) & GIN Indexes**:
   - Enable PostgreSQL's trigram extension: `CREATE EXTENSION pg_trgm;`.
   - Add a Generalized Inverted Index (GIN) over the searchable fields:
     ```python
     from django.contrib.postgres.indexes import GinIndex

     class Meta:
         indexes = [
             GinIndex(fields=['title'], opclasses=['gin_trgm_ops'], name='title_trgm_gin_idx')
         ]
     ```
   - GIN trigram indexes evaluate substring searches in single-digit milliseconds without requiring external search clusters.

---

### Question 2: Designing API Rate Limiting & Throttling
**Interview Scenario:**
> *"How does DRF enforce rate limiting (e.g. 60 requests/minute)? How does it track rates in distributed environments?"*

#### Senior Mentor Answer & Key Points:
1. **The Sliding Window / Token Bucket Algorithm**:
   - DRF uses Redis cache keys (e.g. `throttle_anon_<ip>` or `throttle_user_<user_id>`).
   - Each request appends the current timestamp to a Redis list and trims timestamps older than 60 seconds.
   - If the list length exceeds 60, DRF raises `Throttled(detail=...)` and returns `429 Too Many Requests`.
2. **Headers**:
   - Always include the `Retry-After: 35` header indicating the number of seconds the client must wait before retrying.
