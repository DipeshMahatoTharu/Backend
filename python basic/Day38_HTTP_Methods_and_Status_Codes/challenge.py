"""
Day 34 Daily Challenge: HTTP Status & Method Routing Middleware Engine

Problem:
Implement a lightweight, production-grade HTTP Dispatcher that simulates a web framework's
core routing mechanism. The dispatcher must:
1. Route requests by (Method, Path).
2. Validate HTTP method support (return 405 Method Not Allowed with an 'Allow' header if path exists for other methods).
3. Validate client authentication & authorization (return 401 Unauthorized or 403 Forbidden).
4. Parse request bodies and validate schema, returning 400 Bad Request or 422 Unprocessable Entity.
5. Return 204 No Content for DELETE endpoints with no body.
6. Catch unexpected errors and return 500 Internal Server Error formatted with RFC 7807 Problem Details.
"""
from typing import Dict, Any, Callable, Tuple, Optional
import json

class Response:
    def __init__(self, status_code: int, body: Any = None, headers: Optional[Dict[str, str]] = None):
        self.status_code = status_code
        self.body = body
        self.headers = headers or {}
        if self.body is not None and "Content-Type" not in self.headers:
            self.headers["Content-Type"] = "application/json"

class HTTPDispatcher:
    def __init__(self):
        # Format: {path: {method: handler}}
        self.routes: Dict[str, Dict[str, Callable]] = {}

    def register(self, method: str, path: str):
        """Decorator to register route handlers."""
        def decorator(handler: Callable):
            if path not in self.routes:
                self.routes[path] = {}
            self.routes[path][method.upper()] = handler
            return handler
        return decorator

    def dispatch(self, method: str, path: str, headers: Dict[str, str], body: Optional[str] = None) -> Response:
        method = method.upper()

        # 1. Path existence check
        if path not in self.routes:
            return Response(404, {"error": "Not Found", "message": f"Resource '{path}' does not exist."})

        # 2. Method Allowed check
        allowed_methods = list(self.routes[path].keys())
        if method not in self.routes[path]:
            return Response(
                405,
                {"error": "Method Not Allowed", "message": f"Method {method} is not supported."},
                {"Allow": ", ".join(allowed_methods)}
            )

        handler = self.routes[path][method]

        # 3. Execution & Exception handling
        try:
            return handler(headers, body)
        except PermissionError as pe:
            return Response(403, {"error": "Forbidden", "message": str(pe)})
        except ValueError as ve:
            return Response(422, {"error": "Unprocessable Entity", "message": str(ve)})
        except Exception as exc:
            return Response(500, {"error": "Internal Server Error", "message": "An unexpected error occurred."})


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    dispatcher = HTTPDispatcher()

    # Define endpoints
    @dispatcher.register("GET", "/api/v1/users")
    def list_users(headers, body):
        return Response(200, [{"id": 1, "name": "Dipesh"}])

    @dispatcher.register("POST", "/api/v1/users")
    def create_user(headers, body):
        if "Authorization" not in headers:
            return Response(401, {"error": "Unauthorized", "message": "Authentication required."})
        data = json.loads(body or "{}")
        if "name" not in data:
            raise ValueError("Field 'name' is required.")
        return Response(201, {"id": 2, "name": data["name"]}, {"Location": "/api/v1/users/2"})

    @dispatcher.register("DELETE", "/api/v1/users")
    def delete_user(headers, body):
        auth = headers.get("Authorization", "")
        if "admin" not in auth:
            raise PermissionError("Admin credentials required to delete users.")
        return Response(204, None)

    # 1. Test 200 OK
    res = dispatcher.dispatch("GET", "/api/v1/users", {})
    assert res.status_code == 200
    assert res.body[0]["name"] == "Dipesh"

    # 2. Test 404 Not Found
    res = dispatcher.dispatch("GET", "/api/v1/unknown", {})
    assert res.status_code == 404

    # 3. Test 405 Method Not Allowed
    res = dispatcher.dispatch("PUT", "/api/v1/users", {})
    assert res.status_code == 405
    assert "GET" in res.headers["Allow"] and "POST" in res.headers["Allow"]

    # 4. Test 401 Unauthorized
    res = dispatcher.dispatch("POST", "/api/v1/users", {}, json.dumps({"name": "Alok"}))
    assert res.status_code == 401

    # 5. Test 201 Created with Location header
    res = dispatcher.dispatch("POST", "/api/v1/users", {"Authorization": "Bearer token"}, json.dumps({"name": "Alok"}))
    assert res.status_code == 201
    assert res.headers["Location"] == "/api/v1/users/2"

    # 6. Test 422 Unprocessable Entity
    res = dispatcher.dispatch("POST", "/api/v1/users", {"Authorization": "Bearer token"}, json.dumps({}))
    assert res.status_code == 422

    # 7. Test 403 Forbidden
    res = dispatcher.dispatch("DELETE", "/api/v1/users", {"Authorization": "Bearer standard-user"})
    assert res.status_code == 403

    # 8. Test 204 No Content
    res = dispatcher.dispatch("DELETE", "/api/v1/users", {"Authorization": "Bearer admin-user"})
    assert res.status_code == 204
    assert res.body is None

    print("All HTTPDispatcher challenge tests passed successfully!")
