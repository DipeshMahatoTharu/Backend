"""
Day 51 Daily Challenge: Automated Collection Test Runner Engine (Mini-Newman)

Problem:
Implement an automated API test runner that:
1. Loads a simulated Postman Collection containing multiple HTTP requests.
2. Supports environment variable substitution (`{{base_url}}`, `{{token}}`).
3. Executes requests against a mock API dispatcher.
4. Evaluates response status codes, header expectations, and JSON body field assertions.
5. Emits a clean test execution report.
"""
from typing import Dict, Any, List, Optional, Tuple

class MockAPIServer:
    def __init__(self):
        self.users = {1: {"id": 1, "name": "Dipesh", "role": "admin"}}

    def handle(self, method: str, path: str, headers: Dict[str, str], body: Optional[Dict[str, Any]] = None) -> Tuple[int, Dict[str, str], Dict[str, Any]]:
        auth = headers.get("Authorization", "")
        if not auth.startswith("Bearer "):
            return 401, {}, {"error": "Unauthorized"}

        if path == "/api/v1/users/1" and method == "GET":
            return 200, {"Content-Type": "application/json"}, self.users[1]
        elif path == "/api/v1/users" and method == "POST":
            if not body or "name" not in body:
                return 400, {}, {"error": "Name required"}
            new_user = {"id": 2, "name": body["name"], "role": "user"}
            return 201, {"Location": "/api/v1/users/2"}, new_user
        return 404, {}, {"error": "Not Found"}


class MiniCollectionRunner:
    def __init__(self, server: MockAPIServer, environment: Dict[str, str]):
        self.server = server
        self.environment = environment
        self.results: List[Dict[str, Any]] = []

    def _interpolate(self, text: str) -> str:
        for k, v in self.environment.items():
            text = text.replace(f"{{{{{k}}}}}", v)
        return text

    def run_request(self, test_item: Dict[str, Any]) -> bool:
        name = test_item["name"]
        method = test_item["request"]["method"]
        raw_url = test_item["request"]["url"]
        path = self._interpolate(raw_url).replace("https://api.example.com", "")

        raw_headers = test_item["request"].get("headers", {})
        headers = {k: self._interpolate(v) for k, v in raw_headers.items()}
        body = test_item["request"].get("body")

        # Execute
        status, resp_headers, resp_data = self.server.handle(method, path, headers, body)

        # Assertions
        expected_status = test_item.get("expected_status", 200)
        status_ok = (status == expected_status)
        fields_ok = True
        for rf in test_item.get("required_fields", []):
            if rf not in resp_data:
                fields_ok = False
                break

        passed = status_ok and fields_ok
        self.results.append({
            "test_name": name,
            "passed": passed,
            "status": status,
            "expected_status": expected_status
        })
        return passed


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    server = MockAPIServer()
    env = {"base_url": "https://api.example.com", "auth_token": "secret_jwt_123"}
    runner = MiniCollectionRunner(server, env)

    collection = [
        {
            "name": "Get User Profile",
            "request": {
                "method": "GET",
                "url": "{{base_url}}/api/v1/users/1",
                "headers": {"Authorization": "Bearer {{auth_token}}"}
            },
            "expected_status": 200,
            "required_fields": ["id", "name"]
        },
        {
            "name": "Create User",
            "request": {
                "method": "POST",
                "url": "{{base_url}}/api/v1/users",
                "headers": {"Authorization": "Bearer {{auth_token}}"},
                "body": {"name": "Bob"}
            },
            "expected_status": 201,
            "required_fields": ["id", "name"]
        },
        {
            "name": "Unauthorized Test",
            "request": {
                "method": "GET",
                "url": "{{base_url}}/api/v1/users/1",
                "headers": {}  # Missing auth
            },
            "expected_status": 401
        }
    ]

    for item in collection:
        success = runner.run_request(item)
        assert success is True

    assert len(runner.results) == 3
    assert all(r["passed"] for r in runner.results)

    print("All MiniCollectionRunner challenge tests passed successfully!")
