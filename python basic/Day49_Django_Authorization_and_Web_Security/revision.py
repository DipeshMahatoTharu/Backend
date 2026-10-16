"""
============================================================
DAY 49 REVISION SESSION (~10–15 MINUTES)
Topic: Session Security, Cookies & @login_required
============================================================

Verified Prerequisites: Days 1–48 (Day 48 Authentication & Sessions, Day 15 OOP Inheritance)

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
# 1. How does Django session authentication use a session cookie (`sessionid`) to identify the user on subsequent requests?
#
# 2. Why should session cookies be configured with `HttpOnly` and `Secure` flags in production?
#
# 3. What does the `@login_required` decorator do when an unauthenticated user visits a protected view?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `validate_session(session_data: dict) -> bool` returning True if `user_id` exists and `is_active` is True.

def validate_session(session_data: dict) -> bool:
    """
    Returns True if session_data contains 'user_id' and 'is_active' is True.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 49 Revision Challenge ---")
    s1 = validate_session({"user_id": 1, "is_active": True})
    s2 = validate_session({"user_id": 2, "is_active": False})
    s3 = validate_session({"is_active": True})
    if s1 is None:
        print("[!] Function `validate_session` is not yet implemented.")
        return
    if s1 is True and s2 is False and s3 is False:
        print("[+] Test Passed: Session validity verified.")
    else:
        print(f"[-] Test Failed: s1={s1}, s2={s2}, s3={s3}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Check that `user_id` is present and `is_active` is truthy.
# Hint 2: Use `return bool(session_data.get('user_id') and session_data.get('is_active'))`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(session_data: dict) -> bool:
    return bool(session_data.get("user_id") and session_data.get("is_active"))


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
