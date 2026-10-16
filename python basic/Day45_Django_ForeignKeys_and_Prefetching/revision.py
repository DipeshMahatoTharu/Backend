"""
============================================================
DAY 45 REVISION SESSION (~10–15 MINUTES)
Topic: QuerySet Lazy Evaluation, Q Objects & SQL Joins
============================================================

Verified Prerequisites: Days 1–44 (Day 44 ORM Queries & Q Objects, Day 30 SQL Joins)

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
# 1. What does 'lazy evaluation' mean for Django QuerySets, and what triggers an actual SQL execution (iteration, slicing, len)?
#
# 2. How do Django `Q` objects allow OR queries (e.g. `Q(status='A') | Q(status='B')`)?
#
# 3. Why is filtering in the database using QuerySets vastly more efficient than fetching all records and filtering in Python?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `simulate_q_filter(items: list[dict], cat: str = None, min_price: float = None) -> list[dict]` matching items where category matches OR price >= min_price.

def simulate_q_filter(items: list[dict], cat: str = None, min_price: float = None) -> list[dict]:
    """
    Simulates Django Q(category=cat) | Q(price__gte=min_price)
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 45 Revision Challenge ---")
    data = [
        {"name": "A", "category": "books", "price": 10},
        {"name": "B", "category": "tech", "price": 100},
        {"name": "C", "category": "clothing", "price": 50},
    ]
    res = simulate_q_filter(data, cat="books", min_price=80)
    if res is None:
        print("[!] Function `simulate_q_filter` is not yet implemented.")
        return
    names = [r["name"] for r in res]
    if sorted(names) == ["A", "B"]:
        print("[+] Test Passed: Disjunctive OR filter simulation succeeded.")
    else:
        print(f"[-] Test Failed: Got names={names}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: For each item, test if it matches condition 1 OR condition 2.
# Hint 2: Use `[i for i in items if (cat and i.get('category') == cat) or (min_price is not None and i.get('price', 0) >= min_price)]`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(items: list[dict], cat: str = None, min_price: float = None) -> list[dict]:
    return [
        i for i in items
        if (cat and i.get("category") == cat) or (min_price is not None and i.get("price", 0) >= min_price)
    ]


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
