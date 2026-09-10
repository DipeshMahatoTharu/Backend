# Day 49 — DRF Object-Level Permissions Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 49.1 Why `has_object_permission` is Never Called on `POST` or `list`
**QUESTION:**
Why does DRF never invoke `has_object_permission` during `list` (GET collection) or `create` (POST collection) requests? How do you enforce security for those endpoints?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 49.2 `SAFE_METHODS` in DRF
**QUESTION:**
What HTTP methods are included in `rest_framework.permissions.SAFE_METHODS`? Why are they considered "safe"?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 49.3 The Danger of Manually Querying without `get_object()`
**QUESTION:**
If a developer writes `def put(self, request, pk): obj = Model.objects.get(pk=pk)`, why will DRF's `permission_classes` completely fail to protect the object? How does `self.get_object()` fix this?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
