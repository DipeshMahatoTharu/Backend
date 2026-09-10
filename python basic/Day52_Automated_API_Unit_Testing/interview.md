# Day 52 — Real-World Backend Engineering Interview

These questions test your understanding of automated testing strategy, mock boundaries, and CI test performance.

---

### Question 1: How Do You Test Third-Party Payment Webhooks in Django Tests?
**Interview Scenario:**
> *"When a Stripe charge completes, Stripe posts to `/api/v1/stripe/webhook/`. The view verifies Stripe's cryptographic signature header `Stripe-Signature`. How do you write a unit test for this without calling real Stripe servers or failing signature checks?"*

#### Senior Mentor Answer & Key Points:
1. **The Architecture of Webhook Testing**:
   - The view uses `stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)`.
2. **Mocking at the SDK Boundary**:
   - Use `@patch('stripe.Webhook.construct_event')`:
     ```python
     @patch('stripe.Webhook.construct_event')
     def test_webhook_successful_payment(self, mock_construct):
         mock_construct.return_value = {
             "type": "payment_intent.succeeded",
             "data": {"object": {"id": "pi_123", "amount": 5000}}
         }
         response = self.client.post(
             '/api/v1/stripe/webhook/',
             data=json.dumps({"dummy": "payload"}),
             content_type="application/json",
             HTTP_STRIPE_SIGNATURE="fake_sig"
         )
         self.assertEqual(response.status_code, 200)
     ```
   - This tests your view's business logic (updating user subscriptions, creating receipts) in isolation without depending on external network connections.

---

### Question 2: Why Database Transaction Rollback is Essential for Fast Unit Tests
**Interview Scenario:**
> *"Why does Django's `TestCase` wrap every test in a database transaction and roll it back, instead of dropping and recreating the database tables?"*

#### Senior Mentor Answer & Key Points:
1. **The Cost of DDL Operations**:
   - Dropping and recreating tables (`CREATE TABLE`, creating indexes, foreign key constraints) takes seconds per test. A suite of 1,000 tests would take hours!
2. **The Atomic Savepoint Solution**:
   - Django starts a database transaction at the beginning of each test method.
   - Any rows inserted or updated during the test exist only within that transaction.
   - When the test completes (pass or fail), Django issues an immediate `ROLLBACK`.
   - The database returns to its clean baseline state in single-digit milliseconds without any disk I/O.
