# Day 37 — Real-World Backend Engineering Interview

These questions assess your understanding of Django request dispatching, view architecture, and performance.

---

### Question 1: Class-Based Views (CBVs) vs Function-Based Views (FBVs)
**Interview Scenario:**
> *"Some developers swear by Function-Based Views (FBVs) for simplicity, while others mandate Class-Based Views (CBVs) for DRY principles. What is the pragmatic senior engineering recommendation?"*

#### Senior Mentor Answer & Key Points:
1. **Pragmatic Rule of Thumb**:
   - **Use CBVs (`ListView`, `DetailView`, `CreateView`, DRF `ModelViewSet`)** for standard CRUD operations that map directly to database models. Django's generic CBVs eliminate hundreds of lines of boilerplate.
   - **Use FBVs (or simple `APIView`)** for highly custom, non-CRUD workflows, such as multi-step checkout workflows, custom webhook ingestion, or single-purpose calculators.
2. **The Risk of Over-Abstraction**:
   - Deep CBV inheritance hierarchies (subclassing 5 layers of mixins) make code hard to read and debug. If modifying a view requires reading 6 separate source files to understand method resolution order (MRO), an FBV is cleaner.

---

### Question 2: Why `APPEND_SLASH` Can Silently Break API POST Requests
**Interview Scenario:**
> *"A mobile app developer reports that their `POST /api/v1/orders` request randomly loses its JSON body and fails. You discover Django returned a `301 Moved Permanently` to `/api/v1/orders/`. What happened?"*

#### Senior Mentor Answer & Key Points:
1. **The HTTP 301 Downgrade Trap**:
   - When a client sends a `POST` request to `/api/v1/orders` without a trailing slash, Django's `CommonMiddleware` (with `APPEND_SLASH=True`) issues an HTTP `301 Moved Permanently` redirect to `/api/v1/orders/`.
   - By HTTP/1.1 specification, many HTTP client libraries automatically downgrade `POST` to a `GET` upon receiving a 301 redirect, discarding the request body!
2. **The Architectural Fix**:
   - For REST APIs, disable trailing slash redirection or ensure mobile/web clients explicitly include trailing slashes in all endpoint paths.
   - Alternatively, return HTTP `307 Temporary Redirect` or `308 Permanent Redirect`, which strictly forbids changing the HTTP method or dropping the body.
