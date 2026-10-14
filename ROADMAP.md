# 🚀 75-Day Python Backend & Database Engineering Roadmap (Zero-to-Hired Edition)

Welcome to your comprehensive 75-Day Python, PostgreSQL, Django, DRF, and Production Backend curriculum! This roadmap is engineered to take you from foundational programming to an **internship and junior-level backend engineer who can confidently pass technical interviews and build production systems by age 24**.

---

## 📊 Program Progress Tracker

- **Current Day**: Day 32 (PostgreSQL Architecture, Python Drivers & Connection Pooling)
- **Completed Days**: 31 / 75
- **Progress**: [████████░░░░░░░░░░░░] 41.3%
- **Current Phase**: Phase 3 — Relational Databases & PostgreSQL Deep Dive
- **Internship Readiness**: In Progress (Targeting Early Applications after Milestone 4 on Day 63)

---

## 🎯 Realistic Completion System
A day is officially considered **Done** when you can satisfy three concrete benchmarks:
1. **Explain the core concept** in plain English without looking at documentation (e.g., explaining why connection pooling prevents server crashes).
2. **Solve the core coding exercise** with reasonable independence.
3. **Debug or explain at least one relevant mistake** (e.g., diagnosing an uncommitted transaction, an index invalidation, or an unhandled permission error).

---

## 🏆 Job-Readiness Milestones & Application Triggers

- **Milestone 1 (Day 36)**: **Relational Database & PostgreSQL Fluency** — Can write complex SQL, explain B-Tree indexes with `EXPLAIN ANALYZE`, design normalized schemas (3NF), and handle concurrency locking.
- **Milestone 2 (Day 39)**: **HTTP & REST API Foundation** — Can structure clean HTTP request/response payloads, status codes, idempotency, and RESTful resource endpoints.
- **Milestone 3 (Day 50)**: **Django Web Framework & ORM Mastery** — Can build a complete relational web app, write defensive model constraints, execute zero-downtime migrations, and eliminate N+1 queries.
- **Milestone 4 (Day 63)**: **Production DRF REST API & Automated Testing** — Can build secure, token-authenticated REST APIs with nested serializers, custom permissions, pagination, and a complete `pytest` test suite.
  > 🚀 **JOB APPLICATION TRIGGER**: At Day 63, you have a fully tested, production-grade REST API repository on GitHub. You are now qualified to **start actively applying for Backend Internships and Junior Developer roles** while completing the remaining advanced phases!
- **Milestone 5 (Day 72)**: **Dockerized Microservices & CI/CD Pipelines** — Can containerize Django, PostgreSQL, Redis, and Celery with Docker Compose and run automated GitHub Actions CI/CD pipelines.
- **Milestone 6 (Day 75)**: **Enterprise Portfolio Capstone & Interview Mastery** — Can defend system design choices (caching, task queues, database sharding) and complete live coding interviews.

---

## 🏗️ Integrated Project Journey

Instead of leaving projects for the final days, practical development is integrated directly into your learning:

1. **Project 1: PostgreSQL Relational Analytics Engine** (Days 32–36)
   - *Features*: High-speed e-commerce schema, connection pooling with `psycopg2`, B-Tree and GIN indexes, transaction isolation, and full-text search.
2. **Project 2: Progressive Django App — "DevFlow" Project & Task Management Monolith** (Days 40–50)
   - *Features*: Custom User model (`AbstractUser`), RBAC, multi-table relationships with `through` models, forms with clean validations, model manager filters, and N+1 query optimization.
3. **Project 3: Production DRF E-Commerce Backend — "ShopCraft API"** (Days 51–63)
   - *Features*: JWT authentication with token rotation, writable nested order serializers, object-level permissions, rate limiting, OpenAPI 3.0/Swagger documentation, and a 100% passing `pytest-django` test suite.
4. **Project 4: Asynchronous Task Processing & Caching Service** (Days 64–68)
   - *Features*: Redis cache-aside caching, Celery background email and invoice generation with exponential retries, scheduled cron cleanup tasks (`celery-beat`), and payment webhook idempotency.
5. **Project 5: DevOps & Containerized Cloud Deployment** (Days 69–72)
   - *Features*: Multi-container `docker-compose` setup (web, postgres, redis, celery), Nginx reverse proxy with SSL, and GitHub Actions CI pipeline.
6. **Project 6: Final Capstone — Enterprise Hotel Booking & Inventory Backend** (Days 73–75)
   - *Features*: High-concurrency seat/room reservation engine preventing double-booking via `SELECT FOR UPDATE`, dynamic pricing, audit trails, and system design defense.

---

# 📅 Detailed Daily Curriculum (Days 32–75)

---

### 🗄️ Phase 3: Relational Databases & PostgreSQL Deep Dive (Days 32–36)

#### Day 32: PostgreSQL Architecture, Python Drivers & Connection Pooling [CURRENT DAY]
- **Learning Objectives**: Connect Python to PostgreSQL using `psycopg2`/`psycopg3`, understand the operating system cost of database connections, and implement thread-safe connection pooling.
- **Essential Concepts**: Process-based PostgreSQL architecture (5MB–10MB RAM per connection), connection latency overhead, `SimpleConnectionPool` vs `ThreadedConnectionPool`, connection leaks in `try/finally`, and PgBouncer connection multiplexing.
- **Practical Coding Exercise**: Implement a database utility that initializes a `ThreadedConnectionPool`, checks out connections, executes parameterized queries using `%s`, and returns connections in a `finally` block.
- **Independent Challenge**: Build a resilient `UserRepository` that checks out pooled connections, queries users by role using `RealDictCursor`, and gracefully handles pool exhaustion when requests spike.
- **Definition of Done**: Explain why opening a fresh TCP connection per API request causes server crashes; execute pooled queries with zero leaked connections.
- **How It Relates to Real Backend Work**: High-traffic web servers (Gunicorn) share database connection pools to prevent database server memory exhaustion under thousands of concurrent requests.
- **Optional Extension**: Configure connection pool keep-alive and test idle connection timeout settings.

#### Day 33: PostgreSQL Indexing, B-Trees & Query Optimization
- **Learning Objectives**: Dissect query execution plans using `EXPLAIN (ANALYZE, BUFFERS)` and design optimal B-Tree and Composite indexes.
- **Essential Concepts**: B-Tree tree structure, $O(\log N)$ traversal, Sequential Scan vs Index Scan vs Index-Only Scan vs Bitmap Heap Scan, the Leftmost Prefix Rule on composite indexes, Partial Indexes (`WHERE is_active = TRUE`), and Expression Indexes (`LOWER(email)`).
- **Practical Coding Exercise**: Benchmark a 50,000-row table search before and after adding a B-Tree index; measure the 400x speedup and inspect `EXPLAIN QUERY PLAN` output.
- **Independent Challenge**: Design the optimal composite index for `SELECT * FROM orders WHERE customer_id = ? AND status = 'PAID' ORDER BY created_at DESC LIMIT 20;` to eliminate in-memory sorting.
- **Definition of Done**: Explain why `WHERE LOWER(email) = ?` bypasses a standard B-Tree index; read and interpret an `EXPLAIN ANALYZE` query plan.
- **How It Relates to Real Backend Work**: Slow database queries are the #1 cause of API latency. Senior backend engineers optimize queries using indexes before paying for larger database hardware.
- **Optional Extension**: Use partial indexing on a high-volume boolean column (e.g. indexing only `is_unprocessed = TRUE`).

