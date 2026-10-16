"""
============================================================
DAY 46 REVISION SESSION (~10–15 MINUTES)
Topic: N+1 Query Problem, select_related & B-Tree Index Traversal
============================================================

Verified Prerequisites: Days 1–45 (Day 45 Prefetching & ForeignKeys, Day 33 Indexing)

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
# 1. What is the N+1 query problem in ORMs, and how does `select_related` fix it using an SQL JOIN?
#
# 2. What is the difference between `select_related` (single-valued FKs/OneToOne) and `prefetch_related` (ManyToMany/reverse FKs)?
#
# 3. How does an indexed foreign key column speed up JOIN lookups in PostgreSQL?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `count_simulated_queries(item_count: int, use_select_related: bool) -> int` returning the number of database queries executed when accessing a foreign key attribute for N items.

def count_simulated_queries(item_count: int, use_select_related: bool) -> int:
    """
    If use_select_related is True: executes exactly 1 query (with SQL JOIN).
    If False: executes 1 initial query + 1 query per item (1 + N queries).
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 46 Revision Challenge ---")
    q_opt = count_simulated_queries(50, True)
    q_naive = count_simulated_queries(50, False)
    if q_opt is None:
        print("[!] Function `count_simulated_queries` is not yet implemented.")
        return
    if q_opt == 1 and q_naive == 51:
        print("[+] Test Passed: N+1 query count calculation verified.")
    else:
        print(f"[-] Test Failed: q_opt={q_opt}, q_naive={q_naive}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: If select_related is enabled, only 1 SQL JOIN query is sent.
# Hint 2: Return 1 if `use_select_related` else `item_count + 1`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(item_count: int, use_select_related: bool) -> int:
    return 1 if use_select_related else item_count + 1


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
