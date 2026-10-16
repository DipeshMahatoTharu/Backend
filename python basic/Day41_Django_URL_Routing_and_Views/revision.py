"""
============================================================
DAY 41 REVISION SESSION (~10–15 MINUTES)
Topic: Django MVT Pattern, Environment Variables & Python Decorators
============================================================

Verified Prerequisites: Days 1–40 (Day 40 Django Intro & Settings, Day 22 Decorators)

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
# 1. What are the distinct responsibilities of Model, View, and Template in Django's MVT pattern?
#
# 2. Why must SECRET_KEY and DB credentials be read from environment variables rather than hardcoded in `settings.py`?
#
# 3. How does a Python decorator wrap and modify the execution of an underlying view function?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write a decorator `require_auth` that inspects a simulated `request` dict. If `request.get('is_authenticated')` is True, it calls the function; otherwise, it returns `{'error': 'Unauthorized', 'status': 401}`.

import functools

def require_auth(func):
    """
    Decorator that checks if request['is_authenticated'] is True.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 41 Revision Challenge ---")
    wrapper = require_auth(lambda r: {"status": 200})
    if wrapper is None:
        print("[!] Decorator `require_auth` is not yet implemented.")
        return

    @require_auth
    def profile_view(request):
        return {"data": f"Welcome user {request.get('user_id')}", "status": 200}

    r_anon = profile_view({"is_authenticated": False})
    r_user = profile_view({"is_authenticated": True, "user_id": 42})
    if r_anon.get("status") == 401 and r_user.get("status") == 200:
        print("[+] Test Passed: require_auth decorator enforced access control.")
    else:
        print(f"[-] Test Failed: anon={r_anon}, user={r_user}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Use `functools.wraps(func)` and define an inner wrapper that accepts `request, *args, **kwargs`.
# Hint 2: Inside wrapper: `if not request.get('is_authenticated'): return {'error': 'Unauthorized', 'status': 401}` else return `func(request, *args, **kwargs)`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
import functools

def _reference_solution(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.get("is_authenticated"):
            return {"error": "Unauthorized", "status": 401}
        return func(request, *args, **kwargs)
    return wrapper


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
