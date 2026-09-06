# Day 24 — Files, Modules & Packages in Backend Engineering

## 🎯 Learning Objectives
- Master modern, cross-platform file system operations using Python's `pathlib.Path`.
- Understand safe resource management and context managers (`with open(...) as f:`).
- Read, write, and validate structured backend data payloads in **JSON** and **CSV** formats.
- Understand Python's import system, modular architectures, packages (`__init__.py`), and script entry points (`__name__ == '__main__'`).
- Build production-ready logging, configuration management, and data export pipelines.

---

## 📚 Core Backend Concepts

### 1. Modern File Handling with `pathlib`
In backend engineering, hardcoding file paths like `C:\app\logs\app.log` or `/var/log/app.log` causes catastrophic cross-platform deployment bugs when moving from Windows development to Linux Docker containers.
Python 3.4+ introduced `pathlib.Path`, which provides an object-oriented, platform-agnostic API:

```python
from pathlib import Path

# Always resolve paths relative to the current file's directory:
BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "config" / "settings.json"

# Check existence and create directories safely:
CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
```

### 2. Resource Management & Context Managers
Every open file consumes an OS file descriptor. If an exception occurs before `.close()` is called, file descriptors leak. In production environments handling thousands of requests, this leads to `OSError: [Errno 24] Too many open files`.
Context managers guarantee cleanup even if exceptions are raised:

```python
# Guaranteed closure via __enter__ and __exit__:
with open(CONFIG_FILE, mode="r", encoding="utf-8") as file:
    content = file.read()
```

### 3. Structured Data: JSON & CSV
Backend services constantly exchange JSON (REST APIs) and CSV (data exports/imports):
- `json.load(file)`: Deserializes JSON directly from an open file stream.
- `json.loads(string)`: Deserializes JSON from an in-memory string.
- `json.dump(data, file, indent=4)`: Serializes Python dict/list directly into a file.
- `json.dumps(data)`: Serializes Python dict/list into a JSON string.
- `csv.DictReader(file)` & `csv.DictWriter(file, fieldnames=...)`: Map rows directly to Python dictionaries.

### 4. Modules, Packages & Entry Guards
- **Module**: A single `.py` file containing functions, classes, and variables.
- **Package**: A directory containing an `__init__.py` file (which indicates Python should treat the directory as an importable package).
- **`__name__ == '__main__'`**: Prevents executable test or setup code from running when a file is imported as a module by another service.

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + CONCEPT DRILLS (60 min)**:
  - 40 min: Study `pathlib`, context managers, JSON/CSV streaming, and modular imports above.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day24/questions.md)**.

- **HOUR 2 — CODING PRACTICE & DEBUGGING (60 min)**:
  - 35 min: Implement the 4 core tasks in **[`practice.py`](file:///d:/Backend/python%20basic/Day24/practice.py)**.
  - 25 min: Diagnose and resolve production file bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day24/debugging.py)**.

- **HOUR 3 — INTERVIEW & PORTFOLIO CHALLENGE (60 min)**:
  - 20 min: Review senior backend scenarios in **[`interview.md`](file:///d:/Backend/python%20basic/Day24/interview.md)**.
  - 20 min: Solve the blank-page streaming log parser in **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day24/whiteboard.py)**.
  - 20 min: Build the Server Access Log Analyzer in **[`challenge.py`](file:///d:/Backend/python%20basic/Day24/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Read concepts and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day24/questions.md)**
- [ ] Completed all 4 tasks in **[`practice.py`](file:///d:/Backend/python%20basic/Day24/practice.py)**
- [ ] Fixed all 3 bug scenarios in **[`debugging.py`](file:///d:/Backend/python%20basic/Day24/debugging.py)**
- [ ] Solved blank-page coding in **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day24/whiteboard.py)**
- [ ] Built and verified the log analyzer in **[`challenge.py`](file:///d:/Backend/python%20basic/Day24/challenge.py)**
- [ ] Studied backend interview answers in **[`interview.md`](file:///d:/Backend/python%20basic/Day24/interview.md)**

---

## 📊 Daily Scorecard
- **Topic Understanding**: __ / 10
- **Problem Solving Ability**: __ / 10
- **Interview Confidence**: __ / 10

**What I struggled with**:
____________________________________________________

**What I learned**:
____________________________________________________