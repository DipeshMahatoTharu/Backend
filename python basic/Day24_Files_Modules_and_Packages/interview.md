# Day 24 — Real-World Backend Engineering Interview

These questions simulate real technical screenings for Junior-to-Mid Backend Engineer positions.

---

### Question 1: The "Too Many Open Files" Production Outage
**Interview Scenario:**
> *"During a flash-sale event, your backend service suddenly starts returning HTTP 500 errors. When inspecting application logs, you see `OSError: [Errno 24] Too many open files`. What caused this incident, how does the Linux operating system track open files, and how would you resolve and prevent it?"*

#### Senior Mentor Answer & Key Points:
1. **Root Cause**: In Unix/Linux, everything is a file—including regular files on disk, network sockets, database connections, and pipes. Each process has a maximum file descriptor limit (`ulimit -n`, typically 1024 by default). If code opens file handles or network sockets without properly closing them (e.g., missing context managers or unclosed DB connection pools), the process exhausts its file descriptor table.
2. **Immediate Resolution**:
   - Inspect active file descriptors for the running process using `lsof -p <PID>` or `ls -l /proc/<PID>/fd`.
   - Temporarily increase the soft/hard limits (`ulimit -n 65535` or adjust `/etc/security/limits.conf`).
   - Restart the worker process to release leaked file descriptors.
3. **Permanent Code-Level Fix**:
   - Enforce Python context managers (`with open(...)`) across all file I/O.
   - Ensure all third-party HTTP clients (`requests.Session`, `httpx.Client`) or socket connections are closed or pooled.
   - Add linter checks (like `flake8` or SonarQube) and automated tests that verify file descriptor counts don't grow monotonically over time.

---

### Question 2: Ingesting a 5GB CSV File via REST API
**Interview Scenario:**
> *"A client wants to upload a 5 GB CSV file containing 10 million rows to sync their inventory. If a junior developer implements this as a synchronous Django view reading `request.FILES['file'].read()`, what will happen? How would you architect this properly?"*

#### Senior Mentor Answer & Key Points:
1. **The Failure Modes of Synchronous Ingestion**:
   - **Out-Of-Memory (OOM) Crash**: Calling `.read()` attempts to allocate 5 GB of RAM for the file string. In containerized environments with 512MB-2GB memory limits, the Linux kernel OOM killer will instantly terminate the container.
   - **HTTP Gateway Timeout**: Ingesting and saving 10 million rows into the DB takes minutes or hours. HTTP reverse proxies (Nginx, Cloudflare) timeout after 30 to 60 seconds (HTTP 504 Gateway Timeout).
   - **Worker Starvation**: The WSGI worker thread is blocked during the entire upload, preventing other users from accessing the API.
2. **The Production Architecture**:
   - **Step 1: Direct Cloud Storage Upload**: Generate a pre-signed S3 / GCS upload URL. The client uploads the 5GB file directly to S3, bypassing the application server entirely.
   - **Step 2: Asynchronous Task Trigger**: The client notifies the backend API with the file's S3 key. The backend enqueues a background job (Celery / Redis Queue) and immediately returns `HTTP 202 Accepted` with a `task_id`.
   - **Step 3: Chunked / Streaming Processing**: The Celery worker streams the file in chunks (e.g., using `csv.DictReader` over a line-by-line stream) rather than loading it all at once.
   - **Step 4: Batch Database Insertions**: Insert rows in batches of 1,000–5,000 using `bulk_create(..., batch_size=2000)` inside a database transaction to keep memory low and database write throughput high.

---

### Question 3: Circular Imports & Module Architecture
**Interview Scenario:**
> *"What are circular imports in Python? Why do they occur in backend frameworks like Django, and what techniques do you use to resolve them?"*

#### Senior Mentor Answer & Key Points:
1. **How Circular Imports Happen**:
   - When Module A imports Module B (`import B`), Python executes Module B.
   - If Module B in turn tries to import Module A (`import A`), and Module A has not finished initializing its symbols, Python encounters an incompletely initialized module and raises `ImportError: cannot import name 'X' from partially initialized module`.
2. **Common Occurrence in Django**:
   - Model `Order` in `orders/models.py` needs a ForeignKey to `UserProfile` in `users/models.py`.
   - Meanwhile, `users/models.py` imports `Order` to calculate user lifetime order totals.
3. **Architectural Solutions**:
   - **Django Lazy String References**: Instead of importing the class directly (`models.ForeignKey(UserProfile, ...)`), Django allows lazy string syntax: `models.ForeignKey('users.UserProfile', ...)`. Django resolves the model name after all apps are loaded in `django.setup()`.
   - **Inside Function / Local Imports**: Move the import inside the specific function or method where it is needed rather than at the top of the file.
   - **Domain Decoupling / Service Layers**: Move shared business logic or lookup models into a separate common module (e.g., `core/` or `services/`) that neither module depends on circularly.