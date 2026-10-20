"""
============================================================
DAY 38 REVISION SESSION (~10–15 MINUTES)
Topic: Properties, OOP Checkpoint & Advanced Data Structures
============================================================

Verified Prerequisites: Days 19–21 (Day 19 Properties & Abstraction, Day 20 OOP Checkpoint, Day 21 Data Structures)

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
# 1. How does `@property` enable getter access while hiding direct field mutation?
#
# 2. What is the difference between a Python `set` (unique elements, fast hashing) and a `list`?
#
# 3. How do you define a setter using `@<property_name>.setter` in Python?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Implement `BankAccount` with protected `_balance: float`. Implement `@property def balance` and `@balance.setter` which raises `ValueError('Deposit must be non-negative')` if new balance < 0.

class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance

    # Implement balance property and setter below:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 38 Revision Challenge ---")
    try:
        acc = BankAccount(100.0)
        if not hasattr(acc, "balance"):
            print("[!] Property `balance` is not yet implemented.")
            return
        if acc.balance != 100.0:
            print("[-] Test Failed: Getter returned unexpected value.")
            return
        acc.balance = 150.0
        try:
            acc.balance = -50.0
            print("[-] Test Failed: Setter did not raise ValueError on negative balance.")
            return
        except ValueError:
            pass
        if acc.balance == 150.0:
            print("[+] Test Passed: BankAccount property encapsulation verified.")
    except Exception as e:
        print(f"[!] Test error: {e}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Decorate getter with `@property def balance(self): return self._balance`.
# Hint 2: Decorate setter with `@balance.setter def balance(self, val): if val < 0: raise ValueError(...) else: self._balance = val`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
class _RefBankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, val: float):
        if val < 0:
            raise ValueError("Deposit must be non-negative")
        self._balance = val


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
