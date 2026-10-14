# Day 46 — DRF Serialization & APIView Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 46.1 `Serializer` vs `ModelSerializer`
**QUESTION:**
What does `serializers.ModelSerializer` automate behind the scenes compared to a plain `serializers.Serializer`? How does it determine field validators and default `create()` / `update()` implementations?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 46.2 `serializer.data` vs `serializer.validated_data`
**QUESTION:**
What is the exact distinction between `serializer.data` and `serializer.validated_data`? Why will accessing `serializer.validated_data` before calling `serializer.is_valid()` raise an `AssertionError`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 46.3 Why `raise_exception=True` is Senior Best Practice
**QUESTION:**
Why do senior backend engineers always pass `raise_exception=True` to `serializer.is_valid()` instead of writing `if not serializer.is_valid(): return Response(serializer.errors, 400)`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
