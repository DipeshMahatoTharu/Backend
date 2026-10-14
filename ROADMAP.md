# 🚀 75-Day Python Backend & Database Engineering Roadmap (Junior Employability Edition)

Welcome to your practical, project-driven 75-Day Python, PostgreSQL, Django, DRF, and Production Backend curriculum! This roadmap is designed to take you from foundational programming to an **employable junior Python backend developer** with solid fundamentals, clean coding habits, and portfolio-ready projects.

---

## 📊 Program Progress Tracker

- **Current Day**: Day 32 (PostgreSQL Setup, Python Drivers & Connection Management)
- **Completed Days**: 31 / 75
- **Progress**: [████████░░░░░░░░░░░░] 41.3%
- **Current Phase**: Phase 3 — Relational Databases & PostgreSQL Deep Dive
- **Internship & Job Readiness**: In Progress *(Application Window opens at Milestone 3 / Day 50 for internships, and Milestone 4 / Day 63 for junior roles)*

---

## 🎯 Realistic Completion Benchmark
To keep your daily pace sustainable without burnout or unrealistic mastery expectations, a day is considered **Completed** when you can:
1. **Explain the key concept in your own words** without looking at notes (e.g. explaining why parameterized queries prevent SQL injection).
2. **Solve the core practical exercise** with reasonable independence (using hints or documentation when needed).
3. **Debug or explain at least one relevant mistake** (e.g. diagnosing an uncommitted transaction, a typo in a join condition, or a missing validation error).

*Optional extensions* are provided for extra practice on days when you have extra time or curiosity; they are never blockers for moving forward.

---

## 🏗️ The 3-Stage Progressive Project Strategy

Instead of building throwaway mini-projects or restarting from scratch, your work consolidates into **three progressive stages**:

### Stage 1: PostgreSQL Data & Query Layer (Days 32–36)
- **Focus**: Pure relational database foundations.
- **Outcome**: A standalone e-commerce/inventory schema with table constraints, B-Tree and GIN indexes, transaction handling, and query profiling.

### Stage 2: The Progressive Django & DRF Backend — "MarketFlow" (Days 40–63)
- **Focus**: One living, production-style application that evolves day-by-day in a single Git repository.
- **Evolution**:
  - *Days 40–43*: Project setup, environment config, custom `User` model, core `Product`, `Category`, and `Order` models with migrations.
  - *Days 44–50*: Relational queries, eliminating N+1 queries, form validation, and session auth.
  - *Days 51–57*: Transforming into a REST API with DRF serializers, writable nested order creation, JWT authentication, permissions, filtering, and OpenAPI/Swagger documentation.
  - *Days 58–63*: Automated testing with `pytest-django`, fixtures, model factories, logging, error handling, and clean service layers.

### Stage 3: The Production Capstone & Deployment (Days 64–75)
- **Focus**: Taking your Stage 2 application to production-readiness.
- **Evolution**:
  - Adding Redis caching for fast product lookups.
  - Offloading slow operations (order confirmation emails, invoice PDFs) to background workers using Celery and Redis.
  - Multi-container containerization with `docker-compose` (Django + PostgreSQL + Redis + Celery).
  - Automated GitHub Actions CI/CD testing pipeline.
  - Junior developer interview practice and project walkthrough defense.

---

## 🏆 Evidence-Based Job-Readiness Milestones

You do **not** need to master every advanced topic before applying for jobs. Job applications unlock progressively:

- **Milestone 1 (Day 36) — SQL & Relational Database Competence**:
  - *Evidence*: Can write complex queries (`JOIN`, `GROUP BY`, subqueries), design 3NF schemas with foreign keys, explain indexes with `EXPLAIN`, and use transactions safely.
- **Milestone 2 (Day 39) — HTTP & REST Fundamentals**:
  - *Evidence*: Can design clean RESTful endpoints, choose appropriate HTTP methods and status codes, and handle structured JSON request/response bodies.
- **Milestone 3 (Day 50) — Functional Django Web Backend**:
  - *Evidence*: Working Django monolith on GitHub with custom user authentication, relational database models, validated forms, and clean ORM queries.
  - 🎯 **INTERNSHIP APPLICATION TRIGGER**: You now have enough practical evidence (Python, Git, SQL, and Django) to start applying for **Backend Internships**!
- **Milestone 4 (Day 63) — Tested Production REST API**:
  - *Evidence*: Complete Django REST Framework API with JWT auth, nested serializers, object-level permissions, and a passing automated `pytest` test suite on GitHub.
  - 🚀 **JUNIOR DEVELOPER APPLICATION TRIGGER**: You are now qualified to apply actively for **Junior Python / Django Backend Developer roles**!
- **Milestone 5 (Day 72) — Containerized Production Deployment**:
  - *Evidence*: Docker Compose setup running Django, PostgreSQL, Redis, and Celery, with automated CI testing via GitHub Actions and live cloud deployment.
- **Milestone 6 (Day 75) — Junior Interview & System Architecture Ready**:
  - *Evidence*: Can walk through project architecture, explain trade-offs (caching, relational vs NoSQL, indexes), and solve practical junior coding/debugging interview problems.

---

# 📅 Detailed Daily Curriculum (Days 32–75)

---

### 🗄️ Phase 3: Relational Databases & PostgreSQL Deep Dive (Days 32–36)
*Stage 1 Project: PostgreSQL Data & Query Layer*

#### Day 32: PostgreSQL Setup, Python Drivers & Connection Management [CURRENT DAY]
- **Learning Objectives**: Connect Python to PostgreSQL using a standard driver (`psycopg2` or `psycopg3`), execute parameterized queries, and implement clean connection and transaction lifecycles.
- **Essential Concepts**: Client-server database model, connection overhead, parameterization with `%s` to prevent SQL injection, `cursor.fetchone()` vs `fetchall()`, explicit `commit()` and `rollback()`, and the purpose of basic connection pools (`ThreadedConnectionPool` or `psycopg.pool.ConnectionPool`).
- **Practical Coding Exercise**: Write a Python script that connects to PostgreSQL, parses database credentials from environment variables, creates a sample table, and safely inserts user records using parameterized tuples.
- **Independent Challenge**: Build a context manager `managed_connection(pool)` that checks out a connection from a pool, commits on success, rolls back on exception, and guarantees the connection returns to the pool in a `finally` block.
- **Definition of Done**: Explain why formatting strings into SQL queries (`f"SELECT * FROM users WHERE name = '{name}'"`) is a security vulnerability; demonstrate clean query execution and rollback on error.
- **How It Relates to Real Backend Work**: Python backends interact with databases through drivers. Handling connections safely ensures database sockets are never leaked or left hanging.
- **Optional Extension**: Read about how connection poolers like PgBouncer manage thousands of client connections in production environments.

