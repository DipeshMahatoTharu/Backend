# Day 50 — DRF Filtering, Search, Ordering & Pagination

## 🎯 Learning Objectives
- Master filtering backends in DRF: `django-filter` (`DjangoFilterBackend`), `filters.SearchFilter`, and `filters.OrderingFilter`.
- Configure search prefixes: `^` (starts with), `=` (exact match), `@` (full-text search), `$` (regex search).
- Compare DRF pagination strategies:
  - `PageNumberPagination` (`?page=2&page_size=20`)
  - `LimitOffsetPagination` (`?limit=10&offset=40`)
  - `CursorPagination` (Keyset / Opaque cursor for massive scale)
- Configure global API pagination and throttling policies in `settings.py`.

---

## 📚 Core Backend Concepts

### 1. The 3 Built-in Filter Backends
```python
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Exact field filters: ?category=electronics&is_available=true
    filterset_fields = ['category', 'is_available']

    # Full text / substring search: ?search=macbook
    # '^title' matches starts-with, '=sku' matches exact
    search_fields = ['^title', '=sku', 'description']

    # Ordering: ?ordering=-price,created_at
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']  # Default ordering
```

### 2. CursorPagination for Billion-Row Tables
```python
from rest_framework.pagination import CursorPagination

class HighVolumeFeedPagination(CursorPagination):
    page_size = 25
    ordering = '-created_at'  # Must be indexed!
```
- Completely eliminates SQL `OFFSET` page drift and high query latency.
- Returns opaque cursors in `next` and `previous` links (`?cursor=cD0yMDI2LTA5...`).

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review filter backends, search lookups, pagination strategies, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build search matchers and cursor builders in [`practice.py`](practice.py), and fix pagination traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Search & Keyset Cursor Pagination Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
