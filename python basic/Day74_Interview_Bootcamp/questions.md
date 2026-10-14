# Day 59 — 30-Question Senior Technical Interview Simulation

Write your comprehensive answers in the designated spaces below each question.

---

### Pillar 1: Python Internals & Concurrency
1. **Explain the Python Global Interpreter Lock (GIL). Why does CPU-bound multithreading in Python not achieve true parallel speedups across multiple cores, and how does `multiprocessing` solve this?**
   *Answer:* __________________________________________________

2. **How does Python's Garbage Collection work? Explain reference counting and the generational cyclic garbage collector.**
   *Answer:* __________________________________________________

3. **What is the difference between a Python Generator and a List comprehension in terms of memory complexity?**
   *Answer:* __________________________________________________

4. **How do Python decorators wrap functions? What does `functools.wraps` preserve?**
   *Answer:* __________________________________________________

---

### Pillar 2: SQL & Database Optimization
5. **How does a database B-Tree index work? Why does querying with a leading wildcard (`LIKE '%test'`) bypass the index?**
   *Answer:* __________________________________________________

6. **Explain the four ACID transaction properties and the difference between Read Committed and Serializable isolation levels.**
   *Answer:* __________________________________________________

7. **What is a database Deadlock? How do you prevent deadlocks when multiple transactions update the same set of rows?**
   *Answer:* __________________________________________________

8. **Compare `select_related()` vs `prefetch_related()` in Django ORM.**
   *Answer:* __________________________________________________

---

### Pillar 3: Django & DRF Architecture
9. **Explain the lifecycle of a Django HTTP request from Nginx to WSGI, Middleware, View, and HttpResponse.**
   *Answer:* __________________________________________________

10. **Why are `F()` expressions critical when updating numerical fields in high-concurrency environments?**
    *Answer:* __________________________________________________

11. **Explain the DRF Serializer validation lifecycle (`to_internal_value`, `validate_<field>`, and `validate`).**
    *Answer:* __________________________________________________

12. **How does stateless JWT authentication differ from session cookie authentication?**
    *Answer:* __________________________________________________

---

### Pillar 4: Distributed Systems & Scalability
13. **What is a Cache Stampede (Thundering Herd)? How does distributed locking mitigate it?**
    *Answer:* __________________________________________________

14. **Why must background task dispatching (`send_email.delay()`) be wrapped in `transaction.on_commit()`?**
    *Answer:* __________________________________________________

15. **How do multi-stage Docker builds optimize image size and security?**
    *Answer:* __________________________________________________
