"""
test_update_revision_tracker.py
--------------------------------
Comprehensive automated test suite for update_revision_tracker.py.
Tests empty log, partial progress, full completion, weak topic detection,
and non-destructive updates.
"""

import os
import re
import tempfile
from update_revision_tracker import update_tracker_file, parse_tracker, calculate_metrics

def run_tests():
    print("--- Starting update_revision_tracker Tests ---")
    
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".md", encoding="utf-8") as tf:
        with open("revision_tracker.md", "r", encoding="utf-8") as f:
            tf.write(f.read())
        temp_path = tf.name

    try:
        # TEST 1: Initial Empty Tracker
        print("[*] Test 1: Testing initial empty tracker state...")
        m1 = update_tracker_file(temp_path)
        assert m1["total_planned"] == 44, f"Expected 44 planned, got {m1['total_planned']}"
        assert m1["completed"] == 0, f"Expected 0 completed, got {m1['completed']}"
        assert m1["not_attempted"] == 44, f"Expected 44 not attempted, got {m1['not_attempted']}"
        assert m1["completion_pct"] == 0.0
        assert m1["reconciled"] is True
        print("[+] Test 1 Passed: Empty tracker accurately reports 0/44 (0.0%).")

        # TEST 2: Partial Progress & Weak Topic Spaced Review Detection
        print("[*] Test 2: Testing partial progress and weak area detection...")
        with open(temp_path, "r", encoding="utf-8") as f:
            c = f.read()

        # Simulate Day 32 INDEPENDENT, Day 33 HINT NEEDED, Day 34 REFRESHER NEEDED
        lines = c.split("\n")
        new_lines = []
        for l in lines:
            if "| **Day 32** |" in l:
                new_lines.append("| **Day 32** | SQL Subqueries & ACID (Day 31), SQL Joins (Day 30), Python `try/except` (Day 23) | 2026-10-17 | `INDEPENDENT` | — | Solved in 8 mins without hints |")
            elif "| **Day 33** |" in l:
                new_lines.append("| **Day 33** | Parameterized Queries (Day 32), SQL Aggregations & `HAVING` (Day 29), Context Managers (Day 24) | 2026-10-18 | `HINT NEEDED` | Day 35 | Needed Hint 1 on parameterized syntax |")
            elif "| **Day 34** |" in l:
                new_lines.append("| **Day 34** | B-Tree Indexes & `EXPLAIN` (Day 33), Composite Index Rules (Day 33), Dict Operations (Day 9) | 2026-10-19 | `REFRESHER NEEDED` | Day 36 | Needed full mentor explanation on composite indexes |")
            else:
                new_lines.append(l)

        with open(temp_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))

        m2 = update_tracker_file(temp_path)
        assert m2["completed"] == 3, f"Expected 3 completed, got {m2['completed']}"
        assert m2["independent"] == 1
        assert m2["hint_needed"] == 1
        assert m2["refresher_needed"] == 1
        assert m2["not_attempted"] == 41
        expected_pct = round(3 / 44 * 100.0, 1)
        assert round(m2["completion_pct"], 1) == expected_pct
        assert m2["reconciled"] is True
        assert len(m2["weak_topics"]) == 2, f"Expected 2 weak topics, got {len(m2['weak_topics'])}"
        assert m2["weak_topics"][0]["day"] == 33
        assert m2["weak_topics"][1]["day"] == 34
        print(f"[+] Test 2 Passed: 3 sessions completed ({expected_pct}%), 2 weak topics flagged.")

        # TEST 3: Non-Destructive Content Verification
        print("[*] Test 3: Checking non-destructive preservation of custom notes...")
        with open(temp_path, "r", encoding="utf-8") as f:
            content_after = f.read()

        assert "Solved in 8 mins without hints" in content_after
        assert "Needed Hint 1 on parameterized syntax" in content_after
        assert "Needed full mentor explanation on composite indexes" in content_after
        assert "Spaced Review Queue (Weak Topics)" in content_after
        assert "**Day 33**" in content_after
        assert "**Day 34**" in content_after
        print("[+] Test 3 Passed: User notes and custom explanations strictly preserved.")

        # TEST 4: Full 100% Completion Simulation
        print("[*] Test 4: Testing 100% completion scenario...")
        all_completed = re.sub(r"`NOT ATTEMPTED`", "`INDEPENDENT`", content_after)
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(all_completed)

        m4 = update_tracker_file(temp_path)
        assert m4["completed"] == 44
        assert m4["not_attempted"] == 0
        assert m4["completion_pct"] == 100.0
        assert m4["reconciled"] is True
        print("[+] Test 4 Passed: 100% completion calculated accurately.")

        print("\n============================================================")
        print("[+] ALL 4 TEST SUITES PASSED FLAWLESSLY!")
        print("============================================================")

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    run_tests()
