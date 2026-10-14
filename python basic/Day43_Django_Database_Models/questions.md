# Day 39 — Django Database Models Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 39.1 `null=True` vs `blank=True`
**QUESTION:**
Explain why setting `null=True` on a Django `CharField` is considered an anti-pattern unless `unique=True` is present. What subtle query bugs does this cause?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 39.2 `auto_now` vs `auto_now_add`
**QUESTION:**
What is the difference between `DateTimeField(auto_now_add=True)` and `DateTimeField(auto_now=True)`? Why does calling `MyModel.objects.filter(...).update(title='...')` NOT update `auto_now` timestamps?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 39.3 Zero-Downtime Migration Strategies
**QUESTION:**
If a database table contains 5 million rows, why will running a migration that adds a new column with `default='active'` lock the table in PostgreSQL? How do you safely deploy this change without downtime?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
