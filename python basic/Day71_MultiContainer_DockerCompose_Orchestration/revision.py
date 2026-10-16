"""
============================================================
DAY 71 REVISION SESSION (~10–15 MINUTES)
Topic: Docker Images, Non-Root Users & DB URL Configuration
============================================================

Verified Prerequisites: Days 1–70 (Day 70 Docker Intro, Day 32 PostgreSQL Configurations, Day 40 Settings)

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
# 1. What is a multi-stage Docker build and why does it keep production image sizes minimal?
#
# 2. Why should production Docker containers run under a dedicated non-root user (`USER appuser`) rather than root?
#
# 3. How does `DATABASE_URL` consolidate user, password, host, port, and database name into a single standardized connection string?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `parse_database_url(url: str) -> dict[str, str]` parsing `postgres://user:password@hostname:5432/dbname` into `{'user': ..., 'password': ..., 'host': ..., 'port': ..., 'name': ...}` using `urllib.parse`.

import urllib.parse

def parse_database_url(url: str) -> dict[str, str]:
    """
    Parses a PostgreSQL URL into component dictionary.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 71 Revision Challenge ---")
    url = "postgres://dipesh:secret123@db.internal:5432/hotel_db"
    res = parse_database_url(url)
    if res is None:
        print("[!] Function `parse_database_url` is not yet implemented.")
        return
    if (res.get("user") == "dipesh" and res.get("password") == "secret123" and
        res.get("host") == "db.internal" and res.get("port") == "5432" and res.get("name") == "hotel_db"):
        print("[+] Test Passed: Database URL parser confirmed.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Use `urllib.parse.urlparse(url)` to extract `.username`, `.password`, `.hostname`, `.port`, and `.path`.
# Hint 2: Use `p = urllib.parse.urlparse(url); return {'user': p.username, 'password': p.password, 'host': p.hostname, 'port': str(p.port), 'name': p.path.lstrip('/')}`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
import urllib.parse

def _reference_solution(url: str) -> dict[str, str]:
    p = urllib.parse.urlparse(url)
    return {
        "user": p.username or "",
        "password": p.password or "",
        "host": p.hostname or "",
        "port": str(p.port or 5432),
        "name": (p.path or "").lstrip("/")
    }


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
