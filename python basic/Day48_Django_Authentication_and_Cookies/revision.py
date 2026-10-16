"""
============================================================
DAY 48 REVISION SESSION (~10–15 MINUTES)
Topic: Django Form Validation, cleaned_data & Constraints
============================================================

Verified Prerequisites: Days 1–47 (Day 47 Django Forms & clean_* Validation, Day 34 Database Constraints)

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
# 1. In Django forms, what is the purpose of the `clean_<fieldname>()` and `clean()` methods?
#
# 2. What dictionary does Django populate after running form validation, and what happens if validation fails?
#
# 3. Why must validation happen both at the form/serializer level and at the database constraint level?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `clean_date_range(cleaned_data: dict) -> tuple[bool, str]` ensuring `start_day` < `end_day` where values are integers.

def clean_date_range(cleaned_data: dict) -> tuple[bool, str]:
    """
    Validates that cleaned_data['start_day'] < cleaned_data['end_day'].
    Returns (True, "Valid") or (False, "End date must be after start date").
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 48 Revision Challenge ---")
    res1 = clean_date_range({"start_day": 10, "end_day": 15})
    if res1 is None:
        print("[!] Function `clean_date_range` is not yet implemented.")
        return
    r1, _ = res1
    r2, _ = clean_date_range({"start_day": 20, "end_day": 15})
    if r1 is True and r2 is False:
        print("[+] Test Passed: Form date range validation succeeded.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Extract `start_day` and `end_day` from `cleaned_data` and compare them.
# Hint 2: If `cleaned_data.get('end_day', 0) <= cleaned_data.get('start_day', 0)` return False, message.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(cleaned_data: dict) -> tuple[bool, str]:
    start = cleaned_data.get("start_day", 0)
    end = cleaned_data.get("end_day", 0)
    if end <= start:
        return False, "End date must be after start date"
    return True, "Valid"


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
