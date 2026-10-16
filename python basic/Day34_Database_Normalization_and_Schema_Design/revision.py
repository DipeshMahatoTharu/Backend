"""
============================================================
DAY 34 REVISION SESSION (~10–15 MINUTES)
Topic: B-Tree Indexes, Composite Index Rules & Dict Operations
============================================================

Verified Prerequisites: Days 1–33 (Day 33 B-Tree Indexing, Day 9 Dictionaries)

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
# 1. Why does a B-Tree index allow O(log n) lookups instead of O(n) table scans?
#
# 2. In a composite index on `(status, created_at)`, why can a query filter on `status` alone use the index, but a query on `created_at` alone cannot?
#
# 3. What is the difference between `dict.get('key')` and `dict['key']` when the key is missing?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `is_using_index(plan_steps: list[str]) -> bool` which inspects a list of EXPLAIN plan step strings and returns True if any step uses an index and False if it only does sequential scans.

def is_using_index(plan_steps: list[str]) -> bool:
    """
    Returns True if any step in plan_steps contains 'INDEX' (case-insensitive),
    False otherwise.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 34 Revision Challenge ---")
    plan1 = ["Seq Scan on users (cost=0.00..35.50 rows=2550 width=36)"]
    plan2 = ["Bitmap Index Scan on idx_users_email (cost=0.00..4.30 rows=10 width=0)"]
    
    r1 = is_using_index(plan1)
    r2 = is_using_index(plan2)
    if r1 is None or r2 is None:
        print("[!] Function `is_using_index` is not yet implemented.")
        return
    if r1 is False and r2 is True:
        print("[+] Test Passed: Correctly identified Sequential Scan vs Index Scan.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Iterate through each step string and check for the substring 'INDEX'.
# Hint 2: Use `any('INDEX' in step.upper() for step in plan_steps)`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(plan_steps: list[str]) -> bool:
    return any("INDEX" in step.upper() for step in plan_steps)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
