# Day 40 — Real-World Backend Engineering Interview

These questions assess your understanding of Django ORM performance, query generation, and database concurrency.

---

### Question 1: How Does QuerySet Caching Work, and How Can It Waste Server RAM?
**Interview Scenario:**
> *"An engineer writes a view that processes orders. They do:
> ```python
> orders = Order.objects.filter(status='pending')
> print(orders[0])
> for o in orders:
>     process(o)
> ```
> How many times does this hit the database? What if there are 500,000 orders?"*

#### Senior Mentor Answer & Key Points:
1. **QuerySet Cache Mechanics**:
   - When you access `orders[0]` on an **unevaluated** QuerySet, Django evaluates `SELECT ... LIMIT 1` without caching the entire QuerySet.
   - Then, when the `for o in orders:` loop runs, Django evaluates `SELECT ...` for all 500,000 orders and stores all 500,000 Python model instances in `orders._result_cache` in RAM!
   - This hits the database **twice** and consumes gigabytes of memory.
2. **The Senior Fix**:
   - Use `.iterator(chunk_size=2000)`:
     ```python
     for order in Order.objects.filter(status='pending').iterator(chunk_size=2000):
         process(order)
     ```
   - `.iterator()` streams rows directly using server-side database cursors and **never** caches them in RAM, keeping memory usage constant ($O(1)$).

---

### Question 2: `Q` Objects vs Raw SQL
**Interview Scenario:**
> *"When should a backend engineer use complex `Q` objects instead of falling back to `cursor.execute()` with raw SQL?"*

#### Senior Mentor Answer & Key Points:
1. **Maintainability & Composability**:
   - `Q` objects allow dynamically assembling filters based on user request parameters:
     ```python
     q_filter = Q()
     if category: q_filter &= Q(category=category)
     if min_price: q_filter &= Q(price__gte=min_price)
     ```
   - Composing raw SQL strings with `WHERE` and `AND` conditions is notoriously error-prone and vulnerable to syntax bugs.
2. **Security & Injection Defense**:
   - `Q` objects are automatically parameterized by Django's SQL compiler, eliminating SQL injection risks.
3. **Database Portability**:
   - The ORM translates `Q` objects to database-specific dialects (PostgreSQL vs MySQL vs SQLite) automatically.
