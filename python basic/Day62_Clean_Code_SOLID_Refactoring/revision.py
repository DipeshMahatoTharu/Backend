"""
============================================================
DAY 62 REVISION SESSION (~10–15 MINUTES)
Topic: Troubleshooting, Debugging ORM & Python Logging
============================================================

Verified Prerequisites: Day 61 (Troubleshooting & Debugging ORM)

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
# 1. What are the 5 standard Python logging levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)?
#
# 2. How do you use `breakpoint()` in Python to pause execution and inspect variables in the terminal?
#
# 3. How do you identify duplicate or slow SQL queries in development using Django Debug Toolbar?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `format_log_entry(level: str, event: str, **context) -> str` which formats a structured log entry string: `[LEVEL] event | key1=val1 key2=val2` with sorted context keys.

def format_log_entry(level: str, event: str, **context) -> str:
    """
    Example: format_log_entry('INFO', 'User logged in', user_id=42, ip='127.0.0.1')
    Returns: '[INFO] User logged in | ip=127.0.0.1 user_id=42'
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 62 Revision Challenge ---")
    l1 = format_log_entry("INFO", "Order created", order_id=101, amount=50.0)
    l2 = format_log_entry("ERROR", "DB connection lost")
    if l1 is None or l2 is None:
        print("[!] Function `format_log_entry` is not yet implemented.")
        return
    if l1 == "[INFO] Order created | amount=50.0 order_id=101" and l2 == "[ERROR] DB connection lost":
        print("[+] Test Passed: Structured log entry formatting confirmed.")
    else:
        print(f"[-] Test Failed: l1='{l1}', l2='{l2}'")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Format the prefix `[{level.upper()}] {event}`. If context has items, sort them and join with spaces.
# Hint 2: Use `ctx_str = ' '.join(f'{k}={context[k]}' for k in sorted(context)); return f'[{level.upper()}] {event} | {ctx_str}' if ctx_str else f'[{level.upper()}] {event}'`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(level: str, event: str, **context) -> str:
    level_str = f"[{level.upper()}] {event}"
    if not context:
        return level_str
    ctx_parts = [f"{k}={context[k]}" for k in sorted(context)]
    return f"{level_str} | {' '.join(ctx_parts)}"


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
