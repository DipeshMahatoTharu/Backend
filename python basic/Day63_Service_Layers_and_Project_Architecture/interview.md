# Day 55 — Real-World Backend Engineering Interview

These questions test your understanding of domain-driven design, service layers, and distributed transactions.

---

### Question 1: Why Does Celery Need `transaction.on_commit()`?
**Interview Scenario:**
> *"A user registers on your site. The view creates the user in `transaction.atomic()` and dispatches `send_welcome_email.delay(user.id)`. In production, Sentry reports intermittent `User.DoesNotExist: User matching query does not exist` inside the Celery worker! Why?"*

#### Senior Mentor Answer & Key Points:
1. **The Concurrency Race Condition**:
   - Celery uses Redis or RabbitMQ as a high-speed message broker.
   - When you call `.delay()`, the task message is pushed to Redis **instantly** (microseconds).
   - The Celery worker on another server picks up the task immediately and runs `User.objects.get(id=user_id)`.
   - Meanwhile, the Django web server is still waiting for PostgreSQL to complete its SSL handshake, write ahead log (WAL), and commit the transaction!
   - Because the transaction is not committed yet, PostgreSQL's MVCC isolation hides the new row from the Celery worker, causing `DoesNotExist`!
2. **The Permanent Fix**:
   - Always wrap async task dispatching in `transaction.on_commit()`:
     ```python
     transaction.on_commit(lambda: send_welcome_email.delay(user.id))
     ```
   - Django guarantees the task message is only pushed to Redis **after** PostgreSQL confirms the transaction commit.

---

### Question 2: When Should You NOT Use the Repository Pattern in Django?
**Interview Scenario:**
> *"Many software architecture books mandate the Repository Pattern for all databases. Why do many senior Django engineers avoid the Repository Pattern for standard applications?"*

#### Senior Mentor Answer & Key Points:
1. **Django's Built-in Active Record & QuerySet API**:
   - In frameworks without rich ORMs, a repository is essential to hide raw SQL queries.
   - However, Django's `QuerySet` is already an implementation of the Repository and Query Object patterns.
   - QuerySets support lazy evaluation, chaining (`.filter().exclude().order_by()`), prefetching, and slicing.
2. **The "Leaky Abstraction" Hazard**:
   - Creating an artificial `UserRepository` with methods like `get_by_id()`, `find_active()`, `find_by_email()` strips away QuerySet composability and leads to hundreds of duplicate query methods.
3. **The Pragmatic Senior Rule**:
   - Use custom `models.QuerySet` / `models.Manager` subclasses to encapsulate complex queries (e.g. `Order.objects.active_for_user(user)`).
   - Reserve strict Repository interfaces only when swapping database engines (e.g. PostgreSQL to DynamoDB) or decoupling microservices.
