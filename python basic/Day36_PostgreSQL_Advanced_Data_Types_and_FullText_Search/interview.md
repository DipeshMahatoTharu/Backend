# Day 36 — Real-World PostgreSQL Advanced Data Types & Search Interview Q&A

### Q1: When should you use `JSONB` in a PostgreSQL database instead of creating a normalized relational table?
**Answer:**
- **Use `JSONB` for**:
  1. **Heterogeneous E-Commerce Product Attributes**: When different products have hundreds of disjoint attributes (e.g. laptops have RAM/CPU, shoes have size/color, books have ISBN/pages).
  2. **Audit Trails & Event Sourcing Payloads**: Capturing arbitrary event snapshots or webhook payloads from Stripe/GitHub where the payload schema changes frequently.
  3. **Third-Party API Response Caching**: Storing external API responses without altering the schema on every upstream change.
- **Do NOT use `JSONB` for**:
  - Core transactional entities (Users, Accounts, Ledger entries, Orders).
  - Columns that require Foreign Key integrity constraints (PostgreSQL cannot enforce foreign keys inside JSON documents).
  - Columns frequently used in `JOIN` conditions or updated concurrently.

---

### Q2: What is the difference between GIN and B-Tree indexes, and why is GIN used for JSONB and Full-Text Search?
**Answer:**
- **B-Tree Index**: Stores single scalar values in a balanced tree. A row with value `"apple"` has one entry in the B-Tree pointing to that row's heap address.
- **GIN (Generalized Inverted Index)**: An "inverted" index stores internal components (lexemes, keys, elements).
  - If a `JSONB` row contains `{"tags": ["python", "django"], "role": "admin"}`, the GIN index breaks this down into separate index entries: `python`, `django`, `role:admin`.
  - Each entry maintains a list of Tuple IDs (`posting list`).
  - When querying for documents with `tags ? 'python'`, PostgreSQL directly looks up `python` in the GIN index in $O(1)$ and retrieves all matching row pointers instantly.

---

### Q3: How does PostgreSQL Full-Text Search work with `to_tsvector` and `to_tsquery`?
**Answer:**
1. **`to_tsvector('english', document_text)`**:
   Parses raw text into normalized tokens called **lexemes**:
   - Strips stop words (`the`, `a`, `is`, `with`).
   - Stems words to their dictionary root (`jumping`, `jumped`, `jumps` -> `jump`).
   - Records position offsets for relevance ranking.
2. **`to_tsquery('english', 'django & backend')`**:
   Parses search keywords into normalized query lexemes with boolean operators (`&` AND, `|` OR, `!` NOT).
3. **Matching (`@@` operator)**:
   `WHERE document_vector @@ to_tsquery('english', 'python & fast')`
   When backed by a GIN index on `document_vector`, PostgreSQL evaluates full-text search across millions of articles in under 2 milliseconds.

---

### Q4: How does Trigram similarity (`pg_trgm`) differ from tsvector Full-Text Search?
**Answer:**
- **`tsvector` (Full-Text Search)**: Word-based and linguistic. Relies on dictionary stemming. Cannot easily match misspelled words (e.g. searching "pythn" will NOT match "python" because "pythn" stems differently).
- **`pg_trgm` (Trigram Fuzzy Search)**: Substring-based and language-agnostic. Breaks strings into 3-character sequences (e.g. `"cat"` -> `"  c"`, `" ca"`, `"cat"`, `"at "`).
  - Supports fuzzy matching using the `%` (similarity) operator.
  - Accelerates arbitrary wildcard queries like `WHERE title LIKE '%sql%'` using GIN or GiST indexes, which standard B-Tree indexes cannot do.

---

### Q5: How do you use PostgreSQL's `JSONB` in Django models, and how do you query nested keys?
**Answer:**
Django natively supports PostgreSQL `JSONB` via `models.JSONField()`:
```python
class Product(models.Model):
    title = models.CharField(max_length=200)
    attributes = models.JSONField(default=dict)

# Querying nested JSON keys using double-underscore syntax:
laptops = Product.objects.filter(attributes__specs__ram_gb__gte=16)

# Querying array containment inside JSON:
apple_gear = Product.objects.filter(attributes__tags__contains=['apple'])
```
Django translates `attributes__specs__ram_gb` directly into PostgreSQL's `attributes #> '{specs,ram_gb}'` or `->>` operators!
