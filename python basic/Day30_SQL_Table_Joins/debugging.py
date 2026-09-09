# Day 30 Debugging — Cartesian Products, LEFT JOIN Traps & Duplicate Rows

import sqlite3

# =====================================================================
# BUGGY SCENARIO 1: The Accidental Cartesian Product (Missing ON Condition)
# =====================================================================
# Goal: Join customers and their active subscriptions.
# Problem: The developer used comma syntax without a WHERE condition, or
# omitted the ON clause.
# If there are 1,000 customers and 1,000 subscriptions, the database
# generates 1,000,000 rows, exhausting memory and hanging the connection!

def buggy_get_customer_subscriptions(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # DISASTER: Cartesian Product (CROSS JOIN) due to missing ON condition!
    cursor.execute("""
        SELECT c.name, s.plan_name 
        FROM customers c 
        JOIN subscriptions s;
    """)
    return cursor.fetchall()

# ---------------------------------------------------------------------
# QUESTION: Why must every JOIN always specify an explicit ON predicate?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite with explicit ON c.id = s.customer_id.
# ---------------------------------------------------------------------
def fixed_get_customer_subscriptions(conn: sqlite3.Connection):
    pass


# =====================================================================
# BUGGY SCENARIO 2: Breaking a LEFT JOIN with a WHERE Filter
# =====================================================================
# Goal: List ALL customers, along with their 'VIP' status orders if they have any.
# Customers with no VIP orders should still appear with order_id = NULL.
# Problem: The developer wrote `WHERE o.order_type = 'VIP'`.
# Since NULL = 'VIP' evaluates to UNKNOWN, all customers without VIP orders
# are discarded, accidentally converting the query into an INNER JOIN!

def buggy_get_all_customers_vip(conn: sqlite3.Connection):
    cursor = conn.cursor()
    # BUG: WHERE clause discards NULL rows produced by LEFT JOIN!
    cursor.execute("""
        SELECT c.name, o.id AS order_id
        FROM customers c
        LEFT JOIN orders o ON c.id = o.customer_id
        WHERE o.order_type = 'VIP';
    """)
    return cursor.fetchall()

# ---------------------------------------------------------------------
# QUESTION: Why does moving the filter to the ON clause fix this?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the query placing the order_type filter in the ON clause.
# ---------------------------------------------------------------------
def fixed_get_all_customers_vip(conn: sqlite3.Connection):
    pass


# =====================================================================
# BUGGY SCENARIO 3: Duplicate Row Inflation in One-to-Many Aggregations
# =====================================================================
# Goal: Calculate total customer account balance and total order spend.
# Problem: Customer has 2 bank accounts ($100 each = $200 total) and 3 orders ($50 each = $150 total).
# Joining both accounts and orders produces 2 x 3 = 6 rows!
# SUM(accounts.balance) calculates $600 instead of $200!
# SUM(orders.total) calculates $300 instead of $150!

def buggy_customer_financial_summary(conn: sqlite3.Connection, customer_id: int):
    cursor = conn.cursor()
    # BUG: Fan-out multiplication causes massive inflation of sums!
    cursor.execute("""
        SELECT 
            c.id, 
            SUM(a.balance) AS total_bank_balance,
            SUM(o.amount) AS total_order_spend
        FROM customers c
        LEFT JOIN accounts a ON c.id = a.customer_id
        LEFT JOIN orders o ON c.id = o.customer_id
        WHERE c.id = ?
        GROUP BY c.id;
    """, (customer_id,))
    return cursor.fetchone()

# ---------------------------------------------------------------------
# QUESTION: How do separate subqueries or CTEs prevent Cartesian fan-out?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite using subqueries to calculate sums independently before joining.
# ---------------------------------------------------------------------
def fixed_customer_financial_summary(conn: sqlite3.Connection, customer_id: int):
    pass