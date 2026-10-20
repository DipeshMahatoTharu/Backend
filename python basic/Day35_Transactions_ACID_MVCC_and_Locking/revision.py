"""
============================================================
DAY 35 REVISION SESSION (~10–15 MINUTES)
Topic: Tuples, Exception Handling & File Safety
============================================================

Verified Prerequisites: Days 10–12 (Day 10 Revision, Day 11 Tuples, Day 12 Exceptions & Files)

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
# 1. Why are tuples immutable while lists are mutable, and why does this allow tuples to be used as dictionary keys?
#
# 2. What is the difference between catching a specific exception (e.g. `except ValueError:`) versus bare `except:`?
#
# 3. What does a `finally` block guarantee in Python exception handling?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `safe_parse_record(raw_record: tuple) -> tuple[bool, dict | str]` that takes a tuple `(id_val, name_val, age_val)`. Ensure tuple length is 3 and convert `id` and `age` to `int`. Return `(True, {'id': int, 'name': str, 'age': int})` or `(False, 'Parsing failed')` if any error occurs.

def safe_parse_record(raw_record: tuple) -> tuple[bool, dict | str]:
    """
    Safely parses (id_val, name_val, age_val).
    Returns (True, dict) or (False, "Parsing failed").
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 35 Revision Challenge ---")
    res1 = safe_parse_record(("101", "Alice", "24"))
    if res1 is None:
        print("[!] Function `safe_parse_record` is not yet implemented.")
        return
    ok1, val1 = res1
    ok2, val2 = safe_parse_record(("bad_id", "Bob", "30"))
    ok3, val3 = safe_parse_record(("102", "Carol")) # wrong length
    if ok1 is True and val1 == {"id": 101, "name": "Alice", "age": 24} and ok2 is False and ok3 is False:
        print("[+] Test Passed: Safe record parsing with exception handling confirmed.")
    else:
        print(f"[-] Test Failed: r1={res1}, ok2={ok2}, ok3={ok3}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Check `if not isinstance(raw_record, tuple) or len(raw_record) != 3: return False, 'Parsing failed'`.
# Hint 2: Wrap conversions `int(raw_record[0])` and `int(raw_record[2])` in a `try...except (ValueError, TypeError):` block.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(raw_record: tuple) -> tuple[bool, dict | str]:
    if not isinstance(raw_record, tuple) or len(raw_record) != 3:
        return False, "Parsing failed"
    try:
        return True, {
            "id": int(raw_record[0]),
            "name": str(raw_record[1]),
            "age": int(raw_record[2])
        }
    except (ValueError, TypeError):
        return False, "Parsing failed"


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
