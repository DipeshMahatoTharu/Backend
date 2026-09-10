# Day 33 Practice — HTTP Request Parsing & Response Formatting

import json
from typing import Any

# =====================================================================
# TASK 1: Raw HTTP Request Line & Header Parser
# =====================================================================
# Complete `parse_http_request(raw_request: str) -> dict`:
# - Extracts: method, path, http_version, headers (dict of lowercase keys), and body.
# - The headers and body are separated by double CRLF: "\r\n\r\n".
# - Headers are separated by single CRLF: "\r\n".

def parse_http_request(raw_request: str) -> dict[str, Any]:
    # TODO: Split into header_section and body_section
    # Extract method, path, http_version from line 1
    # Parse header lines into dictionary
    pass


# =====================================================================
# TASK 2: HTTP Response Formatter
# =====================================================================
# Complete `format_http_response(status_code: int, status_text: str, data: dict) -> str`:
# - Converts `data` dictionary to JSON string.
# - Computes Content-Length in bytes.
# - Returns a fully valid HTTP/1.1 response string with CRLF line endings:
#   HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: ...\r\n\r\n<body>

def format_http_response(status_code: int, status_text: str, data: dict) -> str:
    # TODO: Build valid HTTP/1.1 response string
    pass


# =====================================================================
# TASK 3: Header Extraction Helper
# =====================================================================
# Complete `get_bearer_token(headers: dict[str, str]) -> str | None`:
# - Case-insensitively checks for "authorization" header.
# - If header starts with "Bearer ", returns the token string. Otherwise returns None.

def get_bearer_token(headers: dict[str, str]) -> str | None:
    # TODO: Extract bearer token
    pass


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    print("--- Running Day 33 Practice Tasks ---")
    raw_req = (
        "POST /api/v1/auth/login HTTP/1.1\r\n"
        "Host: localhost:8000\r\n"
        "Content-Type: application/json\r\n"
        "Authorization: Bearer secret_jwt_token_123\r\n"
        "\r\n"
        '{"username": "dipesh", "password": "secure_password"}'
    )
    parsed = parse_http_request(raw_req)
    print("Task 1 (Parsed Method):", parsed.get("method") if parsed else None)
    print("Task 1 (Parsed Path):", parsed.get("path") if parsed else None)
    print("Task 1 (Parsed Body):", parsed.get("body") if parsed else None)

    token = get_bearer_token(parsed.get("headers", {}) if parsed else {})
    print("Task 3 (Extracted Token):", token)

    resp = format_http_response(200, "OK", {"status": "success", "user_id": 42})
    print("\nTask 2 (Formatted Response):")
    print(repr(resp))
