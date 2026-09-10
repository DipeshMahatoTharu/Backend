# Day 50 — DRF Searching & Pagination Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 50.1 PageNumberPagination vs CursorPagination Performance
**QUESTION:**
Why does `PageNumberPagination` cause severe database degradation on page 50,000 of a billion-row table, while `CursorPagination` executes in sub-millisecond time?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 50.2 SearchFilter Prefix Semantics
**QUESTION:**
Explain the behavior of DRF's `search_fields` prefixes:
1. `search_fields = ['title']` (default)
2. `search_fields = ['^title']`
3. `search_fields = ['=title']`

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 50.3 Why `CursorPagination` Mandates an Ordering Column
**QUESTION:**
Why does `CursorPagination` raise an `UnorderedObjectListWarning` if the model or viewset does not specify an explicit ordering column? What happens if the ordering column contains duplicate values?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
