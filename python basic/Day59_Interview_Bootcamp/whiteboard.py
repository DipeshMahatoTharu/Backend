"""
============================================================
DAY 59 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: High-Throughput Sliding Window Log Rate Limiter

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a sliding window log rate limiter:
`class SlidingWindowRateLimiter(max_requests: int, window_seconds: float)`
1. `is_allowed(client_id: str) -> bool`:
   - Checks timestamps for `client_id`.
   - Purges timestamps older than `now - window_seconds`.
   - If remaining count < `max_requests`: records `now` and returns `True`.
   - If count >= `max_requests`: returns `False`.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Smooth rate limiting (no boundary burst resets like fixed window).
- O(1) timestamp pruning with `collections.deque`.

============================================================
MY APPROACH:
============================================================
1. Store timestamps in a dictionary of deques: `clients[client_id] = deque()`.
2. On call, popleft all timestamps <= `now - window_seconds`.
3. Check `len(deque) < max_requests`.
"""
import time
from collections import deque, defaultdict
from typing import Dict, Optional

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.client_windows: Dict[str, deque] = defaultdict(deque)

    def is_allowed(self, client_id: str, current_time: Optional[float] = None) -> bool:
        now = current_time if current_time is not None else time.time()
        window = self.client_windows[client_id]
        cutoff = now - self.window_seconds

        # Evict timestamps outside sliding window
        while window and window[0] <= cutoff:
            window.popleft()

        if len(window) < self.max_requests:
            window.append(now)
            return True

        return False


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    limiter = SlidingWindowRateLimiter(max_requests=2, window_seconds=1.0)

    # Client A: 2 requests at t=0.0 -> allowed
    assert limiter.is_allowed("client_a", current_time=100.0) is True
    assert limiter.is_allowed("client_a", current_time=100.1) is True

    # 3rd request at t=100.2 -> blocked
    assert limiter.is_allowed("client_a", current_time=100.2) is False

    # Independent client B at t=100.2 -> allowed
    assert limiter.is_allowed("client_b", current_time=100.2) is True

    # After window passes at t=101.05 (1st request expired) -> allowed!
    assert limiter.is_allowed("client_a", current_time=101.05) is True

    print("Whiteboard Day 59 challenge passed successfully!")
