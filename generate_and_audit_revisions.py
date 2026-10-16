"""
generate_and_audit_revisions.py
-------------------------------
Updates all revision.py files for Days 33–75 with:
- 3 targeted recall questions strictly from past material.
- 1 practical, self-contained Python backend challenge with ASCII test runner.
- Hint 1 (conceptual clue) AND Hint 2 (direct hint/pointer).
- Hidden reference solution.
- Self-assessment checklist (4 honest outcomes).
- 15-minute attempt rule.
- Windows cp1252 / ASCII safe outputs.
"""

import os
import re

DAYS_DATA = {
    33: {
        "topic": "Parameterized Queries, SQL Aggregations & Context Managers",
        "prereqs": "Days 1–32 (Day 32 Drivers, Day 29 Aggregations, Day 24 Context Managers)",
        "q1": "Why is passing `%s` or `?` with a tuple to cursor.execute() safe against SQL injection, while Python f-strings are not?",
        "q2": "What is the difference between WHERE and HAVING in SQL aggregation queries?",
        "q3": "What does Python's `with` statement guarantee when handling database connections or transactions?",
        "desc": "Fix the SQL injection vulnerability in `search_users(conn, email_prefix)`. Replace string concatenation with parameterized execution.",
        "stub": '''def search_users(conn, email_prefix: str) -> list:
    """
    VULNERABLE CODE TO FIX:
    cur = conn.cursor()
    cur.execute("SELECT id, email FROM users WHERE email LIKE '" + email_prefix + "%';")
    return cur.fetchall()
    """
    # WRITE YOUR FIXED CODE HERE:
    pass''',
        "runner": '''def run_test():
    import sqlite3
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT);")
    cur.execute("INSERT INTO users VALUES (1, 'dipesh@example.com'), (2, 'dev@example.com');")
    conn.commit()

    print("--- Running Day 33 Revision Challenge ---")
    res = search_users(conn, "dipesh")
    if res is None:
        print("[!] Function `search_users` is not yet implemented. Complete the exercise above and re-run!")
        conn.close()
        return

    if len(res) == 1 and res[0][1] == 'dipesh@example.com':
        print("[+] Test Passed: Parameterized search returned expected record.")
    else:
        print(f"[-] Test Failed: Unexpected return: {res}")
    conn.close()''',
        "hint1": "The database driver escapes characters when you pass a query template with a placeholder alongside a tuple of arguments.",
        "hint2": "Use `LIKE ?` in SQLite (or `%s` in PostgreSQL) and pass `(f'{email_prefix}%',)` as the parameter tuple.",
        "sol": '''def _reference_solution(conn, email_prefix: str) -> list:
    cur = conn.cursor()
    cur.execute("SELECT id, email FROM users WHERE email LIKE ?;", (f"{email_prefix}%",))
    return cur.fetchall()'''
    },
    34: {
        "topic": "B-Tree Indexes, Composite Index Rules & Dict Operations",
        "prereqs": "Days 1–33 (Day 33 B-Tree Indexing, Day 9 Dictionaries)",
        "q1": "Why does a B-Tree index allow O(log n) lookups instead of O(n) table scans?",
        "q2": "In a composite index on `(status, created_at)`, why can a query filter on `status` alone use the index, but a query on `created_at` alone cannot?",
        "q3": "What is the difference between `dict.get('key')` and `dict['key']` when the key is missing?",
        "desc": "Write `is_using_index(plan_steps: list[str]) -> bool` which inspects a list of EXPLAIN plan step strings and returns True if any step uses an index and False if it only does sequential scans.",
        "stub": '''def is_using_index(plan_steps: list[str]) -> bool:
    """
    Returns True if any step in plan_steps contains 'INDEX' (case-insensitive),
    False otherwise.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 34 Revision Challenge ---")
    plan1 = ["Seq Scan on users (cost=0.00..35.50 rows=2550 width=36)"]
    plan2 = ["Bitmap Index Scan on idx_users_email (cost=0.00..4.30 rows=10 width=0)"]
    
    r1 = is_using_index(plan1)
    r2 = is_using_index(plan2)
    if r1 is None or r2 is None:
        print("[!] Function `is_using_index` is not yet implemented.")
        return
    if r1 is False and r2 is True:
        print("[+] Test Passed: Correctly identified Sequential Scan vs Index Scan.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}")''',
        "hint1": "Iterate through each step string and check for the substring 'INDEX'.",
        "hint2": "Use `any('INDEX' in step.upper() for step in plan_steps)`.",
        "sol": '''def _reference_solution(plan_steps: list[str]) -> bool:
    return any("INDEX" in step.upper() for step in plan_steps)'''
    },
    35: {
        "topic": "Database Normalization, Foreign Keys & Encapsulation",
        "prereqs": "Days 1–34 (Day 34 Normalization & FKs, Day 19 @property Encapsulation)",
        "q1": "What is 1NF (atomic columns) vs 2NF (removing partial dependencies) vs 3NF (removing transitive dependencies)?",
        "q2": "What happens when you delete a parent row if the foreign key specifies `ON DELETE CASCADE` vs `ON DELETE RESTRICT`?",
        "q3": "Why do we use `@property` and a setter in Python instead of allowing direct public attribute mutation?",
        "desc": "Implement a `Product` class with a protected attribute `_stock`. Use `@property` for `stock`, and in `@stock.setter`, raise `ValueError` if the new stock is negative.",
        "stub": '''class Product:
    def __init__(self, name: str, initial_stock: int):
        self.name = name
        if initial_stock < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = initial_stock

    # Implement @property stock and @stock.setter below:
    pass''',
        "runner": '''def run_test():
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
        print(f"[-] Test error: {e}")''',
        "hint1": "Define a getter method decorated with `@property` and a setter decorated with `@stock.setter`.",
        "hint2": "In setter: `if val < 0: raise ValueError(...)` else `self._stock = val`.",
        "sol": '''class _ReferenceProduct:
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
        self._stock = val'''
    },
    36: {
        "topic": "Concurrency Anomalies, Row Locking & SQL Subqueries",
        "prereqs": "Days 1–35 (Day 35 Concurrency & ACID, Day 31 SQL Subqueries)",
        "q1": "What is a 'Lost Update' anomaly and how does `SELECT ... FOR UPDATE` prevent it?",
        "q2": "What are the four ACID properties, and which one guarantees that intermediate states are never visible?",
        "q3": "Why is an atomic conditional update like `UPDATE accounts SET balance = balance - 50 WHERE id = 1 AND balance >= 50;` safer than reading first and writing later?",
        "desc": "Write `atomic_deduct_stock(conn, product_id, qty)` executing: `UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?`. Return True if rowcount > 0, False otherwise.",
        "stub": '''def atomic_deduct_stock(conn, product_id: int, qty: int) -> bool:
    """
    Executes conditional atomic update.
    Returns True if stock was deducted, False if insufficient stock or product not found.
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
    conn.close()''',
        "hint1": "Run the parameterized UPDATE statement and check `cur.rowcount`.",
        "hint2": "If `cur.rowcount > 0`: `conn.commit()` and return True; else return False.",
        "sol": '''def _reference_solution(conn, product_id: int, qty: int) -> bool:
    cur = conn.cursor()
    cur.execute("UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?;", (qty, product_id, qty))
    conn.commit()
    return cur.rowcount > 0'''
    },
    37: {
        "topic": "JSONB vs Relational Schemas, SQL Joins & List Comprehensions",
        "prereqs": "Days 1–36 (Day 36 PostgreSQL Data Types, Day 30 Joins, Day 8 List Comprehensions)",
        "q1": "When is storing data in a JSON/JSONB column appropriate versus normalizing into separate relational tables?",
        "q2": "What is the difference between a LEFT JOIN and an INNER JOIN when querying orders with optional discount codes?",
        "q3": "How does a Python list comprehension offer cleaner, more readable filtering compared to an explicit for-loop?",
        "desc": "Given a list of user dictionaries representing parsed JSON records, write `get_active_admin_emails(users_data: list[dict]) -> list[str]` using a list comprehension.",
        "stub": '''def get_active_admin_emails(users_data: list[dict]) -> list[str]:
    """
    Returns a list of emails for users who have role == 'ADMIN' and is_active is True.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 37 Revision Challenge ---")
    users = [
        {"email": "alice@admin.com", "role": "ADMIN", "is_active": True},
        {"email": "bob@dev.com", "role": "STAFF", "is_active": True},
        {"email": "carol@admin.com", "role": "ADMIN", "is_active": False},
        {"email": "dave@admin.com", "role": "ADMIN", "is_active": True},
    ]
    res = get_active_admin_emails(users)
    if res is None:
        print("[!] Function `get_active_admin_emails` is not yet implemented.")
        return
    if res == ["alice@admin.com", "dave@admin.com"]:
        print("[+] Test Passed: Active admin emails filtered correctly.")
    else:
        print(f"[-] Test Failed: Got {res}")''',
        "hint1": "Filter each dictionary `u` where `u.get('role') == 'ADMIN'` and `u.get('is_active') is True`.",
        "hint2": "Use `[u['email'] for u in users_data if u.get('role') == 'ADMIN' and u.get('is_active')]`.",
        "sol": '''def _reference_solution(users_data: list[dict]) -> list[str]:
    return [u["email"] for u in users_data if u.get("role") == "ADMIN" and u.get("is_active")]'''
    },
    38: {
        "topic": "HTTP Request-Response Anatomy, Headers & Git Conflicts",
        "prereqs": "Days 1–37 (Day 37 HTTP Anatomy, Day 33 Indexing, Day 26 Git Collaboration)",
        "q1": "What are the three main components of an HTTP Request message (start line, headers, body)?",
        "q2": "Why are HTTP header names considered case-insensitive according to RFC specifications (e.g., `Content-Type` vs `content-type`)?",
        "q3": "In Git, what markers (`<<<<<<<`, `=======`, `>>>>>>>`) appear in a file during a merge conflict?",
        "desc": "Write `get_header_value(headers: dict, target_header: str) -> str | None` which retrieves the value of a header regardless of whether it was stored in lowercase, uppercase, or mixed case.",
        "stub": '''def get_header_value(headers: dict, target_header: str) -> str | None:
    """
    Retrieves the value of target_header from headers dictionary in a case-insensitive way.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 38 Revision Challenge ---")
    headers = {"Content-Type": "application/json", "Authorization": "Bearer token123"}
    v1 = get_header_value(headers, "content-type")
    v2 = get_header_value(headers, "AUTHORIZATION")
    v3 = get_header_value(headers, "Accept")
    if v1 is None and v2 is None:
        print("[!] Function `get_header_value` is not yet implemented.")
        return
    if v1 == "application/json" and v2 == "Bearer token123" and v3 is None:
        print("[+] Test Passed: Case-insensitive header lookup succeeded.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}, v3={v3}")''',
        "hint1": "Compare lowercased keys with `target_header.lower()`.",
        "hint2": "Iterate through `headers.items()`: `for k, v in headers.items(): if k.lower() == target_header.lower(): return v`.",
        "sol": '''def _reference_solution(headers: dict, target_header: str) -> str | None:
    target = target_header.lower()
    for k, v in headers.items():
        if k.lower() == target:
            return v
    return None'''
    },
    39: {
        "topic": "HTTP Idempotency, HTTP Status Codes & Rollback",
        "prereqs": "Days 1–38 (Day 38 HTTP Methods & Status Codes, Day 31/35 Transactions)",
        "q1": "What does it mean for an HTTP method to be 'idempotent', and why is `GET` and `PUT` idempotent while `POST` is not?",
        "q2": "What are the standard HTTP status codes for: Success (`200`), Resource Created (`201`), Bad Request (`400`), Unauthorized (`401`), Forbidden (`403`), and Not Found (`404`)?",
        "q3": "If a transaction raises an exception midway, why must `conn.rollback()` be invoked before releasing or reusing the connection?",
        "desc": "Write `determine_status_code(method: str, resource_found: bool, is_valid_payload: bool) -> int` that maps request parameters to the standard REST status code.",
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
    print("--- Running Day 39 Revision Challenge ---")
    c1 = determine_status_code("POST", True, True)    # 201
    c2 = determine_status_code("GET", False, True)    # 404
    c3 = determine_status_code("POST", True, False)   # 400
    c4 = determine_status_code("GET", True, True)     # 200
    if c1 is None:
        print("[!] Function `determine_status_code` is not yet implemented.")
        return
    if (c1, c2, c3, c4) == (201, 404, 400, 200):
        print("[+] Test Passed: Status codes correctly resolved.")
    else:
        print(f"[-] Test Failed: Got {(c1, c2, c3, c4)}")''',
        "hint1": "Handle the failure cases first (invalid payload -> 400, not found on GET/DELETE -> 404).",
        "hint2": "Check `if not is_valid_payload: return 400`, then `if not resource_found and method in ('GET', 'DELETE'): return 404`, then `if method == 'POST': return 201`.",
        "sol": '''def _reference_solution(method: str, resource_found: bool, is_valid_payload: bool) -> int:
    if not is_valid_payload:
        return 400
    if not resource_found and method.upper() in ("GET", "DELETE"):
        return 404
    if method.upper() == "POST":
        return 201
    return 200'''
    },
    40: {
        "topic": "RESTful URI Conventions, HTTP Methods & Virtual Environments",
        "prereqs": "Days 1–39 (Day 39 REST URI Conventions, Day 38 HTTP Methods, Day 24 Venvs)",
        "q1": "Why do RESTful APIs use plural nouns for URIs (e.g. `/api/v1/orders/`) rather than verbs (e.g. `/api/v1/getOrders`)?",
        "q2": "How does HTTP method choice (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) express the intended action without embedding verbs in the URL path?",
        "q3": "Why is it vital to keep `.venv/` in `.gitignore` rather than committing it to Git?",
        "desc": "Write `is_restful_uri(path: str) -> bool` returning False if the path contains action verbs like 'get', 'create', 'delete', or 'update', and True if it adheres to noun-based REST conventions.",
        "stub": '''def is_restful_uri(path: str) -> bool:
    """
    Returns False if any path segment contains 'get', 'create', 'delete', or 'update' (case-insensitive),
    True otherwise.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 40 Revision Challenge ---")
    bad = is_restful_uri("/api/v1/users/create")
    good = is_restful_uri("/api/v1/users/123")
    if bad is None or good is None:
        print("[!] Function `is_restful_uri` is not yet implemented.")
        return
    if bad is False and good is True:
        print("[+] Test Passed: RESTful URI pattern detected cleanly.")
    else:
        print(f"[-] Test Failed: bad={bad}, good={good}")''',
        "hint1": "Split the path by '/' and check if any forbidden verb is present in lowercased segments.",
        "hint2": "Use `verbs = {'get', 'create', 'delete', 'update'}` and `any(v in segment.lower() for v in verbs for segment in path.split('/'))`.",
        "sol": '''def _reference_solution(path: str) -> bool:
    verbs = {"get", "create", "delete", "update"}
    segments = [s.lower() for s in path.strip("/").split("/")]
    return not any(any(v in s for v in verbs) for s in segments)'''
    },
    41: {
        "topic": "Django MVT Pattern, Environment Variables & Python Decorators",
        "prereqs": "Days 1–40 (Day 40 Django Intro & Settings, Day 22 Decorators)",
        "q1": "What are the distinct responsibilities of Model, View, and Template in Django's MVT pattern?",
        "q2": "Why must SECRET_KEY and DB credentials be read from environment variables rather than hardcoded in `settings.py`?",
        "q3": "How does a Python decorator wrap and modify the execution of an underlying view function?",
        "desc": "Write a decorator `require_auth` that inspects a simulated `request` dict. If `request.get('is_authenticated')` is True, it calls the function; otherwise, it returns `{'error': 'Unauthorized', 'status': 401}`.",
        "stub": '''import functools

def require_auth(func):
    """
    Decorator that checks if request['is_authenticated'] is True.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 41 Revision Challenge ---")
    wrapper = require_auth(lambda r: {"status": 200})
    if wrapper is None:
        print("[!] Decorator `require_auth` is not yet implemented.")
        return

    @require_auth
    def profile_view(request):
        return {"data": f"Welcome user {request.get('user_id')}", "status": 200}

    r_anon = profile_view({"is_authenticated": False})
    r_user = profile_view({"is_authenticated": True, "user_id": 42})
    if r_anon.get("status") == 401 and r_user.get("status") == 200:
        print("[+] Test Passed: require_auth decorator enforced access control.")
    else:
        print(f"[-] Test Failed: anon={r_anon}, user={r_user}")''',
        "hint1": "Use `functools.wraps(func)` and define an inner wrapper that accepts `request, *args, **kwargs`.",
        "hint2": "Inside wrapper: `if not request.get('is_authenticated'): return {'error': 'Unauthorized', 'status': 401}` else return `func(request, *args, **kwargs)`.",
        "sol": '''import functools

def _reference_solution(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.get("is_authenticated"):
            return {"error": "Unauthorized", "status": 401}
        return func(request, *args, **kwargs)
    return wrapper'''
    },
    42: {
        "topic": "URL Converters, FBVs vs CBVs & SQL Aggregations",
        "prereqs": "Days 1–41 (Day 41 URL Routing & Views, Day 29 SQL Aggregations)",
        "q1": "In Django `path('posts/<int:post_id>/', ...)`, what does the `<int:...>` path converter do?",
        "q2": "When is a Function-Based View (FBV) preferred over a Class-Based View (CBV) for beginners?",
        "q3": "In SQL, what is the role of `GROUP BY` when computing summary statistics like `AVG(price)` per category?",
        "desc": "Write `extract_id_from_path(path: str) -> int | None` that simulates Django's `<int:pk>` path converter for URLs formatted like `/api/v1/items/<id>/`.",
        "stub": '''import re

def extract_id_from_path(path: str) -> int | None:
    """
    Extracts integer ID from path segment: '/items/<id>/'. Returns int or None.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 42 Revision Challenge ---")
    i1 = extract_id_from_path("/api/v1/items/456/")
    i2 = extract_id_from_path("/api/v1/items/invalid/")
    if i1 is None and i2 is None:
        print("[!] Function `extract_id_from_path` is not yet implemented.")
        return
    if i1 == 456 and i2 is None:
        print("[+] Test Passed: Path integer converter simulated correctly.")
    else:
        print(f"[-] Test Failed: i1={i1}, i2={i2}")''',
        "hint1": "Use `re.search(r'/items/(\\d+)/', path)` or parse path segments.",
        "hint2": "Match `re.search(r'/items/(\\d+)', path)`: if match, return `int(match.group(1))` else None.",
        "sol": '''import re

def _reference_solution(path: str) -> int | None:
    m = re.search(r'/items/(\\d+)/?', path)
    return int(m.group(1)) if m else None'''
    },
    43: {
        "topic": "Relational Schemas, Model Fields & OOP Inheritance",
        "prereqs": "Days 1–42 (Day 42 Templates, Day 34 Relational Schemas, Day 14 OOP Inheritance)",
        "q1": "How does Django translate Python model class attributes into SQL column definitions?",
        "q2": "What is the difference between `null=True` (database level) and `blank=True` (form validation level)?",
        "q3": "How does class inheritance in `class Product(models.Model)` allow Django models to inherit database behavior?",
        "desc": "Write `validate_model_price(price: float) -> tuple[bool, str]` that ensures a price is a positive number, does not exceed 100000.0, and has at most 2 decimal places.",
        "stub": '''def validate_model_price(price: float) -> tuple[bool, str]:
    """
    Validates model price field:
    - price > 0
    - price <= 100000.0
    - at most 2 decimal places
    Returns (True, "Valid") or (False, "Error message")
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 43 Revision Challenge ---")
    res1 = validate_model_price(49.99)
    if res1 is None:
        print("[!] Function `validate_model_price` is not yet implemented.")
        return
    v1, _ = res1
    v2, _ = validate_model_price(-5.0)
    v3, _ = validate_model_price(19.999)
    if v1 is True and v2 is False and v3 is False:
        print("[+] Test Passed: Model field price constraints validated.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}, v3={v3}")''',
        "hint1": "Check price range first, then check decimals via string representation or `round(price, 2) == price`.",
        "hint2": "Use `if price <= 0 or price > 100000: return False, ...` and `if round(price, 2) != price: return False, ...`.",
        "sol": '''def _reference_solution(price: float) -> tuple[bool, str]:
    if price <= 0:
        return False, "Price must be strictly positive"
    if price > 100000.0:
        return False, "Price exceeds maximum threshold"
    if round(price, 2) != price:
        return False, "Price cannot have more than 2 decimal places"
    return True, "Valid"'''
    },
    44: {
        "topic": "Django Migrations, SQL DDL & Database Constraints",
        "prereqs": "Days 1–43 (Day 43 Django Models & Migrations, Day 34 Database Constraints)",
        "q1": "What is the difference between `makemigrations` (creates Python migration file) and `migrate` (executes SQL DDL against the DB)?",
        "q2": "Why should you never manually alter production database tables using raw SQL when using Django migrations?",
        "q3": "What does a `UNIQUE` constraint prevent at the database level?",
        "desc": "Write `validate_field_constraints(data: dict, schema: dict) -> tuple[bool, list[str]]` that checks if all required schema fields are present and non-null in data.",
        "stub": '''def validate_field_constraints(data: dict, schema: dict) -> tuple[bool, list[str]]:
    """
    schema format: {'fields': {'title': {'required': True}, 'slug': {'required': True}}}
    Returns (is_valid, list_of_missing_fields)
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 44 Revision Challenge ---")
    schema = {"fields": {"title": {"required": True}, "slug": {"required": True}, "desc": {"required": False}}}
    valid_data = {"title": "Post 1", "slug": "post-1"}
    invalid_data = {"title": "Post 2"}
    
    res1 = validate_field_constraints(valid_data, schema)
    if res1 is None:
        print("[!] Function `validate_field_constraints` is not yet implemented.")
        return
    r1, m1 = res1
    r2, m2 = validate_field_constraints(invalid_data, schema)
    if r1 is True and r2 is False and "slug" in m2:
        print("[+] Test Passed: Schema constraint validator succeeded.")
    else:
        print(f"[-] Test Failed: r1={r1}, r2={r2}, m2={m2}")''',
        "hint1": "Iterate through `schema['fields']` and check if `conf.get('required')` is True.",
        "hint2": "If field not in data or data[field] is None: append field name to missing list.",
        "sol": '''def _reference_solution(data: dict, schema: dict) -> tuple[bool, list[str]]:
    missing = []
    for f, conf in schema.get("fields", {}).items():
        if conf.get("required") and (f not in data or data[f] is None):
            missing.append(f)
    return (len(missing) == 0, missing)'''
    },
    45: {
        "topic": "QuerySet Lazy Evaluation, Q Objects & SQL Joins",
        "prereqs": "Days 1–44 (Day 44 ORM Queries & Q Objects, Day 30 SQL Joins)",
        "q1": "What does 'lazy evaluation' mean for Django QuerySets, and what triggers an actual SQL execution (iteration, slicing, len)?",
        "q2": "How do Django `Q` objects allow OR queries (e.g. `Q(status='A') | Q(status='B')`)?",
        "q3": "Why is filtering in the database using QuerySets vastly more efficient than fetching all records and filtering in Python?",
        "desc": "Write `simulate_q_filter(items: list[dict], cat: str = None, min_price: float = None) -> list[dict]` matching items where category matches OR price >= min_price.",
        "stub": '''def simulate_q_filter(items: list[dict], cat: str = None, min_price: float = None) -> list[dict]:
    """
    Simulates Django Q(category=cat) | Q(price__gte=min_price)
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 45 Revision Challenge ---")
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
        "hint1": "For each item, test if it matches condition 1 OR condition 2.",
        "hint2": "Use `[i for i in items if (cat and i.get('category') == cat) or (min_price is not None and i.get('price', 0) >= min_price)]`.",
        "sol": '''def _reference_solution(items: list[dict], cat: str = None, min_price: float = None) -> list[dict]:
    return [
        i for i in items
        if (cat and i.get("category") == cat) or (min_price is not None and i.get("price", 0) >= min_price)
    ]'''
    },
    46: {
        "topic": "N+1 Query Problem, select_related & B-Tree Index Traversal",
        "prereqs": "Days 1–45 (Day 45 Prefetching & ForeignKeys, Day 33 Indexing)",
        "q1": "What is the N+1 query problem in ORMs, and how does `select_related` fix it using an SQL JOIN?",
        "q2": "What is the difference between `select_related` (single-valued FKs/OneToOne) and `prefetch_related` (ManyToMany/reverse FKs)?",
        "q3": "How does an indexed foreign key column speed up JOIN lookups in PostgreSQL?",
        "desc": "Write `count_simulated_queries(item_count: int, use_select_related: bool) -> int` returning the number of database queries executed when accessing a foreign key attribute for N items.",
        "stub": '''def count_simulated_queries(item_count: int, use_select_related: bool) -> int:
    """
    If use_select_related is True: executes exactly 1 query (with SQL JOIN).
    If False: executes 1 initial query + 1 query per item (1 + N queries).
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 46 Revision Challenge ---")
    q_opt = count_simulated_queries(50, True)
    q_naive = count_simulated_queries(50, False)
    if q_opt is None:
        print("[!] Function `count_simulated_queries` is not yet implemented.")
        return
    if q_opt == 1 and q_naive == 51:
        print("[+] Test Passed: N+1 query count calculation verified.")
    else:
        print(f"[-] Test Failed: q_opt={q_opt}, q_naive={q_naive}")''',
        "hint1": "If select_related is enabled, only 1 SQL JOIN query is sent.",
        "hint2": "Return 1 if `use_select_related` else `item_count + 1`.",
        "sol": '''def _reference_solution(item_count: int, use_select_related: bool) -> int:
    return 1 if use_select_related else item_count + 1'''
    },
    47: {
        "topic": "Django Relationships, related_name & String Validation",
        "prereqs": "Days 1–46 (Day 46 CRUD Application & Relationships, Day 23 String Processing)",
        "q1": "What does the `related_name` argument in a `ForeignKey` define on the reverse model?",
        "q2": "If model `Author` has many `Books`, how do you access the books from an author instance if `related_name='books'`?",
        "q3": "Why is regular expression pattern matching useful for validating standardized strings like SKUs or phone numbers?",
        "desc": "Write `validate_sku(sku: str) -> bool` that verifies an SKU follows the format: 3 uppercase letters, a hyphen, and 3 digits (e.g. 'ABC-123').",
        "stub": '''import re

def validate_sku(sku: str) -> bool:
    """
    Returns True if sku matches ^[A-Z]{3}-\\d{3}$, False otherwise.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 47 Revision Challenge ---")
    v1 = validate_sku("PRD-404")
    v2 = validate_sku("prd-404")
    v3 = validate_sku("PRD404")
    if v1 is None:
        print("[!] Function `validate_sku` is not yet implemented.")
        return
    if v1 is True and v2 is False and v3 is False:
        print("[+] Test Passed: SKU pattern validator succeeded.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}, v3={v3}")''',
        "hint1": "Use `re.fullmatch(r'^[A-Z]{3}-\\d{3}$', sku)`.",
        "hint2": "Return `bool(re.fullmatch(r'^[A-Z]{3}-\\d{3}$', sku))`.",
        "sol": '''import re

def _reference_solution(sku: str) -> bool:
    return bool(re.fullmatch(r'^[A-Z]{3}-\\d{3}$', sku))'''
    },
    48: {
        "topic": "Django Form Validation, cleaned_data & Constraints",
        "prereqs": "Days 1–47 (Day 47 Django Forms & clean_* Validation, Day 34 Database Constraints)",
        "q1": "In Django forms, what is the purpose of the `clean_<fieldname>()` and `clean()` methods?",
        "q2": "What dictionary does Django populate after running form validation, and what happens if validation fails?",
        "q3": "Why must validation happen both at the form/serializer level and at the database constraint level?",
        "desc": "Write `clean_date_range(cleaned_data: dict) -> tuple[bool, str]` ensuring `start_day` < `end_day` where values are integers.",
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
        "topic": "Session Security, Cookies & @login_required",
        "prereqs": "Days 1–48 (Day 48 Authentication & Sessions, Day 15 OOP Inheritance)",
        "q1": "How does Django session authentication use a session cookie (`sessionid`) to identify the user on subsequent requests?",
        "q2": "Why should session cookies be configured with `HttpOnly` and `Secure` flags in production?",
        "q3": "What does the `@login_required` decorator do when an unauthenticated user visits a protected view?",
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
        "topic": "Custom User Models, Form Validation & SQL Joins",
        "prereqs": "Days 1–49 (Day 49 Authorization & Custom User Models, Day 47 Forms, Day 30 Joins)",
        "q1": "Why does the official Django documentation recommend creating a custom user model (extending `AbstractBaseUser` or `AbstractUser`) at the start of a project?",
        "q2": "Why should critical business logic be placed in explicit service functions or model methods rather than in Django signals?",
        "q3": "In SQL, what is the effect of an `INNER JOIN` when an employee record has no matching department?",
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
        "topic": "Django ORM QuerySet Optimization & REST JSON Responses",
        "prereqs": "Days 1–50 (Day 45 ORM Prefetching, Day 37/39 HTTP JSON Responses)",
        "q1": "What is the difference between serialization (Python object -> JSON/dict) and deserialization (JSON/dict -> Python object)?",
        "q2": "Why does `only('id', 'name')` or `values('id', 'name')` improve query performance over fetching complete model instances when building lightweight API responses?",
        "q3": "What HTTP status code and response structure should be returned when an incoming JSON payload fails validation?",
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
        "topic": "DRF ModelSerializer & Field Validation",
        "prereqs": "Days 1–51 (Day 51 DRF Serialization, Day 31/35 Transactions)",
        "q1": "In DRF, how does `ModelSerializer` automatically generate serializer fields from model definitions?",
        "q2": "What is the difference between serializer field-level validation (`validate_<field>`) and object-level validation (`validate`)?",
        "q3": "Why is `transaction.atomic()` important when a serializer's `create()` method writes to multiple related database tables?",
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
        "topic": "Writable Nested Serializers & HTTP Methods",
        "prereqs": "Days 1–52 (Day 52 Nested Serializers, Day 38 HTTP Methods, Day 41 CBVs)",
        "q1": "Why does DRF require custom `create()` and `update()` overrides when handling writable nested serializers?",
        "q2": "What HTTP method should be used for full resource replacement (`PUT`) vs partial updates (`PATCH`)?",
        "q3": "In DRF Class-Based Views, how does `get_serializer_class()` allow using different serializers for list vs detail views?",
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
        "topic": "ModelViewSet Routing, Session Auth vs Token Auth",
        "prereqs": "Days 1–53 (Day 53 ViewSets & Routers, Day 48 Session Auth, Day 37 Auth Headers)",
        "q1": "What standard actions (`list`, `create`, `retrieve`, `update`, `partial_update`, `destroy`) does DRF's `ModelViewSet` provide automatically?",
        "q2": "What is the difference between session authentication (cookie-based, stateful on server) and token authentication (header-based, bearer token)?",
        "q3": "How does DRF's `DefaultRouter` generate RESTful URL patterns for a registered ViewSet?",
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
        "topic": "JWT Access vs Refresh Tokens & Role-Based Access Control",
        "prereqs": "Days 1–54 (Day 54 JWT Auth, Day 49 Authorization & Roles)",
        "q1": "What is the role of an Access Token (short-lived, sent with every request) versus a Refresh Token (long-lived, used to acquire new access tokens)?",
        "q2": "Why is storing JWT access tokens in browser local storage vulnerable to XSS attacks?",
        "q3": "In Role-Based Access Control (RBAC), how do roles (e.g. `admin`, `staff`, `customer`) simplify permission management?",
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
        "topic": "Custom Permissions (BasePermission) & Query Filtering",
        "prereqs": "Days 1–55 (Day 55 Object Permissions, Day 39 REST Query Params)",
        "q1": "In DRF `BasePermission`, what is the difference between `has_permission(request, view)` and `has_object_permission(request, view, obj)`?",
        "q2": "What are the HTTP 'SAFE_METHODS' in DRF (`GET`, `HEAD`, `OPTIONS`)?",
        "q3": "Why should object-level permissions allow read access for safe methods while restricting write access to the object's owner or staff?",
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
    
    p1 = has_object_permission(other, obj, "GET")    # True (safe method)
    p2 = has_object_permission(other, obj, "DELETE") # False (not owner)
    p3 = has_object_permission(owner, obj, "PUT")    # True (is owner)
    p4 = has_object_permission(staff, obj, "DELETE") # True (is staff)
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
        "topic": "django-filter, Pagination & API Error Codes",
        "prereqs": "Days 1–56 (Day 56 Filtering & Pagination, Day 38 Error Codes)",
        "q1": "How does `django-filter` simplify URL filtering without writing manual `filter()` queries for every parameter in the view?",
        "q2": "What are the advantages of PageNumberPagination vs CursorPagination when working with large datasets?",
        "q3": "Why is returning structured error dictionaries (e.g. `{'detail': 'Not found'}`) critical for frontend API clients?",
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
        "topic": "OpenAPI / Swagger Documentation & API Envelopes",
        "prereqs": "Days 1–57 (Day 57 OpenAPI & Swagger, Day 37/54 Auth Headers)",
        "q1": "Why is an auto-generated OpenAPI (Swagger) schema valuable when collaborating with frontend engineers?",
        "q2": "What information does OpenAPI capture for each endpoint (parameters, request body, response codes, auth requirements)?",
        "q3": "How do you test an authenticated endpoint using a cURL command with an `Authorization: Bearer <token>` header?",
        "desc": "Write `build_api_response(data: list, status_code: int = 200, message: str = 'Success') -> dict` producing a standardized REST response envelope.",
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
        "topic": "API Testing with Postman, Assertions & Status Codes",
        "prereqs": "Days 1–58 (Day 58 Manual Testing, Day 38 Status Codes, Day 23 Assertions)",
        "q1": "How does automated testing in Postman using JavaScript assertions (`pm.response.to.have.status(200)`) differ from Python unit testing?",
        "q2": "Why should backend tests assert both the HTTP status code AND the JSON response body structure?",
        "q3": "What is Python's `assert` statement and why is it the foundation of unit testing frameworks?",
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
        "topic": "pytest-django Basics, Test DB Rollback & Assertion Best Practices",
        "prereqs": "Days 1–59 (Day 59 Automated Testing & Pytest, Day 43 DB Rollbacks)",
        "q1": "Why does `pytest-django` use an isolated test database and roll back transactions after every test?",
        "q2": "What is the difference between testing 'happy paths' (valid inputs return 200/201) and 'error paths' (invalid inputs return 400/403/404)?",
        "q3": "Why should test assertions be specific (e.g. `assert response.data['count'] == 3`) rather than generic (`assert response.status_code == 200`)?",
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
        "topic": "Model Factories (factory_boy) & Python Exception Hierarchies",
        "prereqs": "Days 1–60 (Day 60 Test Factories & Fixtures, Day 23 Exception Handling)",
        "q1": "Why are model factories (`factory_boy`) preferred over hardcoded fixtures (JSON/YAML) in production test suites?",
        "q2": "In Python, why should you catch specific exception classes (e.g. `ObjectDoesNotExist`, `IntegrityError`) rather than catching bare `Exception`?",
        "q3": "What is the purpose of raising a custom domain exception (e.g. `InsufficientInventoryError`) in a backend service?",
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
        "topic": "Python Logging Levels & Eliminating Fat Views",
        "prereqs": "Days 1–61 (Day 61 Logging & Debugging, Day 50 Clean Views vs Services)",
        "q1": "What are the five standard Python logging levels in order of severity (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)?",
        "q2": "Why is `logger.error('Failed to charge card', exc_info=True)` superior to `print()` in production web servers?",
        "q3": "Why should API views only handle HTTP request parsing and response formatting, delegating business logic to service functions?",
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
        "topic": "SOLID Principles & Clean Code Architecture",
        "prereqs": "Days 1–62 (Day 62 Clean Code & SOLID, Days 51–57 DRF Architecture)",
        "q1": "What is the Single Responsibility Principle (SRP) and how does it prevent bloated classes and 'god functions'?",
        "q2": "What is the Open/Closed Principle (open for extension, closed for modification)?",
        "q3": "How does Dependency Inversion allow business services to depend on abstractions rather than concrete database or external API implementations?",
        "desc": "Refactor a monolithic billing function into decoupled single-responsibility functions: `calculate_tax(subtotal: float, rate: float) -> float` and `calculate_invoice_total(subtotal: float, tax_rate: float) -> dict` returning `{'subtotal': ..., 'tax': ..., 'total': ...}` rounded to 2 decimals.",
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
        "topic": "Service Layer Pattern & Query Latency",
        "prereqs": "Days 1–63 (Day 63 Service Layers, Day 33 Indexing Latency, Day 45 ORM Optimization)",
        "q1": "What is the Service Layer pattern and why does it keep business logic out of views and models?",
        "q2": "Why can an unindexed database query take hundreds of milliseconds on large tables while an indexed query takes under 5 milliseconds?",
        "q3": "How do you measure database query latency in development using tools like Django Debug Toolbar or `EXPLAIN ANALYZE`?",
        "desc": "Implement a service function `calculate_order_totals_service(items: list[dict], discount_pct: float = 0.0) -> dict` returning `{'subtotal': float, 'discount': float, 'total': float}` with all values rounded to 2 decimals.",
        "stub": '''def calculate_order_totals_service(items: list[dict], discount_pct: float = 0.0) -> dict:
    """
    Each item in items: {'price': float, 'qty': int}
    discount_pct is a float between 0.0 and 1.0 (e.g. 0.15 for 15% off).
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 64 Revision Challenge ---")
    items = [{"price": 20.0, "qty": 2}, {"price": 10.0, "qty": 1}] # subtotal = 50.0
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
        "topic": "Cache-Aside Pattern, Redis & Blocking vs Non-Blocking I/O",
        "prereqs": "Days 1–64 (Day 64 Redis Caching Layer, Day 37 HTTP I/O, Day 63 Service Layer)",
        "q1": "What is the Cache-Aside pattern (application checks cache; on miss, reads from DB and writes to cache)?",
        "q2": "What is the difference between an in-memory datastore like Redis and a disk-backed relational database like PostgreSQL?",
        "q3": "Why is caching user sessions or read-heavy catalog data beneficial for backend throughput?",
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
        "topic": "Celery Architecture (Producer/Broker/Worker) & Network Exceptions",
        "prereqs": "Days 1–65 (Day 65 Celery & Task Queues, Day 23 Exception Handling)",
        "q1": "What are the three core roles in a Celery background task system: Producer (Django app), Broker (Redis/RabbitMQ), and Consumer/Worker (Celery process)?",
        "q2": "Why should email sending, PDF generation, and image resizing never be performed synchronously inside an HTTP request handler?",
        "q3": "Why must background tasks be idempotent so running them more than once does not cause duplicate side effects?",
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
        "topic": "Background Task Retries & WebSockets vs HTTP",
        "prereqs": "Days 1–66 (Day 66 Celery Retries, Day 37 HTTP Anatomy, Day 64/65 Redis)",
        "q1": "What is exponential backoff with jitter and why is it essential when retrying failed API or background tasks?",
        "q2": "What is the architectural difference between a short-lived HTTP request-response cycle and a persistent full-duplex WebSocket connection?",
        "q3": "What role does Redis play as a channel layer broker in real-time Django Channels applications?",
        "desc": "Write `calculate_exponential_backoff(attempt: int, base_delay: int = 2, max_delay: int = 60) -> int` returning `min(base_delay ** attempt, max_delay)`.",
        "stub": '''def calculate_exponential_backoff(attempt: int, base_delay: int = 2, max_delay: int = 60) -> int:
    """
    Computes exponential backoff delay in seconds.
    """
    # WRITE YOUR CODE HERE:
    pass''',
        "runner": '''def run_test():
    print("--- Running Day 67 Revision Challenge ---")
    d1 = calculate_exponential_backoff(1, base_delay=2, max_delay=60) # 2
    d2 = calculate_exponential_backoff(3, base_delay=2, max_delay=60) # 8
    d3 = calculate_exponential_backoff(8, base_delay=2, max_delay=60) # 60 (capped)
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
        "topic": "WebSockets vs HTTP, Idempotency & Database Rollbacks",
        "prereqs": "Days 1–67 (Day 67 WebSockets & Real-time, Day 38 Idempotency, Day 31/35 ACID)",
        "q1": "Why do WebSockets require an initial HTTP 101 Switching Protocols handshake before switching to the binary WebSocket protocol?",
        "q2": "What is an idempotency key (often passed in `Idempotency-Key` headers) and how does it prevent double-charging credit cards on network timeouts?",
        "q3": "Why is an atomic database transaction rollback essential if a payment webhook fails after deducting loyalty points?",
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
        "topic": "Webhook Verification, Production Settings & Password Security",
        "prereqs": "Days 1–68 (Day 68 Webhooks & Idempotency, Day 40 Production Settings, Day 48 Password Hashing)",
        "q1": "Why must webhook endpoints verify the cryptographic HMAC signature sent in headers before trusting the payload body?",
        "q2": "Why must `DEBUG = False` and strict `ALLOWED_HOSTS` be set in production Django deployments?",
        "q3": "Why should passwords never be encrypted with reversible encryption, but instead hashed with slow, salted algorithms like PBKDF2, bcrypt, or Argon2?",
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
        "topic": "Linux CLI Basics, Process Management & Virtual Environments",
        "prereqs": "Days 1–69 (Day 69 Gunicorn & Deployment, Day 40 Venvs, Day 26 Git)",
        "q1": "What is the difference between a process running in the foreground versus a daemonized background process managed by systemd or Docker?",
        "q2": "What do Linux file permission modes (e.g. `chmod 755` vs `chmod 600`) control for owner, group, and others?",
        "q3": "Why should environment variables in a `.env` file never be hardcoded into container image layers?",
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
        "hint2": "Split on the first '=' with `line.split('=', 1)`. Strip quotes using `val.strip('\"\\'')`.",
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
        "topic": "Docker Images, Non-Root Users & DB URL Configuration",
        "prereqs": "Days 1–70 (Day 70 Docker Intro, Day 32 PostgreSQL Configurations, Day 40 Settings)",
        "q1": "What is a multi-stage Docker build and why does it keep production image sizes minimal?",
        "q2": "Why should production Docker containers run under a dedicated non-root user (`USER appuser`) rather than root?",
        "q3": "How does `DATABASE_URL` consolidate user, password, host, port, and database name into a single standardized connection string?",
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
        "topic": "Docker Compose Orchestration, GitHub Actions & Pull Requests",
        "prereqs": "Days 1–71 (Day 71 Docker Compose, Day 26 Git Collaboration, Day 59 Pytest)",
        "q1": "In Docker Compose, how does container networking allow the `web` container to reach the database using service name `db` instead of an IP address?",
        "q2": "What is the purpose of a CI workflow (GitHub Actions) running linters and tests automatically on every Pull Request?",
        "q3": "Why should database migrations be run as part of deployment rather than being baked into image builds?",
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
        "topic": "Junior Backend System Design, Caching & Queues",
        "prereqs": "Days 1–72 (Day 64 Caching, Day 33 Indexing, Day 65 Queues)",
        "q1": "In a backend system design interview, how do you explain when to add Redis caching versus optimizing an SQL index?",
        "q2": "What are the trade-offs of horizontal scaling (adding more web servers behind a load balancer) versus vertical scaling (upgrading server RAM/CPU)?",
        "q3": "How does a message queue prevent backend web servers from becoming unresponsive during high-traffic spikes?",
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
        "topic": "SQL Joins & Subqueries, N+1 Queries & Python Data Aggregation",
        "prereqs": "Days 1–73 (Days 30-31 SQL, Day 45 ORM Optimization, Days 14-19 OOP)",
        "q1": "How would you explain the N+1 query problem and its solution to a junior developer in an interview?",
        "q2": "What is the difference between an indexed lookup and a full table scan in terms of algorithmic time complexity?",
        "q3": "In Python, how does using a dictionary or `collections.defaultdict` enable O(n) data aggregation over lists of records?",
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
        "topic": "Architecture Defense, Relational Design & Portfolio Packaging",
        "prereqs": "Days 1–74 (Day 63 Architecture, Day 34 Relational Design, Day 72 CI/CD)",
        "q1": "How do you explain the architectural decision of using PostgreSQL for bookings while using Redis for caching and Celery for emails?",
        "q2": "What are the three most critical sections in a backend GitHub project README for a technical recruiter or hiring engineer?",
        "q3": "How do automated tests and CI/CD pipelines demonstrate professional engineering maturity on a portfolio project?",
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

    print(f"[+] Successfully wrote and updated {updated_count} revision.py files (Days 33–75).")


if __name__ == "__main__":
    apply_all()