#### Day 33: PostgreSQL Indexing, B-Trees & Query Optimization
- **Learning Objectives**: Read query execution plans with `EXPLAIN ANALYZE` and apply B-Tree and composite indexes to resolve slow queries.
- **Essential Concepts**: B-Tree index structure, Sequential Scan (reading every disk page) vs Index Scan, the Leftmost Prefix Rule on composite indexes (`A, B`), and Expression Indexes (e.g. `LOWER(email)`).
- **Practical Coding Exercise**: Seed a test table with 20,000+ rows; profile a search query using `EXPLAIN ANALYZE` before and after adding a B-Tree index to observe the measurable drop in execution time.
- **Independent Challenge**: Given a query with multiple filter criteria (`WHERE customer_id = ? AND status = ? ORDER BY created_at DESC`), design a composite index that satisfies both filtering and ordering without a slow sort step.
- **Definition of Done**: Explain what an index is to a non-technical person; identify whether a query is using an index or a sequential scan from its `EXPLAIN` output.
- **How It Relates to Real Backend Work**: Database indexes are the primary tool backend engineers use to keep queries fast as user data grows from thousands to millions of records.
- **Optional Extension**: Explore partial indexes (`CREATE INDEX ... WHERE is_active = TRUE`) and when they save memory.

#### Day 34: Database Normalization (1NF–3NF), Schema Design & ER Modeling
- **Learning Objectives**: Design clean relational database schemas in Third Normal Form (3NF) and model table relationships with foreign keys.
- **Essential Concepts**: 1NF (atomic values, primary keys), 2NF (no partial key dependencies), 3NF (no transitive dependencies), Many-to-Many junction tables, and foreign key deletion behaviors (`CASCADE` vs `RESTRICT` / `PROTECT` vs `SET NULL`).
- **Practical Coding Exercise**: Take an unnormalized sales table containing duplicate customer and product details, and write DDL statements to split it into normalized `customers`, `products`, and `orders` tables.
- **Independent Challenge**: Design a whiteboard schema for a ride-sharing service with `riders`, `drivers`, `rides`, and `reviews`, enforcing ratings bounds and using `RESTRICT` to prevent accidental deletion of historical rides.
- **Definition of Done**: Explain the difference between `ON DELETE CASCADE` and `ON DELETE RESTRICT`, and why financial systems avoid cascading deletes.
- **How It Relates to Real Backend Work**: Solid schema design prevents data corruption and redundant storage, saving engineering teams from difficult database migrations later.
- **Optional Extension**: Compare `BIGINT` auto-incrementing primary keys with `UUIDv4` keys in terms of readability and storage.

#### Day 35: Transactions, ACID, MVCC & Concurrency Basics
- **Learning Objectives**: Ensure data consistency using database transactions, understand isolation levels, and prevent race conditions.
- **Essential Concepts**: ACID properties (Atomicity, Consistency, Isolation, Durability), how PostgreSQL MVCC allows concurrent reads without table locking, transaction isolation levels (Read Committed vs Repeatable Read), and row-level locking with `SELECT ... FOR UPDATE`.
- **Practical Coding Exercise**: Simulate a concurrent inventory decrement where two processes attempt to buy the last available item simultaneously; use an atomic query or row lock to ensure only one succeeds.
- **Independent Challenge**: Implement a safe bank balance transfer between two accounts that executes inside a transaction, rolls back if any step fails, and acquires row locks in a consistent order to prevent deadlocks.
- **Definition of Done**: Explain what a race condition is in the context of an inventory or wallet system; demonstrate that a transaction rolls back completely on error.
- **How It Relates to Real Backend Work**: E-commerce checkouts and financial operations must be atomic—money and inventory must never be duplicated or lost due to server errors.
- **Optional Extension**: Learn how `SELECT ... FOR UPDATE SKIP LOCKED` enables worker queues to pull jobs concurrently.

#### Day 36: PostgreSQL Advanced Data Types: JSONB & Full-Text Search Basics
- **Learning Objectives**: Store and query semi-structured data using `JSONB` and implement basic full-text search.
- **Essential Concepts**: When to use relational columns vs `JSONB` (semi-structured or variable attributes), querying JSON keys (`->`, `->>`), GIN indexes for JSON documents, and Full-Text Search with `to_tsvector` / `to_tsquery` vs `LIKE '%...%'`.
- **Practical Coding Exercise**: Create a products table with a `JSONB` attributes column (e.g. storage, color, dimensions) and query products matching specific internal JSON keys.
- **Independent Challenge**: Set up a basic full-text search index on product titles and descriptions, and compare its behavior and performance against a standard `LIKE` wildcard search.
- **Definition of Done**: Explain when `JSONB` is appropriate and when traditional relational columns are better; query a nested key from a JSON column.
- **How It Relates to Real Backend Work**: E-commerce catalogs, audit logs, and external API responses often contain flexible fields where `JSONB` avoids managing dozens of sparse columns.
- **Optional Extension**: Explore trigram similarity (`pg_trgm`) for typo-tolerant searches (e.g. matching "iphoen" to "iPhone").

---

### 🌐 Phase 4: HTTP Protocols & REST API Architecture (Days 37–39)

#### Day 37: HTTP Protocols, Request-Response Lifecycle & Headers
- **Learning Objectives**: Understand how client-server web communication works and inspect HTTP headers and payloads.
- **Essential Concepts**: Client-server model, Request structure (method, path, headers, query params, body), Response structure (status code, headers, payload), statelessness, content negotiation (`Content-Type`, `Accept`), and cookies vs auth headers.
- **Practical Coding Exercise**: Use Python's built-in `http.client` or `urllib.request` to send manual HTTP requests, parse status codes, and inspect response headers and JSON bodies.
- **Independent Challenge**: Build a small Python script that takes a URL, sends a request with custom headers (such as `User-Agent` and `Authorization`), and displays the parsed response status and JSON data.
- **Definition of Done**: Trace the path of an HTTP request from client to server and back; explain the difference between query parameters and request body data.
- **How It Relates to Real Backend Work**: Web frameworks like Django are tools for receiving HTTP requests and returning HTTP responses. Understanding raw HTTP makes debugging authentication, CORS, and headers straightforward.
- **Optional Extension**: Inspect network requests and headers in your browser's Developer Tools (Network tab).

