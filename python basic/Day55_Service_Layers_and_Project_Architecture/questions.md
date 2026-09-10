# Day 55 — Service Layers & Project Architecture Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 55.1 Why Use a Service Layer Instead of Putting Logic in Serializers?
**QUESTION:**
Why is putting multi-model business logic (e.g. charging a card, reserving inventory, deducting wallet balance, generating an invoice) inside a DRF Serializer considered an anti-pattern?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 55.2 The Celery `on_commit` Race Condition Trap
**QUESTION:**
If you execute `send_order_notification.delay(order.id)` inside a `with transaction.atomic():` block, what race condition occurs when the background Celery worker picks up the task before PostgreSQL commits?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 55.3 Data Transfer Objects (DTOs) vs Dictionaries
**QUESTION:**
Why do enterprise backend architectures prefer typed Dataclass DTOs (`@dataclass(frozen=True)`) over plain Python dictionaries (`dict`) for passing parameters to service layer functions?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
