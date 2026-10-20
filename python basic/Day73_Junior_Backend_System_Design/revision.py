"""
============================================================
DAY 73 REVISION SESSION (~10–15 MINUTES)
Topic: CI/CD Pipelines & GitHub Actions Workflows
============================================================

Verified Prerequisites: Day 72 (CI/CD Pipelines & GitHub Actions)

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
# 1. What is Continuous Integration (CI) and why should linters and automated tests run on every pull request?
#
# 2. What are GitHub Actions workflows, jobs, and steps?
#
# 3. Why should database migrations be executed as an automated deployment step?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `build_cache_key(prefix: str, **params) -> str` which creates a deterministic, sorted Redis cache key (e.g. `build_cache_key('products', cat='shoes', page=1)` -> `'products:cat=shoes:page=1'`).

def build_cache_key(prefix: str, **params) -> str:
    """
    Constructs deterministic cache key with sorted param items.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 73 Revision Challenge ---")
    k1 = build_cache_key("products", cat="shoes", page=1)
    k2 = build_cache_key("products", page=1, cat="shoes")
    if k1 is None:
        print("[!] Function `build_cache_key` is not yet implemented.")
        return
    if k1 == "products:cat=shoes:page=1" and k1 == k2:
        print("[+] Test Passed: Deterministic cache key generation confirmed.")
    else:
        print(f"[-] Test Failed: k1='{k1}', k2='{k2}'")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Sort the keyword argument items by key.
# Hint 2: Format each parameter as `{k}={v}` and join with ':' after `prefix`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(prefix: str, **params) -> str:
    parts = [prefix]
    for k in sorted(params):
        parts.append(f"{k}={params[k]}")
    return ":".join(parts)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
