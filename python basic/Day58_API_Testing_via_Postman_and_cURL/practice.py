"""
Day 51: API Testing via Postman & cURL — Practice
Hands-on exercises covering cURL command generation, environment variable substitution, and test assertions.
"""
import json
from typing import Dict, Any, List, Optional

# ---------------------------------------------------------------------
# Task 1: cURL Command Generator
# ---------------------------------------------------------------------
def build_curl_command(
    method: str,
    url: str,
    headers: Optional[Dict[str, str]] = None,
    data: Optional[Dict[str, Any]] = None
) -> str:
    """
    Builds a clean, safe cURL command string.
    """
    parts = [f"curl -X {method.upper()} '{url}'"]
    if headers:
        for k, v in headers.items():
            parts.append(f"-H '{k}: {v}'")
    if data is not None:
        payload_str = json.dumps(data)
        parts.append(f"-d '{payload_str}'")
    return " \
     ".join(parts)


# ---------------------------------------------------------------------
# Task 2: Postman Environment Variable Interpolator
# ---------------------------------------------------------------------
def substitute_environment_variables(template_str: str, environment: Dict[str, str]) -> str:
    """
    Replaces Postman {{variable_name}} syntax with values from environment dictionary.
    """
    output = template_str
    for k, v in environment.items():
        placeholder = f"{{{{{k}}}}}"
        output = output.replace(placeholder, v)
    return output


# ---------------------------------------------------------------------
# Task 3: Test Assertion Evaluator
# ---------------------------------------------------------------------
def evaluate_response_assertions(
    response_status: int,
    response_data: Dict[str, Any],
    expected_status: int,
    required_fields: List[str]
) -> Dict[str, Any]:
    """
    Simulates Postman test runner assertions.
    """
    status_passed = response_status == expected_status
    missing_fields = [f for f in required_fields if f not in response_data]
    fields_passed = len(missing_fields) == 0

    return {
        "all_passed": status_passed and fields_passed,
        "status_check": {"passed": status_passed, "expected": expected_status, "actual": response_status},
        "fields_check": {"passed": fields_passed, "missing": missing_fields}
    }


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 51 Practice Tests ---")

    # Test Task 1
    cmd = build_curl_command(
        "POST",
        "https://api.example.com/v1/orders",
        headers={"Content-Type": "application/json", "Authorization": "Bearer tok123"},
        data={"item_id": 99}
    )
    assert "curl -X POST" in cmd
    assert "-H 'Authorization: Bearer tok123'" in cmd
    assert '{"item_id": 99}' in cmd

    # Test Task 2
    env = {"base_url": "https://staging.api.com", "user_id": "42"}
    res_url = substitute_environment_variables("{{base_url}}/users/{{user_id}}/", env)
    assert res_url == "https://staging.api.com/users/42/"

    # Test Task 3
    resp_payload = {"id": 1, "name": "Alice"}
    eval_res = evaluate_response_assertions(200, resp_payload, expected_status=200, required_fields=["id", "name"])
    assert eval_res["all_passed"] is True

    eval_fail = evaluate_response_assertions(400, resp_payload, expected_status=200, required_fields=["id"])
    assert eval_fail["all_passed"] is False

    print("All Day 51 practice assertions passed successfully!")
