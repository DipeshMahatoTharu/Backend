"""
Day 58 Daily Challenge: Distributed Cache-Aside & Stampede Mitigation Engine

Problem:
Implement an advanced Cache Engine with stampede protection:
1. Cache-Aside `get_or_set(key, fetch_fn, timeout)`: Retrieves cached item or computes and saves.
2. Stampede Protection via Mutex Locking:
   - When cache misses, attempts to acquire a non-blocking lock `lock:<key>`.
   - The thread that acquires the lock recomputes the cache.
   - Other concurrent threads wait briefly and retry the cache instead of slamming the database!
3. Key Invalidation: `invalidate_pattern(prefix)` purges all matching cache keys upon update.
"""
import time
from typing import Dict, Any, Optional, Callable, Set

class DistributedCacheEngine:
    def __init__(self):
        self._cache: Dict[str, Tuple[Any, float]] = {}  # key -> (val, exp)
        self._locks: Set[str] = set()
        self.db_query_count = 0

    def get(self, key: str) -> Optional[Any]:
        if key in self._cache:
            val, exp = self._cache[key]
            if time.time() <= exp:
                return val
            del self._cache[key]
        return None

    def set(self, key: str, val: Any, timeout: float = 60.0):
        self._cache[key] = (val, time.time() + timeout)

    def acquire_lock(self, lock_key: str) -> bool:
        if lock_key in self._locks:
            return False
        self._locks.add(lock_key)
        return True

    def release_lock(self, lock_key: str):
        self._locks.discard(lock_key)

    def get_or_set(self, key: str, fetch_fn: Callable[[], Any], timeout: float = 60.0) -> Any:
        cached_val = self.get(key)
        if cached_val is not None:
            return cached_val

        lock_key = f"lock:{key}"
        # Attempt lock acquisition
        if self.acquire_lock(lock_key):
            try:
                # Double check inside lock
                val = self.get(key)
                if val is not None:
                    return val

                self.db_query_count += 1
                val = fetch_fn()
                self.set(key, val, timeout=timeout)
                return val
            finally:
                self.release_lock(lock_key)
        else:
            # Another worker is calculating; poll cache for short period
            for _ in range(5):
                val = self.get(key)
                if val is not None:
                    return val
            # Fallback if lock holder hung
            self.db_query_count += 1
            return fetch_fn()

    def invalidate_prefix(self, prefix: str):
        keys_to_delete = [k for k in self._cache if k.startswith(prefix)]
        for k in keys_to_delete:
            del self._cache[k]


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    engine = DistributedCacheEngine()

    def heavy_db_query():
        return {"report": "Q3 Financials", "revenue": 1000000}

    # 1. First request triggers DB query
    res1 = engine.get_or_set("reports:q3", heavy_db_query, timeout=10.0)
    assert res1["revenue"] == 1000000
    assert engine.db_query_count == 1

    # 2. Subsequent 10 requests hit cache (0 DB queries)
    for _ in range(10):
        res = engine.get_or_set("reports:q3", heavy_db_query, timeout=10.0)
        assert res["revenue"] == 1000000
    assert engine.db_query_count == 1

    # 3. Cache Invalidation
    engine.invalidate_prefix("reports:")
    assert engine.get("reports:q3") is None

    # 4. Request after invalidation triggers DB query again
    res2 = engine.get_or_set("reports:q3", heavy_db_query, timeout=10.0)
    assert engine.db_query_count == 2

    print("All DistributedCacheEngine challenge tests passed successfully!")
