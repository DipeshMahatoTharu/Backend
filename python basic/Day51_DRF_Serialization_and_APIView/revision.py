"""
============================================================
DAY 51 REVISION SESSION (~10–15 MINUTES)
Topic: Django ORM QuerySet Optimization & REST JSON Responses
============================================================

Verified Prerequisites: Days 1–50 (Day 45 ORM Prefetching, Day 37/39 HTTP JSON Responses)

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
# 1. What is the difference between serialization (Python object -> JSON/dict) and deserialization (JSON/dict -> Python object)?
#
# 2. Why does `only('id', 'name')` or `values('id', 'name')` improve query performance over fetching complete model instances when building lightweight API responses?
#
# 3. What HTTP status code and response structure should be returned when an incoming JSON payload fails validation?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `serialize_order_summary(order_dict: dict) -> dict` that converts an internal DB record (price in cents, raw ISO timestamp) into a clean REST API JSON structure with price formatted as dollars (float) and status uppercased.

def serialize_order_summary(order_dict: dict) -> dict:
    """
    Input: {'id': 101, 'price_cents': 2999, 'status': 'completed', 'raw_date': '2026-10-16T12:00:00Z'}
    Output: {'id': 101, 'price_dollars': 29.99, 'status': 'COMPLETED', 'date': '2026-10-16'}
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 51 Revision Challenge ---")
    raw = {"id": 101, "price_cents": 2999, "status": "completed", "raw_date": "2026-10-16T12:00:00Z"}
    res = serialize_order_summary(raw)
    if res is None:
        print("[!] Function `serialize_order_summary` is not yet implemented.")
        return
    if res.get("price_dollars") == 29.99 and res.get("status") == "COMPLETED" and res.get("date") == "2026-10-16":
        print("[+] Test Passed: REST JSON serialization structure verified.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Convert cents to dollars by dividing by 100.0, uppercase status, and slice date up to 'T'.
# Hint 2: Return `{'id': order_dict['id'], 'price_dollars': round(order_dict['price_cents']/100.0, 2), 'status': order_dict['status'].upper(), 'date': order_dict['raw_date'].split('T')[0]}`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(order_dict: dict) -> dict:
    return {
        "id": order_dict["id"],
        "price_dollars": round(order_dict["price_cents"] / 100.0, 2),
        "status": order_dict["status"].upper(),
        "date": order_dict["raw_date"].split("T")[0]
    }


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
