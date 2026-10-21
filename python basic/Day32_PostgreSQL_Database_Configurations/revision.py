"""
============================================================
DAY 32 REVISION SESSION (~10–15 MINUTES)
Topic: Python Variables, Conditionals, Loops & Pattern Printing
============================================================

Verified Prerequisites: Days 1–3 (Day 1 Variables & Conditionals, Day 2 Loops, Day 3 Pattern Printing)

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
# 1. What is the difference between '=' (assignment) and '==' (equality check), and why does `if 10:` evaluate to True in Python?
#= is for assigning and == for comparing
# 2. What is the difference between `break` (terminates the enclosing loop) and `continue` (skips directly to the next iteration)?
#break means will exit the loop and continue menas skip the if condition meet
# 3. In pattern printing with nested loops, what role does the outer loop play versus the inner loop?
#Outer loop: controls the rows — how many lines are printed.
# Inner loop: controls what happens inside each row — how many characters or numbers appear on that line.

# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `generate_number_triangle(n: int) -> list[str]` which returns a list of strings
# representing a number triangle from 1 up to n.
# Example: generate_number_triangle(4) -> ['1', '12', '123', '1234']

def generate_number_triangle(n: int) -> list[str]:
    """
    Returns a list of strings representing a number triangle from 1 to n.
    Example: n = 4 -> ['1', '12', '123', '1234']
    """
    traigle=[]
    # WRITE YOUR CODE HERE:
    for num in range(1,n+1):
        row=""
        for num2 in range(1,num+1): 
            row=row+str(num2)

        
        traigle.append(row)
    return traigle

# print(generate_number_triangle(3))
    


# # ============================================================
# # VERIFICATION RUNNER (Executes your code without revealing solutions)
# # ============================================================
def run_test():
    print("--- Running Day 32 Revision Challenge ---")
    res1 = generate_number_triangle(4)
    if res1 is None:
        print("[!] Function `generate_number_triangle` is not yet implemented.")
        return
    res2 = generate_number_triangle(1)
    if res1 == ["1", "12", "123", "1234"] and res2 == ["1"]:
        print("[+] Test Passed: Number triangle generated successfully.")
    else:
        print(f"[-] Test Failed: res1={res1}, res2={res2}")

if __name__ == "__main__":
    run_test()


# # ============================================================
# # [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# # ============================================================
# # Hint 1: Use an outer loop iterating `i` from 1 to `n` (inclusive).
# # Hint 2: Build each row using `''.join(str(x) for x in range(1, i + 1))` and append to your results list.


# # ============================================================
# # [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# # ============================================================
# def _reference_solution(n: int) -> list[str]:
#     return ["".join(str(x) for x in range(1, i + 1)) for i in range(1, n + 1)]


# # ============================================================
# # [?] SELF-ASSESSMENT CHECKLIST
# # After completing, mark your result in `revision_tracker.md`:
# # [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# # [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# # [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# # [ ] NOT ATTEMPTED: Not attempted yet.
# # ============================================================
# # 