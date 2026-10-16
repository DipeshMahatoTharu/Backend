"""
============================================================
DAY 47 REVISION SESSION (~10–15 MINUTES)
Topic: Django Relationships, related_name & String Validation
============================================================

Verified Prerequisites: Days 1–46 (Day 46 CRUD Application & Relationships, Day 23 String Processing)

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
# 1. What does the `related_name` argument in a `ForeignKey` define on the reverse model?
#
# 2. If model `Author` has many `Books`, how do you access the books from an author instance if `related_name='books'`?
#
# 3. Why is regular expression pattern matching useful for validating standardized strings like SKUs or phone numbers?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `validate_sku(sku: str) -> bool` that verifies an SKU follows the format: 3 uppercase letters, a hyphen, and 3 digits (e.g. 'ABC-123').

import re

def validate_sku(sku: str) -> bool:
    """
    Returns True if sku matches ^[A-Z]{3}-\d{3}$, False otherwise.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 47 Revision Challenge ---")
    v1 = validate_sku("PRD-404")
    v2 = validate_sku("prd-404")
    v3 = validate_sku("PRD404")
    if v1 is None:
        print("[!] Function `validate_sku` is not yet implemented.")
        return
    if v1 is True and v2 is False and v3 is False:
        print("[+] Test Passed: SKU pattern validator succeeded.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}, v3={v3}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Use `re.fullmatch(r'^[A-Z]{3}-\d{3}$', sku)`.
# Hint 2: Return `bool(re.fullmatch(r'^[A-Z]{3}-\d{3}$', sku))`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
import re

def _reference_solution(sku: str) -> bool:
    return bool(re.fullmatch(r'^[A-Z]{3}-\d{3}$', sku))


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
