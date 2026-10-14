# Day 51 — Real-World Backend Engineering Interview

These questions test your mastery of automated API testing, CI/CD regression suites, and webhook debugging.

---

### Question 1: How Do You Test Webhooks Locally in Development?
**Interview Scenario:**
> *"You are building an integration with Stripe or GitHub Webhooks. When an event occurs, Stripe sends an HTTP POST to your webhook URL. How do you test this on `localhost:8000` before deploying to staging?"*

#### Senior Mentor Answer & Key Points:
1. **The Localhost NAT Problem**:
   - `http://localhost:8000` is private to your machine; external SaaS providers (Stripe/GitHub) cannot reach internal RFC 1918 private IP addresses across the public internet.
2. **Reverse Tunneling Tools (`ngrok` / Cloudflare Tunnels)**:
   - Run: `ngrok http 8000`.
   - Ngrok creates a public forwarding URL: `https://abc1234.ngrok-free.app` -> `localhost:8000`.
   - Paste the public URL into the Stripe Webhook Dashboard.
3. **Stripe CLI Alternative**:
   - Stripe provides a dedicated CLI: `stripe listen --forward-to localhost:8000/api/v1/webhooks/stripe/`.
   - It streams events over WebSockets and replays production webhooks locally with signature secrets.

---

### Question 2: Newman vs Pytest for Backend Regression Testing
**Interview Scenario:**
> *"Should backend teams maintain API test suites in Postman (Newman) or in Python (`pytest` with `requests` / `APITestCase`)?"*

#### Senior Mentor Answer & Key Points:
1. **The Senior Consensus**:
   - **`pytest` / Django `APITestCase` (Core Truth)**:
     - Versioned directly in Git alongside source code.
     - Can inspect internal database state, mock external services, and verify queries (`assertNumQueries`).
     - Executes rapidly in-process without spinning up full web servers.
   - **Postman / Newman (End-to-End & QA/Product Interface)**:
     - Excellent for non-engineering stakeholders, manual exploratory testing, and Blackbox smoke testing deployed staging environments.
