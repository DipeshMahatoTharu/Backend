"""
Day 52 Daily Challenge: Full-Featured API Test Harness with Mocking & Assertions

Problem:
Implement a standalone test runner that tests an E-Commerce Order API:
1. Test Unauthenticated access (expect 401).
2. Test Invalid Payload (missing fields, expect 400).
3. Test Successful Checkout with Mocked Payment Gateway (expect 201).
4. Verify mock payment gateway was called with exact currency and amount.
5. Verify test runner captures test results and passes all assertions.
"""
from typing import Dict, Any, Optional
from unittest.mock import MagicMock

# The System Under Test (SUT)
class PaymentGatewayClient:
    def charge(self, amount: int, currency: str) -> Dict[str, Any]:
        raise RuntimeError("Network unavailable in tests!")

class OrderService:
    def __init__(self, payment_client: PaymentGatewayClient):
        self.payment_client = payment_client

    def checkout(self, user: Optional[Dict[str, Any]], order_data: Dict[str, Any]) -> Dict[str, Any]:
        if not user:
            return {"status": 401, "body": {"error": "Authentication required"}}

        amount = order_data.get("amount")
        if not amount or amount <= 0:
            return {"status": 400, "body": {"error": "Invalid amount"}}

        # Charge via payment gateway
        try:
            charge_res = self.payment_client.charge(amount=amount, currency="USD")
            return {
                "status": 201,
                "body": {"order_id": 999, "status": "PAID", "charge_id": charge_res["id"]}
            }
        except Exception as e:
            return {"status": 502, "body": {"error": "Payment processing failed"}}


# ---------------------------------------------------------------------
# Test Suite Implementation
# ---------------------------------------------------------------------
class OrderServiceTestCase:
    def setUp(self):
        self.mock_gateway = MagicMock(spec=PaymentGatewayClient)
        self.service = OrderService(self.mock_gateway)
        self.user = {"id": 1, "username": "dipesh"}

    def test_checkout_unauthenticated(self):
        res = self.service.checkout(None, {"amount": 100})
        assert res["status"] == 401

    def test_checkout_invalid_payload(self):
        res = self.service.checkout(self.user, {"amount": -10})
        assert res["status"] == 400

    def test_checkout_success(self):
        # Configure Mock
        self.mock_gateway.charge.return_value = {"id": "ch_stripe_123", "status": "succeeded"}

        res = self.service.checkout(self.user, {"amount": 250})
        assert res["status"] == 201
        assert res["body"]["status"] == "PAID"
        assert res["body"]["charge_id"] == "ch_stripe_123"

        # Verify Mock Call
        self.mock_gateway.charge.assert_called_once_with(amount=250, currency="USD")


# ---------------------------------------------------------------------
# Test Runner
# ---------------------------------------------------------------------
if __name__ == "__main__":
    suite = OrderServiceTestCase()
    suite.setUp()
    suite.test_checkout_unauthenticated()

    suite.setUp()
    suite.test_checkout_invalid_payload()

    suite.setUp()
    suite.test_checkout_success()

    print("All OrderServiceTestCase unit tests passed successfully!")
