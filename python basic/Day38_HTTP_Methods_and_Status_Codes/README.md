# Day 34 — HTTP Methods, Idempotency & Status Codes

## 🎯 Learning Objectives
- Master HTTP method semantics: Safety (`GET`, `HEAD`, `OPTIONS`) vs Idempotency (`PUT`, `DELETE`, `GET`) vs Non-Idempotent operations (`POST`, `PATCH`).
- Learn precise HTTP status code ranges (2xx Success, 3xx Redirection, 4xx Client Error, 5xx Server Error) and exact usage criteria.
- Master the difference between `401 Unauthorized` (unauthenticated / missing credentials) and `403 Forbidden` (authenticated but insufficient role/scope).
- Implement RFC 7807 ("Problem Details for HTTP APIs") for uniform, machine-readable error responses.
- Understand why returning `200 OK` with an error message payload (`{"status": "error"}`) is an anti-pattern that breaks caching, proxies, and monitoring.

---

## 📚 Core Backend Concepts

### 1. Safe vs Idempotent Methods
| Method | Safe? (No side-effects) | Idempotent? ($f(f(x)) = f(x)$) | Typical Usage |
| :--- | :--- | :--- | :--- |
| `GET` | **Yes** | **Yes** | Read data without mutating server state |
| `HEAD` | **Yes** | **Yes** | Fetch headers only (e.g. check cache or file size) |
| `POST` | **No** | **No** | Create new resource; trigger non-idempotent action |
| `PUT` | **No** | **Yes** | Complete replacement or creation at exact URI |
| `PATCH` | **No** | **No** (by RFC spec) | Partial update of existing resource |
| `DELETE`| **No** | **Yes** | Remove resource (first call deletes, subsequent calls return 404 or 204) |

### 2. Critical Status Codes
- **200 OK**: Request succeeded and returned body.
- **201 Created**: Resource created successfully; should include `Location` header.
- **204 No Content**: Action succeeded, no response body (standard for `DELETE`).
- **301 Moved Permanently**: URL changed permanently; search engines update backlinks.
- **302 Found / 307 Temporary Redirect**: Temporary redirect; 307 guarantees method is preserved.
- **400 Bad Request**: Malformed JSON, missing required fields, schema validation failure.
- **401 Unauthorized**: Missing or invalid authentication credentials (JWT, API key).
- **403 Forbidden**: Identity verified, but user lacks permission to access resource.
- **404 Not Found**: Resource URI does not exist.
- **409 Conflict**: State conflict (e.g., duplicate unique email, version lock mismatch).
- **422 Unprocessable Entity**: Valid syntax, but semantic business logic errors.
- **429 Too Many Requests**: Rate limit exceeded; should include `Retry-After` header.
- **500 Internal Server Error**: Uncaught exception on server.
- **502 Bad Gateway**: Reverse proxy (Nginx) received an invalid/closed response from upstream (Gunicorn).
- **503 Service Unavailable**: Server overloaded or undergoing maintenance.
- **504 Gateway Timeout**: Upstream application took longer to respond than reverse proxy timeout.

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Study method semantics, idempotency, RFC 7807, and answer [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Implement status mappers and idempotency keys in [`practice.py`](practice.py), then fix anti-patterns in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the HTTP Method & Status Router in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
