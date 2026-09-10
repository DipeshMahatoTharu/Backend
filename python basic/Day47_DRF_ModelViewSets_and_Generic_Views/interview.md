# Day 47 — Real-World Backend Engineering Interview

These questions test your mastery of DRF view architectures, routing mechanics, and API design trade-offs.

---

### Question 1: When is `ModelViewSet` an Anti-Pattern?
**Interview Scenario:**
> *"Junior engineers love `ModelViewSet` because 4 lines of code generate a complete CRUD API. When does a Senior Backend Engineer explicitly reject `ModelViewSet`?"*

#### Senior Mentor Answer & Key Points:
1. **The Over-Exposed API Hazard**:
   - `ModelViewSet` exposes `DELETE`, `PUT`, `PATCH`, `POST`, and `GET` by default.
   - For sensitive domain models (e.g. `PaymentTransaction`, `AuditLog`, `SubscriptionInvoice`), deleting or arbitrary updating should **never** be exposed over an API. Exposing them by default violates the principle of least privilege.
2. **Domain-Driven Design (DDD) & Non-CRUD Actions**:
   - Business operations like `approve_loan()`, `refund_charge()`, or `rebalance_portfolio()` are workflows, not generic model field updates.
   - For non-CRUD business actions, clean `APIView` endpoints (or custom service layer methods) prevent leaky database abstractions.

---

### Question 2: How Do You Use Different Serializers for Different ViewSet Actions?
**Interview Scenario:**
> *"When listing 10,000 products (`list`), you only want basic fields (`id`, `title`, `price`). When viewing one product (`retrieve`), you want heavy nested fields (`reviews`, `inventory`, `vendor_details`). How do you achieve this in a single ViewSet?"*

#### Senior Mentor Answer & Key Points:
1. **Override `get_serializer_class(self)`**:
   - DRF provides a hook to dynamically switch serializers based on the current action:
     ```python
     class ProductViewSet(viewsets.ModelViewSet):
         queryset = Product.objects.all()

         def get_serializer_class(self):
             if self.action == 'list':
                 return ProductListSummarySerializer
             elif self.action == 'retrieve':
                 return ProductDetailComplexSerializer
             return ProductCreateUpdateSerializer
     ```
2. **Performance Impact**:
   - This prevents over-fetching on high-volume listing endpoints while preserving rich data schemas for single-item views.
