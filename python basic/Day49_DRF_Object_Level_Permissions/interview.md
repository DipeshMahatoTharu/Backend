# Day 49 — Real-World Backend Engineering Interview

These questions test your mastery of authorization architectures, object permissions, and multi-tenant security.

---

### Question 1: Why Does `has_object_permission` Fail Silently If You Forget `self.get_object()`?
**Interview Scenario:**
> *"An engineer writes a custom `IsOwner` permission class and adds it to an `APIView`. In the `get(request, pk)` method, they write `invoice = Invoice.objects.get(pk=pk)` and return it. Why did the permission check not execute at all?"*

#### Senior Mentor Answer & Key Points:
1. **The DRF Permission Architecture**:
   - DRF's initial request handler automatically calls `self.check_permissions(request)`. This runs **only** `has_permission()`!
   - `has_object_permission()` is **only** executed when `self.check_object_permissions(request, obj)` is called.
   - In standard Generic Views / ViewSets, `self.get_object()` calls `check_object_permissions` automatically.
   - In raw `APIView`, querying `Invoice.objects.get(pk=pk)` bypasses `self.get_object()`, completely skipping `has_object_permission`!
2. **The Senior Fix**:
   - In raw `APIView`, either explicitly call `self.check_object_permissions(request, invoice)` or subclass `RetrieveAPIView`.

---

### Question 2: View-Level Filtering vs Object-Level Permissions in Multi-Tenant APIs
**Interview Scenario:**
> *"Why should you never rely solely on `has_object_permission` for multi-tenant data isolation?"*

#### Senior Mentor Answer & Key Points:
1. **The Difference in Query Execution**:
   - `has_object_permission` runs **after** the database query retrieves the object.
   - If you have a collection endpoint (`GET /api/v1/invoices/`), `has_object_permission` is never called! If `get_queryset()` does not filter by tenant, all tenants' data is returned in the list response!
2. **Defense in Depth**:
   - Always filter at the database level first via `get_queryset()`:
     ```python
     def get_queryset(self):
         return self.queryset.filter(organization=self.request.user.organization)
     ```
   - Use `has_object_permission` as a secondary security gate for granular individual actions (e.g. read-only vs edit).