#### Day 38: HTTP Methods, Idempotency & Standard Status Codes
- **Learning Objectives**: Select appropriate HTTP methods and status codes according to web standards.
- **Essential Concepts**: CRUD mapping to HTTP verbs (GET for read, POST for create, PUT for complete replace, PATCH for partial update, DELETE for remove), idempotency (why GET/PUT/DELETE are idempotent and POST is not), and status code families (200, 201, 204; 400, 401, 403, 404, 422; 500).
- **Practical Coding Exercise**: Write a small Python router function that inspects incoming method and resource paths and returns appropriate mock responses with correct status codes.
- **Independent Challenge**: Create a consistent error response structure for client errors (400, 404) that returns a clear error code, message, and details for invalid fields.
- **Definition of Done**: Explain the difference between `PUT` and `PATCH`, and between `401 Unauthorized` and `403 Forbidden`.
- **How It Relates to Real Backend Work**: Consistent status codes and standard verbs allow frontend and mobile developers to integrate with your API reliably without guesswork.
- **Optional Extension**: Read the RFC specification summary for the `Idempotency-Key` header used in payment APIs.

#### Day 39: RESTful API Conventions & Resource Design
- **Learning Objectives**: Design predictable, REST-compliant API endpoint structures.
- **Essential Concepts**: Resource-oriented URLs (using nouns, e.g. `/api/v1/orders`), plural naming conventions, nested sub-resources (e.g. `/api/v1/users/3/orders`), filtering and pagination via query parameters, and API versioning.
- **Practical Coding Exercise**: Draft the API specification (endpoints, supported methods, request bodies, and responses) for an e-commerce order management system.
- **Independent Challenge**: Review and refactor an anti-pattern API design (e.g. `/getAllProducts`, `/deleteUser?id=5`) into clean, standardized RESTful URIs.
- **Definition of Done**: Defend why REST APIs avoid verbs in URL paths and explain how non-CRUD actions (such as `/orders/12/cancel`) can be represented cleanly.
- **How It Relates to Real Backend Work**: A clean API contract is the foundation of communication between backend developers, frontend teams, and third-party partners.
- **Optional Extension**: Write your API design draft in standard OpenAPI/Swagger format.

---

### 🦄 Phase 5: Progressive Django Web Framework Mastery (Days 40–50)
*Stage 2 Project Begins: "MarketFlow" — Progressive E-Commerce & Inventory Backend*

#### Day 40: Django Project Setup, Virtual Environments & Settings Configuration
- **Learning Objectives**: Initialize a clean Django project, manage virtual environments, and configure settings using environment variables.
- **Essential Concepts**: Python virtual environments (`venv`), `requirements.txt`, Django's architecture, project layout (`manage.py`, project folder, apps), `settings.py` anatomy (`INSTALLED_APPS`, `DATABASES`), and reading configuration from environment variables.
- **Practical Coding Exercise**: Create the "MarketFlow" Django project inside an isolated virtual environment, connect it to PostgreSQL using credentials from a `.env` file, and verify migrations run.
- **Independent Challenge**: Set up separate development and production settings configurations to ensure `DEBUG = False` and secure secrets in production environments.
- **Definition of Done**: Run `python manage.py runserver` connected to PostgreSQL without hardcoding passwords in `settings.py`.
- **How It Relates to Real Backend Work**: Keeping secrets out of Git and managing environments cleanly is a baseline requirement for any professional software repository.
- **Optional Extension**: Create a custom `manage.py` command that prints project configuration details.

#### Day 41: Django URL Routing & Class-Based Views (CBVs) vs FBVs
- **Learning Objectives**: Route incoming URLs to views, extract path parameters, and compare Function-Based Views with Class-Based Views.
- **Essential Concepts**: `urls.py`, path converters (`<int:pk>`, `<slug:slug>`), Function-Based Views (FBVs) vs Class-Based Views (CBVs), View dispatching, and returning `HttpResponse` and `JsonResponse`.
- **Practical Coding Exercise**: Build URL routes for "MarketFlow" mapping to product list and product detail views returning JSON data using both an FBV and a generic `View` class.
- **Independent Challenge**: Build a `ProductDetailView` that handles `GET` requests to display details and returns a clean 404 response if the product ID does not exist.
- **Definition of Done**: Explain when an FBV is simpler and when a CBV provides better code reuse.
- **How It Relates to Real Backend Work**: URL routers and views are the traffic directors of your backend, connecting incoming HTTP requests to business logic.
- **Optional Extension**: Implement a custom path converter for product SKUs matching specific alphanumeric patterns.

#### Day 42: Django Template Engine & Static Files Basics
- **Learning Objectives**: Render server-side templates with dynamic context and manage static assets.
- **Essential Concepts**: Django Template Language (DTL), template inheritance (`{% extends %}`, `{% block %}`), passing context dictionaries, template filters, and static files configuration (`STATIC_URL`, `STATIC_ROOT`).
- **Practical Coding Exercise**: Build a clean base template and an inventory product catalog page for "MarketFlow" displaying product cards, prices, and stock indicators.
- **Independent Challenge**: Create a custom template filter that formats prices with currency symbols and handles discounts cleanly.
- **Definition of Done**: Render a dynamic list of items from a view into an inherited template layout.
- **How It Relates to Real Backend Work**: While modern APIs return JSON, backend developers frequently render server-side admin portals, customer receipts, and email templates.
- **Optional Extension**: Add a context processor that provides global site settings across all templates.

#### Day 43: Django Models, Field Types & The Migrations Engine
- **Learning Objectives**: Define relational models, choose appropriate field types, and manage database schema evolution with migrations.
- **Essential Concepts**: `models.Model`, field types (`CharField`, `DecimalField`, `DateTimeField`, `BooleanField`), field options (`null`, `blank`, `default`, `unique`), and how `makemigrations` and `migrate` generate and apply SQL DDL.
- **Practical Coding Exercise**: Create the core `Category` and `Product` models for "MarketFlow", including price, SKU, stock quantity, and active status; run and inspect the migration.
- **Independent Challenge**: Use `python manage.py sqlmigrate` to inspect the raw SQL generated by your migration, and add a database-level `CheckConstraint` ensuring prices are positive.
- **Definition of Done**: Successfully create and apply a migration to PostgreSQL and inspect the resulting table in your database client.
- **How It Relates to Real Backend Work**: Migrations allow multiple developers and production servers to keep their database schemas in sync safely across software updates.
- **Optional Extension**: Practice reverting a migration safely using `python manage.py migrate <app_name> <previous_migration>`.

#### Day 44: Django ORM Queries: Filtering, Q Objects & Aggregations
- **Learning Objectives**: Query database records using Django's ORM and perform lookups, aggregations, and complex queries.
- **Essential Concepts**: QuerySets, lazy evaluation, field lookups (`__icontains`, `__gte`, `__in`), combining conditions with `Q` objects (`Q(A) | Q(B)`), and summary calculations with `aggregate()` and `annotate()`.
- **Practical Coding Exercise**: Write queries for "MarketFlow" to find low-stock products, search products by keyword in title or description, and calculate the average product price per category.
- **Independent Challenge**: Use `F` expressions to write an atomic query that increments product view counts or decrements stock directly in the database without read-modify-write race conditions.
- **Definition of Done**: Explain why QuerySets are lazy and verify when an actual database query is executed.
- **How It Relates to Real Backend Work**: The ORM translates Python code into optimized SQL queries, providing productivity and SQL injection safety.
- **Optional Extension**: Use Django's `Count` and `Avg` to list categories ordered by their total product count.

