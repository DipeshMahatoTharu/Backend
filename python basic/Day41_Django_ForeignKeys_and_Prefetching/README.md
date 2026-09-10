# Day 41 — Django Relationships, `select_related` & `prefetch_related`

## 🎯 Learning Objectives
- Master relational modeling in Django: `ForeignKey` (one-to-many), `ManyToManyField` (many-to-many), and `OneToOneField`.
- Understand `on_delete` cascades: `CASCADE`, `PROTECT`, `SET_NULL`, `SET_DEFAULT`, and `DO_NOTHING`.
- Diagnose and eliminate the notorious **N+1 Database Query Problem**.
- Master `select_related()`: Performs a single SQL `INNER JOIN` / `LEFT OUTER JOIN` for single-valued relationships (FK, 1-to-1).
- Master `prefetch_related()`: Performs separate batch lookups (`WHERE id IN (...)`) in Python for multi-valued relationships (M2M, reverse FK).

---

## 📚 Core Backend Concepts

### 1. `on_delete` Policies in Financial & Production Systems
- **`CASCADE`**: When parent is deleted, delete all children. (Dangerous for invoices/orders!).
- **`PROTECT`**: Raises `ProtectedError` preventing deletion if related objects exist. (Mandatory for users with financial records).
- **`SET_NULL`**: Sets foreign key column to `NULL` (requires `null=True`).

### 2. The N+1 Problem Illustrated
```python
# BAD: Executes 1 query for orders + N queries for customers (101 SQL queries for 100 orders!)
orders = Order.objects.all()
for order in orders:
    print(order.customer.name)  # Hits database every iteration!

# GOOD (Single-valued): 1 single query using SQL JOIN
orders = Order.objects.select_related('customer')
for order in orders:
    print(order.customer.name)  # In-memory access, 0 extra queries!

# GOOD (Multi-valued / M2M): 2 queries total using prefetch_related
orders = Order.objects.prefetch_related('items')
for order in orders:
    for item in order.items.all():  # Pre-fetched into memory!
        print(item.product_name)
```

### 3. Rule of Thumb: `select_related` vs `prefetch_related`
| Feature | `select_related()` | `prefetch_related()` |
| :--- | :--- | :--- |
| **SQL Strategy** | SQL `JOIN` | Separate query with `WHERE id IN (...)` |
| **Supported Relations** | `ForeignKey`, `OneToOneField` | `ManyToManyField`, Reverse `ForeignKey` |
| **Number of SQL Queries**| Exactly 1 query | 2 or more queries (1 per prefetch) |
| **Limitation** | Cannot join across M2M (row explosion) | Data matched in Python RAM |

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Study relational fields, N+1 patterns, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build prefetchers and join analyzers in [`practice.py`](practice.py), and fix N+1 traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Relational Prefetching Query Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