#### Day 34: Database Normalization (1NF–3NF), Schema Design & ER Modeling
- **Learning Objectives**: Design clean relational schemas in Third Normal Form (3NF), model Many-to-Many relationships with metadata, and enforce data integrity.
- **Essential Concepts**: 1NF (atomic values), 2NF (no partial key dependencies), 3NF (no transitive dependencies), primary key trade-offs (`BIGINT` vs `UUIDv4`), foreign key constraints (`CASCADE`, `RESTRICT`/`PROTECT`, `SET NULL`), and intentional denormalization for read speed.
- **Practical Coding Exercise**: Refactor a denormalized single-table spreadsheet dump into 4 clean 3NF relational tables (`customers`, `products`, `orders`, `order_items`) with foreign key constraints.
- **Independent Challenge**: Design a whiteboard schema for a ride-sharing service (Uber/Pathao) with `riders`, `drivers`, `rides`, and `reviews`, enforcing ratings constraints and preventing historical ride deletion.
- **Definition of Done**: Explain the difference between `ON DELETE CASCADE` and `ON DELETE RESTRICT`; identify and fix a transitive dependency.
- **How It Relates to Real Backend Work**: Schema design is permanent. Fixing a poorly normalized database with millions of rows in production requires painful, multi-month migrations.
- **Optional Extension**: Compare storage and indexing performance of sequential integer IDs vs random UUIDs.

#### Day 35: Transactions, ACID, MVCC & Concurrency Locking
- **Learning Objectives**: Master transaction atomicity, PostgreSQL Multi-Version Concurrency Control (MVCC), and pessimistic row-level locking.
- **Essential Concepts**: ACID guarantees, PostgreSQL MVCC internals (`xmin`, `xmax`, dead tuples, `VACUUM`), transaction isolation levels (Read Committed, Repeatable Read, Serializable), Lost Updates, `SELECT ... FOR UPDATE`, and `SELECT ... FOR UPDATE SKIP LOCKED`.
- **Practical Coding Exercise**: Simulate a concurrent "Lost Update" race condition where 10 threads buy inventory simultaneously; resolve it using atomic database updates.
- **Independent Challenge**: Build a distributed job queue worker engine using `SKIP LOCKED` where multiple concurrent worker processes claim pending tasks without colliding or blocking.
- **Definition of Done**: Explain why "readers never block writers" in PostgreSQL; explain how to prevent database deadlocks through strict primary key ordering.
- **How It Relates to Real Backend Work**: In banking, e-commerce checkouts, and ticketing systems, concurrency control prevents double-spending and inventory overdrafts.
- **Optional Extension**: Simulate a classic deadlock between two transactions and fix it using sorted lock ordering.

#### Day 36: PostgreSQL Advanced Data Types & Full-Text Search
- **Learning Objectives**: Leverage PostgreSQL's hybrid NoSQL capabilities using `JSONB`, Array columns, and Full-Text Search.
- **Essential Concepts**: `JSON` (plain text) vs `JSONB` (decomposed binary), GIN (Generalized Inverted Index) indexing, querying nested JSON keys (`->`, `->>`), native array columns (`tags TEXT[]`), `to_tsvector` lexemes, and Trigram fuzzy matching (`pg_trgm`).
- **Practical Coding Exercise**: Store and query semi-structured event logs using JSON operators; build an Inverted Index simulation matching words to document IDs.
- **Independent Challenge**: Build a dynamic e-commerce product catalog supporting heterogeneous attributes (e.g. laptops with RAM/CPU, shoes with size/color) using `JSONB` and array tags.
- **Definition of Done**: Explain why GIN indexing on `JSONB` is exponentially faster than querying plain `JSON`; explain how Trigram indexing handles typos.
- **How It Relates to Real Backend Work**: Using `JSONB` avoids managing hundreds of sparse, mostly-empty database columns for flexible product attributes and third-party audit payloads.
- **Optional Extension**: Implement fuzzy book title search using trigram similarity sliding windows.

---

### 🌐 Phase 4: HTTP Protocols & REST API Architecture (Days 37–39)

#### Day 37: HTTP Protocols, Request-Response Lifecycle & Headers
- **Learning Objectives**: Trace an HTTP request from DNS lookup to TCP socket, parse headers, and manage client-server communication.
- **Essential Concepts**: TCP/IP handshake, TLS encryption, HTTP/1.1 vs HTTP/2, Request structure (method, path, headers, body), Response structure (status, headers, payload), Content negotiation (`Accept`, `Content-Type`), and statelessness.
- **Practical Coding Exercise**: Write a raw Python socket or HTTP script to send manual HTTP GET and POST requests and parse headers, status codes, and JSON bodies.
- **Independent Challenge**: Build an HTTP request validator that inspects incoming headers for `Authorization`, `Content-Type: application/json`, and user-agent strings.
- **Definition of Done**: Explain every step that happens between typing a URL in a browser and receiving JSON data from a backend server.
- **How It Relates to Real Backend Work**: Every web framework (Django, Flask, FastAPI) is an abstraction over raw HTTP. Understanding headers is critical for debugging auth, CORS, and caching.
- **Optional Extension**: Inspect TLS certificates and cipher suites using Python's `ssl` module.

#### Day 38: HTTP Methods, Idempotency & Standard Status Codes
- **Learning Objectives**: Choose the correct HTTP methods and status codes for production REST APIs.
- **Essential Concepts**: Safe methods (GET, HEAD), Idempotent methods (GET, PUT, DELETE), Non-idempotent methods (POST, PATCH), 2xx Success (200, 201, 204), 3xx Redirection (301, 304), 4xx Client Errors (400, 401, 403, 404, 409, 422), and 5xx Server Errors (500, 502, 503, 504).
- **Practical Coding Exercise**: Build a mock API response dispatcher that maps incoming method/data scenarios to the exact RFC-compliant status codes.
- **Independent Challenge**: Write an error response generator that returns standardized RFC 7807 error objects with `error_code`, `message`, `timestamp`, and field-level validation errors.
- **Definition of Done**: Explain the difference between `PUT` and `PATCH`, and between `401 Unauthorized` and `403 Forbidden`.
- **How It Relates to Real Backend Work**: Professional frontend teams depend on consistent status codes and error payloads to handle UI loading, form errors, and authentication redirects.
- **Optional Extension**: Implement an Idempotency-Key header check for payment operations.

