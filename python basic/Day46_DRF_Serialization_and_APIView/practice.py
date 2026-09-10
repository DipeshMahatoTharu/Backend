"""
Day 46: DRF Serialization & APIView — Practice
Hands-on exercises covering field validation, deserialization, and APIView dispatching.
"""
from typing import Dict, Any, Optional, List

class ValidationError(Exception):
    def __init__(self, detail: Any):
        self.detail = detail
        super().__init__(str(detail))

# ---------------------------------------------------------------------
# Task 1: Field Validator Simulator
# ---------------------------------------------------------------------
def validate_product_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates product data:
    - 'title': required, min 3 characters.
    - 'price': required, float/int > 0.
    - 'sku': required, must start with 'SKU-'.
    """
    errors = {}
    title = data.get("title")
    if not title or len(str(title).strip()) < 3:
        errors["title"] = "Title must be at least 3 characters long."

    price = data.get("price")
    if price is None or not isinstance(price, (int, float)) or price <= 0:
        errors["price"] = "Price must be a positive number."

    sku = data.get("sku")
    if not sku or not str(sku).startswith("SKU-"):
        errors["sku"] = "SKU must start with 'SKU-' prefix."

    if errors:
        raise ValidationError(errors)

    return {
        "title": str(title).strip(),
        "price": float(price),
        "sku": str(sku).strip().upper()
    }


# ---------------------------------------------------------------------
# Task 2: Mock APIView Dispatcher
# ---------------------------------------------------------------------
class MockResponse:
    def __init__(self, data: Any, status: int = 200):
        self.data = data
        self.status = status

class BaseAPIView:
    def dispatch(self, method: str, request_data: Optional[Dict[str, Any]] = None) -> MockResponse:
        handler = getattr(self, method.lower(), None)
        if not handler:
            return MockResponse({"detail": "Method not allowed"}, status=405)
        try:
            return handler(request_data)
        except ValidationError as ve:
            return MockResponse(ve.detail, status=400)


class ProductAPIView(BaseAPIView):
    def __init__(self):
        self._db = []

    def get(self, request_data=None):
        return MockResponse(self._db, status=200)

    def post(self, request_data):
        validated = validate_product_payload(request_data or {})
        self._db.append(validated)
        return MockResponse(validated, status=201)


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 46 Practice Tests ---")

    # Test Task 1: Validation
    valid_p = {"title": "Mechanical Keyboard", "price": 120.0, "sku": "SKU-KEY-01"}
    assert validate_product_payload(valid_p)["sku"] == "SKU-KEY-01"

    try:
        validate_product_payload({"title": "Hi", "price": -5, "sku": "BAD"})
        assert False, "Should raise ValidationError"
    except ValidationError as e:
        assert "title" in e.detail and "price" in e.detail and "sku" in e.detail

    # Test Task 2: APIView dispatch
    view = ProductAPIView()
    res_get = view.dispatch("GET")
    assert res_get.status == 200 and len(res_get.data) == 0

    res_post = view.dispatch("POST", valid_p)
    assert res_post.status == 201
    assert res_post.data["title"] == "Mechanical Keyboard"

    res_bad = view.dispatch("POST", {})
    assert res_bad.status == 400

    print("All Day 46 practice assertions passed successfully!")
