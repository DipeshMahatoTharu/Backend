"""
============================================================
DAY 32 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: Production Transactional Transfer Script in Python (psycopg2 / DB-API)

In technical architecture interviews, interviewers frequently ask you
to write a raw, production-grade Python database function without an ORM,
demonstrating connection pool checkout, row-level pessimistic locking
(`FOR UPDATE`), atomic commits, safe rollbacks, and guaranteed resource cleanup.

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Write a Python function `safe_bank_transfer` that transfers money between
two accounts in PostgreSQL using a connection pool.

Signature:
def safe_bank_transfer(
    pool: Any, 
    from_acc_id: int, 
    to_acc_id: int, 
    amount: float
) -> bool:

------------------------------------------------------------
2. REQUIREMENTS & DEFENSIVE CHECKLIST:
------------------------------------------------------------
1. Connection Management:
   - Check out a connection from `pool.getconn()`.
   - Wrap the entire operation in a `try...finally` block to GUARANTEE that
     `pool.putconn(conn)` is called, even on fatal exceptions.
2. Concurrency Protection (Pessimistic Locking):
   - Use `SELECT balance FROM accounts WHERE id = %s FOR UPDATE;` to lock
     the sender's row before reading or updating balance.
3. Business Validation:
   - If balance < amount, raise a custom `ValueError("Insufficient funds")`.
4. Transaction Execution:
   - Debit sender account (`UPDATE accounts SET balance = balance - %s WHERE id = %s`).
   - Credit recipient account (`UPDATE accounts SET balance = balance + %s WHERE id = %s`).
   - Insert record into `ledger` table.
   - Call `conn.commit()`.
   - Return True.
5. Error Handling:
   - On ANY database error or exception, catch it, execute `conn.rollback()`,
     log/print the failure, and return False (or re-raise).

============================================================
MY ARCHITECTURAL APPROACH & LOCKING PLAN:
============================================================
Explain your error handling and pool release strategy:

____________________________________________________
____________________________________________________
____________________________________________________

============================================================
MY RAW CODE (No autocomplete! Write on blank paper first):
============================================================

def safe_bank_transfer(pool, from_acc_id, to_acc_id, amount):
    # TODO: Write your raw implementation here
    pass

"""