#### Day 39: REST API Conventions, URI Design & Contract Standards
- **Learning Objectives**: Design clean, predictable, intuitive RESTful API endpoints.
- **Essential Concepts**: Nouns over verbs (`/api/v1/orders` vs `/getOrders`), plural resources, nested resources for child entities (`/api/v1/users/5/orders`), filtering via query parameters (`?status=active&sort=-created_at`), pagination parameters, and API versioning strategies.
- **Practical Coding Exercise**: Write an OpenAPI specification draft for an Online Bookstore API detailing endpoints, request bodies, query parameters, and responses.
- **Independent Challenge**: Refactor a messy "RPC-style" API specification (`/createUser`, `/delete_order`, `/update_item_qty`) into clean, standardized RESTful URIs.
- **Definition of Done**: Defend why REST APIs avoid verbs in paths and how to model actions that don't fit clean CRUD (e.g. `/orders/5/cancel`).
- **How It Relates to Real Backend Work**: Clean REST APIs enable mobile and frontend developers to integrate without needing to ask the backend engineer how each route behaves.
- **Optional Extension**: Design a consistent pagination contract returning `count`, `next`, `previous`, and `results`.

---

### 🦄 Phase 5: Progressive Django Web Framework Mastery (Days 40–50)
*Project: "DevFlow" — Project, Sprint & Task Management Backend*

#### Day 40: Django Architecture, Virtual Environments & Settings Configuration
- **Learning Objectives**: Set up a professional Django project, manage isolated Python virtual environments, and configure multi-environment settings.
- **Essential Concepts**: Virtual environments (`venv`), `requirements.txt` vs Poetry, Django MVT (Model-View-Template) pattern, Project vs Apps, `settings.py` anatomy, `INSTALLED_APPS`, `ALLOWED_HOSTS`, and `manage.py` commands.
- **Practical Coding Exercise**: Initialize the "DevFlow" Django project inside a clean virtual environment, configure PostgreSQL in `settings.py` using environment variables, and run migrations.
- **Independent Challenge**: Configure split settings (`settings/base.py`, `settings/local.py`, `settings/production.py`) using `django-environ` to keep secrets out of Git.
- **Definition of Done**: Explain what `manage.py runserver` actually does and how Django routes requests through WSGI/ASGI handlers.
- **How It Relates to Real Backend Work**: Production backends never hardcode database credentials or `DEBUG = True` in version control; managing environment variables is mandatory.
- **Optional Extension**: Create a custom `manage.py` command that prints project database statistics.

#### Day 41: Django URL Routing & Class-Based Views (CBVs) vs FBVs
- **Learning Objectives**: Master URL dispatching with path converters and write modular Class-Based Views.
- **Essential Concepts**: URL pattern matching, path converters (`<int:id>`, `<str:slug>`), Function-Based Views (FBVs) vs Class-Based Views (CBVs), View lifecycle, `View`, `TemplateView`, and returning `JsonResponse`.
- **Practical Coding Exercise**: Build modular URL routes for the "DevFlow" project mapping to both FBVs and CBVs returning structured JSON data.
- **Independent Challenge**: Implement a `ProjectDetailView(View)` that accepts a project slug, validates its existence, and handles `GET`, `POST`, and `DELETE` HTTP methods in distinct class methods.
- **Definition of Done**: Explain the trade-offs between FBVs (explicit, simple) and CBVs (reusable, extensible via inheritance).
- **How It Relates to Real Backend Work**: Enterprise Django projects rely heavily on Class-Based Views and ViewSets to eliminate boilerplate across hundreds of endpoints.
- **Optional Extension**: Implement a custom URL path converter for UUIDs or formatted dates.

#### Day 42: Django Template Engine & Static Files Handling
- **Learning Objectives**: Understand server-side rendering, template inheritance, context processors, and static asset management.
- **Essential Concepts**: Django Template Language (DTL), template inheritance (`{% extends %}`, `{% block %}`), context dictionaries, template filters, context processors, and `STATIC_ROOT` vs `STATICFILES_DIRS`.
- **Practical Coding Exercise**: Build a clean dashboard UI layout for "DevFlow" with a base template, navigation bar, dynamic project cards, and custom template filters.
- **Independent Challenge**: Create a custom template context processor that injects the current environment name and unread notification count into all rendered views.
- **Definition of Done**: Explain why `collectstatic` is required in production deployment when web servers (Nginx) serve CSS/JS directly.
- **How It Relates to Real Backend Work**: Even when building REST APIs, backend developers frequently render server-side admin portals, email templates, and invoice views.
- **Optional Extension**: Build a custom template tag that formats ISO timestamps into relative time (e.g. "3 hours ago").

#### Day 43: Django Database Models, Field Constraints & Migrations Engine
- **Learning Objectives**: Define relational models, enforce database-level constraints, and understand how Django generates migrations under the hood.
- **Essential Concepts**: `models.Model`, field types (`CharField`, `TextField`, `IntegerField`, `DateTimeField`), model constraints (`UniqueConstraint`, `CheckConstraint`), `db_index=True`, `makemigrations` and `migrate`, and inspecting raw SQL via `sqlmigrate`.
- **Practical Coding Exercise**: Implement the core `Project` and `Task` models for "DevFlow" with `CheckConstraint(check=Q(due_date__gte=F('created_at')))` and indexes.
- **Independent Challenge**: Write a custom data migration (using `migrations.RunPython`) that safely populates a newly added non-nullable slug column for existing database records.
- **Definition of Done**: Inspect the generated SQL for a migration file using `python manage.py sqlmigrate`; explain how Django tracks applied migrations in `django_migrations`.
- **How It Relates to Real Backend Work**: Zero-downtime database migrations in production require knowing exactly what DDL commands Django executes when you alter model fields.
- **Optional Extension**: Add a `PositiveIntegerField` with database validation preventing negative task estimates.

#### Day 44: Django ORM Queries: Advanced Filtering, Q Objects & F Expressions
- **Learning Objectives**: Write expressive, high-performance database queries using Django ORM without falling back to raw SQL.
- **Essential Concepts**: QuerySets, lazy evaluation, field lookups (`__icontains`, `__in`, `__range`), complex boolean conditions with `Q` objects (`Q(A) | Q(B)`), atomic in-database updates with `F` expressions (`F('views') + 1`), and aggregations (`aggregate()`, `annotate()`).
- **Practical Coding Exercise**: Write queries for "DevFlow" to find overdue tasks, tasks assigned to specific teams, and calculate the average completion time per project.
- **Independent Challenge**: Implement an atomic task priority bump using `F()` expressions that prevents race conditions when two managers update task order simultaneously.
- **Definition of Done**: Explain why QuerySets are lazy and at what exact moment they execute an actual SQL query to the database.
- **How It Relates to Real Backend Work**: In-database operations using `F` expressions avoid memory bloat and eliminate concurrency race conditions on counters.
- **Optional Extension**: Use `Count()` and `Avg()` annotations to rank developers by completed tasks.

