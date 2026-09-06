# Day 20 Mock OOP Interview Questions

Please answer these questions in the space provided to test your conceptual clarity.

---

### Interview Question 1: Encapsulation Trade-offs
**Question:**
Why should a class hide its internal attributes (like balance or password) using private prefixes? What could go wrong if a developer directly mutates `account.balance = -100` instead of calling `account.withdraw(100)`?

**My Answer:**
____________________________________________________
____________________________________________________

**Follow-up:**
How do getter and setter properties help prevent this issue?

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

---

### Interview Question 3: Multiple Inheritance
**Question:**
What are the potential drawbacks of using multiple inheritance in a production codebase? When would you prefer composition instead?

**My Answer:**
____________________________________________________
____________________________________________________

---

### Interview Question 4: Static Methods vs Class Methods
**Question:**
Explain when you would use `@staticmethod` versus `@classmethod`. What is the primary difference in the arguments they receive?

**My Answer:**
____________________________________________________
____________________________________________________

---

### Interview Question 5: Custom Exceptions
**Question:**
Why should a backend application define custom exception classes (e.g. `class InsufficientFundsError(Exception)`) rather than raising a generic `ValueError` or `Exception`?

**My Answer:**
____________________________________________________
____________________________________________________
____________________________________________________
