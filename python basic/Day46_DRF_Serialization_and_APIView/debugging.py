"""
Day 46: DRF Serialization & APIView — Debugging
Diagnose and fix 3 common DRF serialization errors.
"""
from typing import Dict, Any

# ---------------------------------------------------------------------
# Bug 1: Calling `.save()` Before `.is_valid()`
# Problem: A view called `serializer.save()` without checking `serializer.is_valid()`.
# DRF raises: `AssertionError: You must call .is_valid() before calling .save().`
# Fix: Always call `.is_valid()` first.
# ---------------------------------------------------------------------
class MockSerializer:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.validated = False

    def is_valid(self, raise_exception: bool = False) -> bool:
        self.validated = True
        return True

    def save(self) -> Dict[str, Any]:
        if not self.validated:
            raise AssertionError("You must call .is_valid() before calling .save().")
        return {"status": "saved", "data": self.data}

def handle_submission(data: Dict[str, Any]) -> Dict[str, Any]:
    serializer = MockSerializer(data)
    # BUGGY VERSION:
    # return serializer.save() # Crashes!

    # FIXED VERSION:
    serializer.is_valid(raise_exception=True)
    return serializer.save()


# ---------------------------------------------------------------------
# Bug 2: Mutating Read-Only Fields from Request Payload
# Problem: A client submitted `{"id": 999, "is_staff": True}` in POST `/api/users/`.
# Because `id` and `is_staff` were not marked `read_only=True`, the serializer
# allowed the client to grant themselves staff privileges!
# Fix: Strip read-only fields during deserialization.
# ---------------------------------------------------------------------
def deserialize_user(data: Dict[str, Any], read_only_fields: set) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return data # Kept read-only fields!

    # FIXED VERSION:
    return {k: v for k, v in data.items() if k not in read_only_fields}


# ---------------------------------------------------------------------
# Bug 3: Swallowing Validation Errors
# Problem: A developer wrote `if serializer.is_valid(): serializer.save()` without
# an else block. When invalid data arrived, the view returned `200 OK` with `None`!
# Fix: Always raise or return 400 with errors.
# ---------------------------------------------------------------------
def execute_view_action(is_valid: bool, errors: Dict[str, str]) -> Dict[str, Any]:
    # BUGGY VERSION:
    # if is_valid: return {"status": 200}
    # # Missing else! Returns None!

    # FIXED VERSION:
    if is_valid:
        return {"status": 201, "data": "Created"}
    return {"status": 400, "errors": errors}


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    res1 = handle_submission({"name": "Item"})
    assert res1["status"] == "saved"

    # Test Bug 2 fix
    raw = {"username": "john", "id": 50, "is_staff": True}
    cleaned = deserialize_user(raw, read_only_fields={"id", "is_staff"})
    assert "id" not in cleaned and "is_staff" not in cleaned
    assert cleaned["username"] == "john"

    # Test Bug 3 fix
    assert execute_view_action(True, {})["status"] == 201
    assert execute_view_action(False, {"err": "Bad"})["status"] == 400

    print("All Day 46 debugging fixes verified successfully!")
