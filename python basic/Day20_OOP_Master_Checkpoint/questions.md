# Day 20 OOP Theory Questions

Please write your answers in the spaces provided below each question.

---

### 20.1 Instance vs Class Variables
**QUESTION:**
Explain the difference in storage and behavior between an instance variable and a class variable. What happens if you try to mutate a class variable through an instance (e.g. `self.class_var = new_val`) vs mutating it via the class name (e.g. `ClassName.class_var = new_val`)?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 20.2 Mutable Class Variable Trap
**QUESTION:**
What is the "Mutable Class Variable Problem" in Python? What happens if a class variable is initialized to a mutable object (like a list `[]` or dictionary `{}`), and multiple objects append elements to it?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 20.3 Encapsulation & The Underline Prefix
**QUESTION:**
Why does Python use a single leading underscore prefix (e.g. `self._age`)? Does it strictly prevent external code from accessing or modifying the variable? What is the difference between `_age` and `__age` (double underscore)?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 20.4 Property Getters and Setters
**QUESTION:**
When using the `@property` decorator, why must the actual internal variable name be different from the property method name (e.g. naming the property method `age` but storing the value in `_age`)? What error is triggered if they are named exactly the same?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 20.5 Inheritance & super()
**QUESTION:**
What does `super().__init__()` do inside a child class's constructor, and what happens if you forget to write it?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 20.6 Composition vs Inheritance
**QUESTION:**
Explain the difference between a "has-a" relationship (Composition) and an "is-a" relationship (Inheritance). Give an example of a system where using composition is cleaner than inheritance.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________
