"""
Day 55 Daily Challenge: Banking Funds Transfer Service Layer with Atomic Transactions

Problem:
Implement an enterprise-grade Banking Service Layer:
1. `AccountRepository`: Encapsulates database read/write for Account balances.
2. `TransferFundsDTO`: Immutable data transfer object specifying `from_account`, `to_account`, and `amount`.
3. `TransferService`:
   - Validates balance sufficiency.
   - Enforces atomic transaction rollback on failure.
   - Triggers `on_commit` notification queue only when transfer succeeds.
   - Prevents negative transfers and self-transfers.
"""
from dataclasses import dataclass
from typing import Dict, Any, List, Optional, Callable

@dataclass(frozen=True)
class TransferFundsDTO:
    from_account_id: int
    to_account_id: int
    amount: float

    def __post_init__(self):
        if self.from_account_id == self.to_account_id:
            raise ValueError("Cannot transfer funds to the same account.")
        if self.amount <= 0:
            raise ValueError("Transfer amount must be positive.")


class AccountRepository:
    def __init__(self):
        self._db: Dict[int, Dict[str, Any]] = {
            1: {"id": 1, "owner": "Alice", "balance": 500.0},
            2: {"id": 2, "owner": "Bob", "balance": 100.0}
        }

    def get_account(self, account_id: int) -> Optional[Dict[str, Any]]:
        return self._db.get(account_id)

    def update_balance(self, account_id: int, new_balance: float):
        self._db[account_id]["balance"] = round(new_balance, 2)


class TransferService:
    def __init__(self, repo: AccountRepository):
        self.repo = repo
        self.notifications_sent: List[str] = []

    def execute_transfer(self, dto: TransferFundsDTO) -> Dict[str, Any]:
        from_acc = self.repo.get_account(dto.from_account_id)
        to_acc = self.repo.get_account(dto.to_account_id)

        if not from_acc: raise ValueError(f"Sender account #{dto.from_account_id} not found.")
        if not to_acc: raise ValueError(f"Recipient account #{dto.to_account_id} not found.")

        # Balance check
        if from_acc["balance"] < dto.amount:
            raise ValueError("Insufficient funds for transfer.")

        # Simulate Atomic Transaction
        initial_from_bal = from_acc["balance"]
        initial_to_bal = to_acc["balance"]

        try:
            self.repo.update_balance(dto.from_account_id, initial_from_bal - dto.amount)
            self.repo.update_balance(dto.to_account_id, initial_to_bal + dto.amount)
            # on_commit action
            self.notifications_sent.append(f"Transfer of ${dto.amount} from #{dto.from_account_id} to #{dto.to_account_id} completed.")
            return {"status": "SUCCESS", "from_balance": from_acc["balance"], "to_balance": to_acc["balance"]}
        except Exception as e:
            # Rollback
            self.repo.update_balance(dto.from_account_id, initial_from_bal)
            self.repo.update_balance(dto.to_account_id, initial_to_bal)
            raise e


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    repo = AccountRepository()
    service = TransferService(repo)

    # 1. Successful transfer ($150 from Alice to Bob)
    dto = TransferFundsDTO(from_account_id=1, to_account_id=2, amount=150.0)
    res = service.execute_transfer(dto)
    assert res["status"] == "SUCCESS"
    assert repo.get_account(1)["balance"] == 350.0
    assert repo.get_account(2)["balance"] == 250.0
    assert len(service.notifications_sent) == 1

    # 2. Insufficient Funds transfer ($1000 from Alice)
    try:
        dto_fail = TransferFundsDTO(from_account_id=1, to_account_id=2, amount=1000.0)
        service.execute_transfer(dto_fail)
        assert False, "Should raise ValueError on insufficient funds"
    except ValueError as ve:
        assert "Insufficient funds" in str(ve)

    # Verify balances were NOT changed after failure
    assert repo.get_account(1)["balance"] == 350.0
    assert repo.get_account(2)["balance"] == 250.0

    # 3. Self-transfer validation error
    try:
        TransferFundsDTO(from_account_id=1, to_account_id=1, amount=50.0)
        assert False, "Should raise ValueError on self-transfer"
    except ValueError:
        pass

    print("All TransferService challenge tests passed successfully!")
