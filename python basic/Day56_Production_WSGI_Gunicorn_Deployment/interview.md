# Day 56 — Real-World Backend Engineering Interview

These questions test your mastery of production web server architectures, WSGI concurrency models, and proxy buffering.

---

### Question 1: How Does Nginx Request Buffering Prevent Slowloris Denial-of-Service Attacks?
**Interview Scenario:**
> *"If you deploy Gunicorn directly to the internet with 9 sync workers, an attacker can crash your server using a single laptop sending 9 bytes per second. How does Nginx prevent this?"*

#### Senior Mentor Answer & Key Points:
1. **The Sync Worker Vulnerability (Slowloris)**:
   - A synchronous Gunicorn worker handles exactly one HTTP request at a time.
   - If a client uploads a 1MB payload at 100 bytes/sec, the Gunicorn worker is occupied waiting for socket reads for over 2 hours!
   - 9 slow connections completely exhaust a 9-worker pool, causing all other incoming requests to time out.
2. **Nginx's Asynchronous Event Loop Defense (`proxy_request_buffering on`)**:
   - Nginx uses an asynchronous, non-blocking event-driven architecture (`epoll`/`kqueue`).
   - A single Nginx process can hold 50,000 slow client connections in memory simultaneously with negligible CPU usage.
   - Nginx buffers the client's slow upload completely in disk/RAM.
   - Only once the final byte arrives does Nginx open a connection to Gunicorn, dumping the payload over a fast local UNIX domain socket in 1 millisecond.
   - Gunicorn finishes in 20ms and is instantly free for the next request.

---

### Question 2: UNIX Domain Sockets vs TCP Loopback (`127.0.0.1:8000`)
**Interview Scenario:**
> *"When Nginx and Gunicorn run on the same physical server or container, should you configure `proxy_pass http://127.0.0.1:8000` or `proxy_pass http://unix:/run/gunicorn.sock`?"*

#### Senior Mentor Answer & Key Points:
1. **The TCP Loopback Overhead**:
   - `127.0.0.1` goes through the entire operating system TCP/IP network stack (TCP checksums, packet headers, port allocation, TCP handshake).
   - Under high traffic, loopback TCP can exhaust ephemeral ports (`TIME_WAIT` saturation).
2. **UNIX Domain Socket Performance**:
   - UNIX domain sockets operate entirely within the Linux kernel memory as a file descriptor pipe.
   - Zero TCP overhead, no routing, no checksums, and no ephemeral port limits.
   - UNIX domain sockets typically deliver **15–20% higher throughput** and lower latency.
