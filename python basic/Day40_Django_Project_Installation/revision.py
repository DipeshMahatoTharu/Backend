"""
============================================================
DAY 40 REVISION SESSION (~10–15 MINUTES)
Topic: RESTful URI Conventions, HTTP Methods & Virtual Environments
============================================================

Verified Prerequisites: Days 1–39 (Day 39 REST URI Conventions, Day 38 HTTP Methods, Day 24 Venvs)

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
# 1. Why do RESTful APIs use plural nouns for URIs (e.g. `/api/v1/orders/`) rather than verbs (e.g. `/api/v1/getOrders`)?
#
# 2. How does HTTP method choice (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) express the intended action without embedding verbs in the URL path?
#
# 3. Why is it vital to keep `.venv/` in `.gitignore` rather than committing it to Git?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `is_restful_uri(path: str) -> bool` returning False if the path contains action verbs like 'get', 'create', 'delete', or 'update', and True if it adheres to noun-based REST conventions.

def is_restful_uri(path: str) -> bool:
    """
    Returns False if any path segment contains 'get', 'create', 'delete', or 'update' (case-insensitive),
    True otherwise.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 40 Revision Challenge ---")
    bad = is_restful_uri("/api/v1/users/create")
    good = is_restful_uri("/api/v1/users/123")
    if bad is None or good is None:
        print("[!] Function `is_restful_uri` is not yet implemented.")
        return
    if bad is False and good is True:
        print("[+] Test Passed: RESTful URI pattern detected cleanly.")
    else:
        print(f"[-] Test Failed: bad={bad}, good={good}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Split the path by '/' and check if any forbidden verb is present in lowercased segments.
# Hint 2: Use `verbs = {'get', 'create', 'delete', 'update'}` and `any(v in segment.lower() for v in verbs for segment in path.split('/'))`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(path: str) -> bool:
    verbs = {"get", "create", "delete", "update"}
    segments = [s.lower() for s in path.strip("/").split("/")]
    return not any(any(v in s for v in verbs) for s in segments)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
