# Day 40 — Django ORM Queries, `Q` Objects & `F` Expressions

## 🎯 Learning Objectives
- Master QuerySet internals: Lazy Evaluation, QuerySet caching, and evaluation trigger points.
- Master filtering and lookups: `exact`, `iexact`, `contains`, `icontains`, `in`, `gt`, `gte`, `lt`, `lte`, `range`.
- Master complex boolean logic using `Q` objects (`&` AND, `|` OR, `~` NOT).
- Master atomic in-database calculations with `F` expressions (preventing race conditions).
- Learn database aggregations and annotations: `Count`, `Sum`, `Avg`, `Min`, `Max`, and `annotate()`.

---

## 📚 Core Backend Concepts

### 1. Lazy Evaluation & The QuerySet Lifecycle
A QuerySet does NOT touch the database when constructed:
```python
# No database query is executed yet!
qs = Product.objects.filter(is_active=True).order_by('-price')

# Query executes ONLY when evaluated:
for p in qs: pass       # Iteration triggers SQL
len(qs)                 # Evaluation triggers SQL
list(qs)                # Casting triggers SQL
bool(qs)                # Boolean check triggers SQL
```
**Mentor Rule**: Use `qs.exists()` instead of `bool(qs)` to check presence (runs `SELECT 1 ... LIMIT 1`), and use `qs.count()` instead of `len(qs)` to count records (runs `SELECT COUNT(*)`).

### 2. Complex Boolean Queries with `Q` Objects
```python
from django.db.models import Q

# Find active products that are either tech items OR priced under $20
Product.objects.filter(
    Q(is_active=True) & (Q(category='tech') | Q(price__lt=20.0))
)

# Negation (NOT category == 'archived')
Product.objects.filter(~Q(category='archived'))
```

### 3. Preventing Race Conditions with `F` Expressions
When two concurrent requests try to decrement an item's inventory:
- **Buggy (In-Memory)**:
  ```python
  product = Product.objects.get(id=1)
  product.stock -= 1   # Thread 1 and Thread 2 both read 10, both save 9! (Lost update)
  product.save()
  ```
- **Atomic (In-Database `F` Expression)**:
  ```python
  from django.db.models import F
  # Generates: UPDATE products SET stock = stock - 1 WHERE id = 1;
  Product.objects.filter(id=1).update(stock=F('stock') - 1)
  ```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review QuerySet lifecycle, `Q`, `F`, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build filter chains and atomic operators in [`practice.py`](practice.py), and fix race conditions in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Memory QuerySet & Expression Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