#### Day 45: ORM Performance Mastery: Eliminating the N+1 Query Problem
- **Learning Objectives**: Profile database queries, identify the N+1 query performance bug, and eliminate it using `select_related` and `prefetch_related`.
- **Essential Concepts**: The N+1 Query Problem, `select_related` (SQL `JOIN` for `ForeignKey` and `OneToOne`), `prefetch_related` (separate batch `WHERE IN` queries for `ManyToManyField` and reverse foreign keys), `django.db.connection.queries`, and `django-debug-toolbar`.
- **Practical Coding Exercise**: Intentionally write an unoptimized view that executes 51 SQL queries for 50 tasks; profile it and reduce it to exactly 1 query using `select_related`.
- **Independent Challenge**: Optimize a multi-level relationship query: fetch all Projects with their assigned Developers and all Task Tags using `Prefetch` objects in exactly 2 database queries.
- **Definition of Done**: Explain the exact technical difference in SQL generated by `select_related()` vs `prefetch_related()`.
- **How It Relates to Real Backend Work**: The N+1 query problem is the #1 reason Django applications slow down in production and the most common technical interview question.
- **Optional Extension**: Install and configure `django-debug-toolbar` to visualize query counts and cache hits.

#### Day 46: Django Model Relationships: OneToOne, ForeignKey & ManyToMany with `through`
- **Learning Objectives**: Architect complex relational structures and customize Many-to-Many junction tables.
- **Essential Concepts**: `OneToOneField` (profiles, extensions), `ForeignKey` (one-to-many parent-child), `ManyToManyField` (many-to-many), reverse relations (`related_name`), and intermediate junction models with extra attributes (`through='Membership'`).
- **Practical Coding Exercise**: Implement the "DevFlow" team collaboration schema: `Project` has many `TeamMembers` with custom roles (Admin, Developer, Viewer) and join dates via a `through` model.
- **Independent Challenge**: Query the reverse relationship: given a developer, retrieve all projects where their role is "Admin" using `related_name` in a single query.
- **Definition of Done**: Explain why giving every foreign key an explicit `related_name` is essential for clean codebase architecture.
- **How It Relates to Real Backend Work**: Real-world relationships almost always carry metadata (e.g. who invited the user, what permissions they have, when they joined).
- **Optional Extension**: Enforce a `UniqueConstraint` on `(project, user)` in the junction table to prevent duplicate memberships.

#### Day 47: Django Forms, ModelForms & Clean Validation Methods
- **Learning Objectives**: Validate incoming data defensively using Django Form classes.
- **Essential Concepts**: `Form` vs `ModelForm`, form fields and widgets, form validation lifecycle (`is_valid()`, `cleaned_data`), field-level validators (`clean_<fieldname>`), and cross-field validation (`clean()`).
- **Practical Coding Exercise**: Build a `TaskCreateForm` with date validation ensuring the due date cannot be set in the past and task titles do not contain restricted words.
- **Independent Challenge**: Build a cross-field validation rule in `clean()` that rejects setting a task status to "DONE" if the task has 0 logged hours.
- **Definition of Done**: Explain the difference between database-level constraints (`CheckConstraint`) and application-level form validations (`clean()`).
- **How It Relates to Real Backend Work**: Form validation is the first line of defense against corrupted data and malicious user input.
- **Optional Extension**: Add a custom field validator reusable across multiple forms.

#### Day 48: Django Authentication, Password Hashing & Session Security
- **Learning Objectives**: Secure user sessions, understand cryptographic password hashing, and implement authentication views.
- **Essential Concepts**: Django authentication framework (`django.contrib.auth`), PBKDF2/Argon2 password hashing algorithms, session cookies vs session database backend, login/logout views, password reset tokens, and CSRF protection (`{% csrf_token %}`).
- **Practical Coding Exercise**: Build a complete user registration, login, and logout flow for "DevFlow" with session management and password confirmation.
- **Independent Challenge**: Implement an account lockout mechanism that tracks failed login attempts and locks the account after 5 consecutive bad passwords.
- **Definition of Done**: Explain why passwords must NEVER be encrypted (two-way), but must always be hashed with a cryptographic salt (one-way).
- **How It Relates to Real Backend Work**: Authentication security protects user data; understanding sessions and CSRF prevents account takeover vulnerabilities.
- **Optional Extension**: Configure secure cookie settings (`SESSION_COOKIE_HTTPONLY`, `SESSION_COOKIE_SECURE`).

#### Day 49: Custom User Models (`AbstractUser`), RBAC & Web Security
- **Learning Objectives**: Implement a production-grade Custom User Model and configure Role-Based Access Control (RBAC).
- **Essential Concepts**: Why custom user models must be created before the first migration (`AUTH_USER_MODEL`), `AbstractUser` vs `AbstractBaseUser`, email as the username field, Django Groups and Permissions, `@login_required`, and `@permission_required`.
- **Practical Coding Exercise**: Build a custom `User` model for "DevFlow" with email login, avatar URL, bio, and role choices (Lead, Engineer, QA).
- **Independent Challenge**: Build a custom access control decorator `@project_admin_required` that checks if the logged-in user has the Admin role inside the specific project.
- **Definition of Done**: Explain why starting a Django project with the default `auth.User` model makes future schema changes extremely painful.
- **How It Relates to Real Backend Work**: Every production Django codebase uses a custom user model to allow email login, multi-factor auth, and organizational roles.
- **Optional Extension**: Customize the Django Admin portal with custom search fields and filters for the custom user model.

#### Day 50: Django Signals vs Model Overrides vs Custom Managers
- **Learning Objectives**: Structure clean business logic, know when to use custom QuerySet managers, and avoid common Django signals traps.
- **Essential Concepts**: Model `save()` overrides vs Django Signals (`post_save`, `pre_delete`), the hidden dangers of signals (implicit side-effects, hard to debug, bypassed in bulk updates), and Custom Managers (`objects.active()`).
- **Practical Coding Exercise**: Create a `SoftDeleteManager` and `SoftDeleteModel` abstract base class where `.delete()` sets `is_deleted = True` and default queries exclude deleted rows.
- **Independent Challenge**: Refactor a messy `post_save` signal that sends notification emails into an explicit service function called in the view.
- **Definition of Done**: Defend why senior backend engineers prefer explicit service functions or model method overrides over Django signals for critical business logic.
- **How It Relates to Real Backend Work**: Signals make large codebases unpredictable because saving a model in one place triggers invisible database writes elsewhere.
- **Optional Extension**: Chain custom QuerySet methods: `Task.objects.active().overdue().for_user(request.user)`.

---

### ⚡ Phase 6: Django REST Framework (DRF) Production APIs (Days 51–57)
*Project: "ShopCraft" — Production E-Commerce REST API*

