"""
============================================================
DAY 56 REVISION SESSION (~10–15 MINUTES)
Topic: Custom Permissions (BasePermission) & Query Filtering
============================================================

Verified Prerequisites: Days 1–55 (Day 55 Object Permissions, Day 39 REST Query Params)

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
# 1. In DRF `BasePermission`, what is the difference between `has_permission(request, view)` and `has_object_permission(request, view, obj)`?
#
# 2. What are the HTTP 'SAFE_METHODS' in DRF (`GET`, `HEAD`, `OPTIONS`)?
#
# 3. Why should object-level permissions allow read access for safe methods while restricting write access to the object's owner or staff?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `has_object_permission(user: dict, obj: dict, http_method: str) -> bool` allowing safe methods ('GET', 'HEAD') for everyone, and write methods only if `user['id'] == obj['owner_id']` or `user['is_staff']` is True.

def has_object_permission(user: dict, obj: dict, http_method: str) -> bool:
    """
    Simulates DRF IsOwnerOrReadOnly permission.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 56 Revision Challenge ---")
    owner = {"id": 10, "is_staff": False}
    other = {"id": 20, "is_staff": False}
    staff = {"id": 99, "is_staff": True}
    obj = {"id": 101, "owner_id": 10}
    
    p1 = has_object_permission(other, obj, "GET")    # True (safe method)
    p2 = has_object_permission(other, obj, "DELETE") # False (not owner)
    p3 = has_object_permission(owner, obj, "PUT")    # True (is owner)
    p4 = has_object_permission(staff, obj, "DELETE") # True (is staff)
    if p1 is None:
        print("[!] Function `has_object_permission` is not yet implemented.")
        return
    if (p1, p2, p3, p4) == (True, False, True, True):
        print("[+] Test Passed: DRF object-level permission logic verified.")
    else:
        print(f"[-] Test Failed: Got {(p1, p2, p3, p4)}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: If http_method in ('GET', 'HEAD', 'OPTIONS'): return True.
# Hint 2: Otherwise: `return user.get('id') == obj.get('owner_id') or user.get('is_staff') is True`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(user: dict, obj: dict, http_method: str) -> bool:
    if http_method.upper() in ("GET", "HEAD", "OPTIONS"):
        return True
    return user.get("id") == obj.get("owner_id") or user.get("is_staff") is True


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
