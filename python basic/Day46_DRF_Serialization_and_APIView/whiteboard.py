"""
============================================================
DAY 46 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Schema Validator & Nested Serializer Deserializer

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a nested deserializer function:
`validate_order_payload(data: dict) -> dict`
that validates an Order with nested OrderItems:
Order schema:
- `customer_id`: int > 0
- `items`: list of dicts, must contain at least 1 item
Item schema:
- `product_id`: int > 0
- `quantity`: int > 0
- `unit_price`: float/int >= 0.0

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Return a dictionary with field-specific errors if validation fails.
- Calculate and inject `total_amount` in the returned validated order dict.

============================================================
MY APPROACH:
============================================================
1. Validate top-level `customer_id` and `items` list presence.
2. Validate each item in `items`, tracking nested index errors.
3. Compute total price: sum(quantity * unit_price).
4. If errors exist, raise `ValueError(errors)`.
"""
from typing import Dict, Any, List

def validate_order_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    errors: Dict[str, Any] = {}

    cust_id = data.get("customer_id")
    if not isinstance(cust_id, int) or cust_id <= 0:
        errors["customer_id"] = "Must be a positive integer."

    items = data.get("items")
    if not isinstance(items, list) or len(items) == 0:
        errors["items"] = "At least one item is required."
        raise ValueError(errors)

    validated_items = []
    item_errors = []
    total = 0.0

    for idx, item in enumerate(items):
        i_err = {}
        pid = item.get("product_id")
        qty = item.get("quantity")
        price = item.get("unit_price")

        if not isinstance(pid, int) or pid <= 0:
            i_err["product_id"] = "Invalid product ID."
        if not isinstance(qty, int) or qty <= 0:
            i_err["quantity"] = "Quantity must be > 0."
        if not isinstance(price, (int, float)) or price < 0:
            i_err["unit_price"] = "Price must be >= 0."

        if i_err:
            item_errors.append({"index": idx, "errors": i_err})
        else:
            total += qty * float(price)
            validated_items.append({"product_id": pid, "quantity": qty, "unit_price": float(price)})

    if item_errors:
        errors["item_errors"] = item_errors

    if errors:
        raise ValueError(errors)

    return {
        "customer_id": cust_id,
        "items": validated_items,
        "total_amount": round(total, 2)
    }


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    valid_order = {
        "customer_id": 10,
        "items": [
            {"product_id": 1, "quantity": 2, "unit_price": 50.0},
            {"product_id": 2, "quantity": 1, "unit_price": 25.50}
        ]
    }
    res = validate_order_payload(valid_order)
    assert res["total_amount"] == 125.50
    assert len(res["items"]) == 2

    # Invalid order (empty items)
    try:
        validate_order_payload({"customer_id": 10, "items": []})
        assert False, "Should fail on empty items"
    except ValueError as ve:
        assert "items" in ve.args[0]

    # Invalid item quantity
    bad_item = {
        "customer_id": 10,
        "items": [{"product_id": 1, "quantity": -3, "unit_price": 10.0}]
    }
    try:
        validate_order_payload(bad_item)
        assert False, "Should fail on negative quantity"
    except ValueError as ve:
        assert "item_errors" in ve.args[0]

    print("Whiteboard Day 46 challenge passed successfully!")
