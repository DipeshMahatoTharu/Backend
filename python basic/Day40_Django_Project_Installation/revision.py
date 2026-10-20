"""
============================================================
DAY 40 REVISION SESSION (~10–15 MINUTES)
Topic: Type Hints, PEP 8, Git Workflows & SQL Fundamentals
============================================================

Verified Prerequisites: Days 25–27 (Day 25 Type Hints, Day 26 Git Collaboration, Day 27 SQL Fundamentals)

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
# 1. What are type hints in Python and why do they enhance developer tooling without causing runtime overhead?
#
# 2. What are the stages of Git tracking: Working Directory -> Staging Area -> Local Repo -> Remote Repo?
#
# 3. What SQL keyword creates a table and defines primary key constraints?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `generate_create_table_sql(table_name: str, schema: dict[str, str]) -> str` generating an SQL CREATE TABLE statement. E.g. `schema = {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT NOT NULL'}` -> `CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL);`.

def generate_create_table_sql(table_name: str, schema: dict[str, str]) -> str:
    """
    Generates CREATE TABLE statement from schema dictionary.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 40 Revision Challenge ---")
    s = {"id": "INTEGER PRIMARY KEY", "email": "TEXT NOT NULL"}
    sql = generate_create_table_sql("users", s)
    if sql is None:
        print("[!] Function `generate_create_table_sql` is not yet implemented.")
        return
    expected = "CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT NOT NULL);"
    if sql.strip() == expected:
        print("[+] Test Passed: DDL SQL string accurately generated.")
    else:
        print(f"[-] Test Failed: Got '{sql}'")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Format each column definition as `f'{col} {col_type}'`.
# Hint 2: Join column definitions with `', '` and return `f'CREATE TABLE {table_name} ({cols});'`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(table_name: str, schema: dict[str, str]) -> str:
    cols = ", ".join(f"{col} {ctype}" for col, ctype in schema.items())
    return f"CREATE TABLE {table_name} ({cols});"


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
