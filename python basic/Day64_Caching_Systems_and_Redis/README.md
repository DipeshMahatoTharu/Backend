# Day 58 — In-Memory Caching, Redis & Celery Background Tasks

## 🎯 Learning Objectives
- Master caching topologies: In-Memory Cache (RAM) vs Distributed Cache (Redis) vs CDN Edge Cache.
- Understand caching patterns: Cache-Aside (Lazy Loading), Write-Through, and Write-Back.
- Implement Django caching with `django-redis`: Low-Level Cache API (`cache.get`, `cache.set`), View Caching (`@cache_page`), and Template Fragment Caching.
- Diagnose and eliminate the **Cache Stampede (Thundering Herd)** problem using distributed mutex locks.
- Understand Asynchronous Task Queuing with Celery + Redis broker: background emails, video transcoding, and scheduled jobs (`celery-beat`).

---

## 📚 Core Backend Concepts

### 1. The Cache-Aside Pattern
```python
from django.core.cache import cache

def get_product_details(product_id: int):
    cache_key = f"product:details:{product_id}"
    # 1. Check Redis
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return cached_data

    # 2. Cache Miss: Query PostgreSQL
    product = Product.objects.select_related('category').get(id=product_id)
    serialized_data = ProductSerializer(product).data

    # 3. Store in Redis with 15-minute TTL
    cache.set(cache_key, serialized_data, timeout=900)
    return serialized_data
```

### 2. Cache Stampede (Thundering Herd) Mitigation
When a cached home page visited by 10,000 users/sec expires, all 10,000 requests hit PostgreSQL simultaneously, crashing the database!
**Solution (Distributed Locking)**:
```python
def get_popular_data():
    data = cache.get("popular_data")
    if data is not None:
        return data

    # Acquire distributed lock so ONLY ONE thread recomputes the cache
    with cache.lock("lock:popular_data", timeout=5):
        # Double check cache inside lock
        data = cache.get("popular_data")
        if data is None:
            data = heavy_database_query()
            cache.set("popular_data", data, timeout=3600)
    return data
```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review Cache-Aside, Redis data types, Celery architecture, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build cache-aside decorators and mutex locks in [`practice.py`](practice.py), and fix caching traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Distributed Cache & Stampede Mitigation Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
