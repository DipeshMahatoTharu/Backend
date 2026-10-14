# Day 37 — Django URL Routing & Views Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 37.1 Trailing Slashes and `APPEND_SLASH`
**QUESTION:**
Why does Django's `CommonMiddleware` automatically redirect `/users` to `/users/` by default? What happens if a client sends a `POST` request to `/users` with `APPEND_SLASH=True`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 37.2 CBV Method Resolution Order & `as_view()`
**QUESTION:**
What does `MyView.as_view()` actually do when the URL dispatcher routes a request to a Class-Based View? How does `dispatch()` route to `get()` or `post()`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 37.3 URL Reversing and Decoupling
**QUESTION:**
Why should you never hardcode URLs like `<a href="/store/checkout/">` in templates or view redirects? How does `reverse()` prevent breaking changes?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
