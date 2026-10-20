"""
============================================================
DAY 75 REVISION SESSION (~10–15 MINUTES)
Topic: Technical Interview Bootcamp & Capstone Defense
============================================================

Verified Prerequisites: Day 74 (Technical Interview Bootcamp)

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
# 1. How do you explain the architectural flow of a request from client to Nginx to Gunicorn to Django to PostgreSQL?
#
# 2. What are the three most critical sections in a GitHub project README for hiring engineers?
#
# 3. How do automated tests and CI/CD prove technical competence during junior developer interviews?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Capstone checklist verifier: Write `verify_portfolio_readiness(checklist: dict[str, bool]) -> tuple[bool, list[str]]` verifying that all 6 required portfolio items (`['clean_git_history', 'automated_tests_passing', 'docker_compose_working', 'readme_with_architecture', 'env_example_provided', 'api_docs_available']`) are marked True.

def verify_portfolio_readiness(checklist: dict[str, bool]) -> tuple[bool, list[str]]:
    """
    Verifies that all 6 required checklist items are True.
    Returns (is_ready: bool, missing_or_incomplete_items: list[str])
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 75 Revision Challenge ---")
    complete_portfolio = {
        "clean_git_history": True,
        "automated_tests_passing": True,
        "docker_compose_working": True,
        "readme_with_architecture": True,
        "env_example_provided": True,
        "api_docs_available": True
    }
    partial_portfolio = dict(complete_portfolio)
    partial_portfolio["automated_tests_passing"] = False
    res1 = verify_portfolio_readiness(complete_portfolio)
    if res1 is None:
        print("[!] Function `verify_portfolio_readiness` is not yet implemented.")
        return
    r1, _ = res1
    r2, m2 = verify_portfolio_readiness(partial_portfolio)
    if r1 is True and r2 is False and "automated_tests_passing" in m2:
        print("[+] Test Passed: Capstone portfolio readiness verifier confirmed.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, m2={m2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Define the list of 6 required keys and check each one against `checklist.get(k)`.
# Hint 2: Use `missing = [k for k in required if not checklist.get(k, False)]; return (len(missing) == 0, missing)`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(checklist: dict[str, bool]) -> tuple[bool, list[str]]:
    required = [
        "clean_git_history",
        "automated_tests_passing",
        "docker_compose_working",
        "readme_with_architecture",
        "env_example_provided",
        "api_docs_available"
    ]
    missing = [k for k in required if not checklist.get(k, False)]
    return (len(missing) == 0, missing)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
