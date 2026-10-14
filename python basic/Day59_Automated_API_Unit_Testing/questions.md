# Day 52 — Automated API Unit Testing Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 52.1 `setUpTestData` vs `setUp` Internals
**QUESTION:**
Why does Django run test methods inside database transaction savepoints? Why will mutating an object modified in `setUpTestData` contaminate subsequent test cases?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 52.2 Where to Patch (Mocking Import Trap)
**QUESTION:**
Explain the classic Python mocking trap: *"Mock where the object is used, not where it is defined"*. Why does `@patch('stripe.Charge.create')` fail if your view wrote `from stripe import Charge`?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 52.3 Unit Tests vs End-to-End Integration Tests
**QUESTION:**
What is the difference between testing with `rest_framework.test.APIClient` versus testing against a running live server with `LiveServerTestCase` and Selenium? What are the execution speed trade-offs?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