#### Day 45: ORM Performance: Identifying and Resolving N+1 Queries
- **Learning Objectives**: Detect unoptimized query loops (the N+1 query problem) and eliminate them using `select_related` and `prefetch_related`.
- **Essential Concepts**: What the N+1 problem is, how accessing foreign keys in a loop triggers multiple database hits, `select_related` (SQL `JOIN` for single-valued relationships), and `prefetch_related` (separate batch query for many-valued relationships).
- **Practical Coding Exercise**: Create a view listing 20 products and their categories; inspect the query count using `connection.queries`, observe the N+1 queries, and reduce them using `select_related('category')`.
- **Independent Challenge**: Write an order list view displaying each order, its customer, and all purchased items; use `prefetch_related` to fetch the items efficiently without querying the database inside the loop.
- **Definition of Done**: Explain the difference between `select_related` and `prefetch_related` and show a measurable reduction in query count on a relationship query.
- **How It Relates to Real Backend Work**: Eliminating N+1 queries is one of the most common performance optimizations in Django and a standard technical interview question.
- **Optional Extension**: Configure `django-debug-toolbar` in your development environment to inspect query counts visually.

#### Day 46: Model Relationships: ForeignKey, OneToOne & ManyToMany
- **Learning Objectives**: Model real-world relationships between entities and use custom junction tables.
- **Essential Concepts**: `ForeignKey` (one-to-many), `OneToOneField` (one-to-one), `ManyToManyField` (many-to-many), `related_name` for clean reverse queries, and intermediate models using the `through` argument.
- **Practical Coding Exercise**: Model the "MarketFlow" order structure: `Order` belongs to a user, and contains multiple products through an `OrderItem` model recording quantity and unit price at time of purchase.
- **Independent Challenge**: Query all orders placed by a specific user using the reverse relationship (`user.orders.all()`), and find all products ordered in the last 30 days.
- **Definition of Done**: Explain why `related_name` is useful and why `OrderItem` should store the historical purchase price rather than referencing the live product price.
- **How It Relates to Real Backend Work**: Real-world backend data is relational; modeling parent-child relationships correctly is essential for business integrity.
- **Optional Extension**: Add a `UniqueConstraint` on `(order, product)` in `OrderItem` to prevent duplicate line items.

#### Day 47: Django Forms & ModelForms with Defensive Validation
- **Learning Objectives**: Validate user input and build clean creation and update forms.
- **Essential Concepts**: `Form` vs `ModelForm`, form fields and widgets, `is_valid()`, accessing `cleaned_data`, field-level validation (`clean_<fieldname>`), and cross-field validation (`clean()`).
- **Practical Coding Exercise**: Build a `ProductForm` that validates incoming product data, ensuring titles are descriptive and prices meet minimum requirements.
- **Independent Challenge**: Add a cross-field validation rule in an `OrderForm` ensuring that orders marked "express delivery" include a valid delivery phone number.
- **Definition of Done**: Demonstrate that submitting invalid form data redisplays the form with clear, field-specific error messages.
- **How It Relates to Real Backend Work**: Backend applications must never trust raw incoming data; form validation ensures data conforms to business rules before reaching models.
- **Optional Extension**: Create a reusable custom validator function that can be attached to model or form fields.

#### Day 48: Django Authentication, Password Security & Sessions
- **Learning Objectives**: Authenticate users securely, manage user sessions, and handle login/logout flows.
- **Essential Concepts**: Django's authentication system (`django.contrib.auth`), one-way password hashing (PBKDF2/Argon2), session cookies, login views, logout views, and protecting views with `@login_required`.
- **Practical Coding Exercise**: Build user registration, login, and logout views for "MarketFlow" with session management and password confirmation.
- **Independent Challenge**: Create a user profile view that displays past orders only for the currently logged-in user, redirecting unauthenticated visitors to login.
- **Definition of Done**: Explain why passwords must be hashed rather than encrypted; verify that session cookies maintain user state across requests.
- **How It Relates to Real Backend Work**: User authentication is the gateway to user-specific data, billing, and account management in web applications.
- **Optional Extension**: Configure secure cookie settings (`SESSION_COOKIE_HTTPONLY`, `SESSION_COOKIE_SECURE`) in your settings file.

#### Day 49: Custom User Models (`AbstractUser`) & Role-Based Access
- **Learning Objectives**: Implement a production-recommended Custom User Model and manage user permissions.
- **Essential Concepts**: Why defining a custom user model (`AUTH_USER_MODEL`) is best practice at project start, `AbstractUser` vs `AbstractBaseUser`, using email as the login identifier, Django groups, and permission checks.
- **Practical Coding Exercise**: Implement a custom `User` model for "MarketFlow" with email-based login, full name, and role flags (Customer vs Staff/Manager).
- **Independent Challenge**: Create a permission-checking helper or decorator that restricts inventory editing views to users with the Staff or Manager role.
- **Definition of Done**: Explain why starting with a custom user model avoids difficult database migrations later if user fields need customization.
- **How It Relates to Real Backend Work**: Real-world backends almost always customize user models to support email logins, organization memberships, and role-based permissions.
- **Optional Extension**: Customize the Django Admin portal to display your custom user fields and role filters.

#### Day 50: Project Consolidation: Model Methods, Signals vs Services & Milestone 1 Checkpoint
- **Learning Objectives**: Consolidate your Django monolith, place business logic in clean model methods or services, and review Milestone 3 competencies.
- **Essential Concepts**: Where business logic belongs (Model methods vs dedicated Service functions vs Signals), why explicit service functions are easier to test and debug than signals, and soft deletion patterns.
- **Practical Coding Exercise**: Refactor order completion logic into an explicit service function `process_order_checkout(order, payment_data)` that updates stock and order status inside a transaction.
- **Independent Challenge**: Review the complete "MarketFlow" Django application: ensure migrations are clean, relationships are indexed, and the core purchase flow works smoothly.
- **Definition of Done**: Complete Milestone 3: Demonstrate a working Django application on GitHub with custom auth, models, forms, and clean queries.
- **How It Relates to Real Backend Work**: Keeping business logic organized in service functions keeps codebases readable as features multiply.
- **Optional Extension**: Prepare your resume draft with your Stage 2 repository link and start researching junior backend and internship postings.

---

### ⚡ Phase 6: Django REST Framework (DRF) Production APIs (Days 51–57)
*Stage 2 Continues: Transforming "MarketFlow" into a Production REST API*

