/*
============================================================
DAY 27 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: Multi-Tenant SaaS Subscription Schema Design (DDL & Constraints)

In backend system design interviews, interviewers frequently ask you
to sketch the relational database schema on a whiteboard for a real
business model, complete with primary keys, foreign keys, and constraints.

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Design a PostgreSQL/MySQL DDL relational database schema for a
multi-tenant B2B SaaS platform consisting of 3 core tables:
1. `organizations` (Company accounts)
2. `users` (Team members belonging to an organization)
3. `subscriptions` (Active billing plans for organizations)

------------------------------------------------------------
2. REQUIREMENTS & CONSTRAINTS:
------------------------------------------------------------
1. Table `organizations`:
   - `id`: Auto-incrementing primary key.
   - `name`: Max 150 chars, unique, not null.
   - `created_at`: Timestamp with timezone, defaults to current time.

2. Table `users`:
   - `id`: Auto-incrementing primary key.
   - `org_id`: Foreign key referencing `organizations(id)` ON DELETE CASCADE.
   - `email`: Max 255 chars, unique, not null.
   - `full_name`: Max 100 chars, not null.
   - `role`: VARCHAR(20) constrained to ('OWNER', 'ADMIN', 'MEMBER').
   - `is_active`: Boolean default true.

3. Table `subscriptions`:
   - `id`: Auto-incrementing primary key.
   - `org_id`: Foreign key referencing `organizations(id)` ON DELETE CASCADE.
   - `plan_type`: Constrained to ('STARTER', 'GROWTH', 'ENTERPRISE').
   - `monthly_price`: Numeric(10, 2) >= 0.00.
   - `status`: Constrained to ('ACTIVE', 'PAST_DUE', 'CANCELLED') default 'ACTIVE'.
   - `renews_at`: Timestamp with timezone not null.

============================================================
MY ER DIAGRAM & RELATIONSHIPS (1:N, N:N):
============================================================
Describe the relationships between the entities:

____________________________________________________
____________________________________________________
____________________________________________________

============================================================
MY RAW DDL STATEMENTS (Write on blank paper first!):
============================================================

-- TODO: Write complete CREATE TABLE statements below:

*/