"""
============================================================
DAY 36 REVISION SESSION (~10–15 MINUTES)
Topic: OOP Classes, __init__, Single & Multiple Inheritance
============================================================

Verified Prerequisites: Days 13–15 (Day 13 Classes & Objects, Day 14 Single Inheritance, Day 15 Multiple Inheritance)

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
# 1. What is the purpose of `self` in Python instance methods and what does `__init__` do?
#
# 2. What does `super().__init__(...)` do when initializing a derived subclass?
#
# 3. In multiple inheritance, what is Python's Method Resolution Order (MRO)?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Implement a base class `Employee(name: str, salary: float)` and a subclass `Developer(name: str, salary: float, language: str)`. Subclass must have `get_profile() -> str` returning: `'{name} codes in {language} for ${salary}'`.

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

class Developer(Employee):
    # Complete Developer class inheriting from Employee:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 36 Revision Challenge ---")
    try:
        dev = Developer("Alice", 75000.0, "Python")
        if not hasattr(dev, "get_profile"):
            print("[!] Method `get_profile` is not yet implemented.")
            return
        msg = dev.get_profile()
        if msg == "Alice codes in Python for $75000.0" and isinstance(dev, Employee):
            print("[+] Test Passed: OOP Inheritance and method dispatch verified.")
        else:
            print(f"[-] Test Failed: Got '{msg}'")
    except Exception as e:
        print(f"[!] Test error: {e}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: In `Developer.__init__`, call `super().__init__(name, salary)` and set `self.language = language`.
# Hint 2: In `get_profile`, return `f'{self.name} codes in {self.language} for ${self.salary}'`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
class _RefEmployee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

class _RefDeveloper(_RefEmployee):
    def __init__(self, name: str, salary: float, language: str):
        super().__init__(name, salary)
        self.language = language

    def get_profile(self) -> str:
        return f"{self.name} codes in {self.language} for ${self.salary}"


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
