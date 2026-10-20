"""
============================================================
DAY 39 REVISION SESSION (~10–15 MINUTES)
Topic: Functions, Scope, Closures, Exception Defensiveness & Context Managers
============================================================

Verified Prerequisites: Days 22–24 (Day 22 Scope & Decorators, Day 23 Exception Handling, Day 24 Context Managers)

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
# 1. What is the LEGB rule for Python variable resolution (Local, Enclosing, Global, Built-in)?
#
# 2. What do the `__enter__` and `__exit__` magic methods do when using a `with` statement?
#
# 3. How does a Python decorator use closures to wrap another function?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write a decorator `retry_on_failure(max_retries: int = 2)` that catches exceptions and retries calling the wrapped function up to `max_retries` additional times before re-raising the exception.

import functools

def retry_on_failure(max_retries: int = 2):
    """
    Decorator that retries the wrapped function upon exception up to max_retries times.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 39 Revision Challenge ---")
    dec = retry_on_failure(max_retries=2)
    if dec is None:
        print("[!] Decorator `retry_on_failure` is not yet implemented.")
        return

    attempts = [0]
    @dec
    def flaky():
        attempts[0] += 1
        if attempts[0] < 3:
            raise ValueError("Temporary network glitch")
        return "SUCCESS"

    try:
        res = flaky()
        if res == "SUCCESS" and attempts[0] == 3:
            print("[+] Test Passed: Decorator retried and succeeded on third attempt.")
        else:
            print(f"[-] Test Failed: res={res}, attempts={attempts[0]}")
    except Exception as e:
        print(f"[!] Decorator failed or not implemented: {e}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Define decorator returning an inner wrapper taking `*args, **kwargs`.
# Hint 2: Loop for `max_retries + 1` times: inside `try: return func(*args, **kwargs)` except `Exception: if attempt == max_retries: raise`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
import functools

def _reference_solution(max_retries: int = 2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i == max_retries:
                        raise
        return wrapper
    return decorator


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
