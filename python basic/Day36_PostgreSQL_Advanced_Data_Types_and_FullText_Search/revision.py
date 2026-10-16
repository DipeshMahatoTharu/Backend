"""
============================================================
DAY 36 REVISION SESSION (~10–15 MINUTES)
Topic: Concurrency Anomalies, Row Locking & SQL Subqueries
============================================================

Verified Prerequisites: Days 1–35 (Day 35 Concurrency & ACID, Day 31 SQL Subqueries)

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
# 1. What is a 'Lost Update' anomaly and how does `SELECT ... FOR UPDATE` prevent it?
#
# 2. What are the four ACID properties, and which one guarantees that intermediate states are never visible?
#
# 3. Why is an atomic conditional update like `UPDATE accounts SET balance = balance - 50 WHERE id = 1 AND balance >= 50;` safer than reading first and writing later?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `atomic_deduct_stock(conn, product_id, qty)` executing: `UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?`. Return True if rowcount > 0, False otherwise.

def atomic_deduct_stock(conn, product_id: int, qty: int) -> bool:
    """
    Executes conditional atomic update.
    Returns True if stock was deducted, False if insufficient stock or product not found.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    import sqlite3
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, stock INTEGER);")
    cur.execute("INSERT INTO products VALUES (1, 15);")
    conn.commit()

    print("--- Running Day 36 Revision Challenge ---")
    r1 = atomic_deduct_stock(conn, 1, 10)
    if r1 is None:
        print("[!] Function `atomic_deduct_stock` is not yet implemented.")
        conn.close()
        return

    r2 = atomic_deduct_stock(conn, 1, 10) # should fail (only 5 left)
    cur.execute("SELECT stock FROM products WHERE id = 1;")
    remaining = cur.fetchone()[0]

    if r1 is True and r2 is False and remaining == 5:
        print("[+] Test Passed: Atomic conditional update handled correctly.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, remaining={remaining}")
    conn.close()

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Run the parameterized UPDATE statement and check `cur.rowcount`.
# Hint 2: If `cur.rowcount > 0`: `conn.commit()` and return True; else return False.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(conn, product_id: int, qty: int) -> bool:
    cur = conn.cursor()
    cur.execute("UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?;", (qty, product_id, qty))
    conn.commit()
    return cur.rowcount > 0


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
