"""
Day 53 Daily Challenge: Real-Time Database Query Profiler & N+1 Alert Engine

Problem:
Implement an automated Query Profiler that inspects query logs from an API request:
1. Tracks total query count and total database time.
2. Detects N+1 queries: Identifies parameterized queries executing identical SQL structures with different IDs.
3. Flags Slow Queries exceeding a latency threshold.
4. Generates a comprehensive Diagnostic Health Report with actionable remediation suggestions.
"""
import re
from typing import List, Dict, Any

class QueryProfiler:
    def __init__(self, slow_query_threshold: float = 0.05):
        self.slow_query_threshold = slow_query_threshold

    def _normalize_sql(self, sql: str) -> str:
        # Replaces raw numbers and quoted strings with placeholders to group N+1 patterns
        clean = " ".join(sql.strip().split())
        clean = re.sub(r"=\s*\d+", "= ?", clean)
        clean = re.sub(r"=\s*'[^']*'", "= ?", clean)
        clean = re.sub(r"IN\s*\([^\)]*\)", "IN (?)", clean, flags=re.IGNORECASE)
        return clean

    def analyze(self, query_log: List[Dict[str, Any]]) -> Dict[str, Any]:
        total_queries = len(query_log)
        total_time = sum(q.get("time", 0.0) for q in query_log)

        # 1. Detect slow queries
        slow_queries = [q for q in query_log if q.get("time", 0.0) >= self.slow_query_threshold]

        # 2. Detect N+1 patterns
        template_counts: Dict[str, int] = {}
        for q in query_log:
            norm = self._normalize_sql(q.get("sql", ""))
            template_counts[norm] = template_counts.get(norm, 0) + 1

        n_plus_one_alerts = [
            {"pattern": pattern, "count": count, "remedy": "Consider select_related or prefetch_related"}
            for pattern, count in template_counts.items() if count >= 3
        ]

        return {
            "total_queries": total_queries,
            "total_time_seconds": round(total_time, 4),
            "slow_query_count": len(slow_queries),
            "slow_queries": slow_queries,
            "n_plus_one_alerts": n_plus_one_alerts,
            "is_healthy": len(slow_queries) == 0 and len(n_plus_one_alerts) == 0
        }


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    profiler = QueryProfiler(slow_query_threshold=0.1)

    # Simulated query log with N+1 and 1 slow query
    simulated_queries = [
        {"sql": "SELECT * FROM orders WHERE user_id = 1", "time": 0.01},
        {"sql": "SELECT * FROM orders WHERE user_id = 2", "time": 0.01},
        {"sql": "SELECT * FROM orders WHERE user_id = 3", "time": 0.01},  # N+1 pattern!
        {"sql": "SELECT * FROM analytics_large_report", "time": 0.25},     # Slow query!
    ]

    report = profiler.analyze(simulated_queries)

    assert report["total_queries"] == 4
    assert report["total_time_seconds"] == 0.28
    assert report["slow_query_count"] == 1
    assert len(report["n_plus_one_alerts"]) == 1
    assert report["is_healthy"] is False

    # Verify N+1 pattern matched
    assert "WHERE user_id = ?" in report["n_plus_one_alerts"][0]["pattern"]
    assert report["n_plus_one_alerts"][0]["count"] == 3

    print("All QueryProfiler challenge tests passed successfully!")