#### Day 51: DRF Architecture, Serializers & Field-Level Validations
- **Learning Objectives**: Transform Django models into JSON, validate incoming API payloads, and handle deserialization errors.
- **Essential Concepts**: Django REST Framework architecture, `Serializer` vs `ModelSerializer`, fields (`CharField`, `SerializerMethodField`, `ReadOnlyField`), `validate_<fieldname>()`, and `validate()` for cross-field checks.
- **Practical Coding Exercise**: Build `ProductSerializer` and `CategorySerializer` for "ShopCraft" with price validations and a calculated `discounted_price` method field.
- **Independent Challenge**: Add a validator that ensures a product SKU matches the regex pattern `^[A-Z]{3}-[0-9]{4}$` and reject invalid codes with a 400 error.
- **Definition of Done**: Explain the dual role of a Serializer: converting model instances to JSON (serialization) and converting JSON to validated Python dictionaries (deserialization).
- **How It Relates to Real Backend Work**: Serializers are the gatekeepers of modern web and mobile apps, guaranteeing that bad data never touches the database.
- **Optional Extension**: Use `to_representation()` to customize the outgoing JSON structure dynamically.

#### Day 52: Writable Nested Serializers & Relational Payloads
- **Learning Objectives**: Handle complex multi-table creation and updates in a single atomic API request.
- **Essential Concepts**: Nested serializers, read-only vs writable nested representations, overriding `create()` and `update()` on serializers, and wrapping nested writes in `transaction.atomic()`.
- **Practical Coding Exercise**: Build an `OrderCreateSerializer` that accepts customer info and a list of order items `[{"product_id": 1, "quantity": 2}, ...]`, creating the order and all items in one transaction.
- **Independent Challenge**: Implement stock deduction during nested order creation; if any product has insufficient inventory, raise `serializers.ValidationError` and rollback.
- **Definition of Done**: Explain why DRF `ModelSerializer` cannot automatically save writable nested relationships without overriding `create()` / `update()`.
- **How It Relates to Real Backend Work**: Modern checkouts, invoices, and multi-item submissions require creating a parent record and multiple child rows simultaneously.
- **Optional Extension**: Support nested updates: updating existing line items and adding new ones in a single `PUT` request.

#### Day 53: APIView, Generic Views, Mixins & ModelViewSets with Routers
- **Learning Objectives**: Choose the right view abstraction level in DRF to balance custom logic with rapid development.
- **Essential Concepts**: `APIView` (complete control), `GenericAPIView` with Mixins (`ListModelMixin`, `CreateModelMixin`), `ModelViewSet` (full CRUD in 10 lines of code), and `DefaultRouter` automatic URL generation.
- **Practical Coding Exercise**: Build product catalog views using `ModelViewSet` and a custom checkout view using `APIView` to see both abstraction styles in action.
- **Independent Challenge**: Override `get_serializer_class()` and `get_queryset()` in a ViewSet to return lightweight summaries for list views and full details for retrieve views.
- **Definition of Done**: Explain the hierarchy of DRF views and when you should choose a plain `APIView` over a `ModelViewSet`.
- **How It Relates to Real Backend Work**: Teams use ViewSets for standard resource CRUD, and use `APIView` for custom actions like payment processing or exports.
- **Optional Extension**: Add a custom action to a ViewSet using the `@action(detail=True, methods=['post'])` decorator.

#### Day 54: DRF Authentication: Token Auth & SimpleJWT (Token Rotation)
- **Learning Objectives**: Implement stateless API authentication using JSON Web Tokens (JWT) with refresh token rotation.
- **Essential Concepts**: Stateless API authentication, Token Authentication vs JWT, JWT structure (Header, Payload, Signature), Access Tokens (short-lived, 15m) vs Refresh Tokens (long-lived, 7d), `djangorestframework-simplejwt`, and token blacklisting.
- **Practical Coding Exercise**: Configure `SimpleJWT` in "ShopCraft": build user login returning access and refresh tokens, and protect product creation endpoints.
- **Independent Challenge**: Implement a token refresh rotation endpoint that issues a brand-new refresh token on each refresh and blacklists the previous one to prevent replay attacks.
- **Definition of Done**: Explain what happens if an access token is stolen versus if a refresh token is stolen; explain why JWTs are stateless.
- **How It Relates to Real Backend Work**: Mobile apps and single-page apps (React, Flutter) use JWTs to authenticate API requests without relying on browser cookies.
- **Optional Extension**: Add custom claims (user role, tenant ID) into the JWT payload.

#### Day 55: Object-Level Permissions & API Throttling/Rate Limiting
- **Learning Objectives**: Enforce fine-grained authorization rules and protect APIs from abuse using rate limits.
- **Essential Concepts**: `IsAuthenticated`, `IsAdminUser`, `AllowAny`, Custom permissions via `BasePermission` (`has_permission`, `has_object_permission`), and API Throttling (`AnonRateThrottle`, `UserRateThrottle`).
- **Practical Coding Exercise**: Create a custom permission `IsOwnerOrReadOnly` ensuring users can only edit or delete their own reviews while allowing anyone to read.
- **Independent Challenge**: Configure tiered rate limiting: anonymous users are throttled to 10 requests/minute, while authenticated users get 100 requests/minute.
- **Definition of Done**: Explain the difference between `has_permission` (checked before database query) and `has_object_permission` (checked after retrieving the object).
- **How It Relates to Real Backend Work**: Permissions protect sensitive user data from unauthorized access; rate limiting prevents malicious scrapers and denial-of-service attacks.
- **Optional Extension**: Implement an IP-based blacklist permission that blocks known malicious IP addresses.

#### Day 56: Filtering, Searching, Ordering & Custom Pagination
- **Learning Objectives**: Build flexible list endpoints supporting search, multi-field filtering, sorting, and pagination.
- **Essential Concepts**: `django-filter` integration (`DjangoFilterBackend`), `SearchFilter`, `OrderingFilter`, PageNumberPagination vs CursorPagination (for large datasets), and custom pagination classes.
- **Practical Coding Exercise**: Add full product filtering to "ShopCraft": filter by category, price range (`price__gte`, `price__lte`), search across title/description, and sort by price.
- **Independent Challenge**: Build a custom `StandardResultsSetPagination` returning `page_size`, `total_pages`, `current_page`, and navigation links.
- **Definition of Done**: Explain why `CursorPagination` is superior to `PageNumberPagination` on tables with millions of rapidly updating records.
- **How It Relates to Real Backend Work**: E-commerce, social media, and SaaS platforms require robust filtering and pagination to keep page loads fast and intuitive.
- **Optional Extension**: Implement cursor-based pagination for an infinite scroll mobile API endpoint.

