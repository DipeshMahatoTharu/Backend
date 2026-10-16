"""
============================================================
DAY 72 REVISION SESSION (~10–15 MINUTES)
Topic: Docker Compose Orchestration, GitHub Actions & Pull Requests
============================================================

Verified Prerequisites: Days 1–71 (Day 71 Docker Compose, Day 26 Git Collaboration, Day 59 Pytest)

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
# 1. In Docker Compose, how does container networking allow the `web` container to reach the database using service name `db` instead of an IP address?
#
# 2. What is the purpose of a CI workflow (GitHub Actions) running linters and tests automatically on every Pull Request?
#
# 3. Why should database migrations be run as part of deployment rather than being baked into image builds?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `verify_services_healthy(compose_services: list[dict]) -> tuple[bool, list[str]]` that inspects a list of service status dictionaries and ensures all required services (`web`, `db`, `redis`) have status `'healthy'`.

def verify_services_healthy(compose_services: list[dict]) -> tuple[bool, list[str]]:
    """
    Each dict: {'name': 'web', 'status': 'healthy'}
    Required services: ['web', 'db', 'redis']
    Returns (all_healthy, list_of_unhealthy_or_missing_services)
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 72 Revision Challenge ---")
    good = [
        {"name": "web", "status": "healthy"},
        {"name": "db", "status": "healthy"},
        {"name": "redis", "status": "healthy"}
    ]
    bad = [
        {"name": "web", "status": "healthy"},
        {"name": "db", "status": "starting"},
        {"name": "redis", "status": "unhealthy"}
    ]
    res1 = verify_services_healthy(good)
    if res1 is None:
        print("[!] Function `verify_services_healthy` is not yet implemented.")
        return
    r1, _ = res1
    r2, m2 = verify_services_healthy(bad)
    if r1 is True and r2 is False and "db" in m2 and "redis" in m2:
        print("[+] Test Passed: Docker Compose health check verification confirmed.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, m2={m2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Convert `compose_services` into a dictionary `{s['name']: s['status']}`.
# Hint 2: Check required services `['web', 'db', 'redis']`. If status != 'healthy', append to unhealthy list.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(compose_services: list[dict]) -> tuple[bool, list[str]]:
    status_map = {s["name"]: s.get("status") for s in compose_services}
    required = ["web", "db", "redis"]
    unhealthy = [r for r in required if status_map.get(r) != "healthy"]
    return (len(unhealthy) == 0, unhealthy)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
