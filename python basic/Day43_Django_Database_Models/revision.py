"""
============================================================
DAY 43 REVISION SESSION (~10–15 MINUTES)
Topic: Database Normalization, ACID/MVCC Concurrency & Advanced Data Types
============================================================

Verified Prerequisites: Days 34–36 (Day 34 Normalization, Day 35 Locking & MVCC, Day 36 PostgreSQL JSONB)

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
# 1. What is the difference between 1NF, 2NF, and 3NF database normalization?
#
# 2. How does `SELECT ... FOR UPDATE` row locking prevent concurrent lost update anomalies?
#
# 3. When is storing data in a PostgreSQL `JSONB` column appropriate versus normalized relational tables?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `atomic_deduct_stock(conn, product_id: int, qty: int) -> bool` executing conditional atomic update: `UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?;`. Commit and return True if `cur.rowcount > 0`, otherwise rollback and return False.

def atomic_deduct_stock(conn, product_id: int, qty: int) -> bool:
    """
    Conditional atomic update. Returns True if stock deducted, False if insufficient stock.
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

    print("--- Running Day 43 Revision Challenge ---")
    r1 = atomic_deduct_stock(conn, 1, 10)
    if r1 is None:
        print("[!] Function `atomic_deduct_stock` is not yet implemented.")
        conn.close()
        return
    r2 = atomic_deduct_stock(conn, 1, 10) # should fail (only 5 remaining)
    cur.execute("SELECT stock FROM products WHERE id = 1;")
    rem = cur.fetchone()[0]
    if r1 is True and r2 is False and rem == 5:
        print("[+] Test Passed: Concurrency-safe atomic deduction verified.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, rem={rem}")
    conn.close()

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Execute the parameterized UPDATE statement and inspect `cur.rowcount`.
# Hint 2: If `cur.rowcount > 0`: `conn.commit()` and return True; else `conn.rollback()` and return False.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(conn, product_id: int, qty: int) -> bool:
    cur = conn.cursor()
    cur.execute("UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?;", (qty, product_id, qty))
    if cur.rowcount > 0:
        conn.commit()
        return True
    conn.rollback()
    return False


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
