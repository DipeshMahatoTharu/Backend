"""
============================================================
DAY 61 REVISION SESSION (~10–15 MINUTES)
Topic: Model Factories (factory_boy) & Python Exception Hierarchies
============================================================

Verified Prerequisites: Days 1–60 (Day 60 Test Factories & Fixtures, Day 23 Exception Handling)

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
# 1. Why are model factories (`factory_boy`) preferred over hardcoded fixtures (JSON/YAML) in production test suites?
#
# 2. In Python, why should you catch specific exception classes (e.g. `ObjectDoesNotExist`, `IntegrityError`) rather than catching bare `Exception`?
#
# 3. What is the purpose of raising a custom domain exception (e.g. `InsufficientInventoryError`) in a backend service?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write a factory function `create_mock_user(custom_attrs: dict = None) -> dict` that generates a default user dictionary (`{'id': 1, 'username': 'testuser', 'is_active': True, 'role': 'USER'}`) and cleanly overrides defaults with `custom_attrs`.

def create_mock_user(custom_attrs: dict = None) -> dict:
    """
    Generates a mock user dictionary with defaults, cleanly overridden by custom_attrs.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 61 Revision Challenge ---")
    u1 = create_mock_user()
    u2 = create_mock_user({"username": "custom_dev", "role": "ADMIN"})
    if u1 is None or u2 is None:
        print("[!] Function `create_mock_user` is not yet implemented.")
        return
    if u1.get("username") == "testuser" and u2.get("username") == "custom_dev" and u2.get("role") == "ADMIN" and u2.get("is_active") is True:
        print("[+] Test Passed: Mock user factory implementation verified.")
    else:
        print(f"[-] Test Failed: u1={u1}, u2={u2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Define a base default dict and update it with a copy of `custom_attrs` if provided.
# Hint 2: Use `defaults = {'id': 1, 'username': 'testuser', 'is_active': True, 'role': 'USER'}; if custom_attrs: defaults.update(custom_attrs); return defaults`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(custom_attrs: dict = None) -> dict:
    defaults = {"id": 1, "username": "testuser", "is_active": True, "role": "USER"}
    if custom_attrs:
        defaults.update(custom_attrs)
    return defaults


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
