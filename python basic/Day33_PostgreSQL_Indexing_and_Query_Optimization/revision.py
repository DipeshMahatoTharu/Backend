"""
============================================================
DAY 33 REVISION SESSION (~10–15 MINUTES)
Topic: Function Basics, Default Arguments, *args, **kwargs & Loop Practice
============================================================

Verified Prerequisites: Days 4–6 (Day 4 Functions, Day 5 Advanced Functions, Day 6 Function/Loop Practice)

------------------------------------------------------------
[!] THE 15-MINUTE ATTEMPT RULE
------------------------------------------------------------
1. Start your 15-minute timer before looking at any hints or external resources.
2. Read the recall questions and coding challenge below.
3. Attempt to solve the challenge using your own reasoning and verified notes.
4. If stuck after ~10 minutes, scroll to the HINTS section.
5. If still stuck after ~15 minutes, pause and ask your AI mentor for a targeted clue.
6. After receiving help, type out and solve the problem independently.
7. Record your honest outcome in `revision_tracker.md`!
"""

# ============================================================
# PART 1: RAPID RECALL (2–3 MINUTES)
# Answer these questions in your head or in comments:
# ============================================================
# 1. What value does a Python function return by default if no explicit `return` statement is executed?
#
# 2. In Python function parameters, what is the difference between `*args` (tuple of variable positional args) and `**kwargs` (dict of keyword args)?
#
# 3. Why is using a mutable default argument like `def add_item(item, items=[]):` considered a dangerous bug in Python?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `format_user_summary(name: str, *tags, **metadata) -> dict` returning a summary dictionary with keys:
# 'name' (str), 'tags' (list), 'metadata' (dict), and 'tag_count' (int).

dict={}
def format_user_summary(name: str, *tags, **metadata) -> dict:
    """
    Formats user summary dictionary.
    Returns: {'name': name, 'tags': list(tags), 'metadata': metadata, 'tag_count': len(tags)}
    """
    # WRITE YOUR CODE HERE:
    return {"name":name ,
            "tags":list(tags) ,
            "metadata":metadata,
            "tag_count":len(tags)            
            }

# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 33 Revision Challenge ---")
    res = format_user_summary("Alice", "python", "backend", role="developer", level="junior")
    if res is None:
        print("[!] Function `format_user_summary` is not yet implemented.")
        return
    if (res.get("name") == "Alice" and res.get("tags") == ["python", "backend"] and
        res.get("tag_count") == 2 and res.get("metadata") == {"role": "developer", "level": "junior"}):
        print("[+] Test Passed: Function signature *args and **kwargs handled cleanly.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: `*tags` arrives as a tuple. Convert it to a list using `list(tags)`.
# Hint 2: `**metadata` is already passed in as a dictionary.
# Hint 3: Construct and return the dictionary: `{'name': name, 'tags': list(tags), 'metadata': metadata, 'tag_count': len(tags)}`.


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
