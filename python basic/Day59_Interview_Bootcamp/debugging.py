"""
Day 59: Technical Interview Bootcamp — Debugging
Diagnose and fix 3 classic senior technical interview bugs.
"""
import time
from typing import List, Dict, Any, Tuple

# ---------------------------------------------------------------------
# Bug 1: Deadlock Caused by Inconsistent Resource Locking Order
# Problem: Thread 1 locks Account A then Account B. Thread 2 locks Account B
# then Account A. When both run concurrently, a deadlock freezes the server!
# Fix: Enforce a global lock ordering (always acquire locks in order of Account ID).
# ---------------------------------------------------------------------
def acquire_account_locks_order(account_id_1: int, account_id_2: int) -> Tuple[int, int]:
    # BUGGY VERSION: Acquired in order passed by caller
    # return account_id_1, account_id_2

    # FIXED VERSION: Deterministic ordering prevents circular deadlocks
    return min(account_id_1, account_id_2), max(account_id_1, account_id_2)


# ---------------------------------------------------------------------
# Bug 2: Python Memory Leak in Infinite Generator Loop
# Problem: A background consumer did `cache.append(next(gen))` without bounding,
# causing an Out-Of-Memory crash.
# Fix: Use bounded deque or sliding window.
# ---------------------------------------------------------------------
from collections import deque

class BoundedEventBuffer:
    def __init__(self, max_size: int = 100):
        self.buffer = deque(maxlen=max_size)

    def add(self, item: Any):
        self.buffer.append(item)


# ---------------------------------------------------------------------
# Bug 3: Late Binding in Python Closures
# Problem: `funcs = [lambda: i for i in range(3)]` results in all functions
# returning 2 because `i` is looked up at execution time, not definition time!
# Fix: Bind default argument: `lambda i=i: i`.
# ---------------------------------------------------------------------
def create_multiplier_closures() -> List[Any]:
    # BUGGY VERSION:
    # return [lambda: i for i in range(3)]

    # FIXED VERSION: Default argument binds value at definition time
    return [lambda i=i: i for i in range(3)]


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    first, second = acquire_account_locks_order(42, 10)
    assert first == 10 and second == 42  # Sorted!

    # Test Bug 2 fix
    buf = BoundedEventBuffer(max_size=3)
    for x in range(10): buf.add(x)
    assert len(buf.buffer) == 3
    assert list(buf.buffer) == [7, 8, 9]

    # Test Bug 3 fix
    fns = create_multiplier_closures()
    assert [fn() for fn in fns] == [0, 1, 2]

    print("All Day 59 debugging fixes verified successfully!")
