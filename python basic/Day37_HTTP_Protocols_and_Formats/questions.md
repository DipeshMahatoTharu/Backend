# Day 33 — HTTP Protocols & Formats Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 33.1 Message Framing & CRLF Delimiters
**QUESTION:**
How does an HTTP/1.1 server know where the request headers end and where the request body begins? What happens at the network socket level if a client fails to send the final `\r\n\r\n` delimiter?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 33.2 Payload Encodings: JSON vs Multipart
**QUESTION:**
Why can you not easily upload a 50MB profile image inside a standard `application/json` body without converting it to base64? Why is `multipart/form-data` with streaming boundaries superior for file uploads?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 33.3 Persistent Connections: HTTP/1.0 vs HTTP/1.1 vs HTTP/2
**QUESTION:**
Explain the performance evolution of HTTP connections:
1. HTTP/1.0: Closes TCP connection after every single request.
2. HTTP/1.1: `Connection: keep-alive` (reusing TCP sockets).
3. HTTP/2: Binary multiplexing over a single TCP stream.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 33.4 Cookies vs Authorization Headers
**QUESTION:**
In modern REST APIs, why do single-page applications (React/Vue) and mobile apps prefer sending JWT tokens via `Authorization: Bearer <token>` headers instead of relying on automatic browser cookies?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 33.5 HTTPS and TLS 1.3 Handshake
**QUESTION:**
What does the client verify when the server sends its TLS certificate during the HTTPS handshake? What prevents a malicious actor on public Wi-Fi from reading HTTP headers in an HTTPS request?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
