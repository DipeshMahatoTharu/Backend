# Day 33 — HTTP Protocols, Anatomy & Payload Formats

## 🎯 Learning Objectives
- Master the client-server request-response lifecycle of the Hypertext Transfer Protocol (HTTP).
- Understand the exact physical anatomy of HTTP/1.1 messages: Request Line, Headers, CRLF delimiter, and Body.
- Understand common payload serialization formats: `application/json`, `application/x-www-form-urlencoded`, and `multipart/form-data`.
- Learn how DNS, TCP 3-way handshake, and TLS/HTTPS encryption establish transport security before HTTP bytes are transmitted.
- Understand connection persistence: HTTP/1.0 connection closing vs HTTP/1.1 `Keep-Alive` vs HTTP/2 Multiplexing.

---

## 📚 Core Backend Concepts

### 1. The Physical Anatomy of an HTTP Request
An HTTP request is plain text sent across a TCP socket, formatted with strict CRLF (`\r\n`) separators:
```http
POST /api/v1/users HTTP/1.1\r\n
Host: api.example.com\r\n
Content-Type: application/json\r\n
Content-Length: 42\r\n
Authorization: Bearer eyJhbGciOi...\r\n
\r\n
{"name": "Dipesh", "role": "Backend Dev"}
```
- **Request Line**: `<METHOD> <REQUEST_URI> <HTTP_VERSION>`
- **Headers**: Key-value pairs providing metadata.
- **Empty Line (`\r\n\r\n`)**: Indicates the end of headers and the start of the payload body.
- **Body**: The raw byte payload whose size MUST match `Content-Length` (or use `Transfer-Encoding: chunked`).

### 2. Payload Formats: JSON vs Multipart Form Data
- **`application/json`**: Lightweight, hierarchical key-value structure standard for modern REST APIs.
- **`multipart/form-data`**: Used when uploading binary files (images, PDFs) alongside metadata. Uses boundary strings (e.g. `--boundary123`) to separate distinct file streams.
- **`application/x-www-form-urlencoded`**: Standard HTML form submission format (key=value&key2=val2).

### 3. Transport Lifecycle Before HTTP
Before the first HTTP byte is sent:
1. **DNS Lookup**: Client resolves domain `api.example.com` to IP address `104.21.45.10`.
2. **TCP 3-Way Handshake**: Client sends `SYN`, server responds with `SYN-ACK`, client replies `ACK` (1 round trip time - RTT).
3. **TLS 1.3 Handshake**: Diffie-Hellman key exchange and certificate verification for HTTPS (1 RTT).
4. **HTTP Exchange**: Client sends request, server returns response.

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review HTTP message framing, CRLF delimiters, and answer [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Implement socket request parsers in [`practice.py`](practice.py) and fix protocol bugs in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the raw socket HTTP parser in [`challenge.py`](challenge.py), solve [`whiteboard.py`](whiteboard.py), and study [`interview.md`](interview.md).
