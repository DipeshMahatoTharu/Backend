# Day 41 — Real-World Backend Engineering Interview

These questions evaluate your ability to diagnose database bottlenecks and architect relational databases.

---

### Question 1: How Do You Detect and Permanently Eliminate N+1 Queries in Django?
**Interview Scenario:**
> *"An API endpoint `/api/v1/posts` takes 4.5 seconds to return 100 items. When inspecting the SQL query log with Django Debug Toolbar, you see 201 individual queries executed for a single HTTP request. How did this happen and how do you fix it?"*

#### Senior Mentor Answer & Key Points:
1. **Diagnosis**:
   - The view executes `posts = Post.objects.all()`.
   - In the serializer/template, for each post, the code accesses `post.author.username` and `post.comments.count()`.
   - Each attribute access on un-joined relationships executes a separate `SELECT` query ($1 + 100 + 100 = 201$ queries).
2. **Permanent Fix**:
   - For single-valued foreign keys (`author`): add `.select_related('author')`.
   - For multi-valued reverse relationships (`comments`): add `.prefetch_related('comments')` or use `.annotate(comment_count=Count('comments'))`.
   - Result: Drops from 201 queries to **1 single query**, reducing latency from 4,500ms to 12ms.
3. **Automated Prevention**:
   - Install `django-zen-queries` or write unit tests with `assertNumQueries(2)` to fail CI/CD builds if a developer introduces an N+1 query.

---

### Question 2: Why `select_related` on Many-to-Many Relationships Causes Cartesian Explosions
**Interview Scenario:**
> *"Why doesn't Django allow `select_related()` on `ManyToManyField`? What would happen at the database level if it did?"*

#### Senior Mentor Answer & Key Points:
1. **The Cartesian Product Hazard**:
   - If a `Book` has 5 `Authors` and 10 `Tags`, an SQL `JOIN` across both Many-to-Many junction tables produces $5 	imes 10 = 50$ duplicate rows for a single book!
   - If you query 100 books, the database returns thousands of redundant rows, saturating network bandwidth and database memory.
2. **The `prefetch_related` Architecture**:
   - Instead of a massive Cartesian join, Django runs 3 lean queries:
     1. `SELECT * FROM books;` (100 rows)
     2. `SELECT * FROM authors WHERE book_id IN (...);` (200 rows)
     3. `SELECT * FROM tags WHERE book_id IN (...);` (350 rows)
   - Total rows transferred: 650 rows instead of tens of thousands!
