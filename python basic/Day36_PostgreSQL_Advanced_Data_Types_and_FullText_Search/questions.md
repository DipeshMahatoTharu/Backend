# Day 36 — Advanced PostgreSQL Data Types & Search Questions

Please answer each question thoroughly in the spaces provided below.

---

### 36.1 `JSON` vs `JSONB` Internal Storage & Indexing
**QUESTION:**
Explain the internal architectural differences between `JSON` and `JSONB` in PostgreSQL. Why does `JSONB` have slightly higher write ingestion overhead, but exponentially faster read and indexing performance?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 36.2 GIN (Generalized Inverted Index) Mechanics
**QUESTION:**
How does a GIN index differ from a standard B-Tree index? When you index a `JSONB` column or an `Array` column with a GIN index, what are the keys stored in the index structure?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 36.3 PostgreSQL Array Types vs Junction Tables
**QUESTION:**
When is storing data as a PostgreSQL native Array (e.g. `tags TEXT[]`) appropriate versus creating a fully normalized Many-to-Many junction table? What are the trade-offs in relational integrity, indexability, and foreign key enforcement?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 36.4 Full-Text Search vs `LIKE '%term%'`
**QUESTION:**
1. Why does `LIKE '%search%'` scale terribly on large datasets ($O(N)$ sequential scan)?
2. What are the two essential steps performed by PostgreSQL's `to_tsvector` (parsing and stemming), and how does `to_tsquery` match against it?

**MY ANSWER:**
____________________________________________________
____________________________________________________

---

### 36.5 Trigram Indexes (`pg_trgm`) & Fuzzy Matching
**QUESTION:**
What is a trigram, and how does the PostgreSQL `pg_trgm` extension enable accelerated indexing for arbitrary wildcard searches (`LIKE '%word%'`) and fuzzy typo tolerance (e.g. searching for "pythn" and matching "python")?

**MY ANSWER:**
____________________________________________________
____________________________________________________
