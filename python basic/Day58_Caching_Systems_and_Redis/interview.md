# Day 58 — Real-World Backend Engineering Interview

These questions test your mastery of caching architectures, Redis eviction algorithms, and distributed task queuing.

---

### Question 1: How Do You Prevent Cache Stampede (Thundering Herd) in High-Volume Systems?
**Interview Scenario:**
> *"Your e-commerce home page receives 10,000 requests per second. The home page cache expires every 10 minutes. Exactly at the 10-minute mark, your PostgreSQL database CPU spikes to 100% and crashes. How do you solve this without extending the cache timeout?"*

#### Senior Mentor Answer & Key Points:
1. **The Root Cause (Thundering Herd)**:
   - At second 600, the cache key expires.
   - All 10,000 incoming requests discover a cache miss simultaneously.
   - All 10,000 threads execute the heavy database query at the exact same millisecond, crushing the database.
2. **Solution 1: Distributed Mutex Locking**:
   - The first worker to detect the miss acquires a Redis lock: `SET lock:homepage 1 NX EX 5`.
   - Only this worker runs the DB query and repopulates the cache.
   - The remaining 9,999 requests wait 50ms or return slightly stale data while the lock is held.
3. **Solution 2: Probabilistic Early Expiration (XFetch Algorithm)**:
   - Workers recompute the cache slightly *before* it actually expires:
     $$\Delta 	imes eta 	imes \ln(	ext{random}())$$
   - If a request arrives within 30 seconds of expiration, there is an increasing statistical probability that one single worker asynchronously recalculates the cache before it ever expires!

---

### Question 2: Redis Eviction Policies (`allkeys-lru` vs `volatile-lru`)
**Interview Scenario:**
> *"What happens when Redis runs out of memory (`maxmemory` reached)? How do you choose between `allkeys-lru`, `volatile-lru`, and `noeviction`?"*

#### Senior Mentor Answer & Key Points:
1. **`noeviction` (Default for Queues / Celery)**:
   - When memory is full, Redis returns an error on all new write commands. Mandatory when Redis is used as a message broker where dropping messages means data loss.
2. **`allkeys-lru` (Pure Caching Tier)**:
   - Evicts the least recently used keys out of all keys in the database. Best when Redis is used strictly as an application cache.
3. **`volatile-lru` (Hybrid)**:
   - Evicts LRU keys *only* among keys that have an explicit `TTL` (expiration) set. Keys without an expiration are preserved.
