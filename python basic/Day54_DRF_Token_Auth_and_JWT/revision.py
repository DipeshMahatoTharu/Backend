"""
============================================================
DAY 54 REVISION SESSION (~10–15 MINUTES)
Topic: ModelViewSet Routing, Session Auth vs Token Auth
============================================================

Verified Prerequisites: Days 1–53 (Day 53 ViewSets & Routers, Day 48 Session Auth, Day 37 Auth Headers)

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
# 1. What standard actions (`list`, `create`, `retrieve`, `update`, `partial_update`, `destroy`) does DRF's `ModelViewSet` provide automatically?
#
# 2. What is the difference between session authentication (cookie-based, stateful on server) and token authentication (header-based, bearer token)?
#
# 3. How does DRF's `DefaultRouter` generate RESTful URL patterns for a registered ViewSet?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `parse_auth_header(auth_header: str) -> tuple[str, str] | None` which parses an `Authorization` header value formatted as `Bearer <token>` or `Token <key>` into `(scheme, credential)`.

def parse_auth_header(auth_header: str) -> tuple[str, str] | None:
    """
    Parses 'Bearer eyJhbGciOi...' into ('Bearer', 'eyJhbGciOi...')
    Returns None if format is invalid.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 54 Revision Challenge ---")
    p1 = parse_auth_header("Bearer mysecrettoken123")
    p2 = parse_auth_header("Token keyabc")
    p3 = parse_auth_header("InvalidHeader")
    if p1 is None and p2 is None:
        print("[!] Function `parse_auth_header` is not yet implemented.")
        return
    if p1 == ("Bearer", "mysecrettoken123") and p2 == ("Token", "keyabc") and p3 is None:
        print("[+] Test Passed: Authorization header parser verified.")
    else:
        print(f"[-] Test Failed: p1={p1}, p2={p2}, p3={p3}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Split the header string by whitespace and check that there are exactly 2 parts.
# Hint 2: Use `parts = auth_header.strip().split(); return (parts[0], parts[1]) if len(parts) == 2 else None`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(auth_header: str) -> tuple[str, str] | None:
    parts = auth_header.strip().split()
    if len(parts) == 2:
        return (parts[0], parts[1])
    return None


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
