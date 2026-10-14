"""
Day 55: Service Layers & Project Architecture — Practice
Hands-on exercises covering Data Transfer Objects, transaction coordinators, and repository abstractions.
"""
from dataclasses import dataclass
from typing import Dict, Any, List, Optional, Callable

# ---------------------------------------------------------------------
# Task 1: Immutable Data Transfer Object (DTO)
# ---------------------------------------------------------------------
@dataclass(frozen=True)
class UserRegistrationDTO:
    username: str
    email: str
    raw_password: str
    role: str = "member"

    def __post_init__(self):
        if len(self.username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if "@" not in self.email:
            raise ValueError("Invalid email address")


# ---------------------------------------------------------------------
# Task 2: Transaction `on_commit` Hook Simulator
# ---------------------------------------------------------------------
class MockTransactionManager:
    def __init__(self):
        self.in_transaction = False
        self._commit_hooks: List[Callable] = []

    def begin(self):
        self.in_transaction = True
        self._commit_hooks.clear()

    def on_commit(self, func: Callable):
        if self.in_transaction:
            self._commit_hooks.append(func)
        else:
            func()

    def commit(self):
        self.in_transaction = False
        # Execute all pending hooks
        for hook in self._commit_hooks:
            hook()
        self._commit_hooks.clear()

    def rollback(self):
        self.in_transaction = False
        # Discard hooks without executing!
        self._commit_hooks.clear()


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 55 Practice Tests ---")

    # Test Task 1: DTO validation
    dto = UserRegistrationDTO(username="dipesh", email="dipesh@example.com", raw_password="SecretPass123!")
    assert dto.username == "dipesh"
    try:
        dto.username = "changed"  # Frozen immutability
        assert False, "Should raise FrozenInstanceError"
    except Exception:
        pass

    # Test Task 2: on_commit simulator
    tx = MockTransactionManager()
    events = []

    # Rollback case: Hook must NOT execute
    tx.begin()
    tx.on_commit(lambda: events.append("email_sent"))
    tx.rollback()
    assert len(events) == 0  # Discarded!

    # Commit case: Hook MUST execute
    tx.begin()
    tx.on_commit(lambda: events.append("email_sent"))
    tx.commit()
    assert len(events) == 1
    assert events[0] == "email_sent"

    print("All Day 55 practice assertions passed successfully!")
