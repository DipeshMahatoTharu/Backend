/*
============================================================
DAY 28 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: Multi-Criteria Product Search, Filter & Pagination Query

In backend interviews, interviewers frequently ask you to write a clean,
production-ready SQL query on a whiteboard given a complex set of
business filter requirements from a frontend team.

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Given a table `products` with columns:
  (id, name, category, price, stock, is_featured, is_deleted, created_at)

Write an optimal SQL SELECT query for an API endpoint that:
1. Retrieves products where category is either 'Electronics' OR 'Accessories'.
2. Price is between $20.00 and $250.00 (inclusive).
3. Product is currently in stock (`stock > 0`).
4. Ignores soft-deleted records (`is_deleted = FALSE`).
5. Orders results such that:
   - Featured products appear first (`is_featured DESC`)
   - Then ordered by price lowest to highest (`price ASC`)
   - Ties broken alphabetically by name (`name ASC`)
6. Returns Page 4 of results assuming 15 items per page.

------------------------------------------------------------
2. CONSTRAINTS:
------------------------------------------------------------
- Must write pure SQL (no ORM abstraction).
- Must calculate the exact OFFSET mathematically for Page 4 with limit 15.

============================================================
MY CALCULATION FOR OFFSET & APPROACH:
============================================================
Page formula: OFFSET = (page - 1) * page_size
Calculation: _______________________________________________

Indexes needed for optimal query execution:
____________________________________________________________
____________________________________________________________

============================================================
MY RAW SQL QUERY (Write on blank paper first!):
============================================================

-- TODO: Write your pure SQL SELECT statement below:

*/