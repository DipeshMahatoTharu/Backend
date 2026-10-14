# Day 36 — PostgreSQL Advanced Data Types & Full-Text Search

## 🎯 Learning Objectives
- Master PostgreSQL's hybrid relational/NoSQL power: **`JSONB` vs `JSON`**.
- Query and index semi-structured JSON documents using **GIN (Generalized Inverted Index)**.
- Work with native PostgreSQL **Array Types** (`TEXT[]`, `INTEGER[]`) and array operators (`@>`, `&&`).
- Implement cryptographic **UUID Primary Keys** with `gen_random_uuid()` vs sequential integers.
- Build high-speed **Full-Text Search** engines using `to_tsvector`, `to_tsquery`, and Trigram similarity (`pg_trgm`).
- Integrate advanced PostgreSQL fields directly into Django models (`JSONField`, `ArrayField`).

---

## 📚 Core Backend Concepts

### 1. `JSONB` vs `JSON` in PostgreSQL
PostgreSQL supports two formats for JSON data:
- **`JSON` (Plain Text)**: Stores exact textual representation including whitespace and duplicate keys. Requires re-parsing the JSON string on every single query. Cannot be indexed efficiently.
- **`JSONB` (Decomposed Binary)**: Parses JSON on ingestion into a decomposed binary format. Strips duplicate keys and insignificant whitespace.
  - **Key Advantage**: Supports lightning-fast indexing via **GIN (Generalized Inverted Index)**!
  - **Django ORM Mapping**: `models.JSONField()` defaults to `JSONB` in PostgreSQL!

### 2. GIN Indexing for JSONB
```sql
CREATE TABLE audit_events (
    id SERIAL PRIMARY KEY,
    event_type TEXT NOT NULL,
    payload JSONB NOT NULL
);

-- Create GIN index on entire JSONB document:
CREATE INDEX idx_audit_payload ON audit_events USING gin (payload);

-- Superfast query matching any key/value pair:
SELECT * FROM audit_events WHERE payload @> '{"user": {"role": "ADMIN"}}';
```

### 3. Full-Text Search vs `LIKE '%keyword%'`
- Running `WHERE title LIKE '%python%'` cannot use standard B-Tree indexes because of the leading wildcard `%`. It forces a $100\%$ Sequential Scan!
- **PostgreSQL Full-Text Search Engine**:
  - `to_tsvector('english', document)` parses text, removes stop words ("the", "is", "at"), and stems words to their root form ("running", "runs" -> "run").
  - `to_tsquery('english', 'python & backend')` compiles the search phrase.
  - Accelerated via GIN indexes for sub-millisecond searches across millions of documents.

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + DATA TYPE DRILLS (60 min)**:
  - 40 min: Study JSONB decomposition, GIN indexes, Arrays, and tsvector lexemes.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/questions.md)**.

- **HOUR 2 — JSONB & SEARCH PRACTICE (60 min)**:
  - 35 min: Implement JSON querying and indexing benchmarks in **[`practice.py`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/practice.py)**.
  - 25 min: Fix JSON injection and invalid GIN query operators in **[`debugging.py`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/debugging.py)**.

- **HOUR 3 — FULL-TEXT SEARCH WHITEBOARD & CHALLENGE (60 min)**:
  - 20 min: Study Advanced PostgreSQL interview questions in **[`interview.md`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/interview.md)**.
  - 20 min: Design the blank-page Full-Text Search Engine on **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/whiteboard.py)**.
  - 20 min: Build the E-Commerce Flexible Product Catalog in **[`challenge.py`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Studied JSONB and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/questions.md)**
- [ ] Profiled JSONB lookups and GIN indexes in **[`practice.py`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/practice.py)**
- [ ] Fixed JSON query bugs in **[`debugging.py`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/debugging.py)**
- [ ] Solved Full-Text Search challenge on **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/whiteboard.py)**
- [ ] Passed flexible catalog tests in **[`challenge.py`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/challenge.py)**
- [ ] Mastered Advanced PostgreSQL interview answers in **[`interview.md`](file:///d:/Backend/python%20basic/Day36_PostgreSQL_Advanced_Data_Types_and_FullText_Search/interview.md)**
