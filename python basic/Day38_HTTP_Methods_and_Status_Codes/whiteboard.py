"""
============================================================
DAY 34 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: HTTP Status Code and Error Resolver

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement an HTTP Error Resolver function `resolve_http_error(exception)` that inspects
incoming backend exception objects and maps them to the appropriate standard HTTP status code,
standard HTTP reason phrase, and RFC 7807 error payload.

Exception Mappings:
- KeyError / ObjectDoesNotExist -> 404 Not Found
- PermissionError -> 403 Forbidden
- UnauthenticatedError -> 401 Unauthorized
- ValueError / ValidationError -> 422 Unprocessable Entity
- IntegrityError (Duplicate key) -> 409 Conflict
- All other uncaught exceptions -> 500 Internal Server Error

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Return a tuple: (status_code: int, payload: dict)
- Payload must conform to RFC 7807: {"type": str, "title": str, "status": int, "detail": str}
- For 500 Internal Server Error, do NOT leak internal stack traces or database query details to the client.

============================================================
MY APPROACH:
============================================================
1. Inspect the type of the exception using `isinstance()`.
2. Map known exception types to standard HTTP status codes and RFC titles.
3. Extract exception message for client-safe details, but sanitize 500 error messages to prevent data leakage.
"""
from typing import Tuple, Dict, Any

class UnauthenticatedError(Exception):
    pass

class IntegrityError(Exception):
    pass

def resolve_http_error(exc: Exception) -> Tuple[int, Dict[str, Any]]:
    mapping = [
        (UnauthenticatedError, 401, "Unauthorized"),
        (PermissionError, 403, "Forbidden"),
        (KeyError, 404, "Not Found"),
        (ValueError, 422, "Unprocessable Entity"),
        (IntegrityError, 409, "Conflict"),
    ]

    for exc_type, status_code, title in mapping:
        if isinstance(exc, exc_type):
            return status_code, {
                "type": f"https://api.example.com/errors/{status_code}",
                "title": title,
                "status": status_code,
                "detail": str(exc).strip("'")
            }

    # Fallback to 500 Internal Server Error (never leak raw exception text in production)
    return 500, {
        "type": "https://api.example.com/errors/500",
        "title": "Internal Server Error",
        "status": 500,
        "detail": "An unexpected internal server error occurred. Please contact support."
    }


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    # Test 401
    status, payload = resolve_http_error(UnauthenticatedError("Missing Bearer token"))
    assert status == 401
    assert payload["title"] == "Unauthorized"

    # Test 403
    status, payload = resolve_http_error(PermissionError("User is not an administrator"))
    assert status == 403

    # Test 404
    status, payload = resolve_http_error(KeyError("user_id_44"))
    assert status == 404

    # Test 422
    status, payload = resolve_http_error(ValueError("Email format invalid"))
    assert status == 422

    # Test 409
    status, payload = resolve_http_error(IntegrityError("Unique constraint violated: users_email_key"))
    assert status == 409

    # Test 500 Sanitization
    status, payload = resolve_http_error(ZeroDivisionError("division by zero in database_query_calc()"))
    assert status == 500
    assert "division by zero" not in payload["detail"]

    print("Whiteboard Day 34 challenge passed successfully!")
