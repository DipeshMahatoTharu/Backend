"""
Day 58: Caching Systems & Redis — Practice
Hands-on exercises covering Cache-Aside patterns, TTL expiration tracking, and distributed lock simulation.
"""
import time
from typing import Dict, Any, Optional, Tuple

# ---------------------------------------------------------------------
# Task 1: In-Memory Cache with TTL
# ---------------------------------------------------------------------
class MemoryCache:
    def __init__(self):
        self._store: Dict[str, Tuple[Any, float]] = {}  # key -> (value, expiry_timestamp)

    def get(self, key: str) -> Optional[Any]:
        if key not in self._store:
            return None
        val, expiry = self._store[key]
        if time.time() > expiry:
            del self._store[key]  # Expired
            return None
        return val

    def set(self, key: str, value: Any, timeout: float = 60.0):
        self._store[key] = (value, time.time() + timeout)

    def delete(self, key: str):
        if key in self._store:
            del self._store[key]


# ---------------------------------------------------------------------
# Task 2: Cache-Aside Function Decorator
# ---------------------------------------------------------------------
def cache_aside(cache_instance: MemoryCache, key_prefix: str, timeout: float = 60.0):
    def decorator(fetch_func):
        def wrapper(*args, **kwargs):
            key = f"{key_prefix}:{':'.join(map(str, args))}"
            cached = cache_instance.get(key)
            if cached is not None:
                return cached
            # Cache miss: compute and store
            result = fetch_func(*args, **kwargs)
            cache_instance.set(key, result, timeout=timeout)
            return result
        return wrapper
    return decorator


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 58 Practice Tests ---")

    cache = MemoryCache()

    # Test Task 1: Get/Set with TTL
    cache.set("user:10", {"name": "Alice"}, timeout=10.0)
    assert cache.get("user:10")["name"] == "Alice"

    # Expired key test (simulated past timeout)
    cache.set("temp", "data", timeout=-5.0)
    assert cache.get("temp") is None

    # Test Task 2: Cache-aside decorator
    db_calls = [0]
    @cache_aside(cache, "expensive_calc", timeout=60.0)
    def expensive_query(entity_id: int) -> int:
        db_calls[0] += 1
        return entity_id * 100

    # Call 1: Miss (Hits DB)
    val1 = expensive_query(5)
    assert val1 == 500
    assert db_calls[0] == 1

    # Call 2: Hit (Does NOT hit DB)
    val2 = expensive_query(5)
    assert val2 == 500
    assert db_calls[0] == 1  # Unchanged!

    print("All Day 58 practice assertions passed successfully!")
