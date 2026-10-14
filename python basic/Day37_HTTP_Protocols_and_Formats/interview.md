# Day 33 — Real-World Backend Engineering Interview

These questions test your understanding of web protocols, performance bottlenecks, and transport layer optimizations.

---

### Question 1: HTTP/1.1 vs HTTP/2 vs HTTP/3 (QUIC)
**Interview Scenario:**
> *"How do HTTP/1.1, HTTP/2, and HTTP/3 differ in how they manage transport connections? What is Head-of-Line (HoL) blocking, and how did HTTP/2 and HTTP/3 solve it?"*

#### Senior Mentor Answer & Key Points:
1. **HTTP/1.1 (Sequential Pipelines)**:
   - Each HTTP request on a connection must wait for the preceding response to finish.
   - Browsers worked around this by opening up to 6 parallel TCP connections per domain.
   - **Application HoL Blocking**: If request #1 is slow (e.g. database report), requests #2 through #6 on that socket are stuck behind it.
2. **HTTP/2 (Binary Multiplexing over Single TCP)**:
   - Replaces plain text with binary frames.
   - Multiplexes dozens of concurrent requests and responses over a single TCP connection.
   - **TCP HoL Blocking**: If one packet is dropped in transit, the underlying TCP stack pauses all streams until the missing packet is retransmitted.
3. **HTTP/3 (QUIC over UDP)**:
   - Moves from TCP to QUIC running over UDP.
   - Each HTTP stream is independent at the transport layer. A dropped packet on stream A does not delay streams B or C, eliminating HoL blocking completely.

---

### Question 2: Why APIs Must Never Use `text/html` for Error Payloads
**Interview Scenario:**
> *"A frontend mobile app crashes when an upstream Nginx proxy encounters a timeout. In the crash logs, you see `JSONDecodeError: Expecting value: line 1 column 1 (char 0)` because Nginx returned a default HTML error page `<html><head><title>504 Gateway Timeout</title>...</html>`. How do backend architectures prevent this?"*

#### Senior Mentor Answer & Key Points:
1. **The Problem**: Mobile apps and API clients expect predictable structured JSON formats (`application/json`). If an API gateway returns unstructured HTML, deserialization crashes mobile apps.
2. **Reverse Proxy Error Interception**:
   - Configure Nginx to return JSON formatted error payloads for upstream failures:
     ```nginx
     error_page 502 503 504 /50x.json;
     location = /50x.json {
         return 504 '{"status": 504, "error": "Gateway Timeout", "message": "Upstream service took too long"}';
         add_header Content-Type application/json;
     }
     ```
3. **Standard Error Schema**: Always adhere to RFC 7807 (Problem Details for HTTP APIs) so clients consistently parse error messages.