#### Day 57: API Documentation with OpenAPI 3.0 & Swagger (`drf-spectacular`)
- **Learning Objectives**: Automatically generate interactive API documentation using industry-standard OpenAPI 3.0 schemas.
- **Essential Concepts**: The importance of API documentation, OpenAPI 3.0 specification, `drf-spectacular`, Swagger UI (`/api/docs/`), ReDoc (`/api/redoc/`), and documenting custom headers and error responses with `@extend_schema`.
- **Practical Coding Exercise**: Install `drf-spectacular`, generate the schema, and configure interactive Swagger UI for the complete "ShopCraft" API.
- **Independent Challenge**: Decorate a custom checkout view using `@extend_schema` with request body examples, response status codes, and error descriptions.
- **Definition of Done**: Open the interactive Swagger UI in a browser, execute a live API call, and view the formatted JSON response and schema.
- **How It Relates to Real Backend Work**: Frontend and mobile teams cannot work efficiently without interactive Swagger documentation; it is expected on all portfolio projects.
- **Optional Extension**: Export the OpenAPI JSON schema and import it into Postman as a collection.

---

### 🧪 Phase 7: Automated Testing, Clean Code & Architecture (Days 58–63)

#### Day 58: API Manual Testing: Postman Workspaces & cURL CLI
- **Learning Objectives**: Test and debug API endpoints from the command line and build automated Postman test suites.
- **Essential Concepts**: `curl` commands (`-X`, `-H`, `-d`), Postman collections and environments, environment variables (saving JWT tokens automatically), and writing Postman test assertions in JavaScript (`pm.expect()`).
- **Practical Coding Exercise**: Write `curl` commands to register a user, extract the JWT token, and make an authenticated request; save the workflow in a Postman collection.
- **Independent Challenge**: Write a Postman pre-request script and test script that automatically exchanges a refresh token when an access token expires.
- **Definition of Done**: Execute an entire authenticated API checkout workflow purely from the terminal using `curl` and inspect response headers.
- **How It Relates to Real Backend Work**: Backend engineers must be able to test endpoints without relying on a frontend UI.
- **Optional Extension**: Run a Postman collection headlessly from the command line using Newman.

#### Day 59: Automated API Testing with `pytest-django` & `APITestCase`
- **Learning Objectives**: Write reliable automated unit and integration tests for API endpoints using `pytest`.
- **Essential Concepts**: Why automated testing is mandatory for junior backend jobs, `pytest-django`, `APITestCase`, testing status codes, payload assertions, and testing permissions.
- **Practical Coding Exercise**: Write automated tests for "ShopCraft" covering: creating a product (as admin vs normal user), retrieving product details, and validation errors.
- **Independent Challenge**: Write an integration test for the checkout endpoint that verifies stock decreases by exactly the ordered quantity and returns 400 when stock is depleted.
- **Definition of Done**: Run `pytest` from the terminal and achieve 100% passing tests across at least 10 API test cases.
- **How It Relates to Real Backend Work**: Production engineering teams never deploy code without automated tests passing in their CI/CD pipeline.
- **Optional Extension**: Test database rollback behavior when an unhandled exception occurs inside a transaction.

#### Day 60: Testing Best Practices: Test Fixtures, Model Factories & Coverage
- **Learning Objectives**: Generate realistic test data with `factory_boy` and measure test coverage using `coverage.py`.
- **Essential Concepts**: The problem with hardcoded test fixtures, dynamic factories (`factory_boy`, `Faker`), pytest fixtures (`@pytest.fixture`), mocking third-party calls (`unittest.mock`), and code coverage reports.
- **Practical Coding Exercise**: Build `UserFactory`, `ProductFactory`, and `OrderFactory` to generate clean, dynamic test data; measure test coverage using `pytest-cov`.
- **Independent Challenge**: Mock an external payment gateway call (so tests run instantly offline) and verify the order status updates to "PAID" on simulated success.
- **Definition of Done**: Generate a code coverage report showing > 80% coverage on core model and view logic.
- **How It Relates to Real Backend Work**: Factories make tests fast, maintainable, and resilient to model schema changes.
- **Optional Extension**: Generate an HTML test coverage report (`coverage html`) and view uncovered code lines.

#### Day 61: Backend Debugging, Error Handling, Logging & Tracebacks
- **Learning Objectives**: Systematically diagnose backend bugs, interpret Python stack traces, and configure production application logging.
- **Essential Concepts**: Python `logging` module (DEBUG, INFO, WARNING, ERROR, CRITICAL), configuring loggers and handlers in `settings.py`, reading complex Django tracebacks, and debugging with `pdb` / `breakpoint()`.
- **Practical Coding Exercise**: Configure rotating file loggers and console loggers in Django; log all 4xx/5xx errors with request paths, user IDs, and timestamps.
- **Independent Challenge**: Diagnose and fix three real-world bugs in an intentionally broken legacy view: a circular import, an unhandled `DoesNotExist` exception, and a timezone-naive datetime bug.
- **Definition of Done**: Use `breakpoint()` in a running Django view to inspect local variables, step through execution, and evaluate QuerySets in the terminal.
- **How It Relates to Real Backend Work**: Senior engineers stand out by how quickly they can read an error traceback in production logs and pinpoint the root cause.
- **Optional Extension**: Configure structured JSON logging for compatibility with cloud log aggregators (Datadog, CloudWatch).

