"""
Day 58: Caching Systems & Redis — Debugging
Diagnose and fix 3 common caching pitfalls and stampede bugs.
"""
from typing import Dict, Any, Optional

# ---------------------------------------------------------------------
# Bug 1: Storing Non-JSON-Serializable Objects in Redis
# Problem: A view stored an un-evaluated Django QuerySet directly in cache:
# `cache.set('users', User.objects.all())`. Because QuerySets are not serializable,
# it crashed when retrieved by another worker process!
# Fix: Serialize to list of dicts before caching.
# ---------------------------------------------------------------------
def prepare_data_for_cache(raw_queryset_or_data: Any) -> Any:
    # BUGGY VERSION:
    # return raw_queryset_or_data # Pickling un-evaluated QuerySet!

    # FIXED VERSION:
    if hasattr(raw_queryset_or_data, "values"):
        return list(raw_queryset_or_data.values())
    return raw_queryset_or_data


# ---------------------------------------------------------------------
# Bug 2: Missing Cache Invalidation on Update (Stale Data Trap)
# Problem: A product's price was updated in the database, but users kept seeing
# the old price for 24 hours because the cache was never invalidated on update.
# Fix: Delete or update cache key upon successful model save.
# ---------------------------------------------------------------------
class ProductService:
    def __init__(self, cache_dict: Dict[str, Any]):
        self.cache = cache_dict

    def update_product_price(self, product_id: int, new_price: float):
        # BUGGY VERSION: Updated DB but forgot cache!
        # db.update(product_id, new_price)

        # FIXED VERSION: Invalidate cache key
        cache_key = f"product:{product_id}"
        if cache_key in self.cache:
            del self.cache[cache_key]


# ---------------------------------------------------------------------
# Bug 3: Indefinite Cache Expiration (Memory Leak)
# Problem: An engineer cached temporary user verification codes without setting
# a `timeout`, filling Redis RAM and triggering out-of-memory eviction.
# Fix: Always mandate a timeout.
# ---------------------------------------------------------------------
def set_secure_cache_token(cache_store: Dict[str, Any], key: str, token: str, timeout_seconds: int):
    # BUGGY VERSION:
    # cache_store[key] = token # Indefinite TTL!

    # FIXED VERSION:
    if timeout_seconds <= 0:
        raise ValueError("Timeout must be a positive number of seconds.")
    cache_store[key] = {"token": token, "ttl": timeout_seconds}


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    class MockQS:
        def values(self): return [{"id": 1, "name": "Item"}]
    clean = prepare_data_for_cache(MockQS())
    assert isinstance(clean, list)

    # Test Bug 2 fix
    mock_c = {"product:42": {"price": 10.0}}
    svc = ProductService(mock_c)
    svc.update_product_price(42, 15.0)
    assert "product:42" not in mock_c  # Invalidated!

    # Test Bug 3 fix
    store = {}
    set_secure_cache_token(store, "otp:123", "987654", timeout_seconds=300)
    assert store["otp:123"]["ttl"] == 300

    print("All Day 58 debugging fixes verified successfully!")
