"""
generate_and_audit_revisions.py
-------------------------------
Regenerates all revision.py files for Days 32–75 starting from Day 1:
- Day 32: Days 1, 2, 3
- Day 33: Days 4, 5, 6
- Day 34: Days 7, 8, 9
- Day 35: Days 10, 11, 12
- Day 36: Days 13, 14, 15
- Day 37: Days 16, 17, 18
- Day 38: Days 19, 20, 21
- Day 39: Days 22, 23, 24
- Day 40: Days 25, 26, 27
- Day 41: Days 28, 29, 30
- Day 42: Days 31, 32, 33
- Day 43: Days 34, 35, 36
- Day 44: Days 37, 38, 39
- Day 45: Days 40, 41, 42
- Day 46: Days 43, 44
- Day 47: Days 45, 46
- Day 48: Day 47
- Day 49: Day 48
- Day 50 to 75: Days 49 to 74 (1 curriculum day per revision day)

All 44 revision.py files include:
- 3 recall questions
- 1 targeted coding challenge
- Safe test runner (run_test()) with graceful unimplemented check
- Hint 1 (conceptual clue) & Hint 2 (direct hint/pointer)
- Hidden reference solution
- Self-assessment checklist (4 honest outcomes)
- 15-minute attempt rule
"""

import os
import re

