"""
============================================================
DAY 50 REVISION SESSION (~10–15 MINUTES)
Topic: Custom User Models & Authorization Architecture
============================================================

Verified Prerequisites: Day 49 (Authorization & Custom User Models)

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
# 1. Why does the official Django documentation recommend creating a custom user model at the start of a project?
#
# 2. What is the difference between authentication ('who you are') and authorization ('what you are permitted to do')?
#
# 3. How do Django permissions and groups enforce access control?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `filter_active_users(records: list[dict]) -> list[dict]` filtering out any user dictionary where `is_deleted` is True.

def filter_active_users(records: list[dict]) -> list[dict]:
    """
    Simulates a soft-delete manager filter: returns records where is_deleted is False or missing.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 50 Revision Challenge ---")
    users = [
        {"id": 1, "name": "Alice", "is_deleted": False},
        {"id": 2, "name": "Bob", "is_deleted": True},
        {"id": 3, "name": "Carol"},
    ]
    res = filter_active_users(users)
    if res is None:
        print("[!] Function `filter_active_users` is not yet implemented.")
        return
    ids = [u["id"] for u in res]
    if ids == [1, 3]:
        print("[+] Test Passed: Soft-deleted users filtered out.")
    else:
        print(f"[-] Test Failed: Got ids={ids}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Filter dictionaries where `r.get('is_deleted', False)` is False.
# Hint 2: Use `[r for r in records if not r.get('is_deleted', False)]`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(records: list[dict]) -> list[dict]:
    return [r for r in records if not r.get("is_deleted", False)]


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
