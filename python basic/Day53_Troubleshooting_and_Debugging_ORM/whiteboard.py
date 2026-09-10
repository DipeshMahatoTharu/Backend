"""
============================================================
DAY 53 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: SQL Query Log Analyzer & N+1 Pattern Detector

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement `analyze_sql_log(query_strings: list) -> dict` that:
1. Normalizes SQL queries by replacing numeric literals with `?`.
2. Groups queries by normalized pattern.
3. Returns a summary dictionary:
   - `total_queries`: total number of queries executed.
   - `unique_patterns`: number of distinct normalized patterns.
   - `n_plus_one_patterns`: list of patterns that executed 3 or more times.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Match patterns case-insensitively.
- Collapse consecutive spaces.

============================================================
MY APPROACH:
============================================================
1. Normalize query using regex: replace `\d+` with `?` and collapse spaces.
2. Track count per normalized pattern.
3. Identify patterns with count >= 3.
"""
import re
from typing import List, Dict, Any

def analyze_sql_log(query_strings: List[str]) -> Dict[str, Any]:
    counts: Dict[str, int] = {}

    for q in query_strings:
        # Collapse whitespace
        norm = " ".join(q.strip().split())
        # Replace integer literals with ?
        norm = re.sub('=\s*\d+', '= ?', norm)
        counts[norm] = counts.get(norm, 0) + 1

    n_plus_one = [pat for pat, count in counts.items() if count >= 3]

    return {
        "total_queries": len(query_strings),
        "unique_patterns": len(counts),
        "n_plus_one_patterns": n_plus_one
    }


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    queries = [
        "SELECT * FROM users WHERE id = 10",
        "SELECT * FROM users WHERE id = 11",
        "SELECT * FROM users WHERE id = 12",
        "SELECT * FROM profiles WHERE user_id = 10",
        "SELECT * FROM profiles WHERE user_id = 11"
    ]

    summary = analyze_sql_log(queries)
    assert summary["total_queries"] == 5
    assert summary["unique_patterns"] == 2
    assert len(summary["n_plus_one_patterns"]) == 1
    assert summary["n_plus_one_patterns"][0] == "SELECT * FROM users WHERE id = ?"

    print("Whiteboard Day 53 challenge passed successfully!")
