# Day 51 — API Testing via Postman, Environments & cURL

## 🎯 Learning Objectives
- Master the `curl` CLI for manual API debugging, header inspection, and payload testing.
- Understand core curl flags: `-X`, `-H`, `-d`, `-i` (print headers), `-s` (silent), `--fail-with-body`.
- Build and structure Postman collections: folders, environment variables (`{{base_url}}`, `{{token}}`).
- Write automated Postman test scripts (`pm.test()`, `pm.response.to.have.status(200)`).
- Automate token management using Postman Pre-request scripts to auto-refresh expired JWTs.

---

## 📚 Core Backend Concepts

### 1. Essential cURL Commands for Backend Engineers
```bash
# 1. GET with Bearer Auth and Response Headers
curl -i -X GET https://api.example.com/api/v1/users/ \
     -H "Authorization: Bearer <token>"

# 2. POST with JSON Payload
curl -X POST https://api.example.com/api/v1/orders/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <token>" \
     -d '{"product_id": 42, "quantity": 2}'

# 3. File Upload via Multipart Form Data
curl -X POST https://api.example.com/api/v1/avatar/ \
     -H "Authorization: Bearer <token>" \
     -F "image=@/path/to/profile.png"
```

### 2. Postman Pre-Request & Test Script Life Cycle
1. **Pre-request Script**: Executes before HTTP request (e.g. check if JWT token is expired; if so, fetch fresh token and update `pm.environment.set('token', new_token)`).
2. **HTTP Execution**: Request transmitted with headers and body.
3. **Tests Script**: Executes on response:
   ```javascript
   pm.test("Status code is 201 Created", function () {
       pm.response.to.have.status(201);
   });
   pm.test("Response contains order id", function () {
       var jsonData = pm.response.json();
       pm.expect(jsonData.id).to.be.a('number');
   });
   ```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review curl syntax, Postman environments, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build curl generators and test script runners in [`practice.py`](practice.py), and fix API testing traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Automated Collection Test Runner in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
