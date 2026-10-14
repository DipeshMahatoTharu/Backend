# Day 46 — Real-World Backend Engineering Interview

These questions test your understanding of REST API serialization, validation pipelines, and performance.

---

### Question 1: How Does DRF's Validation Lifecycle Work Behind the Scenes?
**Interview Scenario:**
> *"When `serializer.is_valid()` is called on an incoming JSON request, what exact sequence of methods does DRF execute? Where does field validation happen vs cross-field validation?"*

#### Senior Mentor Answer & Key Points:
1. **The 4-Step Validation Pipeline**:
   - **Step 1 (Base Field Type Conversion)**:
     - Each field's `to_internal_value(raw_data)` converts JSON primitives (e.g. ISO string `"2026-09-09"`) to Python types (`datetime.date`).
   - **Step 2 (Built-in Field Validators)**:
     - Executes field-level validators (`validators=[...]`, `max_length`, `MinValueValidator`).
   - **Step 3 (Custom Field Cleaners)**:
     - Looks for `validate_<fieldname>(self, value)` on the Serializer class.
   - **Step 4 (Object-Level Cross-Field Clean)**:
     - Executes `validate(self, attrs)`. This is where dependencies across fields (e.g. `start_date < end_date`) are evaluated.
2. **Result**:
   - If any step raises `serializers.ValidationError`, the error is captured in `serializer.errors`.
   - If all steps pass, validated and type-cast data is populated into `serializer.validated_data`.

---

### Question 2: Why Nested Serializers Can Cause Severe Performance Degradation (N+1)
**Interview Scenario:**
> *"You create an `AuthorSerializer` that nests `books = BookSerializer(many=True)`. When listing 50 authors, latency jumps to 2,000ms. Why did this happen and how do you fix it?"*

#### Senior Mentor Answer & Key Points:
1. **The Root Cause**:
   - For every author in the list, the nested `BookSerializer` accesses `author.books.all()`.
   - Without prefetching, this triggers 50 separate SQL queries to the `books` table ($1 + 50 = 51$ queries).
2. **The Fix**:
   - In the API view, always prefetch the nested relationship before passing the QuerySet to the serializer:
     ```python
     authors = Author.objects.prefetch_related('books').all()
     serializer = AuthorSerializer(authors, many=True)
     ```
   - This collapses the 51 database queries down to **exactly 2 queries**.
