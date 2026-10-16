"""
============================================================
DAY 35 REVISION SESSION (~10–15 MINUTES)
Topic: Database Normalization, Foreign Keys & Encapsulation
============================================================

Verified Prerequisites: Days 1–34 (Day 34 Normalization & FKs, Day 19 @property Encapsulation)

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
# 1. What is 1NF (atomic columns) vs 2NF (removing partial dependencies) vs 3NF (removing transitive dependencies)?
#
# 2. What happens when you delete a parent row if the foreign key specifies `ON DELETE CASCADE` vs `ON DELETE RESTRICT`?
#
# 3. Why do we use `@property` and a setter in Python instead of allowing direct public attribute mutation?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Implement a `Product` class with a protected attribute `_stock`. Use `@property` for `stock`, and in `@stock.setter`, raise `ValueError` if the new stock is negative.

class Product:
    def __init__(self, name: str, initial_stock: int):
        self.name = name
        if initial_stock < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = initial_stock

    # Implement @property stock and @stock.setter below:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 35 Revision Challenge ---")
    try:
        p = Product("Laptop", 10)
        if not hasattr(p, "stock"):
            print("[!] Property `stock` is not yet implemented.")
            return
        if p.stock != 10:
            print("[-] Test Failed: Initial stock mismatch.")
            return
        p.stock = 5
        if p.stock != 5:
            print("[-] Test Failed: Setter did not update stock.")
            return
        try:
            p.stock = -2
            print("[-] Test Failed: Setter did not raise ValueError on negative stock.")
            return
        except ValueError:
            print("[+] Test Passed: Negative stock correctly raised ValueError.")
    except Exception as e:
        print(f"[-] Test error: {e}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Define a getter method decorated with `@property` and a setter decorated with `@stock.setter`.
# Hint 2: In setter: `if val < 0: raise ValueError(...)` else `self._stock = val`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
class _ReferenceProduct:
    def __init__(self, name: str, initial_stock: int):
        self.name = name
        if initial_stock < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = initial_stock

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, val: int):
        if val < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = val


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
