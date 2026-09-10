# Day 43 — Real-World Backend Engineering Interview

These questions test your understanding of form security, validation lifecycles, and CSRF architecture.

---

### Question 1: How Does Django's CSRF Protection Actually Work? (The Double Submit Cookie Pattern)
**Interview Scenario:**
> *"Walk me through the exact cryptographic mechanism Django uses to protect against Cross-Site Request Forgery (CSRF). What cookie is set, what hidden field is rendered in HTML, and how does the server verify them?"*

#### Senior Mentor Answer & Key Points:
1. **The CSRF Threat**:
   - An attacker lures an authenticated user to `evil.com`. That site contains `<form action="https://bank.com/transfer" method="POST">`.
   - When submitted, the user's browser automatically attaches their `sessionid` cookie to `bank.com`, executing unauthorized actions!
2. **Django's Double Submit Defense**:
   - **Step 1**: Django generates a cryptographically secure random token and sets it in an HTTP cookie named `csrftoken`.
   - **Step 2**: The `{% csrf_token %}` template tag renders a hidden input field: `<input type="hidden" name="csrfmiddlewaretoken" value="...">`.
   - **Step 3 (The Masked Token)**: For security (preventing BREACH attacks), Django does not put the raw secret into the HTML. It scrambles the token with a random mask per request.
   - **Step 4 (Verification)**: When a `POST` arrives, `CsrfViewMiddleware` unmasks both the form token and the cookie token. If their underlying secret keys do not match, Django halts the request with `403 Forbidden` ("CSRF verification failed").

---

### Question 2: Why You Should Never Save Raw `request.POST` into Database Models
**Interview Scenario:**
> *"Why is `Book.objects.create(**request.POST.dict())` considered an extreme security vulnerability (Mass Assignment)?"*

#### Senior Mentor Answer & Key Points:
1. **The Mass Assignment Vulnerability**:
   - If an attacker sends unexpected POST parameters (e.g. `is_staff=True`, `is_superuser=True`, or `balance=999999`), unpacking `request.POST` passes these directly to the database model!
2. **The Defense**:
   - Always use a `ModelForm` with an explicit `fields = ['title', 'author', 'price']` whitelist or a DRF Serializer.
   - Any extra fields injected by an attacker are discarded during form cleaning.
