# Day 39 — Django Database Models, Migrations & Field Types

## 🎯 Learning Objectives
- Master Django's Model layer: subclassing `models.Model` and mapping Python classes to SQL database tables.
- Master core field types: `CharField`, `TextField`, `IntegerField`, `DecimalField`, `BooleanField`, and `DateTimeField`.
- Understand critical field options: `null=True` vs `blank=True`, `default`, `unique=True`, `db_index=True`, `choices`.
- Master model metadata (`class Meta`): `db_table`, `ordering`, `indexes`, and `constraints` (`UniqueConstraint`, `CheckConstraint`).
- Deep dive into Django migrations: `makemigrations`, `migrate`, `sqlmigrate`, `showmigrations`, and dependency management.

---

## 📚 Core Backend Concepts

### 1. `null=True` vs `blank=True` (The Classic Trap)
- **`null=True`**: Database-level constraint (`NULL` vs `NOT NULL`). Determines whether the column allows SQL `NULL` values.
- **`blank=True`**: Application/Form validation level. Determines whether the field is required in forms/admin.
- **The String Field Rule**: Never use `null=True` on `CharField` or `TextField` unless `unique=True` is also specified. Having both empty string `""` and `NULL` creates two distinct "no data" states, complicating queries!

### 2. Model Definition Best Practices
```python
from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=220, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)  # Set once on creation
    updated_at = models.DateTimeField(auto_now=True)      # Updated on every save

    class Meta:
        db_table = 'ecommerce_products'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', '-created_at'], name='status_created_idx')
        ]
```

### 3. Migration Commands
- `python manage.py makemigrations`: Inspects models and writes migration operations.
- `python manage.py migrate`: Applies pending migrations to the active database.
- `python manage.py sqlmigrate products 0001`: Inspects the exact raw SQL queries generated for migration 0001.

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review field options, migrations, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build model field validators in [`practice.py`](practice.py), and fix migration traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Mini-ORM Schema & Migration Generator in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
