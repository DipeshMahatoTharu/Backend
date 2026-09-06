# Day 24 — Files, Modules & Packages Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 24.1 Modern File Paths with `pathlib.Path`
**QUESTION:**
Why is `pathlib.Path` strongly preferred over manual string concatenation (e.g. `"dir/" + filename`) or `os.path.join` in backend systems? Explain the problems that occur when paths are hardcoded with forward slashes `/` or backslashes `\` when moving code from Windows to Linux/Docker.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 24.2 Context Managers & OS File Descriptors
**QUESTION:**
1. What are context managers in Python, and which two dunder methods (`__enter__`, `__exit__`) govern their behavior?
2. What happens at the OS level if a high-throughput backend server opens files with `open()` without using `with` or `.close()`? Explain what error is triggered and why.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 24.3 JSON Serialization vs Deserialization
**QUESTION:**
Explain the exact differences between the following four Python `json` module functions, and provide a backend use case for each:
1. `json.loads()`
2. `json.load()`
3. `json.dumps()`
4. `json.dump()`

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 24.4 Packages, `__init__.py`, and `sys.path`
**QUESTION:**
1. What role does `__init__.py` play in Python package directories?
2. How does Python find imported modules using `sys.path`?
3. What is the purpose of the `__all__` list inside an `__init__.py` file?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 24.5 The `__name__ == '__main__'` Guard
**QUESTION:**
What is the `__name__` variable in Python? Why is `if __name__ == '__main__':` essential in backend services, Celery task files, or utility modules? What unexpected bugs occur if executable code is placed at the root level of an imported module?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________