"""
============================================================
DAY 32 REVISION SESSION (~10–15 MINUTES)
Topic: SQL Subqueries, Table Joins & Defensive Exceptions
============================================================

Verified Prerequisites: Days 1–31
(Covers: Day 31 Transactions & Subqueries, Day 30 SQL Joins, Day 23 Defensive Exceptions)

------------------------------------------------------------
⏱️ THE 15-MINUTE ATTEMPT RULE
------------------------------------------------------------
1. Start your 15-minute timer before looking at any hints or external resources.
2. Read the recall questions and coding challenge below.
3. Attempt to solve the challenge using your own reasoning and verified notes.
4. If stuck after ~10 minutes, scroll to the HINTS section.
5. If still stuck after ~15 minutes, pause and ask ChatGPT / AI mentor for a targeted clue.
6. After receiving help, type out and solve the problem independently.
7. Record your result in `revision_tracker.md`!
"""

import sqlite3

# ============================================================
# PART 1: RAPID RECALL (2–3 MINUTES)
# Answer these questions in your head or in comments:
# ============================================================
# 1. What is the fundamental difference between an INNER JOIN and a LEFT JOIN?
#    (Hint: What happens to rows on the left side that have no matching foreign key on the right?)
#
# 2. In SQL transactions, what is the difference between COMMIT and ROLLBACK?
#    If Python raises an unhandled exception inside a try-block, which one must execute?
#
# 3. Why does a scalar subquery (e.g. `WHERE price = (SELECT ...)`) crash if the inner query
#    returns more than 1 row, and which SQL operator (`IN`, `ANY`, `ALL`) prevents this crash?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# You are given an in-memory SQLite database representing an e-commerce order ledger.
# An account must transfer loyalty reward points between two users.
#
# YOUR TASK:
# Complete the function `safe_points_transfer(conn, from_user, to_user, points)`:
# 1. Verify that `from_user` has enough points using a subquery or check.
# 2. Deduct `points` from `from_user` and add `points` to `to_user`.
# 3. If any step fails or `from_user` has insufficient points, ROLLBACK and return (False, "Reason").
# 4. If successful, COMMIT and return (True, "Transfer successful").
#
# RESTRICTIONS:
# - Do not use string concatenation for SQL queries (use parameterized tuples `?`).
# - Wrap database operations in a try/except/rollback block.

def safe_points_transfer(conn: sqlite3.Connection, from_user: str, to_user: str, points: int) -> tuple[bool, str]:
    """
    Executes an atomic points transfer between two users.
    Returns: (success: bool, message: str)
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (username TEXT PRIMARY KEY, points INTEGER CHECK(points >= 0));")
    cur.execute("INSERT INTO users VALUES ('alice', 100), ('bob', 50);")
    conn.commit()

    print("--- Running Day 32 Revision Challenge ---")
    
    res = safe_points_transfer(conn, 'alice', 'bob', 40)
    if res is None:
        print("[!] Function `safe_points_transfer` is not yet implemented. Complete the exercise above and re-run!")
        conn.close()
        return

    success, msg = res
    cur.execute("SELECT points FROM users WHERE username = 'alice';")
    alice_pts = cur.fetchone()[0]
    cur.execute("SELECT points FROM users WHERE username = 'bob';")
    bob_pts = cur.fetchone()[0]

    if success and alice_pts == 60 and bob_pts == 90:
        print("[+] Test 1 Passed: Valid transfer committed correctly (Alice: 60, Bob: 90).")
    else:
        print(f"[-] Test 1 Failed: Returned ({success}, '{msg}'). Alice: {alice_pts}, Bob: {bob_pts}")

    # Test 2: Overdraft transfer (Should fail and rollback)
    fail_success, fail_msg = safe_points_transfer(conn, 'bob', 'alice', 500)
    cur.execute("SELECT points FROM users WHERE username = 'bob';")
    bob_pts_after = cur.fetchone()[0]

    if not fail_success and bob_pts_after == 90:
        print("[+] Test 2 Passed: Overdraft safely rejected and rolled back.")
    else:
        print(f"[-] Test 2 Failed: Balance was altered on invalid transfer! Bob: {bob_pts_after}")

    conn.close()

if __name__ == "__main__":
    run_test()


# ============================================================
# 💡 HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Begin by fetching the current points of `from_user`:
#         cur.execute("SELECT points FROM users WHERE username = ?;", (from_user,))
# Hint 2: If the user doesn't exist or points < required points, return early with (False, "Insufficient points").
# Hint 3: Remember to wrap the two UPDATE statements in `try: ... conn.commit()` and on error `except Exception: conn.rollback()`.


# ============================================================
# 🔒 SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(conn: sqlite3.Connection, from_user: str, to_user: str, points: int) -> tuple[bool, str]:
    cur = conn.cursor()
    try:
        cur.execute("SELECT points FROM users WHERE username = ?;", (from_user,))
        row = cur.fetchone()
        if not row or row[0] < points:
            return False, "Insufficient points"

        cur.execute("SELECT 1 FROM users WHERE username = ?;", (to_user,))
        if not cur.fetchone():
            return False, "Recipient not found"

        cur.execute("UPDATE users SET points = points - ? WHERE username = ?;", (points, from_user))
        cur.execute("UPDATE users SET points = points + ? WHERE username = ?;", (points, to_user))
        conn.commit()
        return True, "Transfer successful"
    except Exception as e:
        conn.rollback()
        return False, f"Transaction error: {e}"


# ============================================================
# 📋 SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1, 2, or 3.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# ============================================================
