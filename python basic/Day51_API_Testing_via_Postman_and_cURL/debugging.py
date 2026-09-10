"""
Day 51: API Testing via Postman & cURL — Debugging
Diagnose and fix 3 common API testing and CLI curl mistakes.
"""
from typing import Dict, Any, Tuple

# ---------------------------------------------------------------------
# Bug 1: Missing `Content-Type: application/json` in cURL
# Problem: A developer called `curl -X POST -d '{"name": "test"}' http://localhost:8000/api/users/`.
# Django assumed default form-urlencoded, failed to parse JSON, and returned 400 Bad Request.
# Fix: Ensure `Content-Type: application/json` is included whenever JSON body is passed.
# ---------------------------------------------------------------------
def sanitize_curl_headers(headers: Dict[str, str], has_body: bool) -> Dict[str, str]:
    # BUGGY VERSION:
    # return headers

    # FIXED VERSION:
    updated = dict(headers)
    if has_body and "Content-Type" not in updated:
        updated["Content-Type"] = "application/json"
    return updated


# ---------------------------------------------------------------------
# Bug 2: Leaking Production Secrets in Shared Postman Collections
# Problem: A developer exported a collection with hardcoded API keys in the collection
# JSON file and pushed it to public GitHub.
# Fix: Scrub secrets and replace with environment references `{{api_key}}`.
# ---------------------------------------------------------------------
def sanitize_postman_collection(collection_json: Dict[str, Any]) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return collection_json

    # FIXED VERSION:
    clean = dict(collection_json)
    if "values" in clean:
        for item in clean["values"]:
            if "key" in item["key"].lower() or "token" in item["key"].lower():
                item["value"] = ""  # Strip sensitive values from exports
    return clean


# ---------------------------------------------------------------------
# Bug 3: Handling Windows PowerShell Quotes in cURL
# Problem: In PowerShell, single quotes `'{"title": "test"}'` cause argument parsing errors.
# Fix: Escape double quotes properly: `"{"title": "test"}"`.
# ---------------------------------------------------------------------
def format_powershell_curl_body(json_str: str) -> str:
    # BUGGY VERSION:
    # return f"'{json_str}'"

    # FIXED VERSION:
    escaped = json_str.replace('"', '\"')
    return f'"{escaped}"'


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    h = sanitize_curl_headers({}, has_body=True)
    assert h["Content-Type"] == "application/json"

    # Test Bug 2 fix
    coll = {"values": [{"key": "api_token", "value": "super_secret_123"}]}
    sanitized = sanitize_postman_collection(coll)
    assert sanitized["values"][0]["value"] == ""

    # Test Bug 3 fix
    ps_body = format_powershell_curl_body('{"name": "test"}')
    assert ps_body == '"{\"name\": \"test\"}"'

    print("All Day 51 debugging fixes verified successfully!")