DAYS_DATA = {
    32: {
        "topic": "Python Variables, Conditionals, Loops & Pattern Printing",
        "prereqs": "Days 1–3 (Day 1 Variables & Conditionals, Day 2 Loops, Day 3 Pattern Printing)",
        "q1": "What is the difference between '=' (assignment) and '==' (equality check), and why does `if 10:` evaluate to True in Python?",
        "q2": "What is the difference between `break` (terminates the enclosing loop) and `continue` (skips directly to the next iteration)?",
        "q3": "In pattern printing with nested loops, what role does the outer loop play versus the inner loop?",
        "desc": "Write `generate_number_triangle(n: int) -> list[str]` which returns a list of strings representing a number triangle from 1 up to n.\\n# Example: generate_number_triangle(4) -> ['1', '12', '123', '1234']",
        "stub": '''def generate_number_triangle(n: int) -> list[str]:
    """
    Returns a list of strings representing a number triangle from 1 to n.
    Example: n = 4 -> ['1', '12', '123', '1234']
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 32 Revision Challenge ---")
    res1 = generate_number_triangle(4)
    if res1 is None:
        print("[!] Function `generate_number_triangle` is not yet implemented.")
        return
    res2 = generate_number_triangle(1)
    if res1 == ["1", "12", "123", "1234"] and res2 == ["1"]:
        print("[+] Test Passed: Number triangle generated successfully.")
    else:
        print(f"[-] Test Failed: res1={res1}, res2={res2}")''',
        "hint1": "Use an outer loop iterating `i` from 1 to `n` (inclusive).",
        "hint2": "Build each row using `''.join(str(x) for x in range(1, i + 1))` and append to your results list.",
        "sol": '''def _reference_solution(n: int) -> list[str]:
    return ["".join(str(x) for x in range(1, i + 1)) for i in range(1, n + 1)]'''
    },
    33: {
        "topic": "Function Basics, Default Arguments, *args, **kwargs & Loop Practice",
        "prereqs": "Days 4–6 (Day 4 Functions, Day 5 Advanced Functions, Day 6 Function/Loop Practice)",
        "q1": "What value does a Python function return by default if no explicit `return` statement is executed?",
        "q2": "In Python function parameters, what is the difference between `*args` (tuple of variable positional args) and `**kwargs` (dict of keyword args)?",
        "q3": "Why is using a mutable default argument like `def add_item(item, items=[]):` considered a dangerous bug in Python?",
        "desc": "Write `format_user_summary(name: str, *tags, **metadata) -> dict` returning a summary dictionary with keys: 'name', 'tags' (list), 'metadata' (dict), and 'tag_count' (int).",
        "stub": '''def format_user_summary(name: str, *tags, **metadata) -> dict:
    """
    Formats user summary dictionary.
    Returns: {'name': name, 'tags': list(tags), 'metadata': metadata, 'tag_count': len(tags)}
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 33 Revision Challenge ---")
    res = format_user_summary("Alice", "python", "backend", role="developer", level="junior")
    if res is None:
        print("[!] Function `format_user_summary` is not yet implemented.")
        return
    if (res.get("name") == "Alice" and res.get("tags") == ["python", "backend"] and
        res.get("tag_count") == 2 and res.get("metadata") == {"role": "developer", "level": "junior"}):
        print("[+] Test Passed: Function signature *args and **kwargs handled cleanly.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "`*tags` arrives as a tuple. Convert it to a list using `list(tags)`.",
        "hint2": "Construct and return the dictionary: `{'name': name, 'tags': list(tags), 'metadata': metadata, 'tag_count': len(tags)}`.",
        "sol": '''def _reference_solution(name: str, *tags, **metadata) -> dict:
    return {"name": name, "tags": list(tags), "metadata": metadata, "tag_count": len(tags)}'''
    },
    34: {
        "topic": "Lists, List Conditions, Slicing & Dictionaries",
        "prereqs": "Days 7–9 (Day 7 Lists, Day 8 List Operations, Day 9 Dictionaries)",
        "q1": "What is the algorithmic time complexity of checking if a key exists in a Python dict (O(1)) vs an item in an unsorted list (O(n))?",
        "q2": "How does Python list slice step syntax `items[::-1]` reverse a sequence?",
        "q3": "Why is `dict.get(key, default)` preferred over direct bracket indexing `dict[key]` when keys may be absent?",
        "desc": "Write `count_word_frequencies(words: list[str]) -> dict[str, int]` that normalizes all words to lowercase and counts the occurrence of each word in a dictionary.",
        "stub": '''def count_word_frequencies(words: list[str]) -> dict[str, int]:
    """
    Counts frequency of each word normalized to lowercase.
    Example: ['Python', 'Django', 'python'] -> {'python': 2, 'django': 1}
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 34 Revision Challenge ---")
    words = ["Python", "Django", "python", "API", "api", "Python"]
    res = count_word_frequencies(words)
    if res is None:
        print("[!] Function `count_word_frequencies` is not yet implemented.")
        return
    if res.get("python") == 3 and res.get("django") == 1 and res.get("api") == 2:
        print("[+] Test Passed: Word frequency dictionary correctly aggregated.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Iterate through words, calling `.lower()` on each word.",
        "hint2": "Use `counts[w] = counts.get(w, 0) + 1` to accumulate counts in a loop.",
        "sol": '''def _reference_solution(words: list[str]) -> dict[str, int]:
    counts = {}
    for w in words:
        lw = w.lower()
        counts[lw] = counts.get(lw, 0) + 1
    return counts'''
    },
    35: {
        "topic": "Tuples, Exception Handling & File Safety",
        "prereqs": "Days 10–12 (Day 10 Revision, Day 11 Tuples, Day 12 Exceptions & Files)",
        "q1": "Why are tuples immutable while lists are mutable, and why does this allow tuples to be used as dictionary keys?",
        "q2": "What is the difference between catching a specific exception (e.g. `except ValueError:`) versus bare `except:`?",
        "q3": "What does a `finally` block guarantee in Python exception handling?",
        "desc": "Write `safe_parse_record(raw_record: tuple) -> tuple[bool, dict | str]` that takes a tuple `(id_val, name_val, age_val)`. Ensure tuple length is 3 and convert `id` and `age` to `int`. Return `(True, {'id': int, 'name': str, 'age': int})` or `(False, 'Parsing failed')` if any error occurs.",
        "stub": '''def safe_parse_record(raw_record: tuple) -> tuple[bool, dict | str]:
    """
    Safely parses (id_val, name_val, age_val).
    Returns (True, dict) or (False, "Parsing failed").
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 35 Revision Challenge ---")
    res1 = safe_parse_record(("101", "Alice", "24"))
    if res1 is None:
        print("[!] Function `safe_parse_record` is not yet implemented.")
        return
    ok1, val1 = res1
    ok2, val2 = safe_parse_record(("bad_id", "Bob", "30"))
    ok3, val3 = safe_parse_record(("102", "Carol")) # wrong length
    if ok1 is True and val1 == {"id": 101, "name": "Alice", "age": 24} and ok2 is False and ok3 is False:
        print("[+] Test Passed: Safe record parsing with exception handling confirmed.")
    else:
        print(f"[-] Test Failed: r1={res1}, ok2={ok2}, ok3={ok3}")''',
        "hint1": "Check `if not isinstance(raw_record, tuple) or len(raw_record) != 3: return False, 'Parsing failed'`.",
        "hint2": "Wrap conversions `int(raw_record[0])` and `int(raw_record[2])` in a `try...except (ValueError, TypeError):` block.",
        "sol": '''def _reference_solution(raw_record: tuple) -> tuple[bool, dict | str]:
    if not isinstance(raw_record, tuple) or len(raw_record) != 3:
        return False, "Parsing failed"
    try:
        return True, {
            "id": int(raw_record[0]),
            "name": str(raw_record[1]),
            "age": int(raw_record[2])
        }
    except (ValueError, TypeError):
        return False, "Parsing failed"'''
    },
    36: {
        "topic": "OOP Classes, __init__, Single & Multiple Inheritance",
        "prereqs": "Days 13–15 (Day 13 Classes & Objects, Day 14 Single Inheritance, Day 15 Multiple Inheritance)",
        "q1": "What is the purpose of `self` in Python instance methods and what does `__init__` do?",
        "q2": "What does `super().__init__(...)` do when initializing a derived subclass?",
        "q3": "In multiple inheritance, what is Python's Method Resolution Order (MRO)?",
        "desc": "Implement a base class `Employee(name: str, salary: float)` and a subclass `Developer(name: str, salary: float, language: str)`. Subclass must have `get_profile() -> str` returning: `'{name} codes in {language} for ${salary}'`.",
        "stub": '''class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

class Developer(Employee):
    # Complete Developer class inheriting from Employee:
    pass''',
        "runner": '''def run_test():
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
        print(f"[!] Test error: {e}")''',
        "hint1": "In `Developer.__init__`, call `super().__init__(name, salary)` and set `self.language = language`.",
        "hint2": "In `get_profile`, return `f'{self.name} codes in {self.language} for ${self.salary}'`.",
        "sol": '''class _RefEmployee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

class _RefDeveloper(_RefEmployee):
    def __init__(self, name: str, salary: float, language: str):
        super().__init__(name, salary)
        self.language = language

    def get_profile(self) -> str:
        return f"{self.name} codes in {self.language} for ${self.salary}"'''
    },
    37: {
        "topic": "Encapsulation, Polymorphism & Abstract Base Classes",
        "prereqs": "Days 16–18 (Day 16 Encapsulation, Day 17 Polymorphism, Day 18 Abstraction & ABC)",
        "q1": "What is the convention for protected attributes (`_name`) vs private attributes (`__name` with name mangling)?",
        "q2": "What is polymorphism in Python (treating different objects via the same interface)?",
        "q3": "Why cannot an Abstract Base Class (inheriting `abc.ABC` with `@abstractmethod`) be instantiated directly?",
        "desc": "Implement abstract class `Notification(ABC)` with `@abstractmethod def send(recipient: str, msg: str) -> str`. Implement concrete subclasses `EmailNotification` returning `'Email to {recipient}: {msg}'` and `SMSNotification` returning `'SMS to {recipient}: {msg}'`.",
        "stub": '''from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, msg: str) -> str:
        pass

class EmailNotification(Notification):
    # WRITE CODE HERE:
    pass

class SMSNotification(Notification):
    # WRITE CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 37 Revision Challenge ---")
    try:
        e = EmailNotification()
        s = SMSNotification()
        r1 = e.send("alice@mail.com", "Hello")
        r2 = s.send("9841000000", "OTP 1234")
        if r1 is None or r2 is None:
            print("[!] Methods are not yet implemented.")
            return
        if r1 == "Email to alice@mail.com: Hello" and r2 == "SMS to 9841000000: OTP 1234":
            print("[+] Test Passed: Polymorphic Notification subclasses confirmed.")
        else:
            print(f"[-] Test Failed: r1='{r1}', r2='{r2}'")
    except Exception as e:
        print(f"[!] Test error: {e}")''',
        "hint1": "Each subclass overrides `send(self, recipient: str, msg: str) -> str`.",
        "hint2": "EmailNotification returns `f'Email to {recipient}: {msg}'`; SMSNotification returns `f'SMS to {recipient}: {msg}'`.",
        "sol": '''from abc import ABC, abstractmethod

class _RefNotification(ABC):
    @abstractmethod
    def send(self, recipient: str, msg: str) -> str:
        pass

class _RefEmail(_RefNotification):
    def send(self, recipient: str, msg: str) -> str:
        return f"Email to {recipient}: {msg}"

class _RefSMS(_RefNotification):
    def send(self, recipient: str, msg: str) -> str:
        return f"SMS to {recipient}: {msg}"'''
    },
    38: {
        "topic": "Properties, OOP Checkpoint & Advanced Data Structures",
        "prereqs": "Days 19–21 (Day 19 Properties & Abstraction, Day 20 OOP Checkpoint, Day 21 Data Structures)",
        "q1": "How does `@property` enable getter access while hiding direct field mutation?",
        "q2": "What is the difference between a Python `set` (unique elements, fast hashing) and a `list`?",
        "q3": "How do you define a setter using `@<property_name>.setter` in Python?",
        "desc": "Implement `BankAccount` with protected `_balance: float`. Implement `@property def balance` and `@balance.setter` which raises `ValueError('Deposit must be non-negative')` if new balance < 0.",
        "stub": '''class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance

    # Implement balance property and setter below:
    pass''',
        "runner": '''def run_test():
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
        print(f"[!] Test error: {e}")''',
        "hint1": "Decorate getter with `@property def balance(self): return self._balance`.",
        "hint2": "Decorate setter with `@balance.setter def balance(self, val): if val < 0: raise ValueError(...) else: self._balance = val`.",
        "sol": '''class _RefBankAccount:
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
        self._balance = val'''
    },
    39: {
        "topic": "Functions, Scope, Closures, Exception Defensiveness & Context Managers",
        "prereqs": "Days 22–24 (Day 22 Scope & Decorators, Day 23 Exception Handling, Day 24 Context Managers)",
        "q1": "What is the LEGB rule for Python variable resolution (Local, Enclosing, Global, Built-in)?",
        "q2": "What do the `__enter__` and `__exit__` magic methods do when using a `with` statement?",
        "q3": "How does a Python decorator use closures to wrap another function?",
        "desc": "Write a decorator `retry_on_failure(max_retries: int = 2)` that catches exceptions and retries calling the wrapped function up to `max_retries` additional times before re-raising the exception.",
        "stub": '''import functools

def retry_on_failure(max_retries: int = 2):
    """
    Decorator that retries the wrapped function upon exception up to max_retries times.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 39 Revision Challenge ---")
    dec = retry_on_failure(max_retries=2)
    if dec is None:
        print("[!] Decorator `retry_on_failure` is not yet implemented.")
        return

    attempts = [0]
    @dec
    def flaky():
        attempts[0] += 1
        if attempts[0] < 3:
            raise ValueError("Temporary network glitch")
        return "SUCCESS"

    try:
        res = flaky()
        if res == "SUCCESS" and attempts[0] == 3:
            print("[+] Test Passed: Decorator retried and succeeded on third attempt.")
        else:
            print(f"[-] Test Failed: res={res}, attempts={attempts[0]}")
    except Exception as e:
        print(f"[!] Decorator failed or not implemented: {e}")''',
        "hint1": "Define decorator returning an inner wrapper taking `*args, **kwargs`.",
        "hint2": "Loop for `max_retries + 1` times: inside `try: return func(*args, **kwargs)` except `Exception: if attempt == max_retries: raise`.",
        "sol": '''import functools

def _reference_solution(max_retries: int = 2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i == max_retries:
                        raise
        return wrapper
    return decorator'''
    },
    40: {
        "topic": "Type Hints, PEP 8, Git Workflows & SQL Fundamentals",
        "prereqs": "Days 25–27 (Day 25 Type Hints, Day 26 Git Collaboration, Day 27 SQL Fundamentals)",
        "q1": "What are type hints in Python and why do they enhance developer tooling without causing runtime overhead?",
        "q2": "What are the stages of Git tracking: Working Directory -> Staging Area -> Local Repo -> Remote Repo?",
        "q3": "What SQL keyword creates a table and defines primary key constraints?",
        "desc": "Write `generate_create_table_sql(table_name: str, schema: dict[str, str]) -> str` generating an SQL CREATE TABLE statement. E.g. `schema = {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT NOT NULL'}` -> `CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL);`.",
        "stub": '''def generate_create_table_sql(table_name: str, schema: dict[str, str]) -> str:
    """
    Generates CREATE TABLE statement from schema dictionary.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 40 Revision Challenge ---")
    s = {"id": "INTEGER PRIMARY KEY", "email": "TEXT NOT NULL"}
    sql = generate_create_table_sql("users", s)
    if sql is None:
        print("[!] Function `generate_create_table_sql` is not yet implemented.")
        return
    expected = "CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT NOT NULL);"
    if sql.strip() == expected:
        print("[+] Test Passed: DDL SQL string accurately generated.")
    else:
        print(f"[-] Test Failed: Got '{sql}'")''',
        "hint1": "Format each column definition as `f'{col} {col_type}'`.",
        "hint2": "Join column definitions with `', '` and return `f'CREATE TABLE {table_name} ({cols});'`.",
        "sol": '''def _reference_solution(table_name: str, schema: dict[str, str]) -> str:
    cols = ", ".join(f"{col} {ctype}" for col, ctype in schema.items())
    return f"CREATE TABLE {table_name} ({cols});"'''
    },
    41: {
        "topic": "SQL CRUD Operations, Aggregations & Table Joins",
        "prereqs": "Days 28–30 (Day 28 SQL CRUD, Day 29 Aggregation & Grouping, Day 30 Table Joins)",
        "q1": "What is the difference between an INNER JOIN and a LEFT JOIN in SQL?",
        "q2": "Why must all non-aggregated SELECT columns appear in the GROUP BY clause?",
        "q3": "What is the difference between WHERE (row filter) and HAVING (group filter)?",
        "desc": "Write `calculate_customer_totals(conn) -> list[tuple[str, float]]` querying an in-memory SQLite database to compute total order amount per customer using an INNER JOIN and SUM(amount) GROUP BY customer name, sorted by total descending.",
        "stub": '''import sqlite3

def calculate_customer_totals(conn: sqlite3.Connection) -> list[tuple[str, float]]:
    """
    Executes SELECT c.name, SUM(o.amount) FROM customers c JOIN orders o ON c.id = o.customer_id GROUP BY c.name ORDER BY 2 DESC;
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
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
    conn.close()''',
        "hint1": "Write query: `SELECT c.name, SUM(o.amount) FROM customers c JOIN orders o ON c.id = o.customer_id GROUP BY c.name ORDER BY SUM(o.amount) DESC`.",
        "hint2": "Execute query with `conn.cursor()`, run `.fetchall()`, and return the list of tuples.",
        "sol": '''import sqlite3

def _reference_solution(conn: sqlite3.Connection) -> list[tuple[str, float]]:
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, SUM(o.amount)
        FROM customers c
        JOIN orders o ON c.id = o.customer_id
        GROUP BY c.name
        ORDER BY SUM(o.amount) DESC;
    """)
    return cur.fetchall()'''
    },
    42: {
        "topic": "SQL Subqueries, Transactions, Connection Pooling & B-Tree Indexes",
        "prereqs": "Days 31–33 (Day 31 Subqueries & Transactions, Day 32 Drivers & Pooling, Day 33 Indexing)",
        "q1": "What are the four ACID properties in database transaction management?",
        "q2": "Why must SQL queries always use parameterized placeholders (`%s` or `?`) instead of f-string formatting?",
        "q3": "Why does a B-Tree index offer O(log n) lookups instead of O(n) table scans?",
        "desc": "Write `is_using_index(plan_steps: list[str]) -> bool` which inspects a list of EXPLAIN plan step strings and returns True if any step uses an index scan and False if it only does sequential scans.",
        "stub": '''def is_using_index(plan_steps: list[str]) -> bool:
    """
    Returns True if any step in plan_steps contains 'INDEX' (case-insensitive),
    False otherwise.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 42 Revision Challenge ---")
    p1 = ["Seq Scan on users (cost=0.00..35.50 rows=2550 width=36)"]
    p2 = ["Bitmap Index Scan on idx_users_email (cost=0.00..4.30 rows=10 width=0)"]
    r1 = is_using_index(p1)
    r2 = is_using_index(p2)
    if r1 is None or r2 is None:
        print("[!] Function `is_using_index` is not yet implemented.")
        return
    if r1 is False and r2 is True:
        print("[+] Test Passed: B-Tree index scan correctly detected.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}")''',
        "hint1": "Iterate through each step string and check for the substring 'INDEX'.",
        "hint2": "Use `return any('INDEX' in step.upper() for step in plan_steps)`.",
        "sol": '''def _reference_solution(plan_steps: list[str]) -> bool:
    return any("INDEX" in step.upper() for step in plan_steps)'''
    },
    43: {
        "topic": "Database Normalization, ACID/MVCC Concurrency & Advanced Data Types",
        "prereqs": "Days 34–36 (Day 34 Normalization, Day 35 Locking & MVCC, Day 36 PostgreSQL JSONB)",
        "q1": "What is the difference between 1NF, 2NF, and 3NF database normalization?",
        "q2": "How does `SELECT ... FOR UPDATE` row locking prevent concurrent lost update anomalies?",
        "q3": "When is storing data in a PostgreSQL `JSONB` column appropriate versus normalized relational tables?",
        "desc": "Write `atomic_deduct_stock(conn, product_id: int, qty: int) -> bool` executing conditional atomic update: `UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?;`. Commit and return True if `cur.rowcount > 0`, otherwise rollback and return False.",
        "stub": '''def atomic_deduct_stock(conn, product_id: int, qty: int) -> bool:
    """
    Conditional atomic update. Returns True if stock deducted, False if insufficient stock.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
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
    conn.close()''',
        "hint1": "Execute the parameterized UPDATE statement and inspect `cur.rowcount`.",
        "hint2": "If `cur.rowcount > 0`: `conn.commit()` and return True; else `conn.rollback()` and return False.",
        "sol": '''def _reference_solution(conn, product_id: int, qty: int) -> bool:
    cur = conn.cursor()
    cur.execute("UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?;", (qty, product_id, qty))
    if cur.rowcount > 0:
        conn.commit()
        return True
    conn.rollback()
    return False'''
    },
    44: {
        "topic": "HTTP Protocols, Methods, Status Codes & RESTful Conventions",
        "prereqs": "Days 37–39 (Day 37 HTTP Anatomy, Day 38 Methods & Codes, Day 39 REST Conventions)",
        "q1": "What is HTTP method idempotency, and why are GET and PUT idempotent while POST is not?",
        "q2": "What are the standard status codes: Success (200), Created (201), Bad Request (400), Not Found (404)?",
        "q3": "Why do RESTful API conventions use plural nouns for URIs rather than action verbs?",
        "desc": "Write `determine_status_code(method: str, resource_found: bool, is_valid_payload: bool) -> int` mapping request context to standard HTTP status codes.",
        "stub": '''def determine_status_code(method: str, resource_found: bool, is_valid_payload: bool) -> int:
    """
    Rules:
    - If payload is invalid: return 400
    - If method is 'GET' or 'DELETE' and resource not found: return 404
    - If method is 'POST' and valid: return 201
    - If method is 'GET' or 'PUT' and found and valid: return 200
    - Default fallback: 200
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 44 Revision Challenge ---")
    c1 = determine_status_code("POST", True, True)
    c2 = determine_status_code("GET", False, True)
    c3 = determine_status_code("POST", True, False)
    c4 = determine_status_code("GET", True, True)
    if c1 is None:
        print("[!] Function `determine_status_code` is not yet implemented.")
        return
    if (c1, c2, c3, c4) == (201, 404, 400, 200):
        print("[+] Test Passed: REST HTTP status codes verified.")
    else:
        print(f"[-] Test Failed: Got {(c1, c2, c3, c4)}")''',
        "hint1": "Handle errors first (if not valid -> 400, if not found on GET/DELETE -> 404).",
        "hint2": "If method == 'POST': return 201; else return 200.",
        "sol": '''def _reference_solution(method: str, resource_found: bool, is_valid_payload: bool) -> int:
    if not is_valid_payload:
        return 400
    if not resource_found and method.upper() in ("GET", "DELETE"):
        return 404
    if method.upper() == "POST":
        return 201
    return 200'''
    },
    45: {
        "topic": "Django Architecture, Settings, URL Routing & Views",
        "prereqs": "Days 40–42 (Day 40 Django Setup, Day 41 URLs & Views, Day 42 Templates)",
        "q1": "What are the roles of Model, View, and Template in Django's MVT pattern?",
        "q2": "Why must SECRET_KEY and database credentials be read from environment variables rather than committed in settings.py?",
        "q3": "In Django URL routing, how does `<int:pk>` convert and pass path parameters to view functions?",
        "desc": "Write `extract_id_from_path(path: str) -> int | None` simulating Django's `<int:pk>` path converter for URLs formatted like `/api/v1/items/<id>/`.",
        "stub": '''import re

def extract_id_from_path(path: str) -> int | None:
    """
    Extracts integer ID from path segment: '/items/<id>/'. Returns int or None.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 45 Revision Challenge ---")
    i1 = extract_id_from_path("/api/v1/items/456/")
    i2 = extract_id_from_path("/api/v1/items/invalid/")
    if i1 is None and i2 is None:
        print("[!] Function `extract_id_from_path` is not yet implemented.")
        return
    if i1 == 456 and i2 is None:
        print("[+] Test Passed: Path converter simulation confirmed.")
    else:
        print(f"[-] Test Failed: i1={i1}, i2={i2}")''',
        "hint1": "Use regex `re.search(r'/items/(\\d+)/?', path)`.",
        "hint2": "If matched, return `int(m.group(1))` else `None`.",
        "sol": '''import re

