"""
============================================================
DAY 56 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Concurrency & Worker Capacity Calculator

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a capacity estimator function:
`estimate_server_capacity(num_cores: int, worker_model: str, threads_per_worker: int, avg_latency_ms: float) -> dict`

Calculates:
- `worker_count`:
  - If `worker_model == "sync"`: `(2 * num_cores) + 1`
  - If `worker_model == "gthread"`: `num_cores + 1`
- `concurrent_slots`: `worker_count * threads_per_worker` (if sync, threads=1).
- `max_rps`: `concurrent_slots / (avg_latency_ms / 1000)`.
- `recommended_traffic_ceiling_rps`: `max_rps * 0.70` (70% utilization safe operating margin).

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Round `max_rps` and `recommended_traffic_ceiling_rps` to 1 decimal place.

============================================================
MY APPROACH:
============================================================
1. Determine `worker_count` based on `worker_model`.
2. Compute `concurrent_slots`.
3. Calculate max RPS = slots / (latency_seconds).
4. Apply 70% headroom ceiling.
"""
from typing import Dict, Any

def estimate_server_capacity(
    num_cores: int,
    worker_model: str,
    threads_per_worker: int,
    avg_latency_ms: float
) -> Dict[str, Any]:
    if worker_model == "sync":
        workers = (2 * num_cores) + 1
        threads = 1
    elif worker_model == "gthread":
        workers = num_cores + 1
        threads = max(1, threads_per_worker)
    else:
        workers = (2 * num_cores) + 1
        threads = 1

    slots = workers * threads
    latency_sec = avg_latency_ms / 1000.0
    max_rps = slots / latency_sec
    safe_rps = max_rps * 0.70

    return {
        "worker_count": workers,
        "concurrent_slots": slots,
        "max_rps": round(max_rps, 1),
        "recommended_traffic_ceiling_rps": round(safe_rps, 1)
    }


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    # 4-core server, sync workers, 50ms average latency
    res_sync = estimate_server_capacity(num_cores=4, worker_model="sync", threads_per_worker=1, avg_latency_ms=50.0)
    assert res_sync["worker_count"] == 9
    assert res_sync["concurrent_slots"] == 9
    assert res_sync["max_rps"] == 180.0
    assert res_sync["recommended_traffic_ceiling_rps"] == 126.0

    # 4-core server, gthread workers (5 workers * 4 threads = 20 slots)
    res_thread = estimate_server_capacity(num_cores=4, worker_model="gthread", threads_per_worker=4, avg_latency_ms=50.0)
    assert res_thread["worker_count"] == 5
    assert res_thread["concurrent_slots"] == 20
    assert res_thread["max_rps"] == 400.0
    assert res_thread["recommended_traffic_ceiling_rps"] == 280.0

    print("Whiteboard Day 56 challenge passed successfully!")
