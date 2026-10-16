"""
============================================================
DAY 33 REVISION SESSION (~10–15 MINUTES)
Topic: Parameterized Queries, SQL Aggregations & Context Managers
============================================================

Verified Prerequisites: Days 1–32 (Day 32 Drivers, Day 29 Aggregations, Day 24 Context Managers)

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
# 1. Why is passing `%s` or `?` with a tuple to cursor.execute() safe against SQL injection, while Python f-strings are not?
#
# 2. What is the difference between WHERE and HAVING in SQL aggregation queries?
#
# 3. What does Python's `with` statement guarantee when handling database connections or transactions?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Fix the SQL injection vulnerability in `search_users(conn, email_prefix)`. Replace string concatenation with parameterized execution.

def search_users(conn, email_prefix: str) -> list:
    """
    VULNERABLE CODE TO FIX:
    cur = conn.cursor()
    cur.execute("SELECT id, email FROM users WHERE email LIKE '" + email_prefix + "%';")
    return cur.fetchall()
    """
    # WRITE YOUR FIXED CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    import sqlite3
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT);")
    cur.execute("INSERT INTO users VALUES (1, 'dipesh@example.com'), (2, 'dev@example.com');")
    conn.commit()

    print("--- Running Day 33 Revision Challenge ---")
    res = search_users(conn, "dipesh")
    if res is None:
        print("[!] Function `search_users` is not yet implemented. Complete the exercise above and re-run!")
        conn.close()
        return

    if len(res) == 1 and res[0][1] == 'dipesh@example.com':
        print("[+] Test Passed: Parameterized search returned expected record.")
    else:
        print(f"[-] Test Failed: Unexpected return: {res}")
    conn.close()

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: The database driver escapes characters when you pass a query template with a placeholder alongside a tuple of arguments.
# Hint 2: Use `LIKE ?` in SQLite (or `%s` in PostgreSQL) and pass `(f'{email_prefix}%',)` as the parameter tuple.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(conn, email_prefix: str) -> list:
    cur = conn.cursor()
    cur.execute("SELECT id, email FROM users WHERE email LIKE ?;", (f"{email_prefix}%",))
    return cur.fetchall()


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
