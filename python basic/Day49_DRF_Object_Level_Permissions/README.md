# Day 49 — DRF Custom & Object-Level Permissions

## 🎯 Learning Objectives
- Master DRF's built-in permission classes: `AllowAny`, `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly`.
- Understand the permission evaluation lifecycle: View-level (`has_permission`) vs Object-level (`has_object_permission`).
- Implement custom permissions by subclassing `rest_framework.permissions.BasePermission`.
- Build the industry-standard `IsOwnerOrReadOnly` permission class.
- Combine permissions using bitwise operators (`&` AND, `|` OR, `~` NOT).

---

## 📚 Core Backend Concepts

### 1. View-Level vs Object-Level Permissions
- **`has_permission(self, request, view)`**:
  - Evaluated first, before the view handler or model lookup executes.
  - Controls access to the entire endpoint (e.g. "Is user logged in?").
- **`has_object_permission(self, request, view, obj)`**:
  - Evaluated **only** when `self.get_object()` is called on detail endpoints (`retrieve`, `update`, `destroy`).
  - Controls access to the specific model instance (e.g. "Does `request.user == obj.owner`?").

### 2. The Canonical `IsOwnerOrReadOnly` Permission
```python
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Read permissions are allowed to any request (SAFE_METHODS).
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions allowed for GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions require ownership
        return obj.owner == request.user
```

### 3. Bitwise Permission Combinations
In DRF 3.9+, permissions can be composed:
```python
permission_classes = [IsAuthenticated & (IsOwnerOrReadOnly | IsAdminUser)]
```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review permission lifecycles, SAFE_METHODS, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build custom permission classes in [`practice.py`](practice.py), and fix permission traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Object-Level Permission Evaluation Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
