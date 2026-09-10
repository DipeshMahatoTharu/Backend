# Day 42 — Django CRUD Application Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 42.1 The Post/Redirect/Get (PRG) Pattern
**QUESTION:**
Why does returning `render()` directly from a successful `POST` request cause duplicate form submissions when a user refreshes the page? How does returning `redirect()` solve this?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 42.2 `get_object_or_404` vs Manual `try...except`
**QUESTION:**
Why should you prefer `get_object_or_404(Model, pk=pk)` over `Model.objects.get(pk=pk)` inside views? What exception does `objects.get()` raise if the record is missing, and what HTTP status does Django return without a try/except?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 42.3 Concurrency & Double Booking in CRUD
**QUESTION:**
If two users simultaneously open an 'Edit Ticket' page and submit conflicting updates, what happens by default in Django? How does Optimistic Locking (versioning) prevent silent overwrites?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
