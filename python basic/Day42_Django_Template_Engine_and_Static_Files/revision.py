"""
============================================================
DAY 42 REVISION SESSION (~10–15 MINUTES)
Topic: URL Converters, FBVs vs CBVs & SQL Aggregations
============================================================

Verified Prerequisites: Days 1–41 (Day 41 URL Routing & Views, Day 29 SQL Aggregations)

------------------------------------------------------------
[!] THE 15-MINUTE ATTEMPT RULE
------------------------------------------------------------
1. Start your 15-minute timer before looking at any hints or external resources.
2. Read the recall questions and coding challenge below.
3. Attempt to solve the challenge using your own reasoning and verified notes.
4. If stuck after ~10 minutes, scroll to the HINTS section.
5. If still stuck after ~15 minutes, pause and ask ChatGPT / AI mentor for a targeted clue.
6. After receiving help, type out and solve the problem independently.
7. Record your honest outcome in `revision_tracker.md`!
"""

# ============================================================
# PART 1: RAPID RECALL (2–3 MINUTES)
# Answer these questions in your head or in comments:
# ============================================================
# 1. In Django `path('posts/<int:post_id>/', ...)`, what does the `<int:...>` path converter do?
#
# 2. When is a Function-Based View (FBV) preferred over a Class-Based View (CBV) for beginners?
#
# 3. In SQL, what is the role of `GROUP BY` when computing summary statistics like `AVG(price)` per category?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `extract_id_from_path(path: str) -> int | None` that simulates Django's `<int:pk>` path converter for URLs formatted like `/api/v1/items/<id>/`.

import re

def extract_id_from_path(path: str) -> int | None:
    """
    Extracts integer ID from path segment: '/items/<id>/'. Returns int or None.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 42 Revision Challenge ---")
    i1 = extract_id_from_path("/api/v1/items/456/")
    i2 = extract_id_from_path("/api/v1/items/invalid/")
    if i1 is None and i2 is None:
        print("[!] Function `extract_id_from_path` is not yet implemented.")
        return
    if i1 == 456 and i2 is None:
        print("[+] Test Passed: Path integer converter simulated correctly.")
    else:
        print(f"[-] Test Failed: i1={i1}, i2={i2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Use `re.search(r'/items/(\d+)/', path)` or parse path segments.
# Hint 2: Match `re.search(r'/items/(\d+)', path)`: if match, return `int(match.group(1))` else None.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
import re

def _reference_solution(path: str) -> int | None:
    m = re.search(r'/items/(\d+)/?', path)
    return int(m.group(1)) if m else None


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
