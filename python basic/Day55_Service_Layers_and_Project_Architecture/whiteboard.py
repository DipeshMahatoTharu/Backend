"""
============================================================
DAY 55 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Two-Phase Unit of Work & Transaction Coordinator

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a `UnitOfWork` transaction coordinator that manages a queue of database operations:
1. `register_operation(operation_fn, rollback_fn)`
2. `commit()`: Executes all operations in order.
   - If any operation raises an exception, automatically execute the corresponding `rollback_fn`
     for all previously succeeded operations in reverse order!
   - Re-raise the original exception.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Ensure clean rollback on partial failure.
- Return `True` on full success.

============================================================
MY APPROACH:
============================================================
1. Maintain list of registered `(op_fn, rollback_fn)`.
2. On `commit()`, execute each `op_fn` and push executed `rollback_fn` to a stack.
3. On exception, pop and execute rollbacks in reverse order.
"""
from typing import List, Tuple, Callable

class UnitOfWork:
    def __init__(self):
        self._operations: List[Tuple[Callable, Callable]] = []

    def register(self, op_fn: Callable, rollback_fn: Callable):
        self._operations.append((op_fn, rollback_fn))

    def commit(self) -> bool:
        executed_rollbacks: List[Callable] = []

        for op_fn, rollback_fn in self._operations:
            try:
                op_fn()
                executed_rollbacks.append(rollback_fn)
            except Exception as e:
                # Rollback previously succeeded operations in reverse
                for rb in reversed(executed_rollbacks):
                    try:
                        rb()
                    except Exception:
                        pass
                raise e

        self._operations.clear()
        return True


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    state = {"balance": 100, "inventory": 10}
    uow = UnitOfWork()

    # Step 1: Deduct balance
    def deduct_bal(): state["balance"] -= 30
    def restore_bal(): state["balance"] += 30

    # Step 2: Deduct inventory (fails!)
    def deduct_inv(): raise RuntimeError("Out of stock!")
    def restore_inv(): state["inventory"] += 1

    uow.register(deduct_bal, restore_bal)
    uow.register(deduct_inv, restore_inv)

    try:
        uow.commit()
        assert False, "Should raise RuntimeError"
    except RuntimeError:
        pass

    # Balance was rolled back from 70 back to 100!
    assert state["balance"] == 100
    assert state["inventory"] == 10

    print("Whiteboard Day 55 challenge passed successfully!")
