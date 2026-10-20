"""
============================================================
DAY 68 REVISION SESSION (~10–15 MINUTES)
Topic: Real-Time WebSockets vs HTTP & Django Channels
============================================================

Verified Prerequisites: Day 67 (Real-Time WebSockets & Channels)

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
# 1. How does a persistent WebSocket connection differ from a standard HTTP request/response cycle?
#
# 2. What is the purpose of Django Channels and ASGI (Asynchronous Server Gateway Interface)?
#
# 3. What role does Redis play as a channel layer for broadcasting messages across WebSocket connections?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `process_idempotent_event(processed_keys: set, idempotency_key: str, event_data: dict) -> tuple[bool, str]` which checks if `idempotency_key` has already been processed. If yes, returns `(False, 'Duplicate ignored')`. If no, records the key in the set and returns `(True, 'Processed')`.

def process_idempotent_event(processed_keys: set, idempotency_key: str, event_data: dict) -> tuple[bool, str]:
    """
    Prevents duplicate event execution using an idempotency key set.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 68 Revision Challenge ---")
    keys = set()
    res1 = process_idempotent_event(keys, "key-abc-123", {"order_id": 10})
    if res1 is None:
        print("[!] Function `process_idempotent_event` is not yet implemented.")
        return
    s1, m1 = res1
    s2, m2 = process_idempotent_event(keys, "key-abc-123", {"order_id": 10})
    if s1 is True and s2 is False and "Duplicate" in m2:
        print("[+] Test Passed: Idempotency deduplication logic confirmed.")
    else:
        print(f"[-] Test Failed: s1={s1}, s2={s2}, m2={m2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Check if `idempotency_key in processed_keys`.
# Hint 2: If in set: return `(False, 'Duplicate ignored')`. Else: `processed_keys.add(idempotency_key)` and return `(True, 'Processed')`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(processed_keys: set, idempotency_key: str, event_data: dict) -> tuple[bool, str]:
    if idempotency_key in processed_keys:
        return False, "Duplicate ignored"
    processed_keys.add(idempotency_key)
    return True, "Processed"


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
