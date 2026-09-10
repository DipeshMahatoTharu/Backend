"""
============================================================
DAY 33 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: Raw Socket-Level HTTP/1.1 Request Dispatcher & Server Mock

Before web frameworks like Django or FastAPI existed, backend engines
listened directly on raw TCP sockets, parsed incoming HTTP byte streams,
and formatted compliant HTTP/1.1 text responses.

============================================================
REQUIREMENTS:
============================================================
1. Class `SimpleHTTPDispatcher`:
   - `handle_raw_request(self, raw_data: bytes) -> bytes`:
     * Decodes raw incoming bytes using UTF-8.
     * Separates headers from body using `\r\n\r\n`.
     * Validates method and path.
     * If path == "/health", returns 200 OK with `{"status": "healthy"}`.
     * If path == "/echo" and method == "POST", parses JSON body and returns
       200 OK echoing back `{"echo": body_json}`.
     * If path not found, returns 404 Not Found with `{"error": "Endpoint not found"}`.
     * If POST body is invalid JSON, returns 400 Bad Request with `{"error": "Malformed JSON"}`.
     * Encodes formatted HTTP response into UTF-8 bytes with proper Content-Length and Content-Type.
"""

import json
from typing import Any


class SimpleHTTPDispatcher:
    def handle_raw_request(self, raw_data: bytes) -> bytes:
        """Parses raw HTTP bytes and returns valid HTTP/1.1 response bytes."""
        # TODO: Implement request parsing and endpoint dispatching
        pass


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    print("Testing SimpleHTTPDispatcher...")
    dispatcher = SimpleHTTPDispatcher()

    # Test 1: Health check
    req1 = b"GET /health HTTP/1.1\r\nHost: localhost\r\n\r\n"
    res1 = dispatcher.handle_raw_request(req1)
    print("Test 1 (Health Check Output):")
    print(res1.decode("utf-8") if res1 else "None")

    # Test 2: Echo POST
    req2 = (
        b"POST /echo HTTP/1.1\r\n"
        b"Host: localhost\r\n"
        b"Content-Type: application/json\r\n"
        b"\r\n"
        b'{"message": "Hello Backend World"}'
    )
    res2 = dispatcher.handle_raw_request(req2)
    print("Test 2 (Echo Output):")
    print(res2.decode("utf-8") if res2 else "None")

    # Test 3: 404 Route
    req3 = b"GET /unknown HTTP/1.1\r\nHost: localhost\r\n\r\n"
    res3 = dispatcher.handle_raw_request(req3)
    print("Test 3 (404 Output):")
    print(res3.decode("utf-8") if res3 else "None")