#### Day 62: Clean Code, SOLID Principles & Refactoring Anti-Patterns
- **Learning Objectives**: Write maintainable, self-documenting Python code and refactor messy "fat" views.
- **Essential Concepts**: The SOLID principles in Python backend context: Single Responsibility (SRP), Open/Closed (OCP), Dependency Inversion (DIP), DRY (Don't Repeat Yourself), and eliminating "Fat Models / Fat Views" anti-patterns.
- **Practical Coding Exercise**: Refactor a 200-line monolithic Django view handling file uploads, user creation, payment processing, and email dispatch into decoupled, focused components.
- **Independent Challenge**: Apply the Strategy Pattern to support multiple payment providers (Stripe, PayPal, eSewa) sharing a common interface without `if/else` spaghetti code.
- **Definition of Done**: Explain each letter of SOLID with a concrete Python backend example.
- **How It Relates to Real Backend Work**: Clean, modular code can be modified and extended without introducing unexpected regressions.
- **Optional Extension**: Run `flake8` or `ruff` and `black` to format the codebase to strict PEP 8 standards.

#### Day 63: Service Layer Architecture & Domain-Driven Logic
- **Learning Objectives**: Decouple business logic from Django views and models using the Service Layer and Selector patterns.
- **Essential Concepts**: Why "Fat Models" break down as projects grow, the Service Layer pattern (handling writes and business transactions), the Selectors pattern (handling complex read queries), and building clean API boundaries.
- **Practical Coding Exercise**: Implement `services/order_services.py` containing `create_order(user, items)` and `selectors/product_selectors.py` containing `get_featured_products()`.
- **Independent Challenge**: Refactor the checkout endpoint so the view contains only 5 lines of code: parse request, call service, return response.
- **Definition of Done**: Defend why business logic should live in dedicated services rather than in views or serializers.
- **How It Relates to Real Backend Work**: High-scale Django companies (Instagram, DoorDash) structure their codebases using service layers to keep logic reusable across web views, Celery workers, and CLI commands.
- **Optional Extension**: Write unit tests that test the service function directly without needing HTTP client overhead.

---

### ⚡ Phase 8: Asynchronous Systems, Caching & Background Workers (Days 64–68)

#### Day 64: Caching Strategies with Redis: Cache-Aside & Invalidation
- **Learning Objectives**: Accelerate read performance using Redis in-memory caching and master cache invalidation.
- **Essential Concepts**: In-memory key-value stores (Redis), Cache-Aside pattern, Time-to-Live (TTL), Cache Hit vs Cache Miss, and cache invalidation strategies ("There are only two hard things in Computer Science...").
- **Practical Coding Exercise**: Configure Redis as the Django cache backend; cache heavy product catalog query results with a 15-minute TTL.
- **Independent Challenge**: Implement automatic cache invalidation: when an admin updates a product, immediately invalidate its cached representation using Django model save logic or service functions.
- **Definition of Done**: Benchmark an endpoint before and after Redis caching; explain the risk of stale cache data.
- **How It Relates to Real Backend Work**: Caching reduces database load by 80%+ on read-heavy systems, allowing servers to handle sudden viral traffic spikes.
- **Optional Extension**: Use Redis atomic counters (`INCR`) to implement an in-memory page view counter.

#### Day 65: Asynchronous Task Processing: Celery & Redis Setup
- **Learning Objectives**: Offload slow, blocking operations to asynchronous background workers using Celery and Redis.
- **Essential Concepts**: The synchronous HTTP request bottleneck, why slow tasks (sending emails, processing PDFs, calling third-party APIs) must NEVER run inside an HTTP request, Celery architecture (Producer, Broker, Worker, Result Backend), and `@shared_task`.
- **Practical Coding Exercise**: Set up Celery with Redis broker in Django; create a background task `send_order_confirmation_email(order_id)` that executes asynchronously.
- **Independent Challenge**: Benchmark the checkout API: measure the response time when sending email synchronously (2,000ms) versus offloading via Celery (120ms).
- **Definition of Done**: Start a Celery worker from the terminal (`celery -A project worker -l info`) and watch it execute an async task dispatched from Django.
- **How It Relates to Real Backend Work**: Every production backend requires asynchronous task processing to keep web API response times under 200ms.
- **Optional Extension**: Configure Celery to store task results in Redis and check task status from a polling endpoint.

#### Day 66: Advanced Celery: Retries with Backoff & Celery Beat (Cron)
- **Learning Objectives**: Build resilient background tasks that handle network failures gracefully and schedule recurring jobs.
- **Essential Concepts**: Transient network failures, task retries with exponential backoff (`bind=True, retry_backoff=True`), Dead-Letter Queues, and scheduled recurring jobs with Celery Beat (`CELERY_BEAT_SCHEDULE`).
- **Practical Coding Exercise**: Build an async webhook delivery task that retries up to 5 times with exponential backoff if the remote server returns a 503 error.
- **Independent Challenge**: Configure Celery Beat to run a scheduled cron job every midnight that deletes unverified user accounts older than 48 hours.
- **Definition of Done**: Explain what exponential backoff with jitter is and why it prevents the "Thundering Herd" problem on failing third-party services.
- **How It Relates to Real Backend Work**: Scheduled reporting, data cleanup, and external API communication require automated, fault-tolerant background execution.
- **Optional Extension**: Monitor Celery tasks visually using Flower.

#### Day 67: Real-Time Communication: WebSockets & Django Channels Basics
- **Learning Objectives**: Understand bidirectional, real-time client-server communication using WebSockets and Django Channels.
- **Essential Concepts**: HTTP (unidirectional, request-response) vs WebSockets (bidirectional, persistent full-duplex TCP socket), ASGI architecture (`daphne`), Consumers vs Views, and Channel Layers with Redis.
- **Practical Coding Exercise**: Build a real-time order status consumer: when an order status changes in the database, push a WebSocket message to the connected client.
- **Independent Challenge**: Build a live notification system that broadcasts system announcements to all active WebSocket connections simultaneously using channel groups.
- **Definition of Done**: Open a WebSocket connection from a browser terminal and send/receive real-time messages without refreshing the page.
- **How It Relates to Real Backend Work**: Chat applications, live ride-tracking, trading platforms, and notification bells rely on WebSockets.
- **Optional Extension**: Authenticate incoming WebSocket connections using JWT tokens passed in query strings.

#### Day 68: Webhooks, Third-Party API Integrations & Idempotency Keys
- **Learning Objectives**: Safely integrate external APIs (Stripe/Payment Gateways), verify incoming webhooks, and guarantee idempotency.
- **Essential Concepts**: Webhooks (reverse APIs / event notifications), verifying webhook cryptographic signatures, handling out-of-order events, and Idempotency Keys to prevent duplicate charges.
- **Practical Coding Exercise**: Build a mock payment checkout endpoint that accepts an `Idempotency-Key` header; if the same key is submitted twice, return the cached result without charging again.
- **Independent Challenge**: Build a webhook receiver endpoint for payment success events: verify the signature header, update the order status, and dispatch a fulfillment task.
- **Definition of Done**: Explain why checking webhook signatures is mandatory to prevent attackers from sending fake "Payment Successful" payloads.
- **How It Relates to Real Backend Work**: Integrating payment providers (Stripe, PayPal, Khalti) and external SaaS tools is a standard responsibility for backend engineers.
- **Optional Extension**: Store all raw webhook payloads in an audit table for debugging and replay capabilities.

---

### 🐳 Phase 9: DevOps, Docker, CI/CD & Production Deployment (Days 69–72)

#### Day 69: Linux CLI, Secrets Management & Production Django Settings
- **Learning Objectives**: Navigate Linux terminal environments, manage server processes, and secure production Django configurations.
- **Essential Concepts**: Basic Linux server commands (`ssh`, `systemctl`, `journalctl`, `chmod`, `curl`), environment variable injection (`.env`), disabling `DEBUG = False`, configuring `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`, and Security Middleware (`SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`).
- **Practical Coding Exercise**: Audit a Django project using `python manage.py check --deploy` and resolve every security warning.
- **Independent Challenge**: Write a Bash deployment script that pulls the latest Git code, activates the virtualenv, installs requirements, runs migrations, and collects static files.
- **Definition of Done**: Pass `python manage.py check --deploy` with 0 security warnings.
- **How It Relates to Real Backend Work**: A single leaked secret key or `DEBUG = True` in production can expose entire databases to attackers.
- **Optional Extension**: Set up SSH key authentication on a remote Linux cloud server.

#### Day 70: Docker Fundamentals: Dockerfile & Multi-Stage Builds
- **Learning Objectives**: Containerize Python applications for reproducible execution across development and production environments.
- **Essential Concepts**: Why "It works on my machine" is unacceptable, Containers vs Virtual Machines, Docker images and layers, writing clean `Dockerfile`s, `.dockerignore`, and Multi-Stage builds to keep image sizes small.
- **Practical Coding Exercise**: Write an optimized production `Dockerfile` for your Django application using Python slim base images, non-root users, and cached dependency layers.
- **Independent Challenge**: Build the Docker image from terminal, run it as a container with port mapping (`-p 8000:8000`), and verify API endpoints respond.
- **Definition of Done**: Build a Docker image under 250MB that runs the Django application without root user privileges.
- **How It Relates to Real Backend Work**: Modern backend teams deploy containerized applications to Kubernetes, AWS ECS, or cloud platforms (Render, Railway).
- **Optional Extension**: Scan the Docker container image for security vulnerabilities using `docker scan`.

#### Day 71: Multi-Container Orchestration with `docker-compose`
- **Learning Objectives**: Orchestrate multi-service application stacks containing Django, PostgreSQL, Redis, and Celery.
- **Essential Concepts**: `docker-compose.yml`, container networking, persistent named volumes for PostgreSQL data, service dependencies (`depends_on`), and environment variable passing.
- **Practical Coding Exercise**: Write a complete `docker-compose.yml` file that orchestrates:
  1. `web` (Django Gunicorn app)
  2. `db` (PostgreSQL with persistent volume)
  3. `redis` (In-memory cache & message broker)
  4. `celery_worker` (Background task processor)
- **Independent Challenge**: Boot the entire 4-container stack with a single command (`docker compose up --build`), run database migrations inside the web container, and verify Celery processes tasks.
- **Definition of Done**: Execute `docker compose up` and have web, database, cache, and background workers communicate seamlessly with zero manual setup.
- **How It Relates to Real Backend Work**: New developers can onboard and run the entire company backend locally in 5 minutes using Docker Compose.
- **Optional Extension**: Add a PgBouncer service container between Django and PostgreSQL in the docker-compose stack.

#### Day 72: CI/CD Pipelines with GitHub Actions & Cloud Deployment
- **Learning Objectives**: Build an automated Continuous Integration & Continuous Deployment (CI/CD) pipeline that tests and deploys code on every `git push`.
- **Essential Concepts**: CI/CD concepts, GitHub Actions workflows (`.github/workflows/ci.yml`), automated linting (`flake8`/`black`), running test suites against a live PostgreSQL service container in GitHub, and deploying to cloud hosts (Render / Railway / VPS).
- **Practical Coding Exercise**: Create a GitHub Actions workflow that triggers on every pull request, sets up Python and PostgreSQL, installs dependencies, and runs `pytest`.
- **Independent Challenge**: Configure automatic cloud deployment: when pull requests are merged into `main`, GitHub Actions automatically triggers a production deployment.
- **Definition of Done**: Push a commit with an intentional failing test and watch GitHub Actions block the build; fix the test and see the green checkmark deploy.
- **How It Relates to Real Backend Work**: Automated CI/CD pipelines prevent broken code from ever reaching production servers.
- **Optional Extension**: Add automated test coverage percentage reporting as a PR comment in GitHub Actions.

---

### 🏆 Phase 10: Junior System Design, Interview Bootcamp & Capstone (Days 73–75)

#### Day 73: Junior Backend System Design Masterclass
- **Learning Objectives**: Think like a systems architect and answer standard junior system design interview questions.
- **Essential Concepts**: High-Level Architecture diagrams, Vertical vs Horizontal scaling, Load Balancers (Round Robin, Least Connections), Database Read Replicas vs Write Primary, Database Sharding vs Partitioning, Caching layers, and Rate Limiting algorithms (Token Bucket).
- **Practical Coding Exercise**: Design the architecture for a URL Shortener service (TinyURL) on a whiteboard: calculate QPS, storage requirements for 5 years, Base62 encoding, and cache sizing.
- **Independent Challenge**: Design the high-level architecture for a Real-Time Notification Service handling 1 million concurrent users, detailing databases, message queues, and WebSocket servers.
- **Definition of Done**: Present and defend a complete system architecture diagram explaining how data flows from user click to database write and cache.
- **How It Relates to Real Backend Work**: Junior backend interviews at top tech companies increasingly include a 45-minute basic system design interview.
- **Optional Extension**: Calculate read/write throughput and storage requirements for a Twitter-like feed service.

#### Day 74: 50-Question Senior Mock Technical Interview Bootcamp
- **Learning Objectives**: Articulate complex technical concepts clearly under simulated interview pressure.
- **Essential Concepts**: The STAR interview method (Situation, Task, Action, Result), live coding on a blank whiteboard without autocomplete, answering rapid-fire conceptual questions across Python, SQL, Django, and Concurrency.
- **Practical Coding Exercise**: Solve three live whiteboard coding problems in timed 20-minute sessions:
  1. Two-Sum / Duplicate detection with $O(N)$ time complexity.
  2. SQL query finding the second-highest salary and duplicate emails.
  3. Writing a thread-safe Django model method preventing negative balances.
- **Independent Challenge**: Conduct a full mock interview recording yourself explaining:
  - "How does PostgreSQL's B-Tree index work?"
  - "What is the N+1 problem and how do you fix it?"
  - "What is the difference between processes and threads in Python?"
- **Definition of Done**: Answer 50 technical interview questions across Python, SQL, Django, and Systems with confident, concise, technically rigorous answers.
- **How It Relates to Real Backend Work**: Being a great engineer is only half the battle; being able to communicate technical decisions clearly is what gets you hired.
- **Optional Extension**: Do a peer mock interview or record and critique your video answers.

#### Day 75: Capstone Project Defense & Portfolio Packaging
- **Learning Objectives**: Package your projects into an impressive portfolio, write README documentation, and defend your architectural choices.
- **Essential Concepts**: GitHub profile optimization, writing professional repository READMEs (architecture diagrams, setup instructions, API documentation links, test coverage badges), CV tailoring for backend roles, and presenting project demos.
- **Practical Coding Exercise**: Conduct the final code audit of your Capstone Project (Enterprise Hotel Booking & Inventory Backend); ensure all tests pass and documentation is complete.
- **Independent Challenge**: Write a comprehensive, professional `README.md` for your primary portfolio project including:
  - System Architecture Diagram
  - Tech Stack & Trade-offs Justification
  - Local Setup with Docker Compose
  - API Endpoints Table
  - Test Suite Execution Guide
- **Definition of Done**: Present a public, clean GitHub repository with clear documentation, passing CI tests, and a live deployed API link ready to send to hiring managers.
- **How It Relates to Real Backend Work**: Hiring managers spend less than 60 seconds reviewing a junior developer's GitHub. A clean README and well-architected project is what lands interview callbacks.
- **Optional Extension**: Publish a technical blog post or LinkedIn article explaining how you eliminated N+1 queries or built background queues with Celery.