def _reference_solution(path: str) -> int | None:
    m = re.search(r'/items/(\\d+)/?', path)
    return int(m.group(1)) if m else None'''
    },
    46: {
        "topic": "Django Database Models, Migrations & ORM Queries",
        "prereqs": "Days 43–44 (Day 43 Models & Migrations, Day 44 ORM Queries & Q Objects)",
        "q1": "What is the difference between `makemigrations` (generates migration code) and `migrate` (executes SQL DDL)?",
        "q2": "What does 'lazy evaluation' mean for Django QuerySets and what actions trigger database execution?",
        "q3": "How do Django `Q` objects allow constructing queries with `OR` logic?",
        "desc": "Write `simulate_q_filter(items: list[dict], cat: str = None, min_price: float = None) -> list[dict]` matching items where category matches OR price >= min_price.",
        "stub": '''def simulate_q_filter(items: list[dict], cat: str = None, min_price: float = None) -> list[dict]:
    """
    Simulates Django Q(category=cat) | Q(price__gte=min_price)
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 46 Revision Challenge ---")
    data = [
        {"name": "A", "category": "books", "price": 10},
        {"name": "B", "category": "tech", "price": 100},
        {"name": "C", "category": "clothing", "price": 50},
    ]
    res = simulate_q_filter(data, cat="books", min_price=80)
    if res is None:
        print("[!] Function `simulate_q_filter` is not yet implemented.")
        return
    names = [r["name"] for r in res]
    if sorted(names) == ["A", "B"]:
        print("[+] Test Passed: Disjunctive OR filter simulation succeeded.")
    else:
        print(f"[-] Test Failed: Got names={names}")''',
        "hint1": "Check if an item matches `cat` OR meets `min_price`.",
        "hint2": "Use `[i for i in items if (cat and i.get('category') == cat) or (min_price is not None and i.get('price', 0) >= min_price)]`.",
        "sol": '''def _reference_solution(items: list[dict], cat: str = None, min_price: float = None) -> list[dict]:
    return [
        i for i in items
        if (cat and i.get("category") == cat) or (min_price is not None and i.get("price", 0) >= min_price)
    ]'''
    },
    47: {
        "topic": "ForeignKeys, select_related, Prefetching & CRUD Views",
        "prereqs": "Days 45–46 (Day 45 ForeignKeys & N+1 Problem, Day 46 CRUD Application)",
        "q1": "What is the N+1 query problem in ORMs, and how does `select_related` fix it using an SQL JOIN?",
        "q2": "What is the difference between `select_related` (single-valued FK) and `prefetch_related` (many-to-many / reverse FK)?",
        "q3": "What does `related_name` in a `ForeignKey` field define on the reverse model?",
        "desc": "Write `count_simulated_queries(item_count: int, use_select_related: bool) -> int` returning query count: 1 query if select_related is True, 1 + item_count queries if False.",
        "stub": '''def count_simulated_queries(item_count: int, use_select_related: bool) -> int:
    """
    If use_select_related is True: executes 1 query (with SQL JOIN).
    If False: executes 1 initial query + 1 query per item (1 + N queries).
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 47 Revision Challenge ---")
    q_opt = count_simulated_queries(50, True)
    q_naive = count_simulated_queries(50, False)
    if q_opt is None:
        print("[!] Function `count_simulated_queries` is not yet implemented.")
        return
    if q_opt == 1 and q_naive == 51:
        print("[+] Test Passed: N+1 query optimization verified.")
    else:
        print(f"[-] Test Failed: q_opt={q_opt}, q_naive={q_naive}")''',
        "hint1": "If select_related is enabled, only 1 SQL JOIN query is sent.",
        "hint2": "Return 1 if `use_select_related` else `item_count + 1`.",
        "sol": '''def _reference_solution(item_count: int, use_select_related: bool) -> int:
    return 1 if use_select_related else item_count + 1'''
    },
    48: {
        "topic": "Django Forms, clean_* Validations & Error Handling",
        "prereqs": "Day 47 (Django Forms & Clean Validations)",
        "q1": "How does Django form validation execute field `clean_<field>()` methods before form `clean()`?",
        "q2": "What dictionary holds validated, type-coerced form fields in Django (`form.cleaned_data`)?",
        "q3": "Why should validation happen at both the form layer and the database constraint layer?",
        "desc": "Write `clean_date_range(cleaned_data: dict) -> tuple[bool, str]` validating that `start_day` < `end_day`.",
        "stub": '''def clean_date_range(cleaned_data: dict) -> tuple[bool, str]:
    """
    Validates that cleaned_data['start_day'] < cleaned_data['end_day'].
    Returns (True, "Valid") or (False, "End date must be after start date").
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 48 Revision Challenge ---")
    res1 = clean_date_range({"start_day": 10, "end_day": 15})
    if res1 is None:
        print("[!] Function `clean_date_range` is not yet implemented.")
        return
    r1, _ = res1
    r2, _ = clean_date_range({"start_day": 20, "end_day": 15})
    if r1 is True and r2 is False:
        print("[+] Test Passed: Form date range validation succeeded.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}")''',
        "hint1": "Extract `start_day` and `end_day` from `cleaned_data` and compare them.",
        "hint2": "If `cleaned_data.get('end_day', 0) <= cleaned_data.get('start_day', 0)` return False, message.",
        "sol": '''def _reference_solution(cleaned_data: dict) -> tuple[bool, str]:
    start = cleaned_data.get("start_day", 0)
    end = cleaned_data.get("end_day", 0)
    if end <= start:
        return False, "End date must be after start date"
    return True, "Valid"'''
    },
    49: {
        "topic": "Django Authentication, Sessions & Password Security",
        "prereqs": "Day 48 (Django Authentication & Sessions)",
        "q1": "How does Django session authentication use cookies (`sessionid`) to maintain user state?",
        "q2": "Why must session cookies have `HttpOnly` and `Secure` flags in production deployments?",
        "q3": "What does the `@login_required` decorator do when an unauthenticated user accesses a protected view?",
        "desc": "Write `validate_session(session_data: dict) -> bool` returning True if `user_id` exists and `is_active` is True.",
        "stub": '''def validate_session(session_data: dict) -> bool:
    """
    Returns True if session_data contains 'user_id' and 'is_active' is True.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 49 Revision Challenge ---")
    s1 = validate_session({"user_id": 1, "is_active": True})
    s2 = validate_session({"user_id": 2, "is_active": False})
    s3 = validate_session({"is_active": True})
    if s1 is None:
        print("[!] Function `validate_session` is not yet implemented.")
        return
    if s1 is True and s2 is False and s3 is False:
        print("[+] Test Passed: Session validity verified.")
    else:
        print(f"[-] Test Failed: s1={s1}, s2={s2}, s3={s3}")''',
        "hint1": "Check that `user_id` is present and `is_active` is truthy.",
        "hint2": "Use `return bool(session_data.get('user_id') and session_data.get('is_active'))`.",
        "sol": '''def _reference_solution(session_data: dict) -> bool:
    return bool(session_data.get("user_id") and session_data.get("is_active"))'''
    },
    50: {
        "topic": "Custom User Models & Authorization Architecture",
        "prereqs": "Day 49 (Authorization & Custom User Models)",
        "q1": "Why does the official Django documentation recommend creating a custom user model at the start of a project?",
        "q2": "What is the difference between authentication ('who you are') and authorization ('what you are permitted to do')?",
        "q3": "How do Django permissions and groups enforce access control?",
        "desc": "Write `filter_active_users(records: list[dict]) -> list[dict]` filtering out any user dictionary where `is_deleted` is True.",
        "stub": '''def filter_active_users(records: list[dict]) -> list[dict]:
    """
    Simulates a soft-delete manager filter: returns records where is_deleted is False or missing.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 50 Revision Challenge ---")
    users = [
        {"id": 1, "name": "Alice", "is_deleted": False},
        {"id": 2, "name": "Bob", "is_deleted": True},
        {"id": 3, "name": "Carol"},
    ]
    res = filter_active_users(users)
    if res is None:
        print("[!] Function `filter_active_users` is not yet implemented.")
        return
    ids = [u["id"] for u in res]
    if ids == [1, 3]:
        print("[+] Test Passed: Soft-deleted users filtered out.")
    else:
        print(f"[-] Test Failed: Got ids={ids}")''',
        "hint1": "Filter dictionaries where `r.get('is_deleted', False)` is False.",
        "hint2": "Use `[r for r in records if not r.get('is_deleted', False)]`.",
        "sol": '''def _reference_solution(records: list[dict]) -> list[dict]:
    return [r for r in records if not r.get("is_deleted", False)]'''
    },
    51: {
        "topic": "Signals, Custom Managers & Service Layer Patterns",
        "prereqs": "Day 50 (Django Signals, Managers & Overrides)",
        "q1": "Why should critical business logic live in explicit service functions rather than implicit Django signals?",
        "q2": "What is a custom Django `models.Manager` and how does `get_queryset()` allow encapsulating common filters?",
        "q3": "When is overriding a model's `save()` method appropriate versus using a service layer?",
        "desc": "Write `serialize_order_summary(order_dict: dict) -> dict` that converts an internal DB record (price in cents, raw ISO timestamp) into a clean REST API JSON structure with price formatted as dollars (float) and status uppercased.",
        "stub": '''def serialize_order_summary(order_dict: dict) -> dict:
    """
    Input: {'id': 101, 'price_cents': 2999, 'status': 'completed', 'raw_date': '2026-10-16T12:00:00Z'}
    Output: {'id': 101, 'price_dollars': 29.99, 'status': 'COMPLETED', 'date': '2026-10-16'}
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 51 Revision Challenge ---")
    raw = {"id": 101, "price_cents": 2999, "status": "completed", "raw_date": "2026-10-16T12:00:00Z"}
    res = serialize_order_summary(raw)
    if res is None:
        print("[!] Function `serialize_order_summary` is not yet implemented.")
        return
    if res.get("price_dollars") == 29.99 and res.get("status") == "COMPLETED" and res.get("date") == "2026-10-16":
        print("[+] Test Passed: REST JSON serialization structure verified.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Convert cents to dollars by dividing by 100.0, uppercase status, and slice date up to 'T'.",
        "hint2": "Return `{'id': order_dict['id'], 'price_dollars': round(order_dict['price_cents']/100.0, 2), 'status': order_dict['status'].upper(), 'date': order_dict['raw_date'].split('T')[0]}`.",
        "sol": '''def _reference_solution(order_dict: dict) -> dict:
    return {
        "id": order_dict["id"],
        "price_dollars": round(order_dict["price_cents"] / 100.0, 2),
        "status": order_dict["status"].upper(),
        "date": order_dict["raw_date"].split("T")[0]
    }'''
    },
    52: {
        "topic": "DRF Serialization, Serializer Fields & APIView",
        "prereqs": "Day 51 (DRF Serialization & APIView)",
        "q1": "What is the role of a DRF Serializer in converting complex QuerySets to Python datatypes (JSON)?",
        "q2": "How does `ModelSerializer` differ from a regular `Serializer` in DRF?",
        "q3": "What is the difference between `APIView` and Django's standard `View`?",
        "desc": "Write `validate_product_serializer(payload: dict) -> tuple[bool, dict]` that validates `title` (required, min 3 chars) and `price` (required, float > 0). Returns `(True, {})` or `(False, errors_dict)`.",
        "stub": '''def validate_product_serializer(payload: dict) -> tuple[bool, dict]:
    """
    Validates product fields. Returns (is_valid, errors_dict).
    errors_dict contains field names mapped to list of error strings.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 52 Revision Challenge ---")
    res1 = validate_product_serializer({"title": "Laptop", "price": 999.0})
    if res1 is None:
        print("[!] Function `validate_product_serializer` is not yet implemented.")
        return
    v1, e1 = res1
    v2, e2 = validate_product_serializer({"title": "AB", "price": -10.0})
    if v1 is True and v2 is False and "title" in e2 and "price" in e2:
        print("[+] Test Passed: Serializer field validation logic confirmed.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}, e2={e2}")''',
        "hint1": "Create an empty errors dict and populate it with lists of error messages for failing fields.",
        "hint2": "If 'title' not in payload or len(payload['title']) < 3: errors['title'] = ['Min 3 chars']. If 'price' not in payload or payload['price'] <= 0: errors['price'] = ['Must be positive'].",
        "sol": '''def _reference_solution(payload: dict) -> tuple[bool, dict]:
    errors = {}
    title = payload.get("title", "")
    if not title or len(title) < 3:
        errors["title"] = ["Title must be at least 3 characters long"]
    price = payload.get("price")
    if price is None or price <= 0:
        errors["price"] = ["Price must be a positive number"]
    return (len(errors) == 0, errors)'''
    },
    53: {
        "topic": "DRF Writable Nested Serializers & Transactions",
        "prereqs": "Day 52 (DRF Writable Nested Serializers)",
        "q1": "Why does DRF require overriding `create()` and `update()` on serializers with writable nested relationships?",
        "q2": "How do you handle database atomicity (`transaction.atomic()`) when creating parent and child records in a nested serializer?",
        "q3": "What is the difference between `validate_<field>()` and `validate()` in DRF?",
        "desc": "Write `flatten_nested_payload(payload: dict) -> dict` that extracts a nested `address` dict into top-level keys `address_city` and `address_zip`.",
        "stub": '''def flatten_nested_payload(payload: dict) -> dict:
    """
    Input: {'user': 'alice', 'address': {'city': 'Kathmandu', 'zip': '44600'}}
    Output: {'user': 'alice', 'address_city': 'Kathmandu', 'address_zip': '44600'}
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 53 Revision Challenge ---")
    inp = {"user": "alice", "address": {"city": "Kathmandu", "zip": "44600"}}
    res = flatten_nested_payload(inp)
    if res is None:
        print("[!] Function `flatten_nested_payload` is not yet implemented.")
        return
    if res.get("address_city") == "Kathmandu" and "address" not in res:
        print("[+] Test Passed: Nested payload transformation succeeded.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Copy the payload dict, pop the 'address' key, and assign the nested fields with prefixes.",
        "hint2": "Use `out = dict(payload); addr = out.pop('address', {}); out['address_city'] = addr.get('city'); out['address_zip'] = addr.get('zip'); return out`.",
        "sol": '''def _reference_solution(payload: dict) -> dict:
    out = dict(payload)
    addr = out.pop("address", {})
    out["address_city"] = addr.get("city")
    out["address_zip"] = addr.get("zip")
    return out'''
    },
    54: {
        "topic": "DRF ModelViewSets, Generic Views & Routers",
        "prereqs": "Day 53 (DRF ModelViewSets & Generic Views)",
        "q1": "What standard HTTP actions (`list`, `create`, `retrieve`, `update`, `partial_update`, `destroy`) does `ModelViewSet` provide automatically?",
        "q2": "How does DRF's `DefaultRouter` generate RESTful URL patterns for a registered ViewSet?",
        "q3": "When should you use the `@action(detail=True)` decorator in a ViewSet?",
        "desc": "Write `parse_auth_header(auth_header: str) -> tuple[str, str] | None` which parses an `Authorization` header value formatted as `Bearer <token>` or `Token <key>` into `(scheme, credential)`.",
        "stub": '''def parse_auth_header(auth_header: str) -> tuple[str, str] | None:
    """
    Parses 'Bearer eyJhbGciOi...' into ('Bearer', 'eyJhbGciOi...')
    Returns None if format is invalid.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 54 Revision Challenge ---")
    p1 = parse_auth_header("Bearer mysecrettoken123")
    p2 = parse_auth_header("Token keyabc")
    p3 = parse_auth_header("InvalidHeader")
    if p1 is None and p2 is None:
        print("[!] Function `parse_auth_header` is not yet implemented.")
        return
    if p1 == ("Bearer", "mysecrettoken123") and p2 == ("Token", "keyabc") and p3 is None:
        print("[+] Test Passed: Authorization header parser verified.")
    else:
        print(f"[-] Test Failed: p1={p1}, p2={p2}, p3={p3}")''',
        "hint1": "Split the header string by whitespace and check that there are exactly 2 parts.",
        "hint2": "Use `parts = auth_header.strip().split(); return (parts[0], parts[1]) if len(parts) == 2 else None`.",
        "sol": '''def _reference_solution(auth_header: str) -> tuple[str, str] | None:
    parts = auth_header.strip().split()
    if len(parts) == 2:
        return (parts[0], parts[1])
    return None'''
    },
    55: {
        "topic": "DRF Token Authentication & JWT (SimpleJWT)",
        "prereqs": "Day 54 (DRF Token Auth & JWT)",
        "q1": "What is the difference between an Access Token (short-lived) and a Refresh Token (long-lived) in JWT?",
        "q2": "What are the three parts of a JSON Web Token (Header, Payload, Signature)?",
        "q3": "Why should JWT access tokens never be stored in browser `localStorage` due to XSS risks?",
        "desc": "Write `check_role_permission(role: str, action: str) -> bool` enforcing: 'admin' can perform any action; 'staff' can perform 'read' and 'update'; 'customer' can only perform 'read'.",
        "stub": '''def check_role_permission(role: str, action: str) -> bool:
    """
    Enforces RBAC permissions. Actions: 'read', 'update', 'delete', 'create'.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 55 Revision Challenge ---")
    a1 = check_role_permission("admin", "delete")
    s1 = check_role_permission("staff", "update")
    s2 = check_role_permission("staff", "delete")
    c1 = check_role_permission("customer", "read")
    c2 = check_role_permission("customer", "update")
    if a1 is None:
        print("[!] Function `check_role_permission` is not yet implemented.")
        return
    if (a1, s1, s2, c1, c2) == (True, True, False, True, False):
        print("[+] Test Passed: RBAC permission check verified.")
    else:
        print(f"[-] Test Failed: Got {(a1, s1, s2, c1, c2)}")''',
        "hint1": "Define a permissions dictionary mapping roles to allowed action sets.",
        "hint2": "Use `perms = {'admin': {'read', 'update', 'delete', 'create'}, 'staff': {'read', 'update'}, 'customer': {'read'}}; return action in perms.get(role, set())`.",
        "sol": '''def _reference_solution(role: str, action: str) -> bool:
    perms = {
        "admin": {"read", "update", "delete", "create"},
        "staff": {"read", "update"},
        "customer": {"read"}
    }
    return action in perms.get(role, set())'''
    },
    56: {
        "topic": "DRF Object-Level Permissions & Custom BasePermission",
        "prereqs": "Day 55 (DRF Object-Level Permissions)",
        "q1": "In DRF `BasePermission`, what is the difference between `has_permission()` and `has_object_permission()`?",
        "q2": "What are `SAFE_METHODS` in DRF (`GET`, `HEAD`, `OPTIONS`)?",
        "q3": "How does `IsOwnerOrReadOnly` allow public reads while restricting writes to the creator?",
        "desc": "Write `has_object_permission(user: dict, obj: dict, http_method: str) -> bool` allowing safe methods ('GET', 'HEAD') for everyone, and write methods only if `user['id'] == obj['owner_id']` or `user['is_staff']` is True.",
        "stub": '''def has_object_permission(user: dict, obj: dict, http_method: str) -> bool:
    """
    Simulates DRF IsOwnerOrReadOnly permission.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 56 Revision Challenge ---")
    owner = {"id": 10, "is_staff": False}
    other = {"id": 20, "is_staff": False}
    staff = {"id": 99, "is_staff": True}
    obj = {"id": 101, "owner_id": 10}
    p1 = has_object_permission(other, obj, "GET")
    p2 = has_object_permission(other, obj, "DELETE")
    p3 = has_object_permission(owner, obj, "PUT")
    p4 = has_object_permission(staff, obj, "DELETE")
    if p1 is None:
        print("[!] Function `has_object_permission` is not yet implemented.")
        return
    if (p1, p2, p3, p4) == (True, False, True, True):
        print("[+] Test Passed: DRF object-level permission logic verified.")
    else:
        print(f"[-] Test Failed: Got {(p1, p2, p3, p4)}")''',
        "hint1": "If http_method in ('GET', 'HEAD', 'OPTIONS'): return True.",
        "hint2": "Otherwise: `return user.get('id') == obj.get('owner_id') or user.get('is_staff') is True`.",
        "sol": '''def _reference_solution(user: dict, obj: dict, http_method: str) -> bool:
    if http_method.upper() in ("GET", "HEAD", "OPTIONS"):
        return True
    return user.get("id") == obj.get("owner_id") or user.get("is_staff") is True'''
    },
    57: {
        "topic": "DRF Filtering, Ordering & Pagination",
        "prereqs": "Day 56 (DRF Searching & Pagination)",
        "q1": "What are the benefits of `django-filter` over writing manual `.filter()` code for every query parameter?",
        "q2": "What is the difference between `PageNumberPagination` and `CursorPagination`?",
        "q3": "Why is database indexing critical on columns used in `OrderingFilter` (e.g. `created_at`)?",
        "desc": "Write `filter_and_paginate(items: list[dict], category: str = None, page: int = 1, page_size: int = 2) -> dict` returning a paginated API response with `count`, `results`, and `total_pages`.",
        "stub": '''def filter_and_paginate(items: list[dict], category: str = None, page: int = 1, page_size: int = 2) -> dict:
    """
    Returns: {'count': int, 'total_pages': int, 'results': list[dict]}
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    import math
    print("--- Running Day 57 Revision Challenge ---")
    data = [
        {"id": 1, "cat": "books"},
        {"id": 2, "cat": "books"},
        {"id": 3, "cat": "books"},
        {"id": 4, "cat": "tech"},
    ]
    res = filter_and_paginate(data, category="books", page=1, page_size=2)
    if res is None:
        print("[!] Function `filter_and_paginate` is not yet implemented.")
        return
    if res.get("count") == 3 and res.get("total_pages") == 2 and len(res.get("results", [])) == 2:
        print("[+] Test Passed: Filter and pagination simulation verified.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Filter items first by category (if specified), then calculate total_pages using `math.ceil(len(filtered) / page_size)`.",
        "hint2": "Slice the results: `start = (page - 1) * page_size`, `end = start + page_size`. Return dictionary with count, total_pages, and sliced results.",
        "sol": '''import math

def _reference_solution(items: list[dict], category: str = None, page: int = 1, page_size: int = 2) -> dict:
    filtered = [i for i in items if category is None or i.get("cat") == category]
    count = len(filtered)
    total_pages = math.ceil(count / page_size) if page_size > 0 else 1
    start = (page - 1) * page_size
    results = filtered[start : start + page_size]
    return {"count": count, "total_pages": total_pages, "results": results}'''
    },
    58: {
        "topic": "OpenAPI / Swagger Documentation & API Contracts",
        "prereqs": "Day 57 (DRF OpenAPI / Swagger Documentation)",
        "q1": "Why is an auto-generated OpenAPI (Swagger) schema valuable when collaborating with frontend engineers?",
        "q2": "What information does OpenAPI capture for each endpoint (parameters, request body, response codes, auth)?",
        "q3": "What is the benefit of standardized response envelopes across all endpoints?",
        "desc": "Write `build_api_response(data: list, status_code: int = 200, message: str = 'Success') -> dict` producing a standardized REST response envelope with `status`, `message`, `count`, and `data`.",
        "stub": '''def build_api_response(data: list, status_code: int = 200, message: str = 'Success') -> dict:
    """
    Standard envelope: {'status': status_code, 'message': message, 'count': len(data), 'data': data}
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 58 Revision Challenge ---")
    res = build_api_response([{"id": 1}], status_code=200, message="OK")
    if res is None:
        print("[!] Function `build_api_response` is not yet implemented.")
        return
    if res.get("status") == 200 and res.get("count") == 1 and res.get("message") == "OK":
        print("[+] Test Passed: Standard API response envelope verified.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Construct a dictionary with the four required keys: status, message, count, and data.",
        "hint2": "Use `return {'status': status_code, 'message': message, 'count': len(data), 'data': data}`.",
        "sol": '''def _reference_solution(data: list, status_code: int = 200, message: str = "Success") -> dict:
    return {"status": status_code, "message": message, "count": len(data), "data": data}'''
    },
    59: {
        "topic": "Manual Testing with Postman, Assertions & Status Codes",
        "prereqs": "Day 58 (API Testing via Postman & cURL)",
        "q1": "How do you test an authenticated endpoint using a cURL command with an `Authorization: Bearer <token>` header?",
        "q2": "Why should backend tests assert both the HTTP status code AND the JSON response body structure?",
        "q3": "What is an API response contract?",
        "desc": "Write `assert_response_contract(response: dict, required_keys: list[str]) -> bool` that verifies a response dictionary contains all required keys and none of their values are None.",
        "stub": '''def assert_response_contract(response: dict, required_keys: list[str]) -> bool:
    """
    Returns True if all required_keys exist in response and have non-None values, False otherwise.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 59 Revision Challenge ---")
    resp_ok = {"id": 1, "name": "Book", "price": 19.99}
    resp_missing = {"id": 2, "name": "Pencil"}
    resp_null = {"id": 3, "name": None, "price": 5.0}
    r1 = assert_response_contract(resp_ok, ["id", "name", "price"])
    r2 = assert_response_contract(resp_missing, ["id", "name", "price"])
    r3 = assert_response_contract(resp_null, ["id", "name", "price"])
    if r1 is None:
        print("[!] Function `assert_response_contract` is not yet implemented.")
        return
    if r1 is True and r2 is False and r3 is False:
        print("[+] Test Passed: API response contract assertion validated.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, r3={r3}")''',
        "hint1": "Loop over `required_keys` and verify each key is in the dict and not None.",
        "hint2": "Use `all(k in response and response[k] is not None for k in required_keys)`.",
        "sol": '''def _reference_solution(response: dict, required_keys: list[str]) -> bool:
    return all(k in response and response[k] is not None for k in required_keys)'''
    },
    60: {
        "topic": "Automated Unit Testing & Django Test Client",
        "prereqs": "Day 59 (Automated API Unit Testing)",
        "q1": "Why does Django's `TestCase` wrap each test in a database transaction and roll it back after execution?",
        "q2": "What is the difference between unit testing an isolated service function versus integration testing an API endpoint?",
        "q3": "Why should automated tests assert both HTTP status codes AND specific JSON response values?",
        "desc": "Write `validate_registration_payload(payload: dict) -> tuple[bool, str]` testing email format (`@` present) and password strength (min 8 chars, at least 1 digit).",
        "stub": '''def validate_registration_payload(payload: dict) -> tuple[bool, str]:
    """
    Validates:
    - email has '@'
    - password >= 8 characters and contains at least 1 digit
    Returns (True, "Valid") or (False, "Error message")
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 60 Revision Challenge ---")
    res1 = validate_registration_payload({"email": "alice@example.com", "password": "SecurePass1"})
    if res1 is None:
        print("[!] Function `validate_registration_payload` is not yet implemented.")
        return
    v1, _ = res1
    v2, _ = validate_registration_payload({"email": "bademail", "password": "SecurePass1"})
    v3, _ = validate_registration_payload({"email": "bob@example.com", "password": "short"})
    v4, _ = validate_registration_payload({"email": "bob@example.com", "password": "NoDigitsPassword"})
    if (v1, v2, v3, v4) == (True, False, False, False):
        print("[+] Test Passed: Registration test validation rules verified.")
    else:
        print(f"[-] Test Failed: Got {(v1, v2, v3, v4)}")''',
        "hint1": "Check email '@' first, then check password length >= 8, then check `any(ch.isdigit() for ch in pwd)`.",
        "hint2": "Return False with descriptive message if email lacks '@', length < 8, or no digit is found.",
        "sol": '''def _reference_solution(payload: dict) -> tuple[bool, str]:
    email = payload.get("email", "")
    pwd = payload.get("password", "")
    if "@" not in email:
        return False, "Invalid email format"
    if len(pwd) < 8:
        return False, "Password must be at least 8 characters"
    if not any(ch.isdigit() for ch in pwd):
        return False, "Password must contain at least one digit"
    return True, "Valid"'''
    },
    61: {
        "topic": "Test Fixtures, Model Factories (factory_boy) & Coverage",
        "prereqs": "Day 60 (Test Fixtures, Factories & Coverage)",
        "q1": "Why are model factories (`factory_boy`) more maintainable than hardcoded JSON/YAML fixtures in test suites?",
        "q2": "What does test coverage measure, and why is testing critical business logic more important than achieving 100% line coverage?",
        "q3": "In pytest, what is a fixture and how does it promote clean test setup and teardown?",
        "desc": "Write a factory function `create_mock_user(custom_attrs: dict = None) -> dict` that generates a default user dictionary (`{'id': 1, 'username': 'testuser', 'is_active': True, 'role': 'USER'}`) and cleanly overrides defaults with `custom_attrs`.",
        "stub": '''def create_mock_user(custom_attrs: dict = None) -> dict:
    """
    Generates a mock user dictionary with defaults, cleanly overridden by custom_attrs.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 61 Revision Challenge ---")
    u1 = create_mock_user()
    u2 = create_mock_user({"username": "custom_dev", "role": "ADMIN"})
    if u1 is None or u2 is None:
        print("[!] Function `create_mock_user` is not yet implemented.")
        return
    if u1.get("username") == "testuser" and u2.get("username") == "custom_dev" and u2.get("role") == "ADMIN" and u2.get("is_active") is True:
        print("[+] Test Passed: Mock user factory implementation verified.")
    else:
        print(f"[-] Test Failed: u1={u1}, u2={u2}")''',
        "hint1": "Define a base default dict and update it with a copy of `custom_attrs` if provided.",
        "hint2": "Use `defaults = {'id': 1, 'username': 'testuser', 'is_active': True, 'role': 'USER'}; if custom_attrs: defaults.update(custom_attrs); return defaults`.",
        "sol": '''def _reference_solution(custom_attrs: dict = None) -> dict:
    defaults = {"id": 1, "username": "testuser", "is_active": True, "role": "USER"}
    if custom_attrs:
        defaults.update(custom_attrs)
    return defaults'''
    },
    62: {
        "topic": "Troubleshooting, Debugging ORM & Python Logging",
        "prereqs": "Day 61 (Troubleshooting & Debugging ORM)",
        "q1": "What are the 5 standard Python logging levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)?",
        "q2": "How do you use `breakpoint()` in Python to pause execution and inspect variables in the terminal?",
        "q3": "How do you identify duplicate or slow SQL queries in development using Django Debug Toolbar?",
        "desc": "Write `format_log_entry(level: str, event: str, **context) -> str` which formats a structured log entry string: `[LEVEL] event | key1=val1 key2=val2` with sorted context keys.",
        "stub": '''def format_log_entry(level: str, event: str, **context) -> str:
    """
    Example: format_log_entry('INFO', 'User logged in', user_id=42, ip='127.0.0.1')
    Returns: '[INFO] User logged in | ip=127.0.0.1 user_id=42'
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 62 Revision Challenge ---")
    l1 = format_log_entry("INFO", "Order created", order_id=101, amount=50.0)
    l2 = format_log_entry("ERROR", "DB connection lost")
    if l1 is None or l2 is None:
        print("[!] Function `format_log_entry` is not yet implemented.")
        return
    if l1 == "[INFO] Order created | amount=50.0 order_id=101" and l2 == "[ERROR] DB connection lost":
        print("[+] Test Passed: Structured log entry formatting confirmed.")
    else:
        print(f"[-] Test Failed: l1='{l1}', l2='{l2}'")''',
        "hint1": "Format the prefix `[{level.upper()}] {event}`. If context has items, sort them and join with spaces.",
        "hint2": "Use `ctx_str = ' '.join(f'{k}={context[k]}' for k in sorted(context)); return f'[{level.upper()}] {event} | {ctx_str}' if ctx_str else f'[{level.upper()}] {event}'`.",
        "sol": '''def _reference_solution(level: str, event: str, **context) -> str:
    level_str = f"[{level.upper()}] {event}"
    if not context:
        return level_str
    ctx_parts = [f"{k}={context[k]}" for k in sorted(context)]
    return f"{level_str} | {' '.join(ctx_parts)}"'''
    },
    63: {
        "topic": "Clean Code, SOLID Principles & Refactoring",
        "prereqs": "Day 62 (Clean Code & SOLID Refactoring)",
        "q1": "What is the Single Responsibility Principle (SRP) in software engineering?",
        "q2": "What is the Open/Closed Principle (open for extension, closed for modification)?",
        "q3": "Why is eliminating 'fat views' by moving business logic into helper services essential for clean code?",
        "desc": "Refactor billing functions: `calculate_tax(subtotal: float, rate: float = 0.10) -> float` and `calculate_invoice_total(subtotal: float, tax_rate: float = 0.10) -> dict` returning `{'subtotal': float, 'tax': float, 'total': float}` with all values rounded to 2 decimals.",
        "stub": '''def calculate_tax(subtotal: float, rate: float = 0.10) -> float:
    # WRITE CODE HERE:
    pass

def calculate_invoice_total(subtotal: float, tax_rate: float = 0.10) -> dict:
    # WRITE CODE HERE (MUST CALL calculate_tax):
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 63 Revision Challenge ---")
    tax = calculate_tax(100.0, 0.13)
    inv = calculate_invoice_total(100.0, 0.13)
    if tax is None or inv is None:
        print("[!] Functions are not yet implemented.")
        return
    if tax == 13.0 and inv.get("total") == 113.0 and inv.get("tax") == 13.0:
        print("[+] Test Passed: Decoupled single-responsibility billing verified.")
    else:
        print(f"[-] Test Failed: tax={tax}, inv={inv}")''',
        "hint1": "In `calculate_tax`: return `round(subtotal * rate, 2)`.",
        "hint2": "In `calculate_invoice_total`: call `calculate_tax(subtotal, tax_rate)`, add to subtotal, round total, and return the dictionary.",
        "sol": '''def _reference_solution_tax(subtotal: float, rate: float = 0.10) -> float:
    return round(subtotal * rate, 2)

def _reference_solution_invoice(subtotal: float, tax_rate: float = 0.10) -> dict:
    tax = _reference_solution_tax(subtotal, tax_rate)
    return {"subtotal": round(subtotal, 2), "tax": tax, "total": round(subtotal + tax, 2)}'''
    },
    64: {
        "topic": "Service Layer Pattern & Backend Architecture",
        "prereqs": "Day 63 (Service Layers & Project Architecture)",
        "q1": "What is the Service Layer pattern in Django projects and why does it keep business logic out of views and models?",
        "q2": "Why does separating domain logic into a service layer make automated unit testing faster and simpler?",
        "q3": "How does database query latency impact overall API response time?",
        "desc": "Implement `calculate_order_totals_service(items: list[dict], discount_pct: float = 0.0) -> dict` returning `{'subtotal': float, 'discount': float, 'total': float}` with all values rounded to 2 decimals.",
        "stub": '''def calculate_order_totals_service(items: list[dict], discount_pct: float = 0.0) -> dict:
    """
    Each item in items: {'price': float, 'qty': int}
    discount_pct is a float between 0.0 and 1.0 (e.g. 0.10 for 10% off).
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 64 Revision Challenge ---")
    items = [{"price": 20.0, "qty": 2}, {"price": 10.0, "qty": 1}]
    res = calculate_order_totals_service(items, discount_pct=0.10)
    if res is None:
        print("[!] Function `calculate_order_totals_service` is not yet implemented.")
        return
    if res.get("subtotal") == 50.0 and res.get("discount") == 5.0 and res.get("total") == 45.0:
        print("[+] Test Passed: Service layer calculation logic confirmed.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Compute subtotal = sum(i['price'] * i['qty'] for i in items).",
        "hint2": "Compute discount = round(subtotal * discount_pct, 2) and total = round(subtotal - discount, 2).",
        "sol": '''def _reference_solution(items: list[dict], discount_pct: float = 0.0) -> dict:
    subtotal = round(sum(i["price"] * i["qty"] for i in items), 2)
    discount = round(subtotal * discount_pct, 2)
    total = round(subtotal - discount, 2)
    return {"subtotal": subtotal, "discount": discount, "total": total}'''
    },
    65: {
        "topic": "Caching Systems, Redis & Cache-Aside Pattern",
        "prereqs": "Day 64 (Caching Systems & Redis)",
        "q1": "What is the Cache-Aside pattern (read-through caching)?",
        "q2": "What is Cache Invalidation, and why is setting a Time-To-Live (TTL) essential?",
        "q3": "Why is Redis faster than disk-backed PostgreSQL for read-heavy operations?",
        "desc": "Write `cache_aside_lookup(cache_dict: dict, db_fetch_fn, key: str) -> tuple[object, str]` that checks `cache_dict[key]`. If present, returns `(value, 'CACHE_HIT')`. If missing, calls `db_fetch_fn(key)`, stores result in `cache_dict`, and returns `(value, 'CACHE_MISS')`.",
        "stub": '''def cache_aside_lookup(cache_dict: dict, db_fetch_fn, key: str) -> tuple[object, str]:
    """
    Implements Cache-Aside pattern simulation.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 65 Revision Challenge ---")
    cache = {}
    db_calls = [0]
    def mock_db(k):
        db_calls[0] += 1
        return f"db_val_{k}"

    res1 = cache_aside_lookup(cache, mock_db, "user:1")
    if res1 is None:
        print("[!] Function `cache_aside_lookup` is not yet implemented.")
        return
    val1, status1 = res1
    val2, status2 = cache_aside_lookup(cache, mock_db, "user:1")
    if status1 == "CACHE_MISS" and status2 == "CACHE_HIT" and val1 == "db_val_user:1" and db_calls[0] == 1:
        print("[+] Test Passed: Cache-Aside pattern logic confirmed.")
    else:
        print(f"[-] Test Failed: s1={status1}, s2={status2}, db_calls={db_calls[0]}")''',
        "hint1": "Check `if key in cache_dict: return (cache_dict[key], 'CACHE_HIT')`.",
        "hint2": "On miss: `val = db_fetch_fn(key); cache_dict[key] = val; return (val, 'CACHE_MISS')`.",
        "sol": '''def _reference_solution(cache_dict: dict, db_fetch_fn, key: str) -> tuple[object, str]:
    if key in cache_dict:
        return (cache_dict[key], "CACHE_HIT")
    val = db_fetch_fn(key)
    cache_dict[key] = val
    return (val, "CACHE_MISS")'''
    },
    66: {
        "topic": "Celery Architecture & Background Task Queues",
        "prereqs": "Day 65 (Celery Architecture & Task Queues)",
        "q1": "What are the 3 core components of a background task system (Producer, Broker, Worker)?",
        "q2": "Why should slow I/O operations (sending emails, processing payments, resizing images) never run synchronously in an HTTP view?",
        "q3": "What is a task broker (e.g. Redis or RabbitMQ)?",
        "desc": "Write `simulate_task_queue(tasks: list[dict], max_retries: int = 3) -> dict` that processes a list of tasks `[{'id': 1, 'attempts': 2}]`. If `attempts <= max_retries`, mark `'SUCCESS'`, otherwise mark `'DEAD_LETTER_QUEUE'`.",
        "stub": '''def simulate_task_queue(tasks: list[dict], max_retries: int = 3) -> dict:
    """
    Returns {'processed': count_success, 'failed': count_dlq}
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 66 Revision Challenge ---")
    tasks = [{"id": 1, "attempts": 1}, {"id": 2, "attempts": 4}, {"id": 3, "attempts": 3}]
    res = simulate_task_queue(tasks, max_retries=3)
    if res is None:
        print("[!] Function `simulate_task_queue` is not yet implemented.")
        return
    if res.get("processed") == 2 and res.get("failed") == 1:
        print("[+] Test Passed: Background task queue simulation verified.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Count tasks where `attempts <= max_retries` as processed, and others as failed.",
        "hint2": "Use `success = sum(1 for t in tasks if t.get('attempts', 1) <= max_retries); return {'processed': success, 'failed': len(tasks) - success}`.",
        "sol": '''def _reference_solution(tasks: list[dict], max_retries: int = 3) -> dict:
    success = sum(1 for t in tasks if t.get("attempts", 1) <= max_retries)
    return {"processed": success, "failed": len(tasks) - success}'''
    },
    67: {
        "topic": "Celery Retries, Exponential Backoff & Celery Beat",
        "prereqs": "Day 66 (Advanced Celery Retries & Beat)",
        "q1": "What is exponential backoff and why is it used when retrying network operations?",
        "q2": "What does Celery Beat do for scheduled/periodic tasks (cron jobs)?",
        "q3": "Why must background tasks be idempotent so retrying them does not cause duplicate side effects?",
        "desc": "Write `calculate_exponential_backoff(attempt: int, base_delay: int = 2, max_delay: int = 60) -> int` returning `min(base_delay ** attempt, max_delay)`.",
        "stub": '''def calculate_exponential_backoff(attempt: int, base_delay: int = 2, max_delay: int = 60) -> int:
    """
    Computes exponential backoff delay in seconds.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 67 Revision Challenge ---")
    d1 = calculate_exponential_backoff(1, base_delay=2, max_delay=60)
    d2 = calculate_exponential_backoff(3, base_delay=2, max_delay=60)
    d3 = calculate_exponential_backoff(8, base_delay=2, max_delay=60)
    if d1 is None:
        print("[!] Function `calculate_exponential_backoff` is not yet implemented.")
        return
    if (d1, d2, d3) == (2, 8, 60):
        print("[+] Test Passed: Exponential backoff calculations verified.")
    else:
        print(f"[-] Test Failed: Got {(d1, d2, d3)}")''',
        "hint1": "Compute `base_delay ** attempt` and return the minimum of that value and `max_delay`.",
        "hint2": "Use `return min(base_delay ** attempt, max_delay)`.",
        "sol": '''def _reference_solution(attempt: int, base_delay: int = 2, max_delay: int = 60) -> int:
    return min(base_delay ** attempt, max_delay)'''
    },
    68: {
        "topic": "Real-Time WebSockets vs HTTP & Django Channels",
        "prereqs": "Day 67 (Real-Time WebSockets & Channels)",
        "q1": "How does a persistent WebSocket connection differ from a standard HTTP request/response cycle?",
        "q2": "What is the purpose of Django Channels and ASGI (Asynchronous Server Gateway Interface)?",
        "q3": "What role does Redis play as a channel layer for broadcasting messages across WebSocket connections?",
        "desc": "Write `process_idempotent_event(processed_keys: set, idempotency_key: str, event_data: dict) -> tuple[bool, str]` which checks if `idempotency_key` has already been processed. If yes, returns `(False, 'Duplicate ignored')`. If no, records the key in the set and returns `(True, 'Processed')`.",
        "stub": '''def process_idempotent_event(processed_keys: set, idempotency_key: str, event_data: dict) -> tuple[bool, str]:
    """
    Prevents duplicate event execution using an idempotency key set.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 68 Revision Challenge ---")
    keys = set()
    res1 = process_idempotent_event(keys, "key-abc-123", {"order_id": 10})
    if res1 is None:
        print("[!] Function `process_idempotent_event` is not yet implemented.")
        return
    s1, m1 = res1
    s2, m2 = process_idempotent_event(keys, "key-abc-123", {"order_id": 10})
    if s1 is True and s2 is False and "Duplicate" in m2:
        print("[+] Test Passed: Idempotency deduplication logic confirmed.")
    else:
        print(f"[-] Test Failed: s1={s1}, s2={s2}, m2={m2}")''',
        "hint1": "Check if `idempotency_key in processed_keys`.",
        "hint2": "If in set: return `(False, 'Duplicate ignored')`. Else: `processed_keys.add(idempotency_key)` and return `(True, 'Processed')`.",
        "sol": '''def _reference_solution(processed_keys: set, idempotency_key: str, event_data: dict) -> tuple[bool, str]:
    if idempotency_key in processed_keys:
        return False, "Duplicate ignored"
    processed_keys.add(idempotency_key)
    return True, "Processed"'''
    },
    69: {
        "topic": "Webhooks, Payment Gateways & Cryptographic Verification",
        "prereqs": "Day 68 (Webhooks & Payment Gateways)",
        "q1": "How does an asynchronous webhook notification work from payment providers (Stripe, PayPal)?",
        "q2": "Why must webhook handlers verify the HMAC signature header before processing the request body?",
        "q3": "What is an idempotency key and how does it prevent duplicate charges?",
        "desc": "Write `verify_webhook_signature(payload_bytes: bytes, secret: str, signature_header: str) -> bool` using standard library `hmac` and `hashlib.sha256`.",
        "stub": '''import hmac
import hashlib

def verify_webhook_signature(payload_bytes: bytes, secret: str, signature_header: str) -> bool:
    """
    Verifies HMAC-SHA256 signature using hmac.compare_digest.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    import hmac, hashlib
    print("--- Running Day 69 Revision Challenge ---")
    secret = "my_webhook_secret_key"
    payload = b'{"event": "payment_succeeded", "amount": 100}'
    expected_sig = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    v1 = verify_webhook_signature(payload, secret, expected_sig)
    v2 = verify_webhook_signature(payload, secret, "tampered_signature")
    if v1 is None:
        print("[!] Function `verify_webhook_signature` is not yet implemented.")
        return
    if v1 is True and v2 is False:
        print("[+] Test Passed: HMAC webhook signature verification succeeded.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}")''',
        "hint1": "Compute the hex digest using `hmac.new(secret.encode(), payload_bytes, hashlib.sha256).hexdigest()`.",
        "hint2": "Use `hmac.compare_digest(computed_sig, signature_header)` to prevent timing attacks.",
        "sol": '''import hmac
import hashlib

def _reference_solution(payload_bytes: bytes, secret: str, signature_header: str) -> bool:
    computed = hmac.new(secret.encode(), payload_bytes, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature_header)'''
    },
    70: {
        "topic": "Linux CLI, Production WSGI & Gunicorn Deployment",
        "prereqs": "Day 69 (Production WSGI & Gunicorn)",
        "q1": "What is the difference between a development server (`runserver`) and a production WSGI server (`gunicorn`)?",
        "q2": "What are workers and threads in Gunicorn and how do you calculate optimal worker counts (`2 * CPU + 1`)?",
        "q3": "Why should production Django applications always run with `DEBUG = False` and defined `ALLOWED_HOSTS`?",
        "desc": "Write `parse_env_file_string(env_text: str) -> dict[str, str]` which parses a multi-line string in `.env` format, ignoring empty lines and comments (`#`), and stripping surrounding quotes from values.",
        "stub": '''def parse_env_file_string(env_text: str) -> dict[str, str]:
    """
    Parses key=value pairs into a Python dictionary.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 70 Revision Challenge ---")
    sample = """
    # Database config
    DB_NAME=production_db
    DB_PORT="5432"
    DEBUG=False
    """
    res = parse_env_file_string(sample)
    if res is None:
        print("[!] Function `parse_env_file_string` is not yet implemented.")
        return
    if res.get("DB_NAME") == "production_db" and res.get("DB_PORT") == "5432" and res.get("DEBUG") == "False":
        print("[+] Test Passed: Environment string parser confirmed.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Split into lines, strip each line, and ignore lines starting with '#' or empty lines.",
        "hint2": "Split on the first '=' with `line.split('=', 1)`. Strip quotes using `val.strip('\"').strip(\"'\")`.",
        "sol": '''def _reference_solution(env_text: str) -> dict[str, str]:
    out = {}
    for line in env_text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out'''
    },
    71: {
        "topic": "Dockerizing Backend Applications & Dockerfiles",
        "prereqs": "Day 70 (Dockerizing Application Environments)",
        "q1": "What is a Docker container versus a virtual machine?",
        "q2": "Why should production Docker containers run as a non-root user (`USER appuser`)?",
        "q3": "What is the role of `.dockerignore` in keeping image build context small and secure?",
        "desc": "Write `parse_database_url(url: str) -> dict[str, str]` parsing `postgres://user:password@hostname:5432/dbname` into `{'user': ..., 'password': ..., 'host': ..., 'port': ..., 'name': ...}` using `urllib.parse`.",
        "stub": '''import urllib.parse

def parse_database_url(url: str) -> dict[str, str]:
    """
    Parses a PostgreSQL URL into component dictionary.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 71 Revision Challenge ---")
    url = "postgres://dipesh:secret123@db.internal:5432/hotel_db"
    res = parse_database_url(url)
    if res is None:
        print("[!] Function `parse_database_url` is not yet implemented.")
        return
    if (res.get("user") == "dipesh" and res.get("password") == "secret123" and
        res.get("host") == "db.internal" and res.get("port") == "5432" and res.get("name") == "hotel_db"):
        print("[+] Test Passed: Database URL parser confirmed.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Use `urllib.parse.urlparse(url)` to extract `.username`, `.password`, `.hostname`, `.port`, and `.path`.",
        "hint2": "Use `p = urllib.parse.urlparse(url); return {'user': p.username, 'password': p.password, 'host': p.hostname, 'port': str(p.port), 'name': p.path.lstrip('/')}`.",
        "sol": '''import urllib.parse

def _reference_solution(url: str) -> dict[str, str]:
    p = urllib.parse.urlparse(url)
    return {
        "user": p.username or "",
        "password": p.password or "",
        "host": p.hostname or "",
        "port": str(p.port or 5432),
        "name": (p.path or "").lstrip("/")
    }'''
    },
    72: {
        "topic": "Docker Compose Multi-Container Orchestration",
        "prereqs": "Day 71 (Multi-Container Docker Compose)",
        "q1": "In Docker Compose, how do containers communicate over the internal network using service names (e.g. `db`, `redis`)?",
        "q2": "What is the purpose of volume mounts (`volumes:`) for database persistence in Docker Compose?",
        "q3": "What does `depends_on` control in a `docker-compose.yml` file?",
        "desc": "Write `verify_services_healthy(compose_services: list[dict]) -> tuple[bool, list[str]]` that inspects a list of service status dictionaries and ensures all required services (`web`, `db`, `redis`) have status `'healthy'`.",
        "stub": '''def verify_services_healthy(compose_services: list[dict]) -> tuple[bool, list[str]]:
    """
    Each dict: {'name': 'web', 'status': 'healthy'}
    Required services: ['web', 'db', 'redis']
    Returns (all_healthy, list_of_unhealthy_or_missing_services)
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 72 Revision Challenge ---")
    good = [
        {"name": "web", "status": "healthy"},
        {"name": "db", "status": "healthy"},
        {"name": "redis", "status": "healthy"}
    ]
    bad = [
        {"name": "web", "status": "healthy"},
        {"name": "db", "status": "starting"},
        {"name": "redis", "status": "unhealthy"}
    ]
    res1 = verify_services_healthy(good)
    if res1 is None:
        print("[!] Function `verify_services_healthy` is not yet implemented.")
        return
    r1, _ = res1
    r2, m2 = verify_services_healthy(bad)
    if r1 is True and r2 is False and "db" in m2 and "redis" in m2:
        print("[+] Test Passed: Docker Compose health check verification confirmed.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, m2={m2}")''',
        "hint1": "Convert `compose_services` into a dictionary `{s['name']: s['status']}`.",
        "hint2": "Check required services `['web', 'db', 'redis']`. If status != 'healthy', append to unhealthy list.",
        "sol": '''def _reference_solution(compose_services: list[dict]) -> tuple[bool, list[str]]:
    status_map = {s["name"]: s.get("status") for s in compose_services}
    required = ["web", "db", "redis"]
    unhealthy = [r for r in required if status_map.get(r) != "healthy"]
    return (len(unhealthy) == 0, unhealthy)'''
    },
    73: {
        "topic": "CI/CD Pipelines & GitHub Actions Workflows",
        "prereqs": "Day 72 (CI/CD Pipelines & GitHub Actions)",
        "q1": "What is Continuous Integration (CI) and why should linters and automated tests run on every pull request?",
        "q2": "What are GitHub Actions workflows, jobs, and steps?",
        "q3": "Why should database migrations be executed as an automated deployment step?",
        "desc": "Write `build_cache_key(prefix: str, **params) -> str` which creates a deterministic, sorted Redis cache key (e.g. `build_cache_key('products', cat='shoes', page=1)` -> `'products:cat=shoes:page=1'`).",
        "stub": '''def build_cache_key(prefix: str, **params) -> str:
    """
    Constructs deterministic cache key with sorted param items.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 73 Revision Challenge ---")
    k1 = build_cache_key("products", cat="shoes", page=1)
    k2 = build_cache_key("products", page=1, cat="shoes")
    if k1 is None:
        print("[!] Function `build_cache_key` is not yet implemented.")
        return
    if k1 == "products:cat=shoes:page=1" and k1 == k2:
        print("[+] Test Passed: Deterministic cache key generation confirmed.")
    else:
        print(f"[-] Test Failed: k1='{k1}', k2='{k2}'")''',
        "hint1": "Sort the keyword argument items by key.",
        "hint2": "Format each parameter as `{k}={v}` and join with ':' after `prefix`.",
        "sol": '''def _reference_solution(prefix: str, **params) -> str:
    parts = [prefix]
    for k in sorted(params):
        parts.append(f"{k}={params[k]}")
    return ":".join(parts)'''
    },
    74: {
        "topic": "Junior Backend System Design & Scaling",
        "prereqs": "Day 73 (Junior Backend System Design)",
        "q1": "What is the difference between vertical scaling (scale up) and horizontal scaling (scale out)?",
        "q2": "When would you recommend adding a Redis cache versus optimizing an SQL query and adding an index?",
        "q3": "How do database connection pools and read replicas improve backend throughput?",
        "desc": "Technical interview challenge: Write `top_customers(transactions: list[dict], n: int = 2) -> list[tuple[str, float]]` that aggregates total spending per customer from `transactions` (`[{'customer': 'Alice', 'amount': 150.0}, ...]`) and returns the top `n` customers as sorted `(customer_name, total_spent)` tuples (descending by total).",
        "stub": '''def top_customers(transactions: list[dict], n: int = 2) -> list[tuple[str, float]]:
    """
    Aggregates spending per customer and returns top n sorted tuples.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 74 Revision Challenge ---")
    txs = [
        {"customer": "Alice", "amount": 100.0},
        {"customer": "Bob", "amount": 250.0},
        {"customer": "Alice", "amount": 75.0},
        {"customer": "Carol", "amount": 500.0},
    ]
    res = top_customers(txs, n=2)
    if res is None:
        print("[!] Function `top_customers` is not yet implemented.")
        return
    expected = [("Carol", 500.0), ("Bob", 250.0)]
    if res == expected:
        print("[+] Test Passed: Interview data aggregation challenge verified.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Use a dictionary to aggregate sums: `totals[cust] = totals.get(cust, 0.0) + amt`.",
        "hint2": "Sort dictionary items by value descending: `sorted(totals.items(), key=lambda x: x[1], reverse=True)[:n]`.",
        "sol": '''def _reference_solution(transactions: list[dict], n: int = 2) -> list[tuple[str, float]]:
    totals = {}
    for t in transactions:
        c = t["customer"]
        totals[c] = totals.get(c, 0.0) + t["amount"]
    sorted_customers = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return sorted_customers[:n]'''
    },
    75: {
        "topic": "Technical Interview Bootcamp & Capstone Defense",
        "prereqs": "Day 74 (Technical Interview Bootcamp)",
        "q1": "How do you explain the architectural flow of a request from client to Nginx to Gunicorn to Django to PostgreSQL?",
        "q2": "What are the three most critical sections in a GitHub project README for hiring engineers?",
        "q3": "How do automated tests and CI/CD prove technical competence during junior developer interviews?",
        "desc": "Capstone checklist verifier: Write `verify_portfolio_readiness(checklist: dict[str, bool]) -> tuple[bool, list[str]]` verifying that all 6 required portfolio items (`['clean_git_history', 'automated_tests_passing', 'docker_compose_working', 'readme_with_architecture', 'env_example_provided', 'api_docs_available']`) are marked True.",
        "stub": '''def verify_portfolio_readiness(checklist: dict[str, bool]) -> tuple[bool, list[str]]:
    """
    Verifies that all 6 required checklist items are True.
    Returns (is_ready: bool, missing_or_incomplete_items: list[str])
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 75 Revision Challenge ---")
    complete_portfolio = {
        "clean_git_history": True,
        "automated_tests_passing": True,
        "docker_compose_working": True,
        "readme_with_architecture": True,
        "env_example_provided": True,
        "api_docs_available": True
    }
    partial_portfolio = dict(complete_portfolio)
    partial_portfolio["automated_tests_passing"] = False
    res1 = verify_portfolio_readiness(complete_portfolio)
    if res1 is None:
        print("[!] Function `verify_portfolio_readiness` is not yet implemented.")
        return
    r1, _ = res1
    r2, m2 = verify_portfolio_readiness(partial_portfolio)
    if r1 is True and r2 is False and "automated_tests_passing" in m2:
        print("[+] Test Passed: Capstone portfolio readiness verifier confirmed.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, m2={m2}")''',
        "hint1": "Define the list of 6 required keys and check each one against `checklist.get(k)`.",
        "hint2": "Use `missing = [k for k in required if not checklist.get(k, False)]; return (len(missing) == 0, missing)`.",
        "sol": '''def _reference_solution(checklist: dict[str, bool]) -> tuple[bool, list[str]]:
    required = [
        "clean_git_history",
        "automated_tests_passing",
        "docker_compose_working",
        "readme_with_architecture",
        "env_example_provided",
        "api_docs_available"
    ]
    missing = [k for k in required if not checklist.get(k, False)]
    return (len(missing) == 0, missing)'''
    }
}


def build_revision_file_content(day_num: int, data: dict) -> str:
    return f'''"""
============================================================
DAY {day_num} REVISION SESSION (~10–15 MINUTES)
Topic: {data["topic"]}
============================================================

Verified Prerequisites: {data["prereqs"]}

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
# 1. {data["q1"]}
#
# 2. {data["q2"]}
#
# 3. {data["q3"]}


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# {data["desc"]}

{data["stub"]}


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
{data["runner"]}

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: {data["hint1"]}
# Hint 2: {data["hint2"]}


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
{data["sol"]}


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
'''


def apply_all():
    base_dir = "python basic"
    day_dirs = {int(re.search(r'\d+', d).group()): d for d in os.listdir(base_dir) if d.startswith("Day")}

    updated_count = 0
    for day_num, data in DAYS_DATA.items():
        if day_num not in day_dirs:
            print(f"[!] Warning: directory for Day {day_num} not found!")
            continue
        day_folder = os.path.join(base_dir, day_dirs[day_num])
        rev_path = os.path.join(day_folder, "revision.py")
        content = build_revision_file_content(day_num, data)

        with open(rev_path, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1

    print(f"[+] Successfully wrote and updated {updated_count} revision.py files (Days 32–75).")


if __name__ == "__main__":
    apply_all()
