"""
Day 52: Automated API Unit Testing — Debugging
Diagnose and fix 3 common unit testing and mocking bugs.
"""
from unittest.mock import MagicMock
from typing import Dict, Any, Optional

# ---------------------------------------------------------------------
# Bug 1: Mocking the Wrong Import Location
# Problem: Module `app.views` does `from app.utils import send_email`.
# In the test, `@patch('app.utils.send_email')` was used instead of
# `@patch('app.views.send_email')`. The real email sender was executed!
# Fix: Always patch where the function is looked up (in the importing module).
# ---------------------------------------------------------------------
def resolve_mock_target(importing_module: str, function_name: str) -> str:
    # BUGGY VERSION:
    # return f"app.utils.{function_name}"

    # FIXED VERSION:
    return f"{importing_module}.{function_name}"


# ---------------------------------------------------------------------
# Bug 2: Mutating Test Fixtures Across Tests
# Problem: A test modified a class-level dictionary `cls.shared_user['balance'] += 100`.
# Subsequent tests failed because initial state was polluted.
# Fix: Deepcopy or re-instantiate fixtures per test.
# ---------------------------------------------------------------------
def get_clean_test_fixture(base_fixture: Dict[str, Any]) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return base_fixture # Mutates shared reference!

    # FIXED VERSION:
    import copy
    return copy.deepcopy(base_fixture)


# ---------------------------------------------------------------------
# Bug 3: Missing Assertion on Mock Calls
# Problem: A test passed because it called the endpoint, but forgot to assert
# whether the mock was actually called or what arguments were passed!
# Fix: Enforce `assert_called_once_with`.
# ---------------------------------------------------------------------
def verify_mock_execution(mock_fn: MagicMock, expected_arg: str) -> bool:
    mock_fn(expected_arg)
    mock_fn.assert_called_once_with(expected_arg)
    return True


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    assert resolve_mock_target("app.views", "send_email") == "app.views.send_email"

    # Test Bug 2 fix
    fixture = {"user_id": 1, "roles": ["admin"]}
    f1 = get_clean_test_fixture(fixture)
    f1["roles"].append("editor")
    assert "editor" not in fixture["roles"]  # Original clean!

    # Test Bug 3 fix
    mock = MagicMock()
    assert verify_mock_execution(mock, "test_payload") is True

    print("All Day 52 debugging fixes verified successfully!")
