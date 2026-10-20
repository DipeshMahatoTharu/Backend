"""
============================================================
DAY 41 REVISION SESSION (~10–15 MINUTES)
Topic: SQL CRUD Operations, Aggregations & Table Joins
============================================================

Verified Prerequisites: Days 28–30 (Day 28 SQL CRUD, Day 29 Aggregation & Grouping, Day 30 Table Joins)

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
# 1. What is the difference between an INNER JOIN and a LEFT JOIN in SQL?
#
# 2. Why must all non-aggregated SELECT columns appear in the GROUP BY clause?
#
# 3. What is the difference between WHERE (row filter) and HAVING (group filter)?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `calculate_customer_totals(conn) -> list[tuple[str, float]]` querying an in-memory SQLite database to compute total order amount per customer using an INNER JOIN and SUM(amount) GROUP BY customer name, sorted by total descending.

import sqlite3

def calculate_customer_totals(conn: sqlite3.Connection) -> list[tuple[str, float]]:
    """
    Executes SELECT c.name, SUM(o.amount) FROM customers c JOIN orders o ON c.id = o.customer_id GROUP BY c.name ORDER BY 2 DESC;
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
    cur.execute("CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);")
    cur.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL);")
    cur.execute("INSERT INTO customers VALUES (1, 'Alice'), (2, 'Bob');")
    cur.execute("INSERT INTO orders VALUES (101, 1, 50.0), (102, 1, 75.0), (103, 2, 20.0);")
    conn.commit()

    print("--- Running Day 41 Revision Challenge ---")
    res = calculate_customer_totals(conn)
    if res is None:
        print("[!] Function `calculate_customer_totals` is not yet implemented.")
        conn.close()
        return
    if res == [("Alice", 125.0), ("Bob", 20.0)]:
        print("[+] Test Passed: SQL JOIN and GROUP BY aggregation calculated accurately.")
    else:
        print(f"[-] Test Failed: Got {res}")
    conn.close()

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Write query: `SELECT c.name, SUM(o.amount) FROM customers c JOIN orders o ON c.id = o.customer_id GROUP BY c.name ORDER BY SUM(o.amount) DESC`.
# Hint 2: Execute query with `conn.cursor()`, run `.fetchall()`, and return the list of tuples.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
import sqlite3

def _reference_solution(conn: sqlite3.Connection) -> list[tuple[str, float]]:
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, SUM(o.amount)
        FROM customers c
        JOIN orders o ON c.id = o.customer_id
        GROUP BY c.name
        ORDER BY SUM(o.amount) DESC;
    """)
    return cur.fetchall()


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
