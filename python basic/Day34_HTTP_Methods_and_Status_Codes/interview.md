# Day 34 — Real-World Backend Engineering Interview

These questions test your mastery of HTTP status semantics, API security, and payment transaction idempotency.

---

### Question 1: How Idempotency Keys Prevent Duplicate Charges in Payment APIs
**Interview Scenario:**
> *"A customer clicks 'Pay $100' on a mobile app. The server processes the charge successfully in the database, but right before sending the HTTP 200 response back, the customer's phone loses cellular signal. The mobile app automatically retries the POST request. How does Stripe/backend architecture prevent double-charging?"*

#### Senior Mentor Answer & Key Points:
1. **The Idempotency Key**:
   - The client generates a unique UUID (v4) client-side before the first request and attaches it: `Idempotency-Key: 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d`.
2. **Atomic Lock & Cache in Redis**:
   - When the backend receives the request, it checks Redis for the key using `SET idempotency:<key> <request_hash> NX EX 86400`.
   - **In-flight**: If the key exists and has status `PROCESSING`, subsequent requests wait or receive `409 Conflict` ("Request in progress").
   - **Completed**: If the key already has a cached response, the server returns the cached response **immediately** without calling the credit card processor.
3. **Payload Verification**:
   - The backend hashes the request body. If a second request arrives with the same `Idempotency-Key` but a different amount (e.g. \$200), the server returns `422 Unprocessable Entity` ("Idempotency key reused with different parameters").

---

### Question 2: Designing Robust API Error Payloads (RFC 7807)
**Interview Scenario:**
> *"Why should production APIs never return generic `{error: 'Something went wrong'}` or raw database exception tracebacks? How does RFC 7807 standardise error handling?"*

#### Senior Mentor Answer & Key Points:
1. **Security Vulnerability of Stack Traces**:
   - Leaking raw database exceptions reveals database engines, table names, ORM versions, and SQL syntax to attackers, enabling targeted SQL injection.
2. **RFC 7807 Standard Structure**:
   - Standardizes the response header: `Content-Type: application/problem+json`.
   - Requires consistent top-level fields:
     - `type`: URI identifying the problem type documentation.
     - `title`: Short, human-readable summary of problem type (static per status code).
     - `status`: HTTP status code (must match response status line).
     - `detail`: Human-readable explanation specific to this occurrence.
     - `instance`: URI of the specific request that caused the error.
     - `invalid_params`: Optional list of field-level validation errors.
