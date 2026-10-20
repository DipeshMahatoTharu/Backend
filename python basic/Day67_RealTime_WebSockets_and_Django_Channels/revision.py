"""
============================================================
DAY 67 REVISION SESSION (~10–15 MINUTES)
Topic: Celery Retries, Exponential Backoff & Celery Beat
============================================================

Verified Prerequisites: Day 66 (Advanced Celery Retries & Beat)

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
# 1. What is exponential backoff and why is it used when retrying network operations?
#
# 2. What does Celery Beat do for scheduled/periodic tasks (cron jobs)?
#
# 3. Why must background tasks be idempotent so retrying them does not cause duplicate side effects?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `calculate_exponential_backoff(attempt: int, base_delay: int = 2, max_delay: int = 60) -> int` returning `min(base_delay ** attempt, max_delay)`.

def calculate_exponential_backoff(attempt: int, base_delay: int = 2, max_delay: int = 60) -> int:
    """
    Computes exponential backoff delay in seconds.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 67 Revision Challenge ---")
    d1 = calculate_exponential_backoff(1, base_delay=2, max_delay=60)
    d2 = calculate_exponential_backoff(3, base_delay=2, max_delay=60)
    d3 = calculate_exponential_backoff(8, base_delay=2, max_delay=60)
    if d1 is None:
        print("[!] Function `calculate_exponential_backoff` is not yet implemented.")
        return
    if (d1, d2, d3) == (2, 8, 60):
        print("[+] Test Passed: Exponential backoff calculations verified.")
    else:
        print(f"[-] Test Failed: Got {(d1, d2, d3)}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Compute `base_delay ** attempt` and return the minimum of that value and `max_delay`.
# Hint 2: Use `return min(base_delay ** attempt, max_delay)`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(attempt: int, base_delay: int = 2, max_delay: int = 60) -> int:
    return min(base_delay ** attempt, max_delay)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
