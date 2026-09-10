"""
============================================================
DAY 58 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Least Recently Used (LRU) Cache Implementation

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Design and implement a data structure for a Least Recently Used (LRU) cache:
`class LRUCache(capacity: int)`:
1. `get(key: int) -> int`: Returns value if key exists, else -1. Moves key to most recently used.
2. `put(key: int, value: int)`: Inserts or updates key-value pair.
   If total keys exceed `capacity`, evict the least recently used key!
3. Both operations must run in O(1) average time complexity.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Use Python's `collections.OrderedDict`.

============================================================
MY APPROACH:
============================================================
1. Inherit or wrap `collections.OrderedDict`.
2. On `get(key)`: If present, call `move_to_end(key)` and return value.
3. On `put(key, value)`: If present, update and `move_to_end(key)`.
   If new and `len(self) >= capacity`, call `popitem(last=False)` (evicts oldest).
"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return

        if len(self.cache) >= self.capacity:
            # Evict first item (least recently used)
            self.cache.popitem(last=False)

        self.cache[key] = value


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    lru = LRUCache(capacity=2)

    lru.put(1, 10)
    lru.put(2, 20)
    assert lru.get(1) == 10  # Access key 1 -> key 2 is now LRU!

    lru.put(3, 30)           # Evicts key 2!
    assert lru.get(2) == -1  # Key 2 was evicted
    assert lru.get(3) == 30
    assert lru.get(1) == 10

    print("Whiteboard Day 58 challenge passed successfully!")