#### Day 51: DRF Architecture, ModelSerializers & Field Validation
- **Learning Objectives**: Build REST API endpoints using Django REST Framework and validate incoming JSON payloads.
- **Essential Concepts**: Serialization (Model to Python/JSON) vs Deserialization (JSON to validated Python), `ModelSerializer`, declaring read-only fields, field validators (`validate_<fieldname>`), and cross-field validation (`validate()`).
- **Practical Coding Exercise**: Build `CategorySerializer` and `ProductSerializer` for "MarketFlow" with field validations ensuring positive prices and valid SKUs.
- **Independent Challenge**: Add a `SerializerMethodField` to `ProductSerializer` that calculates whether the item is in stock (`is_in_stock = True/False`) based on current inventory count.
- **Definition of Done**: Send a POST request with invalid data and verify that DRF returns a `400 Bad Request` with structured field-specific error messages.
- **How It Relates to Real Backend Work**: Serializers are the core building block of DRF APIs, ensuring incoming data is clean before it touches the database.
- **Optional Extension**: Use the `depth` option or a nested serializer to represent category details inside a product response.

#### Day 52: Writable Nested Serializers: Managing Related Records
- **Learning Objectives**: Create and update related parent-child objects in a single API request.
- **Essential Concepts**: Nested relationships in serializers, read-only vs writable nested serializers, overriding `create()` and `update()` on serializers, and wrapping multi-table writes in `transaction.atomic()`.
- **Practical Coding Exercise**: Build an `OrderCreateSerializer` that accepts customer information along with a list of line items (`[{"product": 1, "quantity": 2}, ...]`) and creates both the `Order` and its `OrderItem` records.
- **Independent Challenge**: Add validation to ensure that all requested items are in stock before creating the order; if any item is out of stock, raise a validation error so no records are written.
- **Definition of Done**: Send a single JSON payload that creates an order with multiple line items atomically; verify all records are created in PostgreSQL.
- **How It Relates to Real Backend Work**: In real APIs, clients submit full shopping carts, invoices, and forms in a single payload rather than making separate calls for every row.
- **Optional Extension**: Support updating an existing order's status and line items through a `PUT` request.

#### Day 53: APIView, Generic Views, Mixins & ModelViewSets with Routers
- **Learning Objectives**: Choose the appropriate view abstraction in DRF and use Routers for clean URL generation.
- **Essential Concepts**: `APIView` (full control), `GenericAPIView` with mixins (`ListModelMixin`, `CreateModelMixin`), `ModelViewSet` (standard CRUD in minimal code), and `DefaultRouter` for automatic URL routing.
- **Practical Coding Exercise**: Build product catalog endpoints using `ModelViewSet` with a router, and implement a custom checkout endpoint using `APIView`.
- **Independent Challenge**: Override `get_queryset()` on your `ProductViewSet` so that inactive products are hidden from public users but visible to staff users.
- **Definition of Done**: Explain when a `ModelViewSet` is appropriate and when an `APIView` is a better choice for custom business logic.
- **How It Relates to Real Backend Work**: ViewSets eliminate repetitive boilerplate for standard CRUD operations, while `APIView` handles specialized business endpoints.
- **Optional Extension**: Add a custom endpoint to a ViewSet using the `@action` decorator (e.g. `/api/products/featured/`).

#### Day 54: DRF Authentication: Token Auth & JWT with SimpleJWT
- **Learning Objectives**: Authenticate API requests using JSON Web Tokens (JWT) and implement token refresh flows.
- **Essential Concepts**: Token-based authentication vs session cookies, JWT anatomy (Header, Payload, Signature), short-lived Access Tokens vs long-lived Refresh Tokens, and `djangorestframework-simplejwt`.
- **Practical Coding Exercise**: Install and configure `SimpleJWT` in "MarketFlow", verify that obtaining a token returns access and refresh tokens, and protect product creation endpoints.
- **Independent Challenge**: Build a custom token serializer that includes the user's role and username in the token response payload.
- **Definition of Done**: Successfully make an authenticated API request using the `Authorization: Bearer <token>` header; verify that unauthenticated requests receive a `401 Unauthorized`.
- **How It Relates to Real Backend Work**: Single-page web apps (React, Vue) and mobile apps (iOS, Android) authenticate to backend APIs primarily using JWTs.
- **Optional Extension**: Configure token refresh rotation so that using a refresh token automatically issues a new one.

#### Day 55: Permissions, Role-Based Access & API Throttling Basics
- **Learning Objectives**: Protect API endpoints with permissions and configure basic rate limiting to prevent abuse.
- **Essential Concepts**: Standard permissions (`IsAuthenticated`, `IsAdminUser`, `AllowAny`), creating custom permissions with `BasePermission` (`has_permission`, `has_object_permission`), and API throttling (`AnonRateThrottle`, `UserRateThrottle`).
- **Practical Coding Exercise**: Build a custom permission `IsOwnerOrReadOnly` allowing any user to view an order, but only the order's creator (or admin) to edit or cancel it.
- **Independent Challenge**: Configure rate limiting so that anonymous users are restricted to a reasonable threshold (e.g. 20 requests per minute) on sensitive endpoints.
- **Definition of Done**: Test an endpoint with two different users and verify that user A cannot edit user B's order.
- **How It Relates to Real Backend Work**: Permissions ensure that users can only access and modify their own data, preventing unauthorized data access.
- **Optional Extension**: Create a permission class that checks for specific Django group memberships.

#### Day 56: Filtering, Searching, Ordering & Custom Pagination
- **Learning Objectives**: Add search, filtering, sorting, and pagination to list endpoints.
- **Essential Concepts**: Query parameter filtering with `django-filter`, search filtering (`SearchFilter`), sorting (`OrderingFilter`), and `PageNumberPagination` vs `LimitOffsetPagination`.
- **Practical Coding Exercise**: Add multi-field filtering to the product list endpoint (filter by category, price range, search in title, and order by price or creation date).
- **Independent Challenge**: Build a custom pagination class that returns metadata (such as `total_items`, `total_pages`, `current_page`) along with the results array.
- **Definition of Done**: Query an endpoint using filter parameters (e.g. `?category=electronics&price_min=50&ordering=-price`) and observe correctly filtered, paginated JSON results.
- **How It Relates to Real Backend Work**: Frontend applications rely on backend filtering and pagination to deliver fast, responsive search and catalog browsing.
- **Optional Extension**: Explore how CursorPagination avoids issues with duplicate items on rapidly updating datasets.

