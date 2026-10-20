"""
============================================================
DAY 74 REVISION SESSION (~10–15 MINUTES)
Topic: Junior Backend System Design & Scaling
============================================================

Verified Prerequisites: Day 73 (Junior Backend System Design)

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
# 1. What is the difference between vertical scaling (scale up) and horizontal scaling (scale out)?
#
# 2. When would you recommend adding a Redis cache versus optimizing an SQL query and adding an index?
#
# 3. How do database connection pools and read replicas improve backend throughput?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Technical interview challenge: Write `top_customers(transactions: list[dict], n: int = 2) -> list[tuple[str, float]]` that aggregates total spending per customer from `transactions` (`[{'customer': 'Alice', 'amount': 150.0}, ...]`) and returns the top `n` customers as sorted `(customer_name, total_spent)` tuples (descending by total).

def top_customers(transactions: list[dict], n: int = 2) -> list[tuple[str, float]]:
    """
    Aggregates spending per customer and returns top n sorted tuples.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 74 Revision Challenge ---")
    txs = [
        {"customer": "Alice", "amount": 100.0},
        {"customer": "Bob", "amount": 250.0},
        {"customer": "Alice", "amount": 75.0},
        {"customer": "Carol", "amount": 500.0},
    ]
    res = top_customers(txs, n=2)
    if res is None:
        print("[!] Function `top_customers` is not yet implemented.")
        return
    expected = [("Carol", 500.0), ("Bob", 250.0)]
    if res == expected:
        print("[+] Test Passed: Interview data aggregation challenge verified.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Use a dictionary to aggregate sums: `totals[cust] = totals.get(cust, 0.0) + amt`.
# Hint 2: Sort dictionary items by value descending: `sorted(totals.items(), key=lambda x: x[1], reverse=True)[:n]`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(transactions: list[dict], n: int = 2) -> list[tuple[str, float]]:
    totals = {}
    for t in transactions:
        c = t["customer"]
        totals[c] = totals.get(c, 0.0) + t["amount"]
    sorted_customers = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return sorted_customers[:n]


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
