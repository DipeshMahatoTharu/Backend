"""
Day 60: Hotel Booking Capstone — Practice
Hands-on exercises covering date interval overlap detection, dynamic room pricing, and reservation validation.
"""
from datetime import date
from typing import List, Dict, Any, Tuple

# ---------------------------------------------------------------------
# Task 1: Date Interval Overlap Checker (Hotel Booking Semantics)
# Note: Check-out on day X allows a new guest to check in on day X!
# ---------------------------------------------------------------------
def has_date_overlap(start1: date, end1: date, start2: date, end2: date) -> bool:
    """
    Intervals overlap if and only if: start1 < end2 and end1 > start2.
    Same-day turnover (end1 == start2) is NOT considered an overlap!
    """
    return start1 < end2 and end1 > start2


# ---------------------------------------------------------------------
# Task 2: Dynamic Room Pricing Calculator
# ---------------------------------------------------------------------
def calculate_stay_price(base_price_per_night: float, nights: int, is_weekend: bool = False, cleaning_fee: float = 30.0) -> float:
    """
    Calculates total reservation cost:
    - Base price * nights
    - 20% weekend surge multiplier if stay spans weekend
    - Flat cleaning fee added
    - 10% tax added
    """
    rate = base_price_per_night * 1.20 if is_weekend else base_price_per_night
    subtotal = (rate * nights) + cleaning_fee
    tax = subtotal * 0.10
    return round(subtotal + tax, 2)


# ---------------------------------------------------------------------
# Task 3: Reservation State Transition Machine
# ---------------------------------------------------------------------
VALID_TRANSITIONS = {
    "PENDING": ["CONFIRMED", "CANCELLED"],
    "CONFIRMED": ["CHECKED_IN", "CANCELLED"],
    "CHECKED_IN": ["CHECKED_OUT"],
    "CHECKED_OUT": [],
    "CANCELLED": []
}

def transition_reservation_status(current_status: str, new_status: str) -> str:
    allowed = VALID_TRANSITIONS.get(current_status, [])
    if new_status not in allowed:
        raise ValueError(f"Invalid transition from {current_status} to {new_status}")
    return new_status


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 60 Practice Tests ---")

    # Test Task 1: Overlap
    # Guest A: Sept 1 to Sept 5
    d1_in, d1_out = date(2026, 9, 1), date(2026, 9, 5)

    # Guest B: Sept 3 to Sept 7 (Overlaps!)
    assert has_date_overlap(d1_in, d1_out, date(2026, 9, 3), date(2026, 9, 7)) is True

    # Guest C: Sept 5 to Sept 10 (Same-day turnover -> Allowed, no overlap!)
    assert has_date_overlap(d1_in, d1_out, date(2026, 9, 5), date(2026, 9, 10)) is False

    # Test Task 2: Pricing
    # 2 nights @ $100 + $30 cleaning = $230 + 10% tax = $253.00
    total = calculate_stay_price(100.0, nights=2, is_weekend=False)
    assert total == 253.00

    # Test Task 3: State Machine
    assert transition_reservation_status("PENDING", "CONFIRMED") == "CONFIRMED"
    try:
        transition_reservation_status("CANCELLED", "CONFIRMED")
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    print("All Day 60 practice assertions passed successfully!")
