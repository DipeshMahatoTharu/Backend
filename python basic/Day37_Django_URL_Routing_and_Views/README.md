# Day 37 — Django URL Routing, Path Converters & Views

## 🎯 Learning Objectives
- Understand Django's URL dispatcher mechanism (`urls.py`, `urlpatterns`, `path()`, and `re_path()`).
- Master built-in path converters: `str`, `int`, `slug`, `uuid`, and `path`.
- Implement custom path converters for domain-specific parameters (e.g. 4-digit years or ISO dates).
- Understand Function-Based Views (FBVs) vs Class-Based Views (CBVs: `View`, `TemplateView`, `RedirectView`).
- Master the `HttpRequest` and `HttpResponse` lifecycle, including `JsonResponse`, headers, and status codes.

---

## 📚 Core Backend Concepts

### 1. URL Path Converters
```python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),       # Matches positive integers
    path('articles/<slug:slug>/', views.article_detail),    # Matches letters, numbers, hyphens, underscores
    path('users/<uuid:user_id>/', views.user_profile),      # Matches formatted UUIDs
    path('files/<path:file_path>/', views.download_file),   # Matches complete path including slashes
]
```

### 2. FBV vs CBV Architecture
- **Function-Based Views (FBV)**:
  - Explicit, straightforward to read, minimal boilerplate for simple logic.
  - Handling methods requires explicit `if request.method == 'GET':`.
- **Class-Based Views (CBV)**:
  - Object-oriented: separates HTTP verbs into class methods (`get()`, `post()`, `delete()`).
  - Supports code reuse via mixins (`LoginRequiredMixin`, `MultipleObjectMixin`).

### 3. URL Namespacing and Reverse Resolution
Always provide `name` arguments to `path()`:
```python
path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail')
```
In Python code: `reverse('order-detail', kwargs={'pk': 42})` -> `'/orders/42/'`.
In Templates: `{% url 'order-detail' pk=order.id %}`.

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review URL dispatchers, converters, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build custom converters and CBV dispatchers in [`practice.py`](practice.py), and fix routing traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Dynamic URL Router & CBV Dispatcher in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
