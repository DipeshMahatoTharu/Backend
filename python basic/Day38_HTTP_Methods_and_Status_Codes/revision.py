"""
============================================================
DAY 38 REVISION SESSION (~10–15 MINUTES)
Topic: HTTP Request-Response Anatomy, Headers & Git Conflicts
============================================================

Verified Prerequisites: Days 1–37 (Day 37 HTTP Anatomy, Day 33 Indexing, Day 26 Git Collaboration)

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
# 1. What are the three main components of an HTTP Request message (start line, headers, body)?
#
# 2. Why are HTTP header names considered case-insensitive according to RFC specifications (e.g., `Content-Type` vs `content-type`)?
#
# 3. In Git, what markers (`<<<<<<<`, `=======`, `>>>>>>>`) appear in a file during a merge conflict?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `get_header_value(headers: dict, target_header: str) -> str | None` which retrieves the value of a header regardless of whether it was stored in lowercase, uppercase, or mixed case.

def get_header_value(headers: dict, target_header: str) -> str | None:
    """
    Retrieves the value of target_header from headers dictionary in a case-insensitive way.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 38 Revision Challenge ---")
    headers = {"Content-Type": "application/json", "Authorization": "Bearer token123"}
    v1 = get_header_value(headers, "content-type")
    v2 = get_header_value(headers, "AUTHORIZATION")
    v3 = get_header_value(headers, "Accept")
    if v1 is None and v2 is None:
        print("[!] Function `get_header_value` is not yet implemented.")
        return
    if v1 == "application/json" and v2 == "Bearer token123" and v3 is None:
        print("[+] Test Passed: Case-insensitive header lookup succeeded.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}, v3={v3}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Compare lowercased keys with `target_header.lower()`.
# Hint 2: Iterate through `headers.items()`: `for k, v in headers.items(): if k.lower() == target_header.lower(): return v`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(headers: dict, target_header: str) -> str | None:
    target = target_header.lower()
    for k, v in headers.items():
        if k.lower() == target:
            return v
    return None


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
