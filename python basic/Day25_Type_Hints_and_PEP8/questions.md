# Day 25 — Type Hints & PEP 8 Static Analysis Questions

Write your answers in the designated spaces below each question.

---

### 25.1 Runtime vs Static Type Checking
**QUESTION:**
Does standard Python enforce type hints at runtime? For example, if a function is defined as `def add(a: int, b: int) -> int: return a + b`, what happens if you call `add("hello", "world")`? How do backend engineering teams use static analysis tools like `mypy` in CI/CD pipelines to prevent type bugs from reaching production?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 25.2 Python `@dataclass` vs Standard Classes
**QUESTION:**
What boilerplate code does the `@dataclass` decorator automatically synthesize for you? What is the purpose of setting `frozen=True`, and in what backend scenarios (e.g. caching keys, configuration objects) is an immutable dataclass desirable?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 25.3 The Mutable Default Trap in Dataclasses
**QUESTION:**
Why does Python raise a `ValueError: mutable default <class 'list'> for field is not allowed` if you write:
```python
@dataclass
class User:
    roles: list[str] = []
```
Explain what `dataclasses.field(default_factory=list)` does and why it prevents memory sharing between different instances.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 25.4 `Optional`, `Union`, and `Literal`
**QUESTION:**
Explain the meaning and use-case of each typing construct in a backend API service:
1. `Optional[int]` (or `int | None`)
2. `Union[int, str]` (or `int | str`)
3. `Literal["GET", "POST", "DELETE"]`

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 25.5 PEP 8 Naming Conventions & Code Style
**QUESTION:**
List the PEP 8 casing conventions for:
1. Module names
2. Class names
3. Function and variable names
4. Global constants
Why is adhering to PEP 8 critical when collaborating on a team of backend developers?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________