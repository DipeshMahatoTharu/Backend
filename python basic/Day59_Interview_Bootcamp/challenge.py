"""
Day 59 Daily Challenge: Token Bucket Rate Limiter Engine

Problem:
Implement a thread-safe, high-precision Token Bucket Algorithm for API rate limiting:
1. `TokenBucket(capacity: int, refill_rate_per_second: float)`:
   - Capacity: Maximum burst size allowed.
   - Refill Rate: Number of tokens added per second.
2. `consume(tokens: int = 1) -> bool`:
   - Calculates tokens accumulated since last consumption based on elapsed time.
   - If sufficient tokens exist: deducts tokens and returns `True`.
   - If insufficient: returns `False` without deducting.
3. Simulate burst traffic and verify that traffic exceeding capacity is rejected.
"""
import time
from typing import Dict, Any

class TokenBucket:
    def __init__(self, capacity: int, refill_rate_per_sec: float):
        self.capacity = float(capacity)
        self.refill_rate = float(refill_rate_per_sec)
        self.tokens = float(capacity)
        self.last_refill = time.time()

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        self.last_refill = now
        # Add tokens accumulated over elapsed time
        self.tokens = min(self.capacity, self.tokens + (elapsed * self.refill_rate))

    def consume(self, tokens: int = 1) -> bool:
        self._refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Capacity 5 tokens, refills 2 tokens per second
    bucket = TokenBucket(capacity=5, refill_rate_per_sec=2.0)

    # 1. Burst of 5 requests succeeds
    for _ in range(5):
        assert bucket.consume(1) is True

    # 2. 6th immediate request must fail (bucket exhausted)
    assert bucket.consume(1) is False

    # 3. Simulate passage of time by artificially moving last_refill back by 1 second
    bucket.last_refill -= 1.0  # 1.0s elapsed -> refilled 2 tokens!
    assert bucket.consume(1) is True
    assert bucket.consume(1) is True
    assert bucket.consume(1) is False  # Exhausted again!

    print("All TokenBucket challenge tests passed successfully!")
