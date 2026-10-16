"""
============================================================
DAY 63 REVISION SESSION (~10–15 MINUTES)
Topic: SOLID Principles & Clean Code Architecture
============================================================

Verified Prerequisites: Days 1–62 (Day 62 Clean Code & SOLID, Days 51–57 DRF Architecture)

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
# 1. What is the Single Responsibility Principle (SRP) and how does it prevent bloated classes and 'god functions'?
#
# 2. What is the Open/Closed Principle (open for extension, closed for modification)?
#
# 3. How does Dependency Inversion allow business services to depend on abstractions rather than concrete database or external API implementations?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Refactor a monolithic billing function into decoupled single-responsibility functions: `calculate_tax(subtotal: float, rate: float) -> float` and `calculate_invoice_total(subtotal: float, tax_rate: float) -> dict` returning `{'subtotal': ..., 'tax': ..., 'total': ...}` rounded to 2 decimals.

def calculate_tax(subtotal: float, rate: float = 0.10) -> float:
    # WRITE CODE HERE:
    pass

def calculate_invoice_total(subtotal: float, tax_rate: float = 0.10) -> dict:
    # WRITE CODE HERE (MUST CALL calculate_tax):
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 63 Revision Challenge ---")
    tax = calculate_tax(100.0, 0.13)
    inv = calculate_invoice_total(100.0, 0.13)
    if tax is None or inv is None:
        print("[!] Functions are not yet implemented.")
        return
    if tax == 13.0 and inv.get("total") == 113.0 and inv.get("tax") == 13.0:
        print("[+] Test Passed: Decoupled single-responsibility billing verified.")
    else:
        print(f"[-] Test Failed: tax={tax}, inv={inv}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: In `calculate_tax`: return `round(subtotal * rate, 2)`.
# Hint 2: In `calculate_invoice_total`: call `calculate_tax(subtotal, tax_rate)`, add to subtotal, round total, and return the dictionary.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution_tax(subtotal: float, rate: float = 0.10) -> float:
    return round(subtotal * rate, 2)

def _reference_solution_invoice(subtotal: float, tax_rate: float = 0.10) -> dict:
    tax = _reference_solution_tax(subtotal, tax_rate)
    return {"subtotal": round(subtotal, 2), "tax": tax, "total": round(subtotal + tax, 2)}


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
