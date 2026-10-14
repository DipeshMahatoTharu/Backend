# Day 52 — Automated API Testing: `APITestCase`, Mocking & Fixtures

## 🎯 Learning Objectives
- Master DRF's testing framework: `APITestCase`, `APIClient`, and `force_authenticate()`.
- Structure deterministic test suites: `setUpTestData()` (class-level db setup) vs `setUp()` (per-test setup).
- Test status codes, JSON payload schemas, header invariants, and permission barriers.
- Master mocking external third-party APIs (Stripe, Twilio, SendGrid) using `unittest.mock.patch`.
- Measure test coverage using `coverage.py` (`coverage run manage.py test && coverage report`).

---

## 📚 Core Backend Concepts

### 1. `setUpTestData` vs `setUp` Performance
- **`setUpTestData(cls)`**: Executes once per TestCase class. Database state is created once and rolled back via transaction savepoints between tests. (10x faster!).
- **`setUp(self)`**: Executes before **every single test method**. Use only for setting up non-database objects (e.g. `self.client = APIClient()`).

### 2. Mocking Third-Party HTTP Calls
```python
from unittest.mock import patch
from rest_framework.test import APITestCase

class PaymentAPITests(APITestCase):
    @patch('my_app.services.stripe.Charge.create')
    def test_charge_success(self, mock_stripe_charge):
        # Configure mock return value
        mock_stripe_charge.return_value = {"id": "ch_123", "status": "succeeded"}

        response = self.client.post('/api/v1/checkout/', {'amount': 100})
        self.assertEqual(response.status_code, 200)
        # Verify mock was called with exact arguments
        mock_stripe_charge.assert_called_once_with(amount=100)
```

### 3. Testing Permission Gates
Always write 3 tests per protected endpoint:
1. Anonymous request -> `401 Unauthorized`.
2. Authenticated user without ownership/role -> `403 Forbidden`.
3. Authorized owner/admin -> `200 OK` / `204 No Content`.

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review `APITestCase`, mocking mechanics, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build mock runners and test clients in [`practice.py`](practice.py), and fix testing traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Full-Featured API Test Harness in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
