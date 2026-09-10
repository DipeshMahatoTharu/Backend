# Day 33 Debugging — HTTP Protocol Framing, Content-Length & Delimiters

# =====================================================================
# BUGGY SCENARIO 1: The Hanging Connection (Missing Header Delimiter)
# =====================================================================
# Goal: Send a mock HTTP response over a network socket.
# Problem: The developer formatted the response with single newline '\r\n'
# instead of double CRLF '\r\n\r\n' between headers and body.
# Web browsers and curl clients will hang indefinitely waiting for headers to finish!

def buggy_build_response(body_text: str) -> str:
    # BUG: Only one \r\n after Content-Length!
    return f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(body_text)}\r\n{body_text}"

# ---------------------------------------------------------------------
# QUESTION: Why do HTTP parsers hang if double CRLF is omitted?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite with proper \r\n\r\n delimiter.
# ---------------------------------------------------------------------
def fixed_build_response(body_text: str) -> str:
    pass


# =====================================================================
# BUGGY SCENARIO 2: Content-Length Character vs Byte Mismatch
# =====================================================================
# Goal: Send a JSON response containing non-ASCII UTF-8 characters (e.g. emojis or accents).
# Problem: Developer calculated `len(json_string)` in Python characters.
# In UTF-8, multi-byte characters (like '🚀' which is 4 bytes) make the byte length
# larger than string length! The client cuts off the last 3 bytes, corrupting the JSON!

def buggy_unicode_response(data: dict) -> bytes:
    json_str = '{"status": "ok", "icon": "🚀"}'
    # BUG: len(json_str) gives characters, NOT byte count!
    content_length = len(json_str)
    headers = f"HTTP/1.1 200 OK\r\nContent-Length: {content_length}\r\n\r\n"
    return (headers + json_str).encode("utf-8")

# ---------------------------------------------------------------------
# QUESTION: Why must Content-Length always reflect raw byte size?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Encode payload to bytes FIRST, then calculate len(payload_bytes).
# ---------------------------------------------------------------------
def fixed_unicode_response(data: dict) -> bytes:
    pass
