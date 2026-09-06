# Day 25 — Type Hints, Dataclasses & Clean Python (PEP 8)

## 🎯 Learning Objectives
- Master Python's modern typing system (`typing` module, Union, Optional, Literal, Generic collections).
- Understand why production backends (Dropbox, Instagram, Meta) enforce static type checking with `mypy`.
- Build clean, boilerplate-free data models using `@dataclass` and `dataclasses.field`.
- Learn the difference between standard classes, `@dataclass`, Pydantic models, and Django ORM models.
- Master PEP 8 formatting standards and linting rules for professional production code.

---

## 📚 Core Backend Concepts

### 1. Modern Type Hints (Python 3.10+)
Python is dynamically typed at runtime, but modern enterprise backends use static type annotations to catch bugs before code reaches production:

```python
from typing import Optional, Literal

def fetch_user_order(
    user_id: int, 
    status: Literal["PENDING", "COMPLETED", "CANCELLED"] = "PENDING"
) -> Optional[dict[str, str | int]]:
    # Clear contract: accepts int, specific string literal, returns dict or None
    return {"id": 1, "status": status}
```

### 2. Python Dataclasses (`@dataclass`)
Writing manual `__init__`, `__repr__`, and `__eq__` methods for simple data-carrying structures adds tedious boilerplate. Python's `@dataclass` generates these automatically:

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True) # frozen=True makes instances immutable and hashable
class DatabaseConfig:
    host: str
    port: int = 5432
    database: str = "postgres"

@dataclass
class OrderItem:
    product_id: int
    quantity: int
    price: float
    tags: list[str] = field(default_factory=list) # Safe mutable default!
    
    @property
    def total(self) -> float:
        return self.quantity * self.price
```

### 3. Static Analysis & PEP 8 Standards
- **Function/Variable names**: `snake_case` (e.g. `get_user_by_id`)
- **Class names**: `PascalCase` (e.g. `AccessLogAnalyzer`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g. `MAX_RETRY_ATTEMPTS = 3`)
- **Indentation**: Exactly 4 spaces (never tabs).
- **Type Checkers**: Tools like `mypy` and `pyright` scan code during CI/CD pipelines to ensure type contracts are strictly respected.

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + CONCEPT DRILLS (60 min)**:
  - 40 min: Review typing system, Union syntax (`A | B`), `Optional`, and `@dataclass`.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day25/questions.md)**.

- **HOUR 2 — CODING PRACTICE & DEBUGGING (60 min)**:
  - 35 min: Implement the 4 typed tasks in **[`practice.py`](file:///d:/Backend/python%20basic/Day25/practice.py)**.
  - 25 min: Diagnose and fix mutable default & typing bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day25/debugging.py)**.

- **HOUR 3 — INTERVIEW & PORTFOLIO CHALLENGE (60 min)**:
  - 20 min: Study dataclasses vs Pydantic vs Django models in **[`interview.md`](file:///d:/Backend/python%20basic/Day25/interview.md)**.
  - 20 min: Solve the typed filter whiteboard problem in **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day25/whiteboard.py)**.
  - 20 min: Build the E-Commerce Typed Order Engine in **[`challenge.py`](file:///d:/Backend/python%20basic/Day25/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Read concepts and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day25/questions.md)**
- [ ] Completed all 4 tasks in **[`practice.py`](file:///d:/Backend/python%20basic/Day25/practice.py)**
- [ ] Fixed all 3 bug scenarios in **[`debugging.py`](file:///d:/Backend/python%20basic/Day25/debugging.py)**
- [ ] Solved blank-page coding in **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day25/whiteboard.py)**
- [ ] Built and verified order engine in **[`challenge.py`](file:///d:/Backend/python%20basic/Day25/challenge.py)**
- [ ] Studied backend interview answers in **[`interview.md`](file:///d:/Backend/python%20basic/Day25/interview.md)**