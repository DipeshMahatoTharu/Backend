"""
============================================================
DAY 60 REVISION SESSION (~10–15 MINUTES)
Topic: Automated Unit Testing & Django Test Client
============================================================

Verified Prerequisites: Day 59 (Automated API Unit Testing)

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
# 1. Why does Django's `TestCase` wrap each test in a database transaction and roll it back after execution?
#
# 2. What is the difference between unit testing an isolated service function versus integration testing an API endpoint?
#
# 3. Why should automated tests assert both HTTP status codes AND specific JSON response values?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `validate_registration_payload(payload: dict) -> tuple[bool, str]` testing email format (`@` present) and password strength (min 8 chars, at least 1 digit).

def validate_registration_payload(payload: dict) -> tuple[bool, str]:
    """
    Validates:
    - email has '@'
    - password >= 8 characters and contains at least 1 digit
    Returns (True, "Valid") or (False, "Error message")
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 60 Revision Challenge ---")
    res1 = validate_registration_payload({"email": "alice@example.com", "password": "SecurePass1"})
    if res1 is None:
        print("[!] Function `validate_registration_payload` is not yet implemented.")
        return
    v1, _ = res1
    v2, _ = validate_registration_payload({"email": "bademail", "password": "SecurePass1"})
    v3, _ = validate_registration_payload({"email": "bob@example.com", "password": "short"})
    v4, _ = validate_registration_payload({"email": "bob@example.com", "password": "NoDigitsPassword"})
    if (v1, v2, v3, v4) == (True, False, False, False):
        print("[+] Test Passed: Registration test validation rules verified.")
    else:
        print(f"[-] Test Failed: Got {(v1, v2, v3, v4)}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Check email '@' first, then check password length >= 8, then check `any(ch.isdigit() for ch in pwd)`.
# Hint 2: Return False with descriptive message if email lacks '@', length < 8, or no digit is found.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(payload: dict) -> tuple[bool, str]:
    email = payload.get("email", "")
    pwd = payload.get("password", "")
    if "@" not in email:
        return False, "Invalid email format"
    if len(pwd) < 8:
        return False, "Password must be at least 8 characters"
    if not any(ch.isdigit() for ch in pwd):
        return False, "Password must contain at least one digit"
    return True, "Valid"


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
