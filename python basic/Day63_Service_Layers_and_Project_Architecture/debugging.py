"""
Day 55: Service Layers & Project Architecture — Debugging
Diagnose and fix 3 critical service layer and transaction bugs.
"""
from typing import Dict, Any, List

# ---------------------------------------------------------------------
# Bug 1: Enqueuing Async Task Inside Transaction (The Celery Race Condition)
# Problem: `send_email.delay()` was called before `transaction.commit()`.
# The Celery worker started immediately, queried the database for the newly created
# object, but got `ObjectDoesNotExist` because the database hadn't committed yet!
# Fix: Wrap async task in `on_commit()`.
# ---------------------------------------------------------------------
class TransactionSimulator:
    def __init__(self):
        self.committed = False
        self.hooks = []

    def add_on_commit(self, hook):
        self.hooks.append(hook)

    def commit(self):
        self.committed = True
        for h in self.hooks:
            h()

def schedule_background_notification(tx: TransactionSimulator, task_fn):
    # BUGGY VERSION:
    # task_fn() # Executed before commit!

    # FIXED VERSION:
    tx.add_on_commit(task_fn)


# ---------------------------------------------------------------------
# Bug 2: Leaking ORM Models into Presentation Layer
# Problem: A service returned raw Django model instances containing sensitive
# fields (password hash) to a view.
# Fix: Transform model into a sanitized DTO.
# ---------------------------------------------------------------------
def sanitize_user_to_dto(user_model: Dict[str, Any]) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return user_model # Leaks password_hash!

    # FIXED VERSION:
    return {
        "id": user_model["id"],
        "username": user_model["username"],
        "email": user_model["email"]
    }


# ---------------------------------------------------------------------
# Bug 3: Swallowing Database Exceptions in Service Layer
# Problem: A service caught all exceptions and returned `None` without rolling back,
# leaving the database in an inconsistent partial state.
# Fix: Allow exceptions to propagate or explicitly trigger rollback.
# ---------------------------------------------------------------------
def execute_atomic_operation(should_fail: bool) -> bool:
    # BUGGY VERSION:
    # try: ... except: return None

    # FIXED VERSION:
    if should_fail:
        raise RuntimeError("Transaction aborted: Rolling back database changes.")
    return True


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    tx = TransactionSimulator()
    executed = []
    schedule_background_notification(tx, lambda: executed.append("task_ran"))
    assert len(executed) == 0  # Not executed before commit
    tx.commit()
    assert len(executed) == 1  # Executed after commit!

    # Test Bug 2 fix
    raw_user = {"id": 1, "username": "alice", "email": "a@example.com", "password_hash": "pbkdf2_..."}
    dto = sanitize_user_to_dto(raw_user)
    assert "password_hash" not in dto
    assert dto["username"] == "alice"

    # Test Bug 3 fix
    try:
        execute_atomic_operation(should_fail=True)
        assert False, "Should raise RuntimeError"
    except RuntimeError:
        pass

    print("All Day 55 debugging fixes verified successfully!")
