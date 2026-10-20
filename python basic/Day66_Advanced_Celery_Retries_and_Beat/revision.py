"""
============================================================
DAY 66 REVISION SESSION (~10–15 MINUTES)
Topic: Celery Architecture & Background Task Queues
============================================================

Verified Prerequisites: Day 65 (Celery Architecture & Task Queues)

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
# 1. What are the 3 core components of a background task system (Producer, Broker, Worker)?
#
# 2. Why should slow I/O operations (sending emails, processing payments, resizing images) never run synchronously in an HTTP view?
#
# 3. What is a task broker (e.g. Redis or RabbitMQ)?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `simulate_task_queue(tasks: list[dict], max_retries: int = 3) -> dict` that processes a list of tasks `[{'id': 1, 'attempts': 2}]`. If `attempts <= max_retries`, mark `'SUCCESS'`, otherwise mark `'DEAD_LETTER_QUEUE'`.

def simulate_task_queue(tasks: list[dict], max_retries: int = 3) -> dict:
    """
    Returns {'processed': count_success, 'failed': count_dlq}
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 66 Revision Challenge ---")
    tasks = [{"id": 1, "attempts": 1}, {"id": 2, "attempts": 4}, {"id": 3, "attempts": 3}]
    res = simulate_task_queue(tasks, max_retries=3)
    if res is None:
        print("[!] Function `simulate_task_queue` is not yet implemented.")
        return
    if res.get("processed") == 2 and res.get("failed") == 1:
        print("[+] Test Passed: Background task queue simulation verified.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Count tasks where `attempts <= max_retries` as processed, and others as failed.
# Hint 2: Use `success = sum(1 for t in tasks if t.get('attempts', 1) <= max_retries); return {'processed': success, 'failed': len(tasks) - success}`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(tasks: list[dict], max_retries: int = 3) -> dict:
    success = sum(1 for t in tasks if t.get("attempts", 1) <= max_retries)
    return {"processed": success, "failed": len(tasks) - success}


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
