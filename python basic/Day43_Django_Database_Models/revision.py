"""
============================================================
DAY 43 REVISION SESSION (~10–15 MINUTES)
Topic: Relational Schemas, Model Fields & OOP Inheritance
============================================================

Verified Prerequisites: Days 1–42 (Day 42 Templates, Day 34 Relational Schemas, Day 14 OOP Inheritance)

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
# 1. How does Django translate Python model class attributes into SQL column definitions?
#
# 2. What is the difference between `null=True` (database level) and `blank=True` (form validation level)?
#
# 3. How does class inheritance in `class Product(models.Model)` allow Django models to inherit database behavior?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `validate_model_price(price: float) -> tuple[bool, str]` that ensures a price is a positive number, does not exceed 100000.0, and has at most 2 decimal places.

def validate_model_price(price: float) -> tuple[bool, str]:
    """
    Validates model price field:
    - price > 0
    - price <= 100000.0
    - at most 2 decimal places
    Returns (True, "Valid") or (False, "Error message")
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 43 Revision Challenge ---")
    res1 = validate_model_price(49.99)
    if res1 is None:
        print("[!] Function `validate_model_price` is not yet implemented.")
        return
    v1, _ = res1
    v2, _ = validate_model_price(-5.0)
    v3, _ = validate_model_price(19.999)
    if v1 is True and v2 is False and v3 is False:
        print("[+] Test Passed: Model field price constraints validated.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}, v3={v3}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Check price range first, then check decimals via string representation or `round(price, 2) == price`.
# Hint 2: Use `if price <= 0 or price > 100000: return False, ...` and `if round(price, 2) != price: return False, ...`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(price: float) -> tuple[bool, str]:
    if price <= 0:
        return False, "Price must be strictly positive"
    if price > 100000.0:
        return False, "Price exceeds maximum threshold"
    if round(price, 2) != price:
        return False, "Price cannot have more than 2 decimal places"
    return True, "Valid"


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
