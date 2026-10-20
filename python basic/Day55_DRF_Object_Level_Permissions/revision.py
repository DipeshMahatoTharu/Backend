"""
============================================================
DAY 55 REVISION SESSION (~10–15 MINUTES)
Topic: DRF Token Authentication & JWT (SimpleJWT)
============================================================

Verified Prerequisites: Day 54 (DRF Token Auth & JWT)

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
# 1. What is the difference between an Access Token (short-lived) and a Refresh Token (long-lived) in JWT?
#
# 2. What are the three parts of a JSON Web Token (Header, Payload, Signature)?
#
# 3. Why should JWT access tokens never be stored in browser `localStorage` due to XSS risks?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `check_role_permission(role: str, action: str) -> bool` enforcing: 'admin' can perform any action; 'staff' can perform 'read' and 'update'; 'customer' can only perform 'read'.

def check_role_permission(role: str, action: str) -> bool:
    """
    Enforces RBAC permissions. Actions: 'read', 'update', 'delete', 'create'.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 55 Revision Challenge ---")
    a1 = check_role_permission("admin", "delete")
    s1 = check_role_permission("staff", "update")
    s2 = check_role_permission("staff", "delete")
    c1 = check_role_permission("customer", "read")
    c2 = check_role_permission("customer", "update")
    if a1 is None:
        print("[!] Function `check_role_permission` is not yet implemented.")
        return
    if (a1, s1, s2, c1, c2) == (True, True, False, True, False):
        print("[+] Test Passed: RBAC permission check verified.")
    else:
        print(f"[-] Test Failed: Got {(a1, s1, s2, c1, c2)}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Define a permissions dictionary mapping roles to allowed action sets.
# Hint 2: Use `perms = {'admin': {'read', 'update', 'delete', 'create'}, 'staff': {'read', 'update'}, 'customer': {'read'}}; return action in perms.get(role, set())`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(role: str, action: str) -> bool:
    perms = {
        "admin": {"read", "update", "delete", "create"},
        "staff": {"read", "update"},
        "customer": {"read"}
    }
    return action in perms.get(role, set())


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
