"""
============================================================
DAY 70 REVISION SESSION (~10–15 MINUTES)
Topic: Linux CLI, Production WSGI & Gunicorn Deployment
============================================================

Verified Prerequisites: Day 69 (Production WSGI & Gunicorn)

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
# 1. What is the difference between a development server (`runserver`) and a production WSGI server (`gunicorn`)?
#
# 2. What are workers and threads in Gunicorn and how do you calculate optimal worker counts (`2 * CPU + 1`)?
#
# 3. Why should production Django applications always run with `DEBUG = False` and defined `ALLOWED_HOSTS`?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `parse_env_file_string(env_text: str) -> dict[str, str]` which parses a multi-line string in `.env` format, ignoring empty lines and comments (`#`), and stripping surrounding quotes from values.

def parse_env_file_string(env_text: str) -> dict[str, str]:
    """
    Parses key=value pairs into a Python dictionary.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 70 Revision Challenge ---")
    sample = """
    # Database config
    DB_NAME=production_db
    DB_PORT="5432"
    DEBUG=False
    """
    res = parse_env_file_string(sample)
    if res is None:
        print("[!] Function `parse_env_file_string` is not yet implemented.")
        return
    if res.get("DB_NAME") == "production_db" and res.get("DB_PORT") == "5432" and res.get("DEBUG") == "False":
        print("[+] Test Passed: Environment string parser confirmed.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Split into lines, strip each line, and ignore lines starting with '#' or empty lines.
# Hint 2: Split on the first '=' with `line.split('=', 1)`. Strip quotes using `val.strip('"').strip("'")`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(env_text: str) -> dict[str, str]:
    out = {}
    for line in env_text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
