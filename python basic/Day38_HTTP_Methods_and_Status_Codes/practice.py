"""
Day 34: HTTP Methods & Status Codes — Practice
Hands-on exercises covering HTTP method safety, idempotency tracking, and RFC 7807 error formatting.
"""
from typing import Dict, Any, Optional, Tuple
import json
import uuid

# ---------------------------------------------------------------------
# Task 1: Method Property Inspector
# ---------------------------------------------------------------------
def inspect_http_method(method: str) -> Dict[str, bool]:
    """
    Returns a dictionary indicating whether the given HTTP method is:
    - 'safe': Does not alter server state.
    - 'idempotent': Multiple identical requests have the exact same side-effect.
    - 'allows_body': Standard specifications permit an entity payload body.
    """
    method = method.upper()
    properties = {
        "GET": {"safe": True, "idempotent": True, "allows_body": False},
        "HEAD": {"safe": True, "idempotent": True, "allows_body": False},
        "OPTIONS": {"safe": True, "idempotent": True, "allows_body": False},
        "POST": {"safe": False, "idempotent": False, "allows_body": True},
        "PUT": {"safe": False, "idempotent": True, "allows_body": True},
        "PATCH": {"safe": False, "idempotent": False, "allows_body": True},
        "DELETE": {"safe": False, "idempotent": True, "allows_body": False},
    }
    return properties.get(method, {"safe": False, "idempotent": False, "allows_body": False})


# ---------------------------------------------------------------------
# Task 2: RFC 7807 Problem Details Formatter
# ---------------------------------------------------------------------
def format_problem_details(
    status: int,
    title: str,
    detail: str,
    instance: str,
    type_uri: str = "about:blank",
    invalid_params: Optional[list] = None
) -> Tuple[int, Dict[str, str], str]:
    """
    Creates an RFC 7807 compliant error response.
    Returns (status_code, headers, json_body_string).
    Headers must include 'Content-Type': 'application/problem+json'.
    """
    payload: Dict[str, Any] = {
        "type": type_uri,
        "title": title,
        "status": status,
        "detail": detail,
        "instance": instance
    }
    if invalid_params:
        payload["invalid_params"] = invalid_params

    headers = {"Content-Type": "application/problem+json"}
    return status, headers, json.dumps(payload)


# ---------------------------------------------------------------------
# Task 3: In-Memory Idempotency Cache Manager
# ---------------------------------------------------------------------
class IdempotencyManager:
    """
    Caches responses by idempotency key. If a request arrives with an existing key:
    - If identical: return the cached response without re-executing.
    - If the request body differs: raise ValueError('Idempotency key reused with different payload').
    """
    def __init__(self):
        self._cache: Dict[str, Tuple[str, Any]] = {}

    def process_request(self, key: str, payload_hash: str, handler_func, *args, **kwargs) -> Any:
        if key in self._cache:
            cached_hash, cached_response = self._cache[key]
            if cached_hash != payload_hash:
                raise ValueError("Idempotency key reused with different payload")
            return cached_response

        # Execute handler
        result = handler_func(*args, **kwargs)
        self._cache[key] = (payload_hash, result)
        return result


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 34 Practice Tests ---")

    # Test Task 1
    get_props = inspect_http_method("GET")
    assert get_props["safe"] is True and get_props["idempotent"] is True
    post_props = inspect_http_method("POST")
    assert post_props["safe"] is False and post_props["idempotent"] is False
    put_props = inspect_http_method("PUT")
    assert put_props["safe"] is False and put_props["idempotent"] is True

    # Test Task 2
    status, headers, body = format_problem_details(
        status=400,
        title="Invalid Order Request",
        detail="The item quantity must be greater than zero.",
        instance="/api/v1/orders/123",
        invalid_params=[{"name": "quantity", "reason": "Must be >= 1"}]
    )
    assert status == 400
    assert headers["Content-Type"] == "application/problem+json"
    parsed_body = json.loads(body)
    assert parsed_body["status"] == 400
    assert len(parsed_body["invalid_params"]) == 1

    # Test Task 3
    mgr = IdempotencyManager()
    calls = []
    def charge_card(amount):
        calls.append(amount)
        return {"charge_id": "ch_999", "amount": amount, "status": "succeeded"}

    res1 = mgr.process_request("key-abc", "hash-100", charge_card, 100)
    assert len(calls) == 1
    assert res1["status"] == "succeeded"

    # Repeated request with same key and payload hash
    res2 = mgr.process_request("key-abc", "hash-100", charge_card, 100)
    assert len(calls) == 1  # Not called again
    assert res2 == res1

    # Conflict request with same key but different hash
    try:
        mgr.process_request("key-abc", "hash-200", charge_card, 200)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    print("All Day 34 practice assertions passed successfully!")
