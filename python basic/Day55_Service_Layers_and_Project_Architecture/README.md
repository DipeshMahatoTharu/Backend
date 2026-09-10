# Day 55 — Service Layers, Repository Pattern & Project Architecture

## 🎯 Learning Objectives
- Master the **Service Layer Pattern**: Decoupling HTTP transport handlers (Views/Serializers) from core business logic.
- Master the **Repository Pattern**: Abstracting database queries away from business services.
- Use **Data Transfer Objects (DTOs)** / Python Dataclasses to pass strongly typed data across application boundaries.
- Manage atomic database transactions using `django.db.transaction.atomic`.
- Understand `transaction.on_commit()`: Why async tasks (Celery) and emails must NEVER be triggered inside an active uncommitted transaction.

---

## 📚 Core Backend Concepts

### 1. The 3-Tier Layered Architecture
```text
[ HTTP Transport Layer ] -> Views, Serializers, HTTP Status Codes, Cookie handling
         │ (Passes DTO)
         ▼
[ Service Layer ]        -> Pure Business Logic, Atomic Transactions, Third-Party Coordination
         │ (Queries Repository)
         ▼
[ Data Access Layer ]    -> Repositories, Django ORM, PostgreSQL Database
```

### 2. The `transaction.on_commit` Rule
```python
from django.db import transaction

def register_user_service(user_dto: UserCreateDTO):
    with transaction.atomic():
        user = User.objects.create(username=user_dto.username, email=user_dto.email)
        Profile.objects.create(user=user)

        # WRONG: If transaction rolls back after this line, email was already sent!
        # send_welcome_email.delay(user.id)

        # RIGHT: Executes ONLY after the database transaction successfully commits!
        transaction.on_commit(lambda: send_welcome_email.delay(user.id))
```

### 3. Data Transfer Objects (DTOs)
```python
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class TransferFundsDTO:
    from_account_id: int
    to_account_id: int
    amount: Decimal
    reference: str
```
DTOs guarantee type safety and prevent leaking raw ORM model instances across architecture layers.

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review 3-tier architecture, DTOs, `on_commit`, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build DTOs and transaction hooks in [`practice.py`](practice.py), and fix transaction traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Banking Transfer Service Layer in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