#### Day 57: API Documentation with OpenAPI 3.0 & Swagger (`drf-spectacular`)
- **Learning Objectives**: Generate interactive, standardized API documentation using `drf-spectacular`.
- **Essential Concepts**: The role of OpenAPI 3.0 / Swagger in backend engineering, `drf-spectacular`, auto-generating schemas, interactive Swagger UI (`/api/docs/`), and documenting custom endpoints with `@extend_schema`.
- **Practical Coding Exercise**: Install and configure `drf-spectacular` in "MarketFlow", generate the OpenAPI schema, and verify the interactive Swagger UI renders in a browser.
- **Independent Challenge**: Document a custom checkout endpoint with `@extend_schema`, including sample request bodies, expected responses, and field descriptions.
- **Definition of Done**: Open `/api/docs/` in a browser, view documented endpoints with parameter types, and execute an authenticated API call directly from the Swagger UI.
- **How It Relates to Real Backend Work**: Frontend developers, QA engineers, and external partners rely on Swagger UI to understand and test API capabilities.
- **Optional Extension**: Export your OpenAPI schema to a static JSON file for import into Postman.

---

### 🧪 Phase 7: Automated Testing, Clean Code & Architecture (Days 58–63)
*Stage 2 Continues: Testing, Hardening & Structuring "MarketFlow"*

#### Day 58: API Manual Testing: Postman Workspaces & cURL CLI
- **Learning Objectives**: Test and debug API endpoints from the command line and build structured Postman test collections.
- **Essential Concepts**: Testing APIs with `curl` (`-X`, `-H`, `-d`), creating Postman collections and environments, storing JWT tokens in environment variables, and writing simple Postman test assertions.
- **Practical Coding Exercise**: Write `curl` commands to log in, extract a JWT token, and make an authenticated POST request to create an order; save this workflow in Postman.
- **Independent Challenge**: Set up a Postman collection test script that automatically captures the access token from the login response and sets it for subsequent requests.
- **Definition of Done**: Execute an authenticated API flow from login to order creation using both `curl` and Postman.
- **How It Relates to Real Backend Work**: Backend developers regularly test and demonstrate endpoints without waiting for a frontend application to be built.
- **Optional Extension**: Export your Postman collection and environment to JSON for sharing in your Git repository.

#### Day 59: Automated API Testing with `pytest-django` & `APITestCase`
- **Learning Objectives**: Write reliable automated unit and integration tests for API endpoints.
- **Essential Concepts**: Why automated testing is essential for backend employability, `pytest-django` vs Django's `TestCase`, `APIClient`, testing HTTP status codes, validating response data, and testing permissions.
- **Practical Coding Exercise**: Write automated test cases for "MarketFlow" verifying that unauthenticated users cannot create products and that valid data returns `201 Created`.
- **Independent Challenge**: Write an integration test for order creation that verifies stock is deducted and that attempting to order more than available stock returns a `400 Bad Request`.
- **Definition of Done**: Run `pytest` from the terminal and achieve passing test results across core happy paths, validation failures, and permission checks.
- **How It Relates to Real Backend Work**: Automated tests give engineering teams confidence that new code changes will not break existing features in production.
- **Optional Extension**: Test that database changes roll back cleanly when a test completes.

#### Day 60: Testing Best Practices: Test Fixtures, Model Factories & Pragmatic Coverage
- **Learning Objectives**: Write maintainable tests using fixtures and model factories, and measure code coverage.
- **Essential Concepts**: `pytest` fixtures (`@pytest.fixture`), generating realistic test data with `factory_boy`, mocking external services with `unittest.mock`, and measuring coverage with `coverage.py` (prioritizing critical business logic over 100% metrics).
- **Practical Coding Exercise**: Build `UserFactory` and `ProductFactory` to generate test data cleanly, eliminating brittle hardcoded database setups across your test files.
- **Independent Challenge**: Use `pytest-cov` to generate a test coverage report for your models and API views, ensuring authentication, permissions, and checkout logic are covered.
- **Definition of Done**: Run your test suite with `pytest --cov` and demonstrate passing tests using factories and fixtures.
- **How It Relates to Real Backend Work**: Model factories keep tests clean, readable, and easy to maintain when schemas change.
- **Optional Extension**: Mock an external API call (like a notification service) so tests run reliably offline.

#### Day 61: Backend Debugging, Error Handling & Logging
- **Learning Objectives**: Diagnose backend issues systematically, interpret tracebacks, and configure application logging.
- **Essential Concepts**: Python's `logging` module (DEBUG, INFO, WARNING, ERROR), configuring logging handlers in `settings.py`, reading Python tracebacks, and debugging with `breakpoint()` / `pdb`.
- **Practical Coding Exercise**: Configure a console and file logger in "MarketFlow" that logs incoming request paths, user actions, and error details when exceptions occur.
- **Independent Challenge**: Introduce an intentional error into a view, trigger it, read the traceback in your log file, and use `breakpoint()` in the terminal to inspect local variables and resolve the issue.
- **Definition of Done**: Demonstrate finding and fixing a bug using log output and interactive terminal debugging.
- **How It Relates to Real Backend Work**: In production, developers cannot attach graphical debuggers; diagnosing issues through server logs is an essential daily skill.
- **Optional Extension**: Log structured error details (timestamp, user ID, path, error message) for easy searching.

#### Day 62: Clean Code & Refactoring Common Backend Anti-Patterns
- **Learning Objectives**: Refactor complex code into clean, readable functions using established design principles.
- **Essential Concepts**: Single Responsibility Principle (functions that do one thing well), eliminating duplicated code (DRY), refactoring "Fat Views" into smaller helper functions, and code formatting tools (`black`, `flake8` / `ruff`).
- **Practical Coding Exercise**: Take a large, multi-step view (handling validation, calculation, database writes, and email notifications) and refactor it into clean, modular functions.
- **Independent Challenge**: Format your entire repository with `black` and run a linter to resolve PEP 8 style issues and unused imports.
- **Definition of Done**: Explain what the Single Responsibility Principle means in a backend context; show before-and-after of a refactored view.
- **How It Relates to Real Backend Work**: Readable, well-structured code is easier for teammates to review, maintain, and extend safely.
- **Optional Extension**: Write a small Python script to check that docstrings are present on public functions.

#### Day 63: Service Layer Architecture & Milestone 4 Checkpoint
- **Learning Objectives**: Decouple business logic from views and serializers using a dedicated service layer, and reach Milestone 4.
- **Essential Concepts**: The Service Layer pattern (placing business operations in dedicated functions/classes), the Selectors pattern (clean query functions), and keeping views thin and focused on HTTP transport.
- **Practical Coding Exercise**: Create a `services/order_services.py` module containing `place_order(user, cart_items)` and update your order API view to simply call this service.
- **Independent Challenge**: Audit your entire "MarketFlow" repository: verify all tests pass, README documentation is clean, and code is organized into apps, services, and serializers.
- **Definition of Done**: Complete Milestone 4: Have a complete, tested, documented DRF REST API repository on GitHub.
- **How It Relates to Real Backend Work**: Service layers keep business logic reusable across web views, background workers, and management commands.
- **Optional Extension**: 🚀 **MILESTONE 4 APPLICATION TRIGGER**: Update your CV and LinkedIn with your "MarketFlow" repository and begin applying for junior backend and internship positions!

