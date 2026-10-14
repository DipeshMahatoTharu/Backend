# Day 43 — Django Forms & Validations Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 43.1 `clean_<fieldname>` vs `clean()`
**QUESTION:**
What is the distinct purpose of `clean_<fieldname>()` versus `clean()` in a Django Form? When must you use `self.add_error()` instead of `raise forms.ValidationError()`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 43.2 CSRF Protection Mechanics
**QUESTION:**
How does Django's `CsrfViewMiddleware` work? Explain the role of the `csrftoken` cookie, the `csrfmiddlewaretoken` hidden input field, and the Double Submit Cookie pattern.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 43.3 `form.cleaned_data` vs `request.POST`
**QUESTION:**
Why must you NEVER read untrusted user data directly from `request.POST` when writing business logic or saving to the database? What sanitization does `form.cleaned_data` provide?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
