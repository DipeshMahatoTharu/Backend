# Day 20 Mock OOP Interview Questions

Please answer these questions in the space provided to test your conceptual clarity.

---

### Interview Question 1: Encapsulation Trade-offs
**Question:**
Why should a class hide its internal attributes (like balance or password) using private prefixes? What could go wrong if a frontend developer directly mutates `account.balance = -100` instead of calling `account.withdraw(100)`?

**My Answer:**
____________________________________________________
____________________________________________________
____________________________________________________

**Follow-up:**
If Python's "privacy" is only name mangling and can still be bypassed, does encapsulation actually prevent bad modifications, or is it just a guideline? How does it help team collaboration?

**My Answer:**
____________________________________________________
____________________________________________________

---

### Interview Question 2: Object Relationships (Composition vs Inheritance)
**Question:**
Suppose you are designing an E-commerce system. You have a `User` class and a `ShoppingCart` class. Should `ShoppingCart` inherit from `User` (i.e., `class ShoppingCart(User)`), or should `User` have a `ShoppingCart` instance as an attribute (composition)? Explain why.

**My Answer:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### Interview Question 3: Multiple Inheritance Pitfalls
**Question:**
What is the "Diamond Problem" in multiple inheritance, and how does Python resolve it? (Hint: Mention Method Resolution Order or `MRO`).

**My Answer:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### Interview Question 4: Static Methods vs Class Methods
**Question:**
Explain when you would use `@staticmethod` versus `@classmethod`. What is the primary difference in the arguments they receive?

**My Answer:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### Interview Question 5: Object Collections Design
**Question:**
You need to write a system that manages thousands of student objects. If you need to look up a student record instantly using their `student_id`, would you store these students in a Python list (e.g. `[student1, student2]`) or a Python dictionary (e.g. `{"S001": student1}`)? Why? Compare their performance (Time Complexity) for lookups.

**My Answer:**
____________________________________________________
____________________________________________________
____________________________________________________
