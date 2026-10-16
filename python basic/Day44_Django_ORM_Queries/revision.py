"""
============================================================
DAY 44 REVISION SESSION (~10–15 MINUTES)
Topic: Django Migrations, SQL DDL & Database Constraints
============================================================

Verified Prerequisites: Days 1–43 (Day 43 Django Models & Migrations, Day 34 Database Constraints)

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
# 1. What is the difference between `makemigrations` (creates Python migration file) and `migrate` (executes SQL DDL against the DB)?
#
# 2. Why should you never manually alter production database tables using raw SQL when using Django migrations?
#
# 3. What does a `UNIQUE` constraint prevent at the database level?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `validate_field_constraints(data: dict, schema: dict) -> tuple[bool, list[str]]` that checks if all required schema fields are present and non-null in data.

def validate_field_constraints(data: dict, schema: dict) -> tuple[bool, list[str]]:
    """
    schema format: {'fields': {'title': {'required': True}, 'slug': {'required': True}}}
    Returns (is_valid, list_of_missing_fields)
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 44 Revision Challenge ---")
    schema = {"fields": {"title": {"required": True}, "slug": {"required": True}, "desc": {"required": False}}}
    valid_data = {"title": "Post 1", "slug": "post-1"}
    invalid_data = {"title": "Post 2"}
    
    res1 = validate_field_constraints(valid_data, schema)
    if res1 is None:
        print("[!] Function `validate_field_constraints` is not yet implemented.")
        return
    r1, m1 = res1
    r2, m2 = validate_field_constraints(invalid_data, schema)
    if r1 is True and r2 is False and "slug" in m2:
        print("[+] Test Passed: Schema constraint validator succeeded.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, m2={m2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Iterate through `schema['fields']` and check if `conf.get('required')` is True.
# Hint 2: If field not in data or data[field] is None: append field name to missing list.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(data: dict, schema: dict) -> tuple[bool, list[str]]:
    missing = []
    for f, conf in schema.get("fields", {}).items():
        if conf.get("required") and (f not in data or data[f] is None):
            missing.append(f)
    return (len(missing) == 0, missing)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
