# Day 47 — DRF ModelViewSets & Generic Views Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 47.1 `APIView` vs `ModelViewSet`
**QUESTION:**
What are the trade-offs between using a explicit `APIView` versus an automated `ModelViewSet`? In what production architectures would using `ModelViewSet` be a dangerous anti-pattern?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 47.2 `@action(detail=True)` vs `@action(detail=False)`
**QUESTION:**
Explain the difference between setting `detail=True` vs `detail=False` on a custom `@action` method. What URL patterns does DRF generate for each?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 47.3 `get_queryset()` and `get_serializer_class()` Overrides
**QUESTION:**
Why do senior backend engineers override `get_queryset()` instead of setting static `queryset = Model.objects.all()`? Give an example using multi-tenant filtering or different serializers for list vs retrieve.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
