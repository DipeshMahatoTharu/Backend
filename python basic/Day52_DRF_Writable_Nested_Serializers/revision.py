"""
============================================================
DAY 52 REVISION SESSION (~10–15 MINUTES)
Topic: DRF Serialization, Serializer Fields & APIView
============================================================

Verified Prerequisites: Day 51 (DRF Serialization & APIView)

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
# 1. What is the role of a DRF Serializer in converting complex QuerySets to Python datatypes (JSON)?
#
# 2. How does `ModelSerializer` differ from a regular `Serializer` in DRF?
#
# 3. What is the difference between `APIView` and Django's standard `View`?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `validate_product_serializer(payload: dict) -> tuple[bool, dict]` that validates `title` (required, min 3 chars) and `price` (required, float > 0). Returns `(True, {})` or `(False, errors_dict)`.

def validate_product_serializer(payload: dict) -> tuple[bool, dict]:
    """
    Validates product fields. Returns (is_valid, errors_dict).
    errors_dict contains field names mapped to list of error strings.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 52 Revision Challenge ---")
    res1 = validate_product_serializer({"title": "Laptop", "price": 999.0})
    if res1 is None:
        print("[!] Function `validate_product_serializer` is not yet implemented.")
        return
    v1, e1 = res1
    v2, e2 = validate_product_serializer({"title": "AB", "price": -10.0})
    if v1 is True and v2 is False and "title" in e2 and "price" in e2:
        print("[+] Test Passed: Serializer field validation logic confirmed.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}, e2={e2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Create an empty errors dict and populate it with lists of error messages for failing fields.
# Hint 2: If 'title' not in payload or len(payload['title']) < 3: errors['title'] = ['Min 3 chars']. If 'price' not in payload or payload['price'] <= 0: errors['price'] = ['Must be positive'].


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(payload: dict) -> tuple[bool, dict]:
    errors = {}
    title = payload.get("title", "")
    if not title or len(title) < 3:
        errors["title"] = ["Title must be at least 3 characters long"]
    price = payload.get("price")
    if price is None or price <= 0:
        errors["price"] = ["Price must be a positive number"]
    return (len(errors) == 0, errors)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
