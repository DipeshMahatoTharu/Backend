"""
============================================================
DAY 33 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: HTTP Request-Response Lifecycle & Transport Architecture

In technical screenings, interviewers frequently ask you to trace the
entire journey of an HTTP request from the moment a user hits Enter
in a browser until the backend returns a JSON payload.

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Write down the comprehensive technical sequence diagram and lifecycle
breakdown for:
`POST https://api.store.com/v1/checkout`
with payload: `{"cart_id": 105, "payment_token": "tok_xyz"}`.

Explain every layer in chronological order:
1. DNS Resolution (Browser cache -> OS cache -> Recursive Resolver -> Authoritative NS)
2. TCP Handshake (SYN, SYN-ACK, ACK)
3. TLS 1.3 Key Exchange & Certificate Handshake
4. Reverse Proxy / Load Balancer (Nginx / Cloudflare) Termination
5. WSGI / ASGI Middleware translation (converting raw socket to Django request object)
6. Backend Processing & HTTP Response generation

============================================================
MY TECHNICAL BREAKDOWN (Write on blank paper first!):
============================================================
Phase 1: DNS Resolution
____________________________________________________________
____________________________________________________________

Phase 2: TCP 3-Way Handshake
____________________________________________________________
____________________________________________________________

Phase 3: TLS Encryption Handshake
____________________________________________________________
____________________________________________________________

Phase 4: Reverse Proxy & Gateway
____________________________________________________________
____________________________________________________________

Phase 5: WSGI Application Execution
____________________________________________________________
____________________________________________________________

"""
