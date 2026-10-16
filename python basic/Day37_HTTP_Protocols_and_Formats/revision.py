"""
============================================================
DAY 37 REVISION SESSION (~10–15 MINUTES)
Topic: JSONB vs Relational Schemas, SQL Joins & List Comprehensions
============================================================

Verified Prerequisites: Days 1–36 (Day 36 PostgreSQL Data Types, Day 30 Joins, Day 8 List Comprehensions)

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
# 1. When is storing data in a JSON/JSONB column appropriate versus normalizing into separate relational tables?
#
# 2. What is the difference between a LEFT JOIN and an INNER JOIN when querying orders with optional discount codes?
#
# 3. How does a Python list comprehension offer cleaner, more readable filtering compared to an explicit for-loop?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Given a list of user dictionaries representing parsed JSON records, write `get_active_admin_emails(users_data: list[dict]) -> list[str]` using a list comprehension.

def get_active_admin_emails(users_data: list[dict]) -> list[str]:
    """
    Returns a list of emails for users who have role == 'ADMIN' and is_active is True.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 37 Revision Challenge ---")
    users = [
        {"email": "alice@admin.com", "role": "ADMIN", "is_active": True},
        {"email": "bob@dev.com", "role": "STAFF", "is_active": True},
        {"email": "carol@admin.com", "role": "ADMIN", "is_active": False},
        {"email": "dave@admin.com", "role": "ADMIN", "is_active": True},
    ]
    res = get_active_admin_emails(users)
    if res is None:
        print("[!] Function `get_active_admin_emails` is not yet implemented.")
        return
    if res == ["alice@admin.com", "dave@admin.com"]:
        print("[+] Test Passed: Active admin emails filtered correctly.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Filter each dictionary `u` where `u.get('role') == 'ADMIN'` and `u.get('is_active') is True`.
# Hint 2: Use `[u['email'] for u in users_data if u.get('role') == 'ADMIN' and u.get('is_active')]`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(users_data: list[dict]) -> list[str]:
    return [u["email"] for u in users_data if u.get("role") == "ADMIN" and u.get("is_active")]


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