---

### ⚡ Phase 8: Asynchronous Systems, Caching & Background Workers (Days 64–68)
*Stage 3 Project Begins: Production Capstone — Enhancing "MarketFlow"*

#### Day 64: Caching Strategies with Redis: Cache-Aside & Invalidation
- **Learning Objectives**: Improve read performance using Redis in-memory caching and manage cache invalidation.
- **Essential Concepts**: In-memory caching, the Cache-Aside pattern (check cache, on miss read DB and set cache), Time-to-Live (TTL), Cache Hit vs Miss, and cache invalidation when data updates.
- **Practical Coding Exercise**: Configure Redis as the Django cache backend; cache the product list endpoint response with a 10-minute TTL and measure the reduction in database queries.
- **Independent Challenge**: Implement cache invalidation: when a product is created or updated by staff, invalidate or refresh the cached product catalog so users see current data.
- **Definition of Done**: Demonstrate that a cached view returns data on repeated requests without executing SQL queries against PostgreSQL.
- **How It Relates to Real Backend Work**: Caching high-traffic, read-heavy endpoints protects your database from excessive load during traffic surges.
- **Optional Extension**: Use Redis to store a simple session counter or view count.

#### Day 65: Asynchronous Task Processing: Celery & Redis Setup
- **Learning Objectives**: Offload time-consuming tasks to background worker processes using Celery and Redis.
- **Essential Concepts**: Why long-running operations (sending emails, generating reports, external API calls) must not block HTTP responses, Celery architecture (Producer, Broker, Worker), and the `@shared_task` decorator.
- **Practical Coding Exercise**: Install and configure Celery with Redis in "MarketFlow"; create an asynchronous task `send_order_notification(order_id)` that executes in the background.
- **Independent Challenge**: Trigger the background task from your order checkout service, verify the HTTP response returns immediately without waiting for the task to finish, and observe the Celery worker log.
- **Definition of Done**: Start a Celery worker from the terminal, dispatch a task from Django, and verify the worker receives and completes the task.
- **How It Relates to Real Backend Work**: Keeping HTTP response times fast and responsive is essential for a good user experience; slow tasks belong in background queues.
- **Optional Extension**: Inspect task status and return values using Celery's result backend.

#### Day 66: Background Task Retries, Error Handling & Scheduled Jobs
- **Learning Objectives**: Build fault-tolerant background tasks that handle transient failures and schedule recurring tasks.
- **Essential Concepts**: Handling network failures in tasks, automatic retries with exponential backoff (`bind=True, retry_backoff=True`), task error logging, and scheduling recurring jobs using Celery Beat.
- **Practical Coding Exercise**: Write a background task that simulates contacting an external shipping API, retries safely on temporary network failures, and logs permanent errors.
- **Independent Challenge**: Configure Celery Beat to run a scheduled task once a day (e.g. generating a summary of daily sales or cleaning expired carts).
- **Definition of Done**: Demonstrate a task retrying on simulated failure before succeeding or recording a final error log.
- **How It Relates to Real Backend Work**: External services fail intermittently; background tasks must be designed to retry gracefully without manual intervention.
- **Optional Extension**: Learn about dead-letter queues and how failed tasks are archived for inspection.

#### Day 67: Real-Time WebSockets & Django Channels Overview
- **Learning Objectives**: Understand when to use WebSockets instead of HTTP and explore real-time message delivery.
- **Essential Concepts**: HTTP polling vs persistent WebSocket connections, ASGI servers (`daphne`), Consumers vs Views, and Channel Layers with Redis.
- **Practical Coding Exercise**: Set up a basic Django Channels consumer that accepts a WebSocket connection and echoes received messages back to the client.
- **Independent Challenge**: Build a real-time notification consumer that notifies connected users when their order status updates (e.g. "Processing" to "Shipped").
- **Definition of Done**: Connect to a WebSocket endpoint from a browser console or WebSocket client and exchange messages in real time.
- **How It Relates to Real Backend Work**: Real-time dashboards, live chat, and instant notifications rely on WebSockets for efficient bidirectional communication.
- **Optional Extension**: Authenticate a WebSocket connection using a query parameter token.

#### Day 68: Webhooks, Third-Party API Integration & Idempotency
- **Learning Objectives**: Integrate external APIs safely, receive webhooks, and ensure duplicate requests are handled idempotently.
- **Essential Concepts**: Webhooks (reverse APIs / incoming event callbacks), verifying cryptographic webhook signatures, handling duplicate events, and using Idempotency Keys in payment processing.
- **Practical Coding Exercise**: Build a mock webhook endpoint that receives payment confirmation events, validates a shared secret or signature, and updates order status.
- **Independent Challenge**: Implement an idempotency check: if the same payment webhook event ID is received twice, return a `200 OK` without processing the payment a second time.
- **Definition of Done**: Explain why webhook signature verification is critical for security; demonstrate that duplicate events do not create duplicate records.
- **How It Relates to Real Backend Work**: Real backends integrate with payment gateways (Stripe, PayPal, Khalti) and external SaaS tools via webhooks.
- **Optional Extension**: Save incoming webhook payloads in an audit log table for troubleshooting.

---

### 🐳 Phase 9: DevOps, Docker, CI/CD & Production Deployment (Days 69–72)
*Stage 3 Continues: Containerizing & Deploying "MarketFlow"*

#### Day 69: Linux Basics, Environment Variables & Production Security
- **Learning Objectives**: Work comfortably in Linux server environments and secure production application settings.
- **Essential Concepts**: Common Linux commands (`ls`, `cd`, `grep`, `ps`, `systemctl`, `journalctl`), environment variable management, production security checklist (`DEBUG = False`, `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`, `SECURE_SSL_REDIRECT`), and running with a WSGI server (Gunicorn).
- **Practical Coding Exercise**: Run `python manage.py check --deploy` on your Django project, identify security warnings, and resolve them in your production settings file.
- **Independent Challenge**: Write a shell script that automates running database migrations, collecting static files, and starting Gunicorn with sensible worker settings.
- **Definition of Done**: Pass `check --deploy` with zero critical warnings; run your application using Gunicorn locally.
- **How It Relates to Real Backend Work**: Production web backends run on Linux servers; knowing basic shell commands and security settings is essential for deployment.
- **Optional Extension**: Explore how Nginx acts as a reverse proxy in front of Gunicorn.

