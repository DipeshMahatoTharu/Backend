"""
============================================================
DAY 39 REVISION SESSION (~10–15 MINUTES)
Topic: HTTP Idempotency, HTTP Status Codes & Rollback
============================================================

Verified Prerequisites: Days 1–38 (Day 38 HTTP Methods & Status Codes, Day 31/35 Transactions)

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
# 1. What does it mean for an HTTP method to be 'idempotent', and why is `GET` and `PUT` idempotent while `POST` is not?
#
# 2. What are the standard HTTP status codes for: Success (`200`), Resource Created (`201`), Bad Request (`400`), Unauthorized (`401`), Forbidden (`403`), and Not Found (`404`)?
#
# 3. If a transaction raises an exception midway, why must `conn.rollback()` be invoked before releasing or reusing the connection?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `determine_status_code(method: str, resource_found: bool, is_valid_payload: bool) -> int` that maps request parameters to the standard REST status code.

def determine_status_code(method: str, resource_found: bool, is_valid_payload: bool) -> int:
    """
    Rules:
    - If payload is invalid: return 400
    - If method is 'GET' or 'DELETE' and resource not found: return 404
    - If method is 'POST' and valid: return 201
    - If method is 'GET' or 'PUT' and found and valid: return 200
    - Default fallback: 200
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 39 Revision Challenge ---")
    c1 = determine_status_code("POST", True, True)    # 201
    c2 = determine_status_code("GET", False, True)    # 404
    c3 = determine_status_code("POST", True, False)   # 400
    c4 = determine_status_code("GET", True, True)     # 200
    if c1 is None:
        print("[!] Function `determine_status_code` is not yet implemented.")
        return
    if (c1, c2, c3, c4) == (201, 404, 400, 200):
        print("[+] Test Passed: Status codes correctly resolved.")
    else:
        print(f"[-] Test Failed: Got {(c1, c2, c3, c4)}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Handle the failure cases first (invalid payload -> 400, not found on GET/DELETE -> 404).
# Hint 2: Check `if not is_valid_payload: return 400`, then `if not resource_found and method in ('GET', 'DELETE'): return 404`, then `if method == 'POST': return 201`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(method: str, resource_found: bool, is_valid_payload: bool) -> int:
    if not is_valid_payload:
        return 400
    if not resource_found and method.upper() in ("GET", "DELETE"):
        return 404
    if method.upper() == "POST":
        return 201
    return 200


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
