"""
============================================================
DAY 33 DEBUGGING — INDEX INVALIDATION & QUERY TRAPS
============================================================

Learn to identify and fix silent bugs where indexes exist in the schema,
but database query planners are forced to ignore them and perform full table scans!

Your mission:
Restore the broken indexing strategies below so all queries use index searches.
"""

import sqlite3

def setup_debugging_db(conn: sqlite3.Connection):
    """Sets up tables with sample data and baseline indexes."""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("DROP TABLE IF EXISTS products;")
    
    # 1. Users table
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            signup_year INTEGER NOT NULL,
            is_active INTEGER NOT NULL DEFAULT 1
        );
    """)
    cursor.execute("CREATE INDEX idx_users_email ON users (email);")
    cursor.execute("CREATE INDEX idx_users_year ON users (signup_year);")
    
    # Seed sample users
    users = [(i, f"user_{i}", f"User_{i}@Example.com", 2024, 1) for i in range(1000)]
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?);", users)
    
    # 2. Products table
    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            sku TEXT NOT NULL,
            name TEXT NOT NULL,
            price REAL NOT NULL
        );
    """)
    cursor.execute("CREATE INDEX idx_products_sku ON products (sku);")
    
    # Seed sample products
    products = [(i, f"PROD-{i:05d}", f"Item {i}", 19.99) for i in range(1000)]
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?);", products)
    
    conn.commit()


# =====================================================================
# BUGGY SCENARIO 1: The Function-Wrapping Index Invalidation
# =====================================================================
# Problem: You want a case-insensitive search for users by email.
# The table has an index on `email` (`idx_users_email`).
# But this query performs a full sequential SCAN users! Why?
def buggy_case_insensitive_search(conn: sqlite3.Connection, search_email: str):
    """
    BUG DEMO:
    Wrapping the indexed column inside LOWER(email) prevents the database
    from using `idx_users_email` because that index stores raw original values.
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, username, email 
        FROM users 
        WHERE LOWER(email) = LOWER(?);
    """, (search_email,))
    return cursor.fetchall()


def fix_case_insensitive_indexing(conn: sqlite3.Connection):
    """
    YOUR TASK (Scenario 1):
    Create an expression / functional index on `users` so that queries filtering
    by `LOWER(email)` can utilize a B-Tree index instead of a full table scan.
    
    HINT:
    In PostgreSQL and SQLite, you can create an index directly on an expression:
    `CREATE INDEX idx_users_lower_email ON users (LOWER(email));`
    """
    # TODO: Implement the expression index creation and commit to conn
    cursor=conn.cursor()
    cursor.execute("""CREATE INDEX IF NOT EXISTS idex_users_lower_email 
                   ON users(LOWER(email)); 
                    
                   """)
    conn.commit()

# =====================================================================
# BUGGY SCENARIO 2: Prefix Search Invalidation (SUBSTR vs Trailing Wildcard)
# =====================================================================
# Problem: A developer needs to search products by their SKU prefix (e.g., 'PROD-').
# The table has an index on `sku` (`idx_products_sku`).
# But the implementation below uses SUBSTR(), which causes a full table scan!
def buggy_sku_prefix_search(conn: sqlite3.Connection, prefix: str):
    """
    BUG DEMO:
    Using SUBSTR() on `sku` invalidates the B-Tree index traversal.
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, sku, name 
        FROM products 
        WHERE SUBSTR(sku, 1, ?) = ?;
    """, (len(prefix), prefix))
    return cursor.fetchall()


def fixed_sku_prefix_search(conn: sqlite3.Connection, prefix: str):
    """
    YOUR TASK (Scenario 2):
    Rewrite this query so that it retrieves all products whose SKU begins with `prefix`,
    while allowing the database planner to use `idx_products_sku`.
    
    HINT:
    A B-Tree index stores keys in alphabetical order. A trailing wildcard like
    `sku LIKE ? || '%'` allows the engine to jump directly to the prefix range!
    """
    # TODO: Implement index-friendly prefix search query and return cursor.fetchall()
    cursor=conn.cursor()
    cursor.execute("""SELECT id ,sku,name
                   FROM products
                   WHERE sku LIKE ?
                   """,(prefix +'%',))
    
    return cursor.fetchall()



# =====================================================================
# CONCEPTUAL SCENARIO 3: Implicit Type Coercion Trap
# =====================================================================
# In PostgreSQL, phone_number is VARCHAR(20) and indexed.
# A developer queries:
#   SELECT * FROM users WHERE phone_number = 9860793587; (Passed as an INTEGER!)
#
# QUESTION: Why does PostgreSQL execute a Sequential Scan instead of using the index?
#
# YOUR EXPLANATION / NOTES:
#The `phone_number` column is stored as `VARCHAR`, but the query passes an integer. 
# PostgreSQL generally cannot compare these types directly, so the query may raise an operator error.
# To compare correctly and allow the index to be used, pass the phone number as a string, for example `'9860793587'`.
# (Hint: Think about which data type takes precedence when casting types)


# =====================================================================
# VERIFICATION RUNNER
# =====================================================================
def run_debugging_checks():
    conn = sqlite3.connect(":memory:")
    setup_debugging_db(conn)
    cursor = conn.cursor()
    
    print("=== SCENARIO 1: Functional / Expression Index ===")
    cursor.execute("EXPLAIN QUERY PLAN SELECT id FROM users WHERE LOWER(email) = 'user_50@example.com';")
    plan_before = cursor.fetchall()
    print(f"[*] Plan Before Fix: {plan_before}")
    
    fix_case_insensitive_indexing(conn)
    
    cursor.execute("EXPLAIN QUERY PLAN SELECT id FROM users WHERE LOWER(email) = 'user_50@example.com';")
    plan_after = cursor.fetchall()
    
    is_scenario_1_fixed = any("idx_users_lower_email" in str(step) for step in plan_after)
    if is_scenario_1_fixed:
        print("[+] SUCCESS: Scenario 1 fixed! Expression index `idx_users_lower_email` is active.")
        print(f"    Plan After Fix: {plan_after}\n")
    else:
        print("[-] NOT FIXED YET: Scenario 1 still performs a full table SCAN.")
        print("    Complete `fix_case_insensitive_indexing(conn)` to resolve.\n")
        
    print("=== SCENARIO 2: Index-Friendly Prefix Search ===")
    cursor.execute("EXPLAIN QUERY PLAN SELECT id, sku, name FROM products WHERE SUBSTR(sku, 1, 5) = 'PROD-';")
    buggy_plan = cursor.fetchall()
    print(f"[*] Buggy Plan (SUBSTR): {buggy_plan}")
    
    fixed_res = fixed_sku_prefix_search(conn, "PROD-")
    if fixed_res is None:
        print("[-] NOT FIXED YET: Scenario 2 `fixed_sku_prefix_search` returned None.")
        print("    Implement the trailing wildcard query to utilize `idx_products_sku`.\n")
    else:
        cursor.execute("EXPLAIN QUERY PLAN SELECT id, sku, name FROM products WHERE sku LIKE 'PROD-%';")
        fixed_plan = cursor.fetchall()
        is_scenario_2_fixed = any("idx_products_sku" in str(step) for step in fixed_plan) and len(fixed_res) > 0
        if is_scenario_2_fixed:
            print(f"[+] SUCCESS: Scenario 2 fixed! Retrieved {len(fixed_res)} rows.")
            print(f"    Fixed Plan: {fixed_plan}\n")
        else:
            print(f"[-] Check query logic: Retrieved {len(fixed_res)} rows but plan needs index traversal.\n")

    conn.close()


if __name__ == "__main__":
    run_debugging_checks()
