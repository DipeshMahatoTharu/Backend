"""
Day 52: Automated API Unit Testing — Practice
Hands-on exercises covering mock objects, call assertions, and API client simulation.
"""
from typing import Dict, Any, List, Optional
from unittest.mock import MagicMock

# ---------------------------------------------------------------------
# Task 1: Mock Gateway Verification
# ---------------------------------------------------------------------
class ExternalPaymentGateway:
    def process_charge(self, card_token: str, amount: float) -> Dict[str, Any]:
        raise NotImplementedError("Real network call to payment processor")

def charge_customer_order(gateway: ExternalPaymentGateway, card_token: str, amount: float) -> bool:
    res = gateway.process_charge(card_token, amount)
    return res.get("status") == "success"


# ---------------------------------------------------------------------
# Task 2: Mock API Client Simulator
# ---------------------------------------------------------------------
class MockAPIClient:
    def __init__(self):
        self._auth_user: Optional[Dict[str, Any]] = None

    def force_authenticate(self, user: Optional[Dict[str, Any]]):
        self._auth_user = user

    def post(self, url: str, data: Dict[str, Any]) -> Dict[str, Any]:
        if not self._auth_user:
            return {"status_code": 401, "data": {"detail": "Authentication required"}}
        if url == "/api/v1/orders/" and data.get("amount", 0) > 0:
            return {"status_code": 201, "data": {"id": 101, "user": self._auth_user["id"], "amount": data["amount"]}}
        return {"status_code": 400, "data": {"detail": "Invalid amount"}}


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 52 Practice Tests ---")

    # Test Task 1: Mocking Gateway
    mock_gw = MagicMock(spec=ExternalPaymentGateway)
    mock_gw.process_charge.return_value = {"status": "success", "tx_id": "tx_999"}

    success = charge_customer_order(mock_gw, "tok_visa", 49.99)
    assert success is True
    mock_gw.process_charge.assert_called_once_with("tok_visa", 49.99)

    # Test Task 2: Client Auth gates
    client = MockAPIClient()

    # 1. Anon -> 401
    resp_anon = client.post("/api/v1/orders/", {"amount": 50})
    assert resp_anon["status_code"] == 401

    # 2. Authenticated -> 201
    client.force_authenticate({"id": 10, "username": "dipesh"})
    resp_auth = client.post("/api/v1/orders/", {"amount": 50})
    assert resp_auth["status_code"] == 201
    assert resp_auth["data"]["user"] == 10

    print("All Day 52 practice assertions passed successfully!")
