"""
============================================================
DAY 64 REVISION SESSION (~10–15 MINUTES)
Topic: Service Layer Pattern & Query Latency
============================================================

Verified Prerequisites: Days 1–63 (Day 63 Service Layers, Day 33 Indexing Latency, Day 45 ORM Optimization)

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
# 1. What is the Service Layer pattern and why does it keep business logic out of views and models?
#
# 2. Why can an unindexed database query take hundreds of milliseconds on large tables while an indexed query takes under 5 milliseconds?
#
# 3. How do you measure database query latency in development using tools like Django Debug Toolbar or `EXPLAIN ANALYZE`?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Implement a service function `calculate_order_totals_service(items: list[dict], discount_pct: float = 0.0) -> dict` returning `{'subtotal': float, 'discount': float, 'total': float}` with all values rounded to 2 decimals.

def calculate_order_totals_service(items: list[dict], discount_pct: float = 0.0) -> dict:
    """
    Each item in items: {'price': float, 'qty': int}
    discount_pct is a float between 0.0 and 1.0 (e.g. 0.15 for 15% off).
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 64 Revision Challenge ---")
    items = [{"price": 20.0, "qty": 2}, {"price": 10.0, "qty": 1}] # subtotal = 50.0
    res = calculate_order_totals_service(items, discount_pct=0.10)
    if res is None:
        print("[!] Function `calculate_order_totals_service` is not yet implemented.")
        return
    if res.get("subtotal") == 50.0 and res.get("discount") == 5.0 and res.get("total") == 45.0:
        print("[+] Test Passed: Service layer calculation logic confirmed.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Compute subtotal = sum(i['price'] * i['qty'] for i in items).
# Hint 2: Compute discount = round(subtotal * discount_pct, 2) and total = round(subtotal - discount, 2).


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(items: list[dict], discount_pct: float = 0.0) -> dict:
    subtotal = round(sum(i["price"] * i["qty"] for i in items), 2)
    discount = round(subtotal * discount_pct, 2)
    total = round(subtotal - discount, 2)
    return {"subtotal": subtotal, "discount": discount, "total": total}


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