#### Day 70: Docker Fundamentals: Writing Clean Dockerfiles
- **Learning Objectives**: Containerize a Python application for consistent execution across development and production.
- **Essential Concepts**: Virtual machines vs containers, Docker images and layers, writing clean `Dockerfile`s using Python slim base images, `.dockerignore`, and avoiding running containers as root.
- **Practical Coding Exercise**: Write a `Dockerfile` for "MarketFlow", build the Docker image, and run the container locally with environment variables passed in.
- **Independent Challenge**: Optimize your `Dockerfile` using layer caching (copying and installing `requirements.txt` before copying application code) to speed up rebuilds.
- **Definition of Done**: Build a Docker image from terminal and successfully start your application inside a container.
- **How It Relates to Real Backend Work**: Containers ensure that applications run with identical dependencies and settings across every developer's laptop and cloud server.
- **Optional Extension**: Inspect running container logs and resource usage with `docker logs` and `docker stats`.

#### Day 71: Multi-Container Orchestration with `docker-compose`
- **Learning Objectives**: Orchestrate multi-service application stacks with Docker Compose.
- **Essential Concepts**: `docker-compose.yml`, service definitions, container networking, persistent volumes for PostgreSQL, and environment variable passing.
- **Practical Coding Exercise**: Write a `docker-compose.yml` file that starts three services: `web` (Django Gunicorn), `db` (PostgreSQL with persistent volume), and `redis`.
- **Independent Challenge**: Add a `celery_worker` service to your Docker Compose setup that runs background tasks alongside the web and database containers.
- **Definition of Done**: Run `docker compose up --build` and verify that the web app, database, Redis, and Celery worker start and communicate successfully.
- **How It Relates to Real Backend Work**: Docker Compose allows new developers and automated testing environments to launch complete multi-service backends with a single command.
- **Optional Extension**: Add a volume mount for local code so edits reflect immediately in development without rebuilding.

#### Day 72: CI/CD Pipelines with GitHub Actions & Cloud Deployment
- **Learning Objectives**: Automate testing and deployment using GitHub Actions CI/CD workflows.
- **Essential Concepts**: Continuous Integration (running linters and tests on every pull request), GitHub Actions workflows (`.github/workflows/`), running test databases in CI, and deploying to cloud hosting (Render, Railway, or VPS).
- **Practical Coding Exercise**: Create a GitHub Actions workflow that runs on push to `main` and PRs: checks out code, sets up Python, installs dependencies, and runs `pytest`.
- **Independent Challenge**: Configure cloud deployment: connect your repository to a cloud platform (e.g. Render / Railway) so that pushes to `main` automatically deploy your container or code.
- **Definition of Done**: Complete Milestone 5: Have a live deployed application link and a green passing CI build badge in your GitHub README.
- **How It Relates to Real Backend Work**: CI/CD pipelines automate testing and deployment, catching bugs before they reach production servers.
- **Optional Extension**: Add a linting step (`flake8` or `ruff`) to your CI pipeline before tests run.

---

### 🏆 Phase 10: Junior System Design, Interview Preparation & Capstone Defense (Days 73–75)
*Stage 3 Concludes: Packaging Your Portfolio & Interview Readiness*

#### Day 73: Junior Backend System Design Fundamentals
- **Learning Objectives**: Reason about system architecture, explain trade-offs, and answer junior-level system design interview questions.
- **Essential Concepts**: Horizontal vs Vertical scaling, the role of load balancers, caching strategies, database read replicas vs primary write database, and basic capacity estimation.
- **Practical Coding Exercise**: Design the architecture for a URL Shortener service (TinyURL) on a whiteboard or diagram: draw client, web tier, caching layer, database, and explain ID generation.
- **Independent Challenge**: Practice explaining your "MarketFlow" system architecture: draw how requests flow from client through Gunicorn, Django, PostgreSQL, Redis, and Celery workers.
- **Definition of Done**: Clearly explain the trade-offs between adding a cache vs adding database indexes when addressing a slow read endpoint.
- **How It Relates to Real Backend Work**: Junior interviews often include a conversational system design question to assess whether you understand how components connect beyond basic framework code.
- **Optional Extension**: Sketch a basic rate-limiting architecture using Redis counters.

#### Day 74: Junior Technical Interview Preparation: Python, SQL & Frameworks
- **Learning Objectives**: Prepare for live technical interview questions across Python, SQL, and Django/DRF.
- **Essential Concepts**: Explaining technical decisions clearly, live problem-solving on a whiteboard or shared editor, common junior Python questions (OOP, mutability, decorators, generators), and core SQL questions (joins, aggregation, indexes).
- **Practical Coding Exercise**: Solve three standard technical interview challenges in timed sessions:
  1. Write a clean Python function to find duplicate items or word frequencies using a dictionary.
  2. Write an SQL query using a `LEFT JOIN` and `GROUP BY` to find customers with zero orders.
  3. Write a Django view that performs an atomic transaction with error handling.
- **Independent Challenge**: Practice answering five common conceptual interview questions out loud:
  - "What happens when you enter a URL in a browser?"
  - "What is the N+1 problem and how do you resolve it in Django?"
  - "What is the difference between an inner join and a left join?"
  - "Why do we use JWTs and what is the purpose of a refresh token?"
  - "When would you use Celery instead of running code directly in a view?"
- **Definition of Done**: Explain each of the five questions out loud clearly, accurately, and concisely without hesitation.
- **How It Relates to Real Backend Work**: Interviewers look for clear communication, solid fundamentals, and a practical understanding of how web applications work.
- **Optional Extension**: Conduct a mock interview with a peer or record yourself answering technical questions.

#### Day 75: Portfolio Packaging, Capstone Project Defense & Career Readiness
- **Learning Objectives**: Present your projects effectively on GitHub, write a professional README, and finalize your portfolio.
- **Essential Concepts**: Writing effective repository READMEs (project overview, architecture diagram, tech stack rationale, setup instructions, API documentation, and test instructions), tailoring your CV for junior backend roles, and preparing project demonstrations.
- **Practical Coding Exercise**: Finalize the `README.md` for your "MarketFlow" project with clear setup steps, an architecture diagram, test commands, and live API documentation links.
- **Independent Challenge**: Prepare a 5-minute project walkthrough explaining your project's features, an interesting technical challenge you solved (e.g. optimizing queries, handling race conditions, or testing), and what you would improve next.
- **Definition of Done**: Complete Milestone 6: A polished, public GitHub portfolio with clear documentation, passing automated tests, and a live project ready to showcase to hiring managers.
- **How It Relates to Real Backend Work**: Hiring managers look for clean code, solid documentation, and proof that a candidate can build and test real applications.
- **Optional Extension**: Publish a short technical post or LinkedIn article explaining a backend problem you solved during your 75-day journey.
