# Day 41 — ForeignKeys & Prefetching Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 41.1 `select_related` vs `prefetch_related` Internals
**QUESTION:**
Explain the architectural difference in SQL execution between `select_related()` and `prefetch_related()`. Why does Django raise an error if you pass a `ManyToManyField` to `select_related()`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 41.2 `on_delete=models.PROTECT` vs `CASCADE`
**QUESTION:**
Why is using `on_delete=models.CASCADE` on an `Invoice.user` foreign key considered a catastrophic risk in financial and accounting applications? How does `models.PROTECT` prevent data loss?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 41.3 Nested Prefetching with `Prefetch` Objects
**QUESTION:**
How do you filter pre-fetched sub-resources? For example, when fetching Authors with their books, how do you ensure only books with `status='published'` are fetched into memory using `Prefetch()`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
