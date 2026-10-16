"""
============================================================
DAY 65 REVISION SESSION (~10–15 MINUTES)
Topic: Cache-Aside Pattern, Redis & Blocking vs Non-Blocking I/O
============================================================

Verified Prerequisites: Days 1–64 (Day 64 Redis Caching Layer, Day 37 HTTP I/O, Day 63 Service Layer)

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
# 1. What is the Cache-Aside pattern (application checks cache; on miss, reads from DB and writes to cache)?
#
# 2. What is the difference between an in-memory datastore like Redis and a disk-backed relational database like PostgreSQL?
#
# 3. Why is caching user sessions or read-heavy catalog data beneficial for backend throughput?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `cache_aside_lookup(cache_dict: dict, db_fetch_fn, key: str) -> tuple[object, str]` that checks `cache_dict[key]`. If present, returns `(value, 'CACHE_HIT')`. If missing, calls `db_fetch_fn(key)`, stores result in `cache_dict`, and returns `(value, 'CACHE_MISS')`.

def cache_aside_lookup(cache_dict: dict, db_fetch_fn, key: str) -> tuple[object, str]:
    """
    Implements Cache-Aside pattern simulation.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 65 Revision Challenge ---")
    cache = {}
    db_calls = [0]
    def mock_db(k):
        db_calls[0] += 1
        return f"db_val_{k}"

    res1 = cache_aside_lookup(cache, mock_db, "user:1")
    if res1 is None:
        print("[!] Function `cache_aside_lookup` is not yet implemented.")
        return
    val1, status1 = res1
    val2, status2 = cache_aside_lookup(cache, mock_db, "user:1")
    if status1 == "CACHE_MISS" and status2 == "CACHE_HIT" and val1 == "db_val_user:1" and db_calls[0] == 1:
        print("[+] Test Passed: Cache-Aside pattern logic confirmed.")
    else:
        print(f"[-] Test Failed: s1={status1}, s2={status2}, db_calls={db_calls[0]}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Check `if key in cache_dict: return (cache_dict[key], 'CACHE_HIT')`.
# Hint 2: On miss: `val = db_fetch_fn(key); cache_dict[key] = val; return (val, 'CACHE_MISS')`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(cache_dict: dict, db_fetch_fn, key: str) -> tuple[object, str]:
    if key in cache_dict:
        return (cache_dict[key], "CACHE_HIT")
    val = db_fetch_fn(key)
    cache_dict[key] = val
    return (val, "CACHE_MISS")


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
