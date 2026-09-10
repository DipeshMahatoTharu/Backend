# Day 35 — REST API Conventions, URI Design & Versioning

## 🎯 Learning Objectives
- Understand the 6 architectural constraints of REST (Client-Server, Statelessness, Cacheability, Layered System, Code on Demand, Uniform Interface).
- Design intuitive, resource-oriented URIs using plural nouns (e.g., `/api/v1/users/42/orders`) and avoid RPC verbs in paths.
- Master query parameters for filtering (`?status=active`), sorting (`?sort=-created_at`), and pagination (`?page=2&page_size=20`).
- Implement industry-standard pagination patterns: Offset-based vs Cursor-based (Keyset) pagination.
- Compare API versioning strategies: URI Path (`/v1/`), Custom Headers (`Accept: application/vnd.company.v1+json`), and Query Parameters (`?version=1`).

---

## 📚 Core Backend Concepts

### 1. Resource Naming Rules
| Action | Bad (RPC Style) | Good (RESTful Resource Style) |
| :--- | :--- | :--- |
| List products | `GET /api/getProducts` | `GET /api/v1/products` |
| Create product | `POST /api/createProduct` | `POST /api/v1/products` |
| Get product 5 | `GET /api/product?id=5` | `GET /api/v1/products/5` |
| Update product 5 | `POST /api/updateProduct/5` | `PATCH /api/v1/products/5` |
| Delete product 5 | `GET /api/deleteProduct/5` | `DELETE /api/v1/products/5` |
| Sub-resource orders | `GET /api/getUserOrders?userId=5` | `GET /api/v1/users/5/orders` |

### 2. Offset Pagination vs Cursor-based Pagination
- **Offset Pagination (`?limit=20&offset=40`)**:
  - Pros: Simple to implement, allows jumping to arbitrary page numbers.
  - Cons: Performance degrades on large datasets ($O(N)$ scanning in SQL `OFFSET`), and suffers from "page drift" when rows are inserted/deleted during pagination.
- **Cursor/Keyset Pagination (`?limit=20&after_cursor=dXNlcl80Mg==`)**:
  - Pros: High performance ($O(1)$ indexed query: `WHERE id > 42 LIMIT 20`), immune to page drift.
  - Cons: Cannot jump directly to "Page 15"; sequential browsing only. Standard for infinite scroll feeds (Twitter, Instagram).

### 3. API Versioning Comparison
1. **URI Path Versioning (`/api/v1/books`)**: Most visible, easy to test via browser and cURL, supported out-of-the-box by API gateways. (Recommended default).
2. **Header Versioning (`Accept: application/vnd.api.v1+json`)**: Keeps URLs clean and resource-focused, but harder to test and debug in browsers.

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Read REST constraints, URI patterns, pagination strategies, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build REST query parsers and pagination envelopes in [`practice.py`](practice.py), and fix anti-patterns in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the RESTful Bookstore Resource Manager in [`challenge.py`](challenge.py), solve [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
