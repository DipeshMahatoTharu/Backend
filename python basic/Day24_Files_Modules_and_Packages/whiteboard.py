"""
============================================================
DAY 24 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: Memory-Efficient Streaming Log Parser (Generators + File I/O)

In a live interview, backend candidates are often asked how they would
process massive files (e.g., a 10 GB server log) without exhausting
RAM and crashing the server with an Out-Of-Memory (OOM) error.

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Design a generator function `stream_error_events(file_path)` that reads
a server log file line-by-line. For every line containing the keyword
'ERROR', yield a structured dictionary:
`{"timestamp": str, "level": "ERROR", "message": str}`.

------------------------------------------------------------
2. REQUIREMENTS & CONSTRAINTS:
------------------------------------------------------------
- Memory constraint: O(1) auxiliary memory. You CANNOT use `f.read()` or
  `f.readlines()` because loading a 10 GB file into RAM will crash the system.
- Use Python's iterator protocol / file stream iterating (`for line in f:`).
- Defensive programming: If the file does not exist, handle `FileNotFoundError`
  gracefully without crashing (e.g., return or log message).
- String parsing: Extract timestamp from square brackets `[YYYY-MM-DD HH:MM:SS]`
  and message following `ERROR: <msg>`.

------------------------------------------------------------
3. EXAMPLE INPUT & OUTPUT:
------------------------------------------------------------
Log file line:
  "[2026-09-06 10:15:30] ERROR: Database connection pool exhausted"

Yielded dictionary:
  {
      "timestamp": "2026-09-06 10:15:30",
      "level": "ERROR",
      "message": "Database connection pool exhausted"
  }

------------------------------------------------------------
4. TEST CASES TO CONSIDER:
------------------------------------------------------------
1. Normal file with mix of [INFO], [WARN], and [ERROR] lines.
2. File with no errors (should yield nothing).
3. File that does not exist (should not raise uncaught exception).
4. Malformed error line missing timestamp brackets.

============================================================
MY APPROACH (Explain O(1) memory & time complexity):
============================================================
Write your plan and algorithmic explanation here:

____________________________________________________
____________________________________________________
____________________________________________________

============================================================
MY RAW CODE (No autocomplete help! Write on blank paper first):
============================================================

def stream_error_events(file_path):
    # TODO: Write your raw generator implementation here
    pass

"""