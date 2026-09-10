"""
============================================================
DAY 52 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Custom Mock Function & Call History Tracker

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a lightweight `MockCallable` class that mimics `unittest.mock.MagicMock`:
1. Records every invocation: args and kwargs.
2. Tracks `call_count`.
3. Method `assert_called_once()`: Raises `AssertionError` if call_count != 1.
4. Method `assert_called_with(*args, **kwargs)`: Raises `AssertionError` if the latest call did not match.
5. Allows configuring a `return_value`.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Do not import `unittest.mock`. Build pure Python tracker.

============================================================
MY APPROACH:
============================================================
1. Implement `__call__(*args, **kwargs)` storing `(args, kwargs)` in a list.
2. Increment `call_count`.
3. Check conditions in assertion methods.
"""
from typing import Any, List, Tuple, Dict

class MockCallable:
    def __init__(self, return_value: Any = None):
        self.return_value = return_value
        self.call_count = 0
        self.calls: List[Tuple[Tuple, Dict]] = []

    def __call__(self, *args, **kwargs) -> Any:
        self.call_count += 1
        self.calls.append((args, kwargs))
        return self.return_value

    def assert_called_once(self):
        if self.call_count != 1:
            raise AssertionError(f"Expected 1 call, but called {self.call_count} times.")

    def assert_called_with(self, *expected_args, **expected_kwargs):
        if not self.calls:
            raise AssertionError("Mock was never called.")
        latest_args, latest_kwargs = self.calls[-1]
        if latest_args != expected_args or latest_kwargs != expected_kwargs:
            raise AssertionError(
                f"Expected call with ({expected_args}, {expected_kwargs}), "
                f"but called with ({latest_args}, {latest_kwargs})"
            )


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    mock_email = MockCallable(return_value=True)

    # Initially 0 calls
    try:
        mock_email.assert_called_once()
        assert False, "Should fail on 0 calls"
    except AssertionError:
        pass

    # Single call
    res = mock_email("user@example.com", subject="Welcome")
    assert res is True
    assert mock_email.call_count == 1
    mock_email.assert_called_once()
    mock_email.assert_called_with("user@example.com", subject="Welcome")

    # Mismatched args
    try:
        mock_email.assert_called_with("wrong@example.com", subject="Welcome")
        assert False, "Should raise AssertionError on arg mismatch"
    except AssertionError:
        pass

    print("Whiteboard Day 52 challenge passed successfully!")
