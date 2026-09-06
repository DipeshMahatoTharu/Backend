# Day 27 — SQL Fundamentals Conceptual Questions

Write your answers in the designated spaces below each question.

---

### 27.1 SQL Sublanguages: DDL, DML, DQL, TCL
**QUESTION:**
Explain the purpose of each SQL sublanguage and classify the following commands under their respective category:
`SELECT`, `CREATE TABLE`, `INSERT`, `ROLLBACK`, `DROP`, `UPDATE`, `COMMIT`, `ALTER`.

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 27.2 Primary Keys vs Unique Constraints
**QUESTION:**
What is the difference between a `PRIMARY KEY` and a `UNIQUE` constraint? Can a relational table have multiple Primary Keys? Can it have multiple Unique constraints? Can a Unique column contain `NULL` values?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 27.3 Referential Integrity & Deletion Actions
**QUESTION:**
Explain the behavior of each Foreign Key deletion rule when a parent record is deleted:
1. `ON DELETE CASCADE`
2. `ON DELETE SET NULL`
3. `ON DELETE RESTRICT` (or `NO ACTION`)
In an e-commerce database, which rule would you use when deleting a user account vs deleting a product that has previous orders?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 27.4 Data Types & Financial Precision
**QUESTION:**
Why is storing account balances or product prices in `FLOAT` or `DOUBLE` a dangerous anti-pattern in backend engineering? What data type should you always use for monetary values in PostgreSQL/MySQL, and how do precision and scale work?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 27.5 `CHAR` vs `VARCHAR` vs `TEXT`
**QUESTION:**
Compare `CHAR(n)`, `VARCHAR(n)`, and `TEXT`. Under what specific scenario is fixed-length `CHAR` preferred over variable-length `VARCHAR` (e.g. ISO 2-letter country codes or fixed hash strings)?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________