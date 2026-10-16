"""
============================================================
DAY 53 REVISION SESSION (~10–15 MINUTES)
Topic: Writable Nested Serializers & HTTP Methods
============================================================

Verified Prerequisites: Days 1–52 (Day 52 Nested Serializers, Day 38 HTTP Methods, Day 41 CBVs)

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
# 1. Why does DRF require custom `create()` and `update()` overrides when handling writable nested serializers?
#
# 2. What HTTP method should be used for full resource replacement (`PUT`) vs partial updates (`PATCH`)?
#
# 3. In DRF Class-Based Views, how does `get_serializer_class()` allow using different serializers for list vs detail views?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `flatten_nested_payload(payload: dict) -> dict` that extracts a nested `address` dict into top-level keys `address_city` and `address_zip`.

def flatten_nested_payload(payload: dict) -> dict:
    """
    Input: {'user': 'alice', 'address': {'city': 'Kathmandu', 'zip': '44600'}}
    Output: {'user': 'alice', 'address_city': 'Kathmandu', 'address_zip': '44600'}
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 53 Revision Challenge ---")
    inp = {"user": "alice", "address": {"city": "Kathmandu", "zip": "44600"}}
    res = flatten_nested_payload(inp)
    if res is None:
        print("[!] Function `flatten_nested_payload` is not yet implemented.")
        return
    if res.get("address_city") == "Kathmandu" and "address" not in res:
        print("[+] Test Passed: Nested payload transformation succeeded.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Copy the payload dict, pop the 'address' key, and assign the nested fields with prefixes.
# Hint 2: Use `out = dict(payload); addr = out.pop('address', {}); out['address_city'] = addr.get('city'); out['address_zip'] = addr.get('zip'); return out`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(payload: dict) -> dict:
    out = dict(payload)
    addr = out.pop("address", {})
    out["address_city"] = addr.get("city")
    out["address_zip"] = addr.get("zip")
    return out


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
