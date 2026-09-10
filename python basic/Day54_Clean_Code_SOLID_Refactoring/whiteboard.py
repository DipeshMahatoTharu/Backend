"""
============================================================
DAY 54 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Extensible Discount Strategy Engine (Open/Closed Principle)

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a discount engine `calculate_best_discount(order_amount: float, strategies: list) -> tuple[str, float, float]`
that:
1. Evaluates multiple discount strategy callables against `order_amount`.
2. Selects the strategy that yields the **highest discount** for the customer.
3. Returns `(best_strategy_name, discount_amount, final_price)`.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Final price cannot be less than 0.0.
- Handle empty strategy list gracefully (0 discount).

============================================================
MY APPROACH:
============================================================
1. Iterate over strategies, calculating discount for each.
2. Track max discount amount and corresponding strategy name.
3. Compute final price = max(0.0, order_amount - max_discount).
"""
from typing import List, Tuple, Callable

def calculate_best_discount(
    order_amount: float,
    strategies: List[Tuple[str, Callable[[float], float]]]
) -> Tuple[str, float, float]:
    if not strategies or order_amount <= 0:
        return "None", 0.0, order_amount

    best_name = "None"
    max_discount = 0.0

    for name, strategy_fn in strategies:
        discount = strategy_fn(order_amount)
        if discount > max_discount:
            max_discount = discount
            best_name = name

    # Cap discount at order_amount
    actual_discount = min(order_amount, max_discount)
    final_price = round(order_amount - actual_discount, 2)

    return best_name, round(actual_discount, 2), final_price


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    # Strategy 1: Flat $15 off
    flat_15 = ("Flat $15", lambda amt: 15.0)
    # Strategy 2: 10% off
    ten_percent = ("10% Off", lambda amt: amt * 0.10)
    # Strategy 3: VIP 25% off
    vip_25 = ("VIP 25%", lambda amt: amt * 0.25)

    # For $100: VIP 25% gives $25 off (better than $15 or $10)
    name, disc, final = calculate_best_discount(100.0, [flat_15, ten_percent, vip_25])
    assert name == "VIP 25%"
    assert disc == 25.0
    assert final == 75.0

    # For $50: Flat $15 gives $15 off (better than $5 or $12.50)
    name, disc, final = calculate_best_discount(50.0, [flat_15, ten_percent, vip_25])
    assert name == "Flat $15"
    assert disc == 15.0
    assert final == 35.0

    print("Whiteboard Day 54 challenge passed successfully!")
