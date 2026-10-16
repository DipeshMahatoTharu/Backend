"""
============================================================
DAY 59 REVISION SESSION (~10–15 MINUTES)
Topic: API Testing with Postman, Assertions & Status Codes
============================================================

Verified Prerequisites: Days 1–58 (Day 58 Manual Testing, Day 38 Status Codes, Day 23 Assertions)

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
# 1. How does automated testing in Postman using JavaScript assertions (`pm.response.to.have.status(200)`) differ from Python unit testing?
#
# 2. Why should backend tests assert both the HTTP status code AND the JSON response body structure?
#
# 3. What is Python's `assert` statement and why is it the foundation of unit testing frameworks?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `assert_response_contract(response: dict, required_keys: list[str]) -> bool` that verifies a response dictionary contains all required keys and none of their values are None.

def assert_response_contract(response: dict, required_keys: list[str]) -> bool:
    """
    Returns True if all required_keys exist in response and have non-None values, False otherwise.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 59 Revision Challenge ---")
    resp_ok = {"id": 1, "name": "Book", "price": 19.99}
    resp_missing = {"id": 2, "name": "Pencil"}
    resp_null = {"id": 3, "name": None, "price": 5.0}
    
    r1 = assert_response_contract(resp_ok, ["id", "name", "price"])
    r2 = assert_response_contract(resp_missing, ["id", "name", "price"])
    r3 = assert_response_contract(resp_null, ["id", "name", "price"])
    if r1 is None:
        print("[!] Function `assert_response_contract` is not yet implemented.")
        return
    if r1 is True and r2 is False and r3 is False:
        print("[+] Test Passed: API response contract assertion validated.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, r3={r3}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Loop over `required_keys` and verify each key is in the dict and not None.
# Hint 2: Use `all(k in response and response[k] is not None for k in required_keys)`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(response: dict, required_keys: list[str]) -> bool:
    return all(k in response and response[k] is not None for k in required_keys)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